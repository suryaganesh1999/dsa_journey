def fun(lists, digit, index=0, hashs={}, comp=""):
    if len(comp)==len(digit):
        print(comp)
        return
    if digit[index] in hashs.keys():
        fun(lists, digit, index+1, hashs, comp+hashs[digit[index]])
    else:
        for i in lists[int(digit[index])]:
            hashs[digit[index]]=i
            fun(lists, digit, index+1, hashs, comp+i)
            hashs.pop(digit[index])
A = [
		['A', 'B', 'C', 'D'],
		['E', 'F', 'G', 'H', 'I', 'J', 'K'],
		['L', 'M', 'N', 'O', 'P', 'Q'],
		['R', 'S', 'T'],
		['U', 'V', 'W', 'X', 'Y', 'Z']
	]
fun(A, '02110')
