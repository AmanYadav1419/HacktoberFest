#!/usr/bin/env python
# coding: utf-8

# In[3]:


def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "123321"
if ans := isPalindrome(s):
	print("Yes")
else:
	print("No")


# In[ ]:




