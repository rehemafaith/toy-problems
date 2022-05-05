def solution(A):
    a = set(A)
    i = 1
    while True:
        if i in a:
            i+=1
        else:
            return i
        print(i) 


solution( [-1,-3])