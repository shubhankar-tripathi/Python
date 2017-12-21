# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Display:
    def _init_(self):
        pass
    def disp(self,char, num = None):
        if num != None:
            print(char,num)
        else:
            print(char)
def main():
    dsp = Display()
    dsp.disp('s')
    dsp.disp('s',12)
if __name__=="__main__":
    main()


