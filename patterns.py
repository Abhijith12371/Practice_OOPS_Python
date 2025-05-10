print("The left pattern")
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()


#right pattern
print("The right pattern")
for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()


#triangle
print("triangle")
for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for k in range(i+1):
        print("*",end="")
    print()


#reverse left pattern
print("reverse left pattern")
for i in range(5):
    for j in range(i,5):
        print("*",end="")
    print()


#reverse right pattern
print("reverse right pattern")
for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,5):
        print("*",end="")
    print()


#complete reverse triangle
print("reverse triangle")
for i in range(5):
    for j in range(i):
        print(" ",end="")
    for j in range(i,5):
        print("*",end=" ")
    print()


