#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 17:28:17 2017

@author: zhouyuzju
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
import xlrd
font_size=10
fig_size=(8,10)
baseArr=[]
VBArr=[]
HNBArr=[]
XenArr=[]
nameArr=[]
VNBArr=[]
fname='/home/zy/codes/Python/xls/baseInt.xlsx'
#custom_font=matplotlib.font_manager.FontProperties()

def getDataFromXLSX(fname,sheetName,nameCol,baseCol,HNBCol,VBCol,XenCol,VNBCol,beginRow,Rows):
    bk=xlrd.open_workbook(fname)
    sh=bk.sheet_by_name(sheetName)
    tmp=''
    for i in range(beginRow,Rows):
        nameArr.append(sh.cell_value(i,nameCol))
        baseArr.append(float(sh.cell_value(i,baseCol)))
        HNBArr.append(float(sh.cell_value(i,HNBCol)))
        VBArr.append(float(sh.cell_value(i,VBCol)))
        XenArr.append(float(sh.cell_value(i,XenCol)))
        VNBArr.append(float(sh.cell_value(i,VNBCol)))
 
def makeFigure(figureName,nameArr,baseArr,VBArr,HNBArr,XenArr,VNBArr):
    fig_size=(len(nameArr)*2,10)
    font_size=10
    for i in range(len(nameArr)):
#    for i in range(10):
        VBArr[i]=VBArr[i]/baseArr[i]
        HNBArr[i]=HNBArr[i]/baseArr[i]
        XenArr[i]=XenArr[i]/baseArr[i]
        VNBArr[i]=VNBArr[i]/baseArr[i]
        baseArr[i]=1
    plt.rcParams['font.size']=font_size
    plt.rcParams['figure.figsize']=fig_size
    bar_width=0.15
    index=np.arange(len(nameArr))
    baseRect=plt.bar(index-bar_width*2,baseArr,bar_width,color='r',label='base',hatch='-',edgecolor='black')
    VBRect=plt.bar(index-bar_width*1,VBArr,bar_width,color='b',label='VB',hatch='x',edgecolor='black')
    HNBRect=plt.bar(index+bar_width*0,HNBArr,bar_width,color='y',label='HNB',hatch='.',edgecolor='black')
    XenRect=plt.bar(index+bar_width*1,XenArr,bar_width,color='#0072BC',label='Xen',hatch='/',edgecolor='black')
    VNBRect=plt.bar(index+bar_width*2,VNBArr,bar_width,color='white',label='VNB',hatch='+',edgecolor='black')
    plt.xticks(index+bar_width*0,nameArr,rotation=40,size=15)

    plt.yticks(size=15)
    plt.ylabel('ratio',size=20,weight='normal')
#    plt.ylim=(0.5,2.5)
    plt.axis([-1,len(nameArr)+1,0.5,2.5])
#    plt.title(u'不同虚拟化场景下的benchmark性能损耗'.decode('utf-8').encode('cp936')) 
    plt.title('benchmark',size=15)
    plt.legend(loc='upper center',bbox_to_anchor=(0.5,-0.2),fancybox=True,ncol=10,fontsize='x-large')
    plt.imshow(cmap='gray')
 
    plt.savefig('/home/zy/codes/Python/xls/'+figureName+'.png')
#    plt.cla()
    
sheetName='Sheet1'
nameCol=0
baseCol=1
HNBCol=2
VBCol=3
XenCol=4
VNBCol=5
Rows=13
beginRow=1    
getDataFromXLSX(fname,sheetName,nameCol,baseCol,HNBCol,VBCol,XenCol,VNBCol,beginRow,Rows)
makeFigure('int',nameArr,baseArr,VBArr,HNBArr,XenArr,VNBArr)
nameArr=[]
baseArr=[]
HNBArr=[]
VBArr=[]
VNBArr=[]
XenArr=[]


fname='/home/zy/codes/Python/xls/baseFloat.xlsx'
nameCol=0
baseCol=1
HNBCol=2
VBCol=3
XenCol=4
Rows=17
beginRow=1
getDataFromXLSX(fname,sheetName,nameCol,baseCol,HNBCol,VBCol,XenCol,VNBCol,beginRow,Rows)
makeFigure('float',nameArr,baseArr,VBArr,HNBArr,XenArr,VNBArr)
