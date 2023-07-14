#!/usr/bin/python3
def print_reversed_list_integer(m_list=[]):
    if m_list:
        if len(m_list) > 0:
            l = len(m_list) - 1
            for i in m_list:
                print('{:d}'.format(m_list[l]))
                l -= 1
