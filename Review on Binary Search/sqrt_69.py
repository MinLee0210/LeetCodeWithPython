def sqrt(x):
    if(x == 0 or x == 1):
        return x
    elif(x == 2 or x == 3):
        return 1
    else:
        temp = x//2
        while (temp != 1):
            if( temp ** 2 <= x and x <= (temp + 1) ** 2):
                return temp
            else:
                temp = temp//2
        return -1

print(sqrt(1))
print(sqrt(12))
print(sqrt(6))
print(6//2)