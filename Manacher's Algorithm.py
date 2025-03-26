def manacher(s:str) -> str:
    if len(s)==0:
        return ""
    
    def expand(l,r):
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l -= 1
            r += 1
        return s[l+1:r]
    result = ""
    for i in range(0, len(s)):
        string1 = expand(i,i)
        string2 = expand(i,i+1)
    
        if(len(string1)>len(result)):
            result = string1
        if(len(string2)>len(result)):
            result = string2
    return result 

string = input()
print(manacher(string))
