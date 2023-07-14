#!/usr/bin/python3
def element_at(m_list, idx):
    if idx >= len(m_list) or idx < 0:
        return None
    return m_list[idx]
