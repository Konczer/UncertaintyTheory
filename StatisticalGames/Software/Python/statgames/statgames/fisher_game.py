import scipy.special

def fishergame_solve(N, KA, KB, M):
    return _fishergame_solve(N, KA, KB, M)

def _fishergame_solve(N, KA, KB, M):
    
    k_A_minmax = [max(0, N - (M - KA)), min(N, KA)]
    k_B_minmax = [max(0, N - (M - KB)), min(N, KB)]

    k_minmax = [min(k_A_minmax[0], k_B_minmax[0]), max(k_A_minmax[1], k_B_minmax[1])]
    k_AB_minmax = [max(k_A_minmax[0], k_B_minmax[0]), min(k_A_minmax[1], k_B_minmax[1])]

    Z = scipy.special.comb(M, N, exact=True)

    def w_k_A(k):
        return scipy.special.comb(KA, k, exact=True) * scipy.special.comb(M - KA, N - k, exact=True) 
    
    def w_k_B(k):
        return scipy.special.comb(KB, k, exact=True) * scipy.special.comb(M - KB, N - k, exact=True) 

    z_AB=[0, 0]
    for k in range(k_minmax[0], k_minmax[1]):

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