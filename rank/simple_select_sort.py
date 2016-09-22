#-*- coding:utf-8 -*-
#!/usr/bin/env python

'''
简单的选择排序，相对于冒泡排序而言，交换移动的次数较少，不用两两都比较
时间复杂度：
  最好最坏的时间复杂度是一样的，SUM_{1,n-1}(n-i) =n-1 + n-2 +...+1  = (n(n-1))/2
因此它的时间复杂度为：O(n^2)

'''

def simple_select(lst):

    length = len(lst)

    for i in range(0,length):
        min = i
        for j in range(i+1,length):
            if lst[min] > lst[j]:
                min = j
        if min != i:
            lst[i],lst[min] = lst[min],lst[i]
    return lst

if __name__ == '__main__':

    lst = [9,3,6,1,0,2,5,8,7,4]
    lst = simple_select(lst)
    print lst
