def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(10):
    print(fib(i),end=" ")


def power(n,p):
    if p==0:
        return 1
    else:
        return n*power(n,p-1)

print(power(2,5))


def prime(n,i):
    if i==1:
        return 1
    if n%i==0:
        return 0
    return prime(n,i-1)

n=int(input("Enter the number: "))
value=prime(n,n-1)
if value==1:
    print("YES")
else:
    print("NO")


def sum_first_n_numbers(n):
    if n==0 or n==1:
        return 1
    else:
        return n+sum_first_n_numbers(n-1)
print(sum_first_n_numbers(10))