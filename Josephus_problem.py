def josephus(n,m):
    if(n==1):
        return 1
    else:
        # print (str(n)+":"+str(m))
        result=(josephus(n-1,m)+m-1)%n+1
        print result
        return result

print(josephus(40,3))