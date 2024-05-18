def gcd(a,b):
    if a == 0: return b
    return a if b == 0 else gcd(b, a%b)

def mmc(a,b):
    return (a/gcd(a,b))*b

