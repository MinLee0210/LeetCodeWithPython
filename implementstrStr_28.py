from tracemalloc import start


def strStr(haystack, needle):
    if len(needle) == 0: 
        return 0
    startIndex = -1 
    for i in range(len(haystack) - len(needle)):
        if haystack[i] == needle[0]:
            startIndex = i 
            for j in range(1, len(needle)): 
                if haystack[i + j] != needle[j]:
                    startIndex = 0 
                    break
    return startIndex

print(strStr('Hello', 'll'))
print(strStr('aaaaa', 'bba'))
print(strStr('a', 'a'))