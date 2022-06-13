def largerPerimeter(nums):
    i = 0
    lp = 0
    n1 = sorted(nums,reverse=True)
    while (i<(len(n1)-2)) and (n1[i]>0) and (n1[i+1]>0)and (n1[i+2]>0):
        if (n1[i] < (n1[i+1]+n1[i+2])):
            lp = n1[i]+n1[i+1]+n1[i+2]
            break
        else:
            i = i+1
    return lp