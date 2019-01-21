#!/usr/bin/python
# -*- coding:utf8 -*-

__author__="wanglongfei@genomics.cn"

import os

class Solution():
    def __init__(self):
        pass
    def twoSum(self,nums,target):
        '''
            两个数相加等于一个给定的值。返回两个数在数组中的下标
            两重循环
            以下代码时间复杂度太高
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]
        选取的两个数不可能都小于和的一半，也不可能都大于和的一半
        时间复杂度仍然是n的平方。第一道题也不简单。
        '''
        small=int(target/2)
        if(target<0):
            small=small-1
        big=small+1
        index=0
        num_index={}
        for i in range(len(nums)):
            num_index[nums[i]]=[]
        for i in range(len(nums)):
            num_index[nums[i]].append(i)
        nums_sort=sorted(nums)
        for i in range(len(nums_sort)):
            if(nums_sort[i]<small):
                index=index+1
            elif(nums_sort[i]==small):
                index=index+1
                break
            else:
                break
        print(index)
        num1=nums_sort[0:index]
        num2=nums_sort[index:]
        n1=len(num1)
        n2=len(num2)
        for i in range(n2):
            for j in range(n1):
                if(num1[n1-j-1]+num2[i]<target):
                    break
                if(num1[n1-j-1]+num2[i]==target):
                    x=num_index[num1[n1-j-1]][0]
                    y=0
                    if(num1[n1-j-1]==num2[i]):
                        y=num_index[num1[n1-j-1]][1]
                    else:
                        y=num_index[num2[i]][0]
                    return sorted([x,y])






if(__name__=="__main__"):
    s=Solution()
    nums = [2, 7, 11, 15]
    nums=[3,3]
    target = 6
    print(s.twoSum(nums,target))
