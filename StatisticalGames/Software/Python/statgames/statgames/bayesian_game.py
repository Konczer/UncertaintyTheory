from typing import Dict, Union, List, Tuple

import numpy as np
import scipy.special

def bayesiangame_solve(
    N: int,
    Kx_list: Union[List[int], List[float], np.ndarray],
    M: Union[int, float] = float('inf'),
    method = "bisection",
    max_iter = float('inf'),
    max_error=1 / 2 ** 10,
    error_type: str = "P"
    # keys: List[str] = "all"
    ) -> Dict[str, Union[float, Tuple[float, float], Dict[int, float]]]:   
    """
    Solves a Bayesian game and calculates equilibrium quantities.

    This function serves as a public interface to solve a Bayesian game
    by invoking the internal `_bayesiangame_solve` or `_binomial_bayesiangame_solve` function.

    Parameters:
    N (int): Number of sampled bits.
    Kx_list (Union[List[int], List[float], np.ndarray]): A list or array containing two elements:
        [K_A, K_B], pair of integers or [x_A, x_B], pair of floats.
    M (Union[int, float], optional): Total length of the binary strings or float('inf'). 
        If M is a finite integer, then Kx_list contains [K_A, K_B];
        if M is infinite, then Kx_list contains [x_A, x_B].
        Default is float('inf').

    Returns:
    dict: A dictionary containing the results:
        - 'P' (float): The probability 0 < P_star < 1.
        - 'P_interval' ([float, float]): The upper and lower bound for P_star
        - 'G' (float): Growth rate in equilibrium.
        - 'p_prime' ({int : float}): Dictionary of equilibrium splitting ratios.

    Raises:
    ValueError: If any parameter is invalid.
    TypeError: If any parameter has none appropriate type.

    References:
    The concept of the Fisher game is introduced in the following paper:
    Jozsef Konczer, "Statistical Games",  arXiv:2402.15892, 2024.
    Available at: https://arxiv.org/abs/2402.15892
    
    Example Usage:
    -------------
    Solving a Bayesian game with finite M:
    
    >>> result = bayesiangame_solve(1, [0, 1], 2)
    >>> print(result)
    {'P': 0.4462890625, 
    'P_interval': [0.4462890625, 0.447265625], 
    'G': -0.4812106300819732, 
    'p_prime': {
        0: 0.6171505739365294, 
        1: 0.0
        }
    }
    
    Solving a Bayesian game with infinite M:
    
    >>> result = bayesiangame_solve(10, [0.3, 0.5])
    >>> print(result)
    {'P': 0.4990234375, 
    'P_interval': [0.498046875, 0.5], 
    'G': -0.5158309498018485, 
    'p_prime': {
        0: 0.9664572431930976, 
        1: 0.925084082646245, 
        2: 0.8410712502801064, 
        3: 0.6940075752961667, 
        4: 0.49290664335788936, 
        5: 0.29407520178603835, 
        6: 0.15148886921226545, 
        7: 0.07107654724506647, 
        8: 0.03175094751718913, 
        9: 0.013858998265404298, 
        10: 0.005986984172753379
        }
    }
    """

    # Check if Kx_list is iterable and attempt to convert it to a list
    if not isinstance(Kx_list, (list, np.ndarray, set, tuple)):
        raise TypeError(f"Kx_list must be an iterable or convertible to a list, got {type(Kx_list)} instead.")
    
    # Converting Kx_list to a list
    try:
        if isinstance(Kx_list, (np.ndarray, set, tuple)):
            Kx_list = list(Kx_list)
    except Exception as e:
        raise TypeError(f"Kx_list conversion to list failed: {e}")

    # Check if Kx_list is a list or array containing two elements
    if len(Kx_list) != 2:
        raise TypeError("Kx_list must be a list or array containing two elements")
    
    # Check if N and M are integers and non-negative
    if not isinstance(N, int) or (not isinstance(M, int) and not np.isinf(M)):
        raise TypeError("N must be an integer and M must be an integer or float('inf')")
    if N < 0 or (isinstance(M, int) and M < 0):
        raise ValueError("N and M must be non-negative")
    if any(param < 0 for param in Kx_list):
        raise ValueError("Values in Kx_list must be non-negative")
    
    # Check the case when M is infinity
    if np.isinf(M):
        if not all(isinstance(param, (int, float)) and 0 <= param <= 1 for param in Kx_list):
            raise TypeError("When M is infinity, Kx_list must contain values between 0 and 1")

    # Check the case when M is a finite integer
    if not np.isinf(M):
        if not all(isinstance(param, int) for param in Kx_list):
            raise TypeError("Kx_list must contain two integers when M is finite")
        KA, KB = Kx_list
        if N > M or KA > M or KB > M:
            raise ValueError("N, KA, and KB must be <= M")

    # Based on the structure of the imput, 
    # returns the output of the internal:
    # _fishergame_solve or _binomial_fishergame_solve  

    if np.isinf(M):
        xA, xB = map(float, Kx_list)
        if xA <= xB:
            return _binomial_bayesiangame_solve(N, xA, xB)
        else:
            # Uses the convention of the paper:
            # https://arxiv.org/pdf/2402.15892#Hfootnote.16 
            return _binomial_bayesiangame_solve(N, xB, xA)
    else:
        KA, KB = Kx_list
        if KA <= KB:
            return _bayesiangame_solve(N, KA, KB, M, method="bisection", max_iter=max_iter, max_error=max_error)
        else:
            # Uses the convention of the paper:
            # https://arxiv.org/pdf/2402.15892#Hfootnote.16 
            return _bayesiangame_solve(N, KB, KA, M, method="bisection", max_iter=max_iter, max_error=max_error)

def _surewinning(k_A_minmax, k_B_minmax):
    """
    Internal function to handle sure winning Bayesian games.

    Parameters:
    k_A_minmax (Tuple[int, int]): Minimum and Maximum of k in case of scenario A.
    k_B_minmax (Tuple[int, int]): Minimum and Maximum of k in case of scenario B.

    Returns:
    dict: Contains 'P', 'P_interval', 'G', 'p_prime'.
    """

    p_prime_A = {k: 1 for k in range(k_A_minmax[0], k_A_minmax[1] + 1)}
    p_prime_B = {k: 0 for k in range(k_B_minmax[0], k_B_minmax[1] + 1)}

    return {'P': None, 'P_interval': [0, 1], 'G': 0, 'p_prime': p_prime_A | p_prime_B}

def _blindguessing(k_A_minmax, k_B_minmax):
    """
    Internal function to handle blind guessing Bayesian games.

    Parameters:
    k_A_minmax (Tuple[int, int]): Minimum and Maximum of k in case of scenario A.
    k_B_minmax (Tuple[int, int]): Minimum and Maximum of k in case of scenario B.

    Returns:
    dict: Contains 'P', 'P_interval', 'G', 'p_prime'.
    """

    p_prime_A = {k: 1/2 for k in range(k_A_minmax[0], k_A_minmax[1] + 1)}
    p_prime_B = {k: 1/2 for k in range(k_B_minmax[0], k_B_minmax[1] + 1)}

    return {'P': 1/2, 'P_interval': [1/2, 1/2], 'G': -np.log(2), 'p_prime': p_prime_A | p_prime_B}


def _bayesiangame_solve(N: int, KA: int, KB: int, M: int, 
    method="bisection",
    max_iter=float('inf'),
    max_error=1 / 2 ** 10
    ):
    """
    Internal function to calculate Bayesian game equilibrium quantities.

    Parameters:
    N (int): Number of sampled bits.
    KA (int): Number of 1-s in scenario A.
    KB (int): Number of 1-s in scenario B.
    M (int): Total length of the binary strings.

    Returns:
    dict: Contains 'P', 'P_interval', 'G', 'p_prime'.
    """
    
    k_A_minmax = [max(0, N - (M - KA)), min(N, KA)]
    k_B_minmax = [max(0, N - (M - KB)), min(N, KB)]

    k_minmax = [min(k_A_minmax[0], k_B_minmax[0]), max(k_A_minmax[1], k_B_minmax[1])]
    k_AB_minmax = [max(k_A_minmax[0], k_B_minmax[0]), min(k_A_minmax[1], k_B_minmax[1])]

    if KA == KB:
        return _blindguessing(k_A_minmax, k_B_minmax)

    if k_AB_minmax[0] > k_AB_minmax[1]:
        return _surewinning(k_A_minmax, k_B_minmax)

    Z = scipy.special.comb(M, N, exact=True)

    # Define the range for k values
    k_values = np.arange(k_minmax[0], k_minmax[1] + 1)

    # Calculate p_A_list and p_B_list using element-wise calculations
    p_A_list = np.array([scipy.special.comb(KA, k, exact=True) * scipy.special.comb(M - KA, N - k, exact=True) for k in k_values]) / Z
    p_B_list = np.array([scipy.special.comb(KB, k, exact=True) * scipy.special.comb(M - KB, N - k, exact=True) for k in k_values]) / Z

    # Define the slices directly for later use
    k_A_slice = slice(k_A_minmax[0] - k_minmax[0], k_A_minmax[1] - k_minmax[0] + 1)
    k_B_slice = slice(k_B_minmax[0] - k_minmax[0], k_B_minmax[1] - k_minmax[0] + 1)

    # Calculate HA and HB using numpy operations
    HA = -np.sum(p_A_list[k_A_slice] * np.log(p_A_list[k_A_slice]))
    HB = -np.sum(p_B_list[k_B_slice] * np.log(p_B_list[k_B_slice]))

    # g being the derivative of G(P) respect to P
    # $\Delta G'(P)$ in the Statistical Games paper:
    # https://arxiv.org/pdf/2402.15892#equation.3.120

    # Optimized g function using vectorized operations and the predefined slice
    def g(P):
        return np.log(P / (1 - P)) - HA + HB - \
            np.sum((p_A_list - p_B_list) * np.log(P * p_A_list + (1 - P) * p_B_list))

    # Simple implementation of the Bisection method:
    # https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.03-Bisection-Method.html
    
    # Or from Numerical Recipes: https://www.numerical.recipes/book.html
    # 9.1 Bracketing and Bisection 445:
    # https://nr304ob.s3.amazonaws.com/MNV7AKCDC7LVFQDK.pdf

    # Initial bounds
    P_lower = 0
    P_upper = 1

    i = 0
    while i < max_iter and (P_upper - P_lower) / 2 > max_error:
        P_mid = (P_lower + P_upper) / 2
        g_P_mid = g(P_mid)
        
        if g_P_mid > 0:
            P_upper = P_mid
        elif g_P_mid < 0:
            P_lower = P_mid
        elif g_P_mid == 0:
            P_lower = P_mid
            P_upper = P_mid
            break
        
        i += 1

    P_star = (P_lower + P_upper) / 2  # Set P_star to the midpoint after the loop

    G_star = P_star * np.log(P_star) + (1 - P_star) * np.log(1 - P_star) - \
            (P_star * HA + (1 - P_star) * HB) - \
            np.sum((P_star * p_A_list + (1 - P_star) * p_B_list) * \
                    np.log(P_star * p_A_list + (1 - P_star) * p_B_list))

    # Calculate p_prime_star
    p_prime_star = {
        k: P_star * p_A_list[i] / (P_star * p_A_list[i] + (1 - P_star) * p_B_list[i])
        if (P_star * p_A_list[i] + (1 - P_star) * p_B_list[i]) != 0 else np.nan
        for i, k in enumerate(k_values)
    }

    return {'P': P_star, 'P_interval': [P_lower,P_upper], 'G': G_star, 'p_prime': p_prime_star}

def _binomial_bayesiangame_solve(N: int, xA: float, xB: float, 
    method="bisection", 
    max_iter=float('inf'), 
    max_error=1 / 2 ** 10):
    """
    Internal function to calculate binomial Bayesian game equilibrium quantities.

    Parameters:
    N (int): Number of sampled bits.
    xA (float): Density of 1 in scenario A.
    xB (float): Density of 1 in scenario B.
    method (str, optional): Method to use for solving the game. Default is "bisection".
    max_iter (int, optional): Maximum number of iterations allowed. Default is float('inf').
    max_error (float, optional): Maximum acceptable error. Default is 1 / 2 ** 10.

    Returns:
    dict: Contains 'P', 'P_interval', 'G', 'p_prime'.
    """

    
    
    if xA == 0 and xB == 1:
        return _surewinning([0,0],[N,N])
    
    # Define the range for k values
    k_values = np.arange(0, N + 1)

    if xA == xB:
        return _blindguessing(k_values, k_values)
    
    # Calculate binomial probabilities p_A_list and p_B_list
    if xA == 0:
        p_A_list = np.zeros(N + 1)
        p_A_list[0] = 1.0
    else:
        p_A_list = np.array([scipy.special.comb(N, k, exact=True) * (xA ** k) * ((1 - xA) ** (N - k)) for k in k_values])
        p_A_list /= np.sum(p_A_list)

    if xB == 1:
        p_B_list = np.zeros(N + 1)
        p_B_list[N] = 1.0
    else:
        p_B_list = np.array([scipy.special.comb(N, k, exact=True) * (xB ** k) * ((1 - xB) ** (N - k)) for k in k_values])

    # Calculate entropies HA and HB using slices
    HA = -np.sum(p_A_list[p_A_list > 0] * np.log(p_A_list[p_A_list > 0]))
    HB = -np.sum(p_B_list[p_B_list > 0] * np.log(p_B_list[p_B_list > 0]))
    
    # g being the derivative of G(P) respect to P
    # $\Delta G'(P)$ in the Statistical Games paper:
    # https://arxiv.org/pdf/2402.15892#equation.3.120

    # Optimized g function using vectorized operations
    def g(P):
        return np.log(P / (1 - P)) - HA + HB - \
            np.sum((p_A_list - p_B_list) * np.log(P * p_A_list + (1 - P) * p_B_list))
    
    # Simple implementation of the Bisection method:
    # https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/chapter19.03-Bisection-Method.html
    
    # Or from Numerical Recipes: https://www.numerical.recipes/book.html
    # 9.1 Bracketing and Bisection 445:
    # https://nr304ob.s3.amazonaws.com/MNV7AKCDC7LVFQDK.pdf

    P_lower = 0
    P_upper = 1
    
    i = 0
    while i < max_iter and (P_upper - P_lower) / 2 > max_error:
        P_mid = (P_lower + P_upper) / 2
        g_P_mid = g(P_mid)
        
        if g_P_mid > 0:
            P_upper = P_mid
        elif g_P_mid < 0:
            P_lower = P_mid
        elif g_P_mid == 0:
            P_star = P_mid
            break
        
        i += 1
    
    P_star = (P_lower + P_upper) / 2  # Set P_star to the midpoint after the loop
    
    G_star = P_star * np.log(P_star) + (1 - P_star) * np.log(1 - P_star) - \
            (P_star * HA + (1 - P_star) * HB) - \
            np.sum((P_star * p_A_list + (1 - P_star) * p_B_list) * \
                    np.log(P_star * p_A_list + (1 - P_star) * p_B_list))
    
    p_prime_star = {
        k: P_star * p_A_list[k] / (P_star * p_A_list[k] + (1 - P_star) * p_B_list[k])
        if (P_star * p_A_list[k] + (1 - P_star) * p_B_list[k]) != 0 else np.nan
        for k in range(N + 1)
    }
    
    return {'P': P_star, 'P_interval': [P_lower, P_upper], 'G': G_star, 'p_prime': p_prime_star}