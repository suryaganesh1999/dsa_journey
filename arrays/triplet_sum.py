arr=[]
for i in range(int(input())):
    arr.append(int(input()))
sum_req=int(input())
def triplet_sum(arr, sum_req):
    l=len(arr)
    for i in range(l-2):
        req_sum=sum_req-arr[i]
        low=i+1
        high=l-1
        while(low!=high):
            lh_sum=arr[low]+arr[high]
            if lh_sum==req_sum:
                return 'True'
            elif lh_sum>req_sum:
                high-=1
            else:
                low+=1
    return 'False'

print(triplet_sum(sorted(arr), sum_req))

