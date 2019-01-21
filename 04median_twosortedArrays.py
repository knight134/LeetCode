#!/usr/bin/python
# -*-coding:utf8 -*-

__author__="wanglongfei@genomics.cn"

import  os


class Solution():
    def findMedianSortedArrays(self,nums1,nums2):
        m=len(nums1)
        n=len(nums2)
        result=self.findNmin(nums1,nums2,int((m+n+1)/2))
        print(int((m+n+1)/2))
        print(result)
        if((m+n)%2==1):
            return result[0]
        else:
            return (result[0]+result[1])/2

    def findNmin(self,nums1,nums2,n):
        # 返回两个数组中第 N小的数，并返回相关的位置
        l=0
        r=n-1
        length1=len(nums1)
        length2=len(nums2)
        if(length1==1 and length2==1):
            return [nums1[0],nums2[0]]
        a=[]
        b=[]
        if(length1>=length2):
            a=nums1
            b=nums2
        else:
            a=nums2
            b=nums1
        length1=len(a)
        length2=len(b)
        # b 数组是比较短的数组
        if(length2<n):
            if(b[length2-1]<=a[n-length2-1]):
                return [a[n-length2-1],a[n-length2]]
            else:
                if(b[length2-1]>a[n-length2]):
                    l=n-length2-1
                else:
                    return [b[length2-1],a[n-length2]]
        if(a[-1]<=b[0]):
            if(n<length1):
                return [a[n-1],a[n]]
            elif(n==length1):
                return [a[n-1],b[0]]
            else:
                return [b[n-length1-1],b[n-length1]]
        if(b[-1]<=a[0]):
            if(n<length2):
                return [b[n-1],b[n]]
            elif(n==length2):
                return [b[n-1],a[0]]
            else:
                return [a[n-length2-1],a[n-length2]]
                    
        while(l<=r):
            x=int((l+r)/2)
            tmp=0
            print("x\t"+str(x))
            '''
            if((n-x)>length2):
                l=x+1
                print("-l\t"+str(l))
                if(l>=r):
                    tmp=a[r]
                    # 
                    if(tmp<b[length2-1]):
                    tmp1=0
                    # 下一个值 初始化
                    if(b[length2-1]>=tmp):
                        tmp1=b[length2-1]
                    if(r+1<length1):
                        if(tmp1<=a[r+1]):
                            tmp1=a[r+1]
                    return [tmp,tmp1]
                continue
            '''
            if(length2<n-x):
                pass
            else:
                if(a[x]<b[n-x-2]):
                    if(n-x-2>=0):
                        tmp=b[n-x-2]
                    else:
                        tmp=b[0]
                else:
                    tmp=a[x]
                print(tmp)
                if(tmp>b[n-x-1]):
                    r=x-1
                    print("r\t"+str(r))
                elif(tmp>a[x+1]):
                    l=x+1
                    print("l\t"+str(l))
                else:
                    print("here")
                    tmp1=0
                    if(length1<=x+1):
                        tmp1=a[length1-1]
                    else:
                        tmp1=a[x+1]
                    if(a[x+1]>b[n-x-1]):
                        tmp1=b[n-x-1]
                    return [tmp,tmp1]

if(__name__=="__main__"):
    s=Solution()
    a=[3]
    b=[1,2,6]
    print(a)
    print(b)
    print(s.findMedianSortedArrays(a,b))

