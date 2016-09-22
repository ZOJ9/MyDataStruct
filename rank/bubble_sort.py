#-*- coding:utf-8 -*-
#!/usr/bin/env python

'''
冒泡排序的时间复杂度为
  最好的情况下：序列本身有序，只需比较n次，为O(n)；
  最坏的情况下：序列逆序，比较SUM_{2,n}(i-1) = 1+2+...+n-1 = (n(n-1))/2
'''


def bubble0(lst):
    '''
    这个不算是一种冒泡排序，他是最简单的交换排序，每一个与其他所有的都进行比较。
    '''
    length = len(lst)

    for i in range(length):
        for j in range(i+1,length):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

def bubble1(lst):

    '''
    正宗的冒泡排序，两两比较。
    '''
    length = len(lst)
    
    for i in range(length):
        for j in range(length-1,i-1,-1):
            if lst[j-1] > lst[j]:
                lst[j-1],lst[j] = lst[j],lst[j-1]
    return lst

def bubble2(lst):

    '''
    对冒泡排序的一种简单优化，像[2,1,3,4,5]这样只需要一轮就有顺序，后面的就不用在进行。
    '''
    length = len(lst)

    flag = True
    for i in range(length):
        flag = False
        for j in range(length-1,i-1,-1):
            if lst[j-1] > lst[j]:
                lst[j-1],lst[j] = lst[j],lst[j-1]
                flag = True
    return lst
            

if __name__ == '__main__':

    lst = [9,3,6,1,0,2,5,8,7,4]
    lst = bubble2(lst)
    print lst
