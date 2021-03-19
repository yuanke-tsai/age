# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#直接寫法
drive = input("你有開過車嗎？(y/n)")

if drive == 'y':
    age_y = input("請問年齡？")
    if int(age_y) < 18:
        print('你騙人')
    else:
        print('你也許開過')
else:
    print('瞭解你不會開車')