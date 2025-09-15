def make(numer, denom):
    numer, denom = normalize(numer, denom)
    return {'numer': numer, 'denom': denom}


def normalize(numer, denom):
    gcd = math.gcd(numer, denom)
    return numer // gcd, denom // gcd


def to_common_denom(rat1, rat2):
    denom1 = rat1['denom']
    denom2 = rat2['denom']
    lcm = abs(denom1 * denom2) // math.gcd(denom1, denom2)
