#-*- coding:utf-8 -*-
#!/usr/bin/env python

'''
选择排序，简单理解就是将数据分为左右两部分，从右部分找到合适的数据插入到左侧的部分。
时间复杂度：
    最好情况：序列本身有序，共比较了SUM_{2，n}1 = n-1,为O(n)
    最坏的情况：比较的次数SUM_{2,n}i=2+3+...+n = ((n+2)(n-1))/2
                移动次数SUM_{2,n}(i+1)= ((n+4)(n-1))/2
    平均时间复杂度为：n^2/4
因此时间复杂度为：O(n^2)
'''


def insert_sort(lst):

    length = len(lst)
    
    for i in range(1,length):
        val = lst[i]
        while(lst[i-1]>val and i>0):
            lst[i] = lst[i-1]
            i -= 1
        lst[i] = val
    return lst

if __name__ == '__main__':

    lst = [9,3,6,1,0,2,5,8,7,4]
    lst = insert_sort(lst)
    print lst
            
