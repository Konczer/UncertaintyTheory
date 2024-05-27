from typing import Dict, Union

import scipy.special

def fishergame_solve(N: int, KA: int, KB: int, M: int) -> Dict[str, Union[int, float]]:
    """
    Solve the Fisher game problem and calculate equilibrium quantities.

    This function serves as a public interface to solve the Fisher game problem
    by invoking the internal `_fishergame_solve` function.

    Parameters:
    N (int): Number of sampled bits.
    KA (int): Number of 1-s in scenario A.
    KB (int): Number of 1-s in scenario B.
    M (int): Total length of the binary strings.

    Returns:
    dict: A dictionary containing the results:
        - 'P' (float): The probability 0 < P_star < 1.
        - 'k' (int): The critical value k_star.
        - 'nu' (float): The probability 0 <= nu_star < 1.
        - 's' (float): The value s_star.
        - 'v' (float): The winning rate v_star.

    Raises:
    ValueError: If any parameter is invalid.
    TypeError: If any parameter is not an integer.

    References:
    The concept of the Fisher game is introduced in the following paper:
    Jozsef Konczer, "Statistical Games",  arXiv:2402.15892, 2024.
    Available at: https://arxiv.org/abs/2402.15892
    """

    # Check if all parameters are integers and non-negative
    if not all(isinstance(param, int) for param in [N, KA, KB, M]):
        raise TypeError("All parameters must be integers")
    if not all(param >= 0 for param in [N, KA, KB, M]):
        raise ValueError("All parameters must be non-negative")
    
    # Check if N <= M and KA, KB <= M
    if N > M:
        raise ValueError("N must be less than or equal to M")
    if KA > M:
        raise ValueError("KA must be less than or equal to M")
    if KB > M:
        raise ValueError("KB must be less than or equal to M")

    # Return the output of the internal _fishergame_solve   
    return _fishergame_solve(N, KA, KB, M)

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