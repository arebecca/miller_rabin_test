import random

def miller_rabin_test(n, epochs = 10):
    # exclude the base cases
    if n == 2 or n == 3:
        return True

    # exclude even numbers
    if n % 2 == 0:
        return False

    q = n - 1
    k = 0
    while q % 2 == 0:
        q = q // 2
        k += 1

    # test the algorithm multiple times
    for _ in range(epochs):
        a = random.randrange(2, n - 1)
        x = pow(a, q, n)
        
        if x == 1 or x == n - 1:
            # is probably prime,
            # so check for other cases
            continue
        for _ in range(k - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # haven't encountered any break statements,
            # then is composite
            return False

    return True
    
def print_number_type(is_prime):
    if is_prime:
        print("maybe prime")
        return
    print("composite")
    
# run the test for a known prime number
is_prime = miller_rabin_test(9999991)
    
print_number_type(is_prime)
