# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#判斷寫法

drive = input("你有開車嗎？(y/n)")
if drive != 'y' and drive != 'n':
    print('輸入錯誤')
    #可在這裡寫 raise SystemExit 做中斷程式
elif drive == 'y':
    age = input("請問年齡？")
    age = int(age)
    if age < 18:
        print('你無照喔')
    else:
        print('所以你有駕照')
elif drive == 'n':
    age = input("請問年齡？")
    age = int(age)
    if age < 18:
        print('那就等到成年在考駕照')
    else:
        print('有空去考個駕照喔')