#Task
#Given an integer, , perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird

#Link : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

def check_weirdness(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 100:
        check_weirdness(n)
    else:
        print("Input must be between 1 and 100")
