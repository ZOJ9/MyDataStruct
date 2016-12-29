#!/usr/bin/env python

def parition(arr,left,right):

    temp = arr[left]
    while left < right:
        while left < right and arr[right] >= temp:
            right -= 1
        arr[left],arr[right] = arr[right],arr[left]
        while left < right and arr[left] <= temp:
            left += 1
        arr[left],arr[right] = arr[right],arr[left]
    return left

def quick_sort(lst,left,right):

    if left < right:
        p = parition(lst,left,right)
        quick_sort(arr,left,p-1)
        quick_sort(arr,p+1,right)

arr = [9,2,5,1,0,4,8,3,7,6]
quick_sort(arr,0,9)
print arr



