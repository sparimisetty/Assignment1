# --------------------
# Title- Looking for Fermat's Last Theorem Near Misses
# Filename- NearMisses.py
# Necessary files- N/A
# Created external files- NearMisses.exe which is an executable for windows platform
# Name- Abhiram Atmuri, Siva Parimisetty
# Explanation- This Program helps an interactive user search for near misses
#               of the form (x, y, z, n, k) in the formula x^n + y^n = z^n, where x, y, z, n, k
#               are positive integers, 2< n <12, 10 <= x <= k, and 10 <= y <= k
# Resource- N/A
# Programming language- Python 3.10
# ---------------------

def calculateMisses(n, k):
    # Calculate near misses usoong of Fermat's Last Theorem formula
    # Calculate x^n + y^n = z^n, and then look for the minimum miss

    relative_miss = 0
    # Outer loop for first variable x of function x^n + y^n = z^n
    for x in range(10, k):
        # loop for y
        for y in range(10, k):
            # calculate (x^n + y^n) using python's built in pow method
            xysum_pow = pow(x, n) + pow(y, n)
            z = int(pow(xysum_pow, 1/n))
            z_pow = pow(z, n)
            z1_pow = pow(z+1, n)
            miss = min( xysum_pow - z_pow, z1_pow - xysum_pow)
            relative_miss_temp = miss / xysum_pow

            # print result when relative miss is small or its the first iteration
            if relative_miss > relative_miss_temp or relative_miss == 0: 
                # get the minimum relative miss
                relative_miss = relative_miss_temp
                print(f"x - {x}      y - {y}      z - {z}       Miss - {miss}      Relative Miss - {round(relative_miss*100,2)}%")
    
    # print the final result
    print("\n----------- Final result ------------\n") 
    print(f"x - {x}      y - {y}      z - {z}       Miss - {miss}      Relative Miss - {round(relative_miss*100,2)}%")

n = int(input("Exponent value- "))
while n>11 or n<3:
        # check if n is bwtween 2 and 12 as requirement
    n = int(input("Exponent value(n) should be between 2 and 12- "))

k = int(input("Limit of x and y- "))
while(k<11):
    # check if k is bigger than 10
    k = int(input("Limit Value(k) should be bigger than 10- "))
calculateMisses(n, k)

# wait
w = input("\nPress any key to Exit- ")