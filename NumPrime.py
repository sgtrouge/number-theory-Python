def sieveList(upper_bound = 10000000):
    return
def simpleGCD(a, b):
    # return the greatest common divisor between a and b
    if (b == 0):
        return a
    else:
        return gcd(b, a % b);

def EuclideGCD(a, b):
    # return the pair of x, y such that a*x + b*y = gcd(a,b);
    return;

def simpleLCM(a, b):
    # return the least common multiple of a and b
    return a*b/gcd(a,b);

def AKSpow(a, rank, modulo = NULL):
    # return a^rank, optionally % modulo
    temp = AKSpow(a, rank/2, modulo);
    temp = (temp * temp) % modulo;
    if (rank % 2 == 0):
        return temp
    else:
        return (temp * a) % modulo

def EuclidmodInverse(int a, int b, int modulo):
    # based on Euclid Extended Method

def FLTmodInverse(int a, int modulo):
    # based on Fermat's little theorem
    # currently require modulo to be a prime number
    return AKSpow(a, modulo-2, modulo)
