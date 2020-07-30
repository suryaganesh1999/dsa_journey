def expand(s, l, r):
    global strings
    le=len(s)
    while (l>=0 and r<le and s[l]==s[r]):
        strings.add(s[l:r+1])
        l-=1
        r+=1

strings=set()
def print_all_palindromic_substring(s):
    global strings
    for i in range(len(s)):
        #odd length
        expand(s,i,i)
        expand(s,i,i+1)
    print(strings)
print_all_palindromic_substring('google')
