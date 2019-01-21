#!/usr/bin/python
# -*-coding:utf8 -*-

__author__="wanglongfei@genomics.cn"


import os

'''
链表表示一个数字。 两个数字相加
'''
class ListNode():
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution():
    def addTwoNumbers(self,l1,l2):
        r=ListNode(0)
        return self.add(l1,l2,r,0)
        


    def add(self,l1,l2,r,c):
        s=0
        if(l1 and l2):
            s=(l1.val+l2.val+c)
        if(not l1):
            s=l2.val+c
        if(not l2):
            s=l1.val+c
        carry=int(s/10)
        s=s%10
        r.val=s
        print(carry) 
        if(l1 and l2):
            if(l1.next or l2.next):
                r.next=ListNode(0)
                self.add(l1.next,l2.next,r.next,carry)
            else:
                if(carry>0):
                    r.next=ListNode(carry)
        if(not l1):
            if(l2.next):
                r.next=ListNode(0)
                self.add(None,l2.next,r.next,carry)
            else:
                if(carry>0):
                    r.next=ListNode(carry)
        if(not l2):
            if(l1.next):
                r.next=ListNode(0)
                self.add(l1.next,None,r.next,carry)
            else:
                if(carry>0):
                    r.next=ListNode(carry)
        if(carry>0):
            print("here")
        return r

    def show(self,l):
        print(str(l.val),end="")
        if(l.next):
            print("->",end="")
            self.show(l.next)
        else:
            print("")
    def creat(self,l):
        r=ListNode(0)
        self.covert(r,l,0)
        return r
    
    def covert(self,r,l,i):
        r.val=l[i]
        if(i+1<len(l)):
            r.next=ListNode(0)
            self.covert(r.next,l,i+1)


if(__name__=="__main__"):
    s=Solution()
    l1=s.creat([1])
    l2=s.creat([9,9,9,9])
    s.show(l1)
    s.show(l2)
    r=s.addTwoNumbers(l1,l2)
    s.show(r)

        
        
