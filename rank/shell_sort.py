#-*- coding:utf-8 -*-

'''
shell 排序是直接插入算法的优化算法，经过每一次调整，将数据基本有序，
所谓基本有序就是小的在前面，大的在后面，这是针对整体而言的。
时间复杂度：
   大量的研究表明，当增量序列为dlta[k]=2^{t-k+1} 其中( 0<= k <= t <= log_2{n+1})时，可以获得不错的效
果，其时间复杂度为O(n^{3/2})，要好于直接排序的O(n^2). 需要注意的是， 增量序列的最后一个增量值必须等于1 才行。
另外由于记录是跳跃式的移动，希尔排序并不是一种稳定的排序算法。
'''

def shell(lst):

    length = len(lst)
    inc = length/3+1

    while(inc >= 1):
        for i in range(inc,length):
            temp = lst[i]
            for j in range(i,0,-inc):
                if lst[j] < lst[j-inc]:
                    lst[j] = lst[j-inc]
                else:
                    j += inc
                    break
                lst[j-inc] = temp
        inc /= 3
    return lst


if __name__ == '__main__':
    lst = [9,3,6,1,0,2,5,8,7,4]
    lst = shell(lst)
    print lst
