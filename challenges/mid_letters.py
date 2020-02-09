# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
#
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(string):
    if len(string) <=2:
        result = ""
    else:
        result = string[1:-1]
    return result

print(mid("1235"))
print(mid('abdepf'))
print(mid(""))
print(mid("12"))

def mid2(string):
    if len(string) <=2 or len(string)//2 != 1:
        result = ""
    else:
        result = string[int(len(string)/2)-2::1]
    return result

print(mid2('abcde'))