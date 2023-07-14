#!/usr/bin/python3
def replace_in_list(m_list, idx, element):
    if idx >= len(m_list) or idx < 0:
        return m_list
    m_list[idx] = element
    return m_list
