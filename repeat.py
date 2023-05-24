def freq(a):
    dic={}
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
print(freq("mississipi"))
