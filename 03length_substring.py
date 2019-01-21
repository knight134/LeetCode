#!/usr/bin/python
# -*-coding:utf8 -*-

__author__="wanglongfei@genomics.cn"

import  os
'''
求一个字符串中，最长非重复子串的长度
'''

class Solution():
    def __init__(self):
        pass
    def lengthOfLongestSubstring(self,s):
        if(not s):
            return 0
        last_substring=s[0]
        current_substring=""

        for i in range(len(s)):
            # 当前字符对当前字符串的检查
            repeat_index=-1
            for j in range(len(current_substring)):
                if(s[i]==current_substring[j]):
                    repeat_index=j
                    break
            if(repeat_index>-1):
                # 字符串分裂成两部分
                before=current_substring[0:repeat_index+1]
                back=current_substring[repeat_index+1:]
                if(len(current_substring)>len(last_substring)):
                #    last_substring=before
                    last_substring=current_substring
                current_substring=back+s[i]
            else:
                current_substring=current_substring+s[i]
            print(last_substring)
        print(current_substring)
        if(len(last_substring)>len(current_substring)):
            print(last_substring)
            return len(last_substring)
        else:
            return len(current_substring)





if(__name__=="__main__"):
    s=Solution()
    s1="abcabcbb"
    s2="bbbbb"
    s3="pwwkew"
    s4="wanglongfei"
    print(s1+"\t"+str(s.lengthOfLongestSubstring(s4)))

    
