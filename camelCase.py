#Complete the solution so that the function will break up camel casing, using a space between words.


def solution(s):
    print(''.join(' ' + c if c.isupper() else c for c in s))
solution("CamelCaseH")

#or def fun(cc):
def fun(cc):
    new=""
    for letter in cc:
        if ord(letter) in range(65,91):
            new+=" "
        new+=letter
    return new
fun("CamelCaseH")