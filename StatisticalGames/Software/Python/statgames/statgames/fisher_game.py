from typing import Dict, Union, List

import numpy as np
import scipy.special

def fishergame_solve(N: int, Kx_list: Union[List[int], List[float], np.ndarray], M: Union[int, float] = float('inf')) -> Dict[str, Union[int, float]]:
    """
    Solves a Fisher game and calculates equilibrium quantities.

    This function serves as a public interface to solve a Fisher game
    by invoking the internal `_fishergame_solve` or `_binomial_fishergame_solve` function.

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
        - 'k' (int): The critical value k_star.
        - 'nu' (float): The probability 0 <= nu_star < 1.
        - 's' (float): The value s_star.
        - 'v' (float): The winning rate v_star.

    Raises:
    ValueError: If any parameter is invalid.
    TypeError: If any parameter has none appropriate type.

    References:
    The concept of the Fisher game is introduced in the following paper:
    Jozsef Konczer, "Statistical Games",  arXiv:2402.15892, 2024.
    Available at: https://arxiv.org/abs/2402.15892

    Example Usage:
    -------------
    Solving a Fisher game with finite M:
    
    >>> result = fishergame_solve(1, [0, 1], 2)
    >>> print(result)
    {'P': 0.6666666666666666, 'k': 0, 'nu': 0.6666666666666666, 's': 0.3333333333333333, 'v': 0.6666666666666666}
    
    Solving a Fisher game with infinite M:
    
    >>> result = fishergame_solve(10, [0.3, 0.5])
    >>> print(result)
    {'P': 0.4938830363664651, 'k': 4, 'nu': 0.4405594510317179, 's': 0.4036872228210653, 'v': 0.737775893831386}
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
            return _binomial_fishergame_solve(N, xA, xB)
        else:
            # Uses the convention of the paper:
            # https://arxiv.org/pdf/2402.15892#Hfootnote.16 
            return _binomial_fishergame_solve(N, xB, xA)
    else:
        KA, KB = Kx_list
        if KA <= KB:
            return _fishergame_solve(N, KA, KB, M)
        else:
            # Uses the convention of the paper:
            # https://arxiv.org/pdf/2402.15892#Hfootnote.16 
            return _fishergame_solve(N, KB, KA, M)

def _fishergame_solve(N: int, KA: int, KB: int, M: int) -> Dict[str, Union[int, float]]:
    """
    Internal function to calculate Fisher game equilibrium quantities.

    Parameters:
    N (int): Number of sampled bits.
    KA (int): Number of 1-s in scenario A.
    KB (int): Number of 1-s in scenario B.
    M (int): Total length of the binary strings.

    Returns:
    dict: Contains 'P', 'k', 'nu', 's', 'v'.
    """
    
    k_A_minmax = [max(0, N - (M - KA)), min(N, KA)]
    k_B_minmax = [max(0, N - (M - KB)), min(N, KB)]

    k_minmax = [min(k_A_minmax[0], k_B_minmax[0]), max(k_A_minmax[1], k_B_minmax[1])]
    k_AB_minmax = [max(k_A_minmax[0], k_B_minmax[0]), min(k_A_minmax[1], k_B_minmax[1])]

    Z = scipy.special.comb(M, N, exact=True)

    def w_k_A(k):
        if k < k_A_minmax[0] or k > k_A_minmax[1]:
            return 0
        return scipy.special.comb(KA, k, exact=True) * scipy.special.comb(M - KA, N - k, exact=True) 
    
    def w_k_B(k):
        if k < k_B_minmax[0] or k > k_B_minmax[1]:
            return 0
        return scipy.special.comb(KB, k, exact=True) * scipy.special.comb(M - KB, N - k, exact=True) 


    z_AB=[0, 0]
    for k in range(k_minmax[0], k_minmax[1] + 1):

        z_AB[0] += w_k_A(k)
        z_AB[1] += w_k_B(k)
        
        if sum(z_AB) > Z:
            k_star = k
            z_AB_star = z_AB
            break
    

    w_A_star = w_k_A(k_star)
    w_B_star = w_k_B(k_star)

    Z_A = z_AB_star[0] - w_A_star
    Z_B = Z - z_AB_star[1]

    P_star = w_A_star / (w_A_star + w_B_star)
    nu_star = (Z_B + w_B_star - Z_A) / (w_A_star + w_B_star)
    v_star = (Z_A + w_A_star * nu_star) / Z
    s_star = (k_star + nu_star) / (N + 1)

    return {'P':P_star, 'k':k_star, 'nu':nu_star, 's':s_star, 'v':v_star}


def _binomial_fishergame_solve(N: int, xA: float, xB: float) -> Dict[str, Union[int, float]]:
    """
    Internal function to calculate Binomial Fisher game equilibrium quantities.

    Parameters:
    N (int): Number of sampled bits.
    xA (float): Fraction of 1-s in case of scenario A.
    xB (float): Fraction of 1-s in case of scenario B.

    Returns:
    dict: Contains 'P', 'k', 'nu', 's', 'v'.
    """
    
    def p_k_A(k):
        if k == 0:
            return (1 - xA) ** N
        elif k == N:
            return xA ** N
        else:
            return scipy.special.comb(N, k, exact=True) * (xA ** k) * ((1 - xA) ** (N - k))

    def p_k_B(k):
        if k == 0:
            return (1 - xB) ** N
        elif k == N:
            return xB ** N
        else:
            return scipy.special.comb(N, k, exact=True) * (xB ** k) * ((1 - xB) ** (N - k))


    s_AB=[0, 0]
    for k in range(0, N + 1):

        s_AB[0] += p_k_A(k)
        s_AB[1] += p_k_B(k)
        
        if sum(s_AB) > 1:
            k_star = k
            s_AB_star = s_AB
            break
    

    p_A_star = p_k_A(k_star)
    p_B_star = p_k_B(k_star)

    Sigma_A = s_AB_star[0] - p_A_star
    Sigma_B = 1 - s_AB_star[1]

    P_star = p_A_star / (p_A_star + p_B_star)
    nu_star = (Sigma_B + p_B_star - Sigma_A) / (p_A_star + p_B_star)
    v_star = Sigma_A + p_A_star * nu_star
    s_star = (k_star + nu_star) / (N + 1)

    return {'P':P_star, 'k':k_star, 'nu':nu_star, 's':s_star, 'v':v_star}