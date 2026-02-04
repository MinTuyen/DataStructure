def quick_sort(nums):
    # Write your code here
    leftlist=[]
    rightlist=[]
    midlist=[]
    if len(nums)<=1:
        return nums[:]
    mid=(len(nums)-1)//2
    
    
    for i in nums:
        if i<nums[mid]:
            leftlist.append(i)
        elif i >nums[mid]:
            rightlist.append(i)
        else:
            midlist.append(i)

        
    return quick_sort(leftlist) + midlist + quick_sort(rightlist)