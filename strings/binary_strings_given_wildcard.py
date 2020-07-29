def get_all_combs(s, i=0):
    if len(s)==i:
        print(''.join(s))
        return
    if s[i]=='?':
        s[i]='0'
        get_all_combs(s, i+1)
        s[i]='1'
        get_all_combs(s, i+1)
        s[i]='?'
    else:
        get_all_combs(s, i+1)
while(1):
    i=input()
    if i!='stop':
        get_all_combs(list(i))
    else:
        break
