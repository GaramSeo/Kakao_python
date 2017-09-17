def solution(n, arr1, arr2):
    bin_or= []
    str_bin=[]
    answer = ['']*n
    #binary operation between arr1 and arr2
    for i in range (n) :
        bin_or.append(arr1[i]|arr2[i])

    #trans bin_or to str
    for i in range (n) :
        str_bin.append(bin(bin_or[i]))

    #change 1 to '#', 0 to ' ''
    for i in range (n) :
        for j in range (2, len(str_bin[i])):
            if (str_bin[i][j] == '1'):
                print(str_bin[i]+ " " + '#')
                answer[i]+='#'
            elif (str_bin[i][j] == '0'):
                print(str_bin[i]+ " " + ' ')
                answer[i]+=' '
    print (answer)
    print (bin(22|14))
    print (bin (22))
    print (bin (14))
    return answer

solution (6, [46, 33, 33 ,22, 31, 50]
, [27 ,56, 19, 14, 14, 10])