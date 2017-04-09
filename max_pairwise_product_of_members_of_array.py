#uses python 3
#To run this:    python3 max_pairwise_product_of_members_of_array.py

def max_product(n,arr):
    if n==1:
        return arr[0]
    elif n<2:
        return 0
    largest_known_till_now = arr[1] if arr[0]<arr[1] else arr[0]
    max_product_till_now=arr[0]*arr[1]

    for i in range(2,n):
        if arr[i]>largest_known_till_now:
            max_product_till_now=largest_known_till_now*arr[i]
            largest_known_till_now=arr[i]
        elif largest_known_till_now*arr[i]<max_product_till_now:
            max_product_till_now=largest_known_till_now*arr[i]

    return max_product_till_now



if __name__=="__main__":
    n=int(input())
    arr=[int(x) for x in input().split()]
    assert(len(arr)==n)
    print(max_product(n,arr))
