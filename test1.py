def solution(S):
    val =[]
    for i in S:
        val =[]
        
        for i in S:
            x = S.count(i)
            while x > 1:
                y = ord(i.upper())
                val.append(y)
                y = chr(max(val))
                return y

                break
            else:
                return 0
                
    #     print(A.count(i))
    #     i = ord(i.upper())
    #     if (max_value is None or i > max_value):
    #         max_value = i
    # print(chr(max_value))


solution('aaBabcDaA')