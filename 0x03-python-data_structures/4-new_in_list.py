#!/usr/bin/python3
def new_in_list(m_list, idx, element):
    if idx >= len(m_list) or idx < 0:
        return m_list
    new_list = m_list[:]
    new_list[idx] = element
    return new_list
