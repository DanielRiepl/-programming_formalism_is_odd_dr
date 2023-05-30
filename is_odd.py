#!/usr/bin/env python
# coding: utf-8

# In[8]:



def is_odd(x):
    """
    - Check is interger is provided
    - CHeck if integer is odd
    """
    if not isinstance(x, int):
        raise TypeError("Please input an integer")
    else:
        return (x % 2 != 0)


is_odd(2)


# In[ ]:




