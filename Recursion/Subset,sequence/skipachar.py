def skip(n,char,ans):
    if n == '':
        return ans
    elif n[0]==char:
        return skip(n[1:],char,ans)
    else:
        ans+=n[0]
        return skip(n[1:],char,ans)



print(skip('baccad','a',''))