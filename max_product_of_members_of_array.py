import unittest

def maxproduct(arr):
    if arr is None:
        return -1
    if len(arr)<2:
        return -1
    largest_till_now=arr[0] if arr[0]>arr[1] else arr[1]
    max=arr[0]*arr[1]

    for i in range(2,len(arr)):
        if arr[i]>largest_till_now:
            max=largest_till_now*arr[i]
            largest_till_now=arr[i]
        elif largest_till_now*arr[i]>max:
            max=largest_till_now*arr[i]
    return max




if __name__=="__main__":
    if(maxproduct([1,2,3,4,5,6])==30):
        print("Test passed")
    if maxproduct([1,6,3,4,5])==30:
        print("Test passed")
    if (maxproduct([1])==-1):
        print("Test passed")
    if (maxproduct([])==-1):
        print("Test passed")
    if maxproduct(None)==-1:
        print("Test passed")
