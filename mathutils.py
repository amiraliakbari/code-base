
primes = []

def fill_primes(maximum=1000000):
    global primes
    primes = []
    for i in range(2, maximum+1):
        prime = True
        for p in primes:
            if p*p > i: break
            if i % p == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    print "primes filled"


def is_prime(x):
    global primes
    return binary_search(primes, x) > -1


def sum_primes(maximum=1000000):
    global primes
    fill_primes(2000000)
    sum = 0
    for p in primes:
        sum += p
    return sum


def circular_primes(maximum=1000000):
    from strutils import rotations
    global primes
    fill_primes(maximum)
    cpa = []
    for p in primes:
        cp = True
        for r in rotations(p):
            if not is_prime(int(r)):
                cp = False
                break
        if cp:
            cpa.append(p)
    return cpa


def factors(x):
    fs = []
    for i in range(2, 1+x):
        if (i<=x) and (x%i==0):
            if (i<=x) and (x%i==0): fs.append([i, 0])
            while (i<=x) and (x%i==0):
                x = x/i
                fs[-1][1] += 1
    return fs


def factorial(x):
    p = 1
    for i in range(1, x+1):
        p *= i
    return p


def digits_sum(x):
    xstr = str(x)
    sum = 0
    for digit in xstr:
	    sum += int(digit)

