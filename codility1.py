def solution(A):
    N = len(A)+2
    list1 = []
    list2 = []
    for i in range(N):
        A.sort()
        list1.append(i)
    list1.remove(0)    
    for i in list1:
        if i not in A:
            list2.append(i)
            
           
        
    print(min(list2))  

solution( [-1,-3])