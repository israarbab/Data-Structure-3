def fac(n):


    # When n is 1 or 0 return 1 

    if(n==1 or n==0):

        return 1

    # Factorial of n = n*n-1*n-2...1

    return n*fac(n-1)

def print1to10(n):

    # Base case to stop the recursion

    if(n>10):

        return

    print(n)


    # Recursive call 1 -> 2 , 2 -> 3, 3 -> 4 and so on

    print1to10(n+1)