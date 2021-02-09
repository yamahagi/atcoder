n = int(input())
abl = []

def prime_factorize(n):
    a = {}
    while n % 2 == 0:
        if 2 not in a:
            a[2] = 1
        else:
            a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f not in a:
                a[f] = 1
            else:
                a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] = 1
    return a


for _ in range(n):
    a,b = map(int,input().split())
    if a > 0:
        af = prime_factorize(a)
    else:
        af = prime_factorize(-a)
    if b > 0:
        bf = prime_factorize(b)
    else:
        bf = prime_factorize(-b)
    lista = list(af.keys())
    listb = list(bf.keys())
    listc = list(set(lista+listb))
    listc.sort()
    cf = {}
    for key in listc:
        if key in lista:
            cf[key] = af[key]
        if key in listb:
            if key not in cf:
                cf[key] = -bf[key]
            else:
                cf[key] -= bf[key]
    print(a)
    print(b)
    print(cf)
