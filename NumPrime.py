from random import randint

def sieveList(upper_bound = 1000):
    sieve = [];
    isPrime = [True] * (upper_bound+1);
    for i in range(2,upper_bound+1):
        if isPrime[i]:
            sieve.append(i);
            j = i;
            while j*i <= upper_bound:
                isPrime[j*i] = False
                j += 1
    return sieve;

def simpleGCD(a, b):
    # return the greatest common divisor between a and b
    if (b == 0):
        return a
    else:
        return simpleGCD(b, a % b);

def simpleLCM(a, b):
    # return the least common multiple of a and b
    return a*b/simpleGCD(a,b);

def euclidGcd(a, b):
    # return the gcd of a and b using euclide extended algorithm
    [x, y] = euclidGcdPair(a,b)
    return x*a+b*y

def euclidGcdPair(a, b):
    # return the pair of x, y such that a*x + b*y = gcd(a,b);
    if (b == 0):
        return [1,0];
    [x_bar, y_bar] = euclidGcdPair(b, a % b);
    q = a/b;
    return [y_bar, x_bar - q*y_bar];

def AKSpow(a, rank, modulo = None):
    # return a^rank, optionally % modulo
    if (rank == 0):
        return 1;
    temp = AKSpow(a, rank/2, modulo);
    if (modulo != None):
        temp = (temp * temp) % modulo;
    else:
        temp = temp * temp;

    if (rank % 2 == 0):
        return temp
    else:
        if (modulo != None):
            return (temp * a) % modulo
        else:
            return (temp * a)

def euclidInverse(a, modulo):
    # return inverse of a, based on module, using the Euclid Extended Method
    [x, y] = euclidGcdPair(a, modulo);
    return x;

def FLTmodInverse(a, modulo):
    # based on Fermat's little theorem
    # currently require modulo to be a prime number
    return AKSpow(a, modulo-2, modulo)

#---------------------------Prime-Testing--------------------------------------#
def isPrime(n, type = 'non-det'):
    if (type == 'non-det'):
        return RMTest(n);

def RMTest(n):
    if ((n > 2) and (n % 2 == 0)):
        return False;
    t = n-1;
    s = 0;
    while (t % 2 == 0):
        t = t/2;
        s = s+1;
    for rep in range(1, 10):
        x = randint(1, n-1);
        if (AKSpow(x, n-1, n) != 1): # according to FLT
            return False;
        mui = 1;
        for i in range (1,s+1):
            mui = mui*2;
            tmp = AKSpow(x, mui/2, n);
            if ((AKSpow(x, mui, n) == 1) and (tmp != 1) and (tmp != n-1)):
                return False;
    return True;
