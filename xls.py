# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xlrd
from pyExcelerator import *
import xlwt
from xlutils.copy import copy

def createXLSX(fname,sheetname,beginRows,nameCols,valueCols,Rows,saveFile):
    bk=xlrd.open_workbook(fname)
    shxrange=range(bk.nsheets)
    try:
        sh=bk.sheet_by_name(sheetname)
    except:
        print "no sheet in %s named Sheet1" %fname
    nrows=sh.nrows
    ncols=sh.ncols
    print "nrows %d ncols %d" %(nrows,ncols)
    name=''
    value=0.0
    adict={}
    for i in range(beginRows,Rows):
        name=sh.cell_value(i,nameCols)
        value=float(sh.cell_value(i,valueCols))
        if adict.has_key(name)==False:
            adict[name]=value
        else:
            if adict[name]>value:
                adict[name]=value
    keys=adict.keys()
    keys.sort(reverse=False)
    xint=Workbook()
#xfloat=Workbook()
    ws=xint.add_sheet('Sheet1')
    ws.write(0,0,'name')
    ws.write(0,1,'base')
    i=1
    for key in keys:
        ws.write(i,0,key)
        ws.write(i,1,adict[key])
        i+=1
    xint.save(saveFile)

def getXLSX(fname,sheetname,beginRow,nameCol,valueCol,Rows):
    bk=xlrd.open_workbook(fname)
    print '%s\n'%fname
    shxrange=range(bk.nsheets)
    try:
        sh=bk.sheet_by_name(sheetname)
    except:
        print "no sheet in %s named Sheet1" %fname
    name=''
    value=0.0
    adict={}
    for i in range(beginRow,Rows):
        name=sh.cell_value(i,nameCol)
        value=float(sh.cell_value(i,valueCol))
        if adict.has_key(name)==False:
            adict[name]=value
        else:
            if adict[name]>value:
                adict[name]=value
    return adict
'''
    for key in adict.keys():
        print '%s %f\n' %(key,adict[key])
'''

def insertValue(fname,name,beginRow,valueCol,rows,adict):
    oldWb=xlrd.open_workbook(fname)
    newWb=copy(oldWb)
    newWs=newWb.get_sheet(0)
    newWs.write(beginRow-1,valueCol,name)
    keys=adict.keys()
    keys.sort(reverse=False)
    i=beginRow
    for key in keys:
        newWs.write(i,valueCol,adict[key])
        i+=1
    newWb.save(fname)

'''
int float init
'''
fname='/home/zy/codes/Python/xls/BSPECCPU——base.xlsx'
sheetname='Sheet1'
beginRows=3
nameCols=0
valueCols=2
Rows=41
saveFile='/home/zy/codes/Python/xls/baseInt.xlsx'
createXLSX(fname,sheetname,beginRows,nameCols,valueCols,Rows,saveFile)
nameCols=7
valueCols=9
Rows=53
saveFile='/home/zy/codes/Python/xls/baseFloat.xlsx'
createXLSX(fname,sheetname,beginRows,nameCols,valueCols,Rows,saveFile)

'''
insert values
'''
intFile='/home/zy/codes/Python/xls/baseInt.xlsx'
floatFile='/home/zy/codes/Python/xls/baseFloat.xlsx'

adict={}
fname='/home/zy/codes/Python/xls/HNBSPECCPU.xlsx'
beginRow=2
sheetname='Sheet1'
nameCol=0
valueCol=2
Rows=15
adict=getXLSX(fname,sheetname,beginRow,nameCol,valueCol,Rows)
iBeginRow=1
iValueCol=2
insertValue(intFile,'HNB',iBeginRow,iValueCol,Rows,adict)

fBeginRow=2
fRows=19
fNameCol=14
fValueCol=16
adict=getXLSX(fname,sheetname,fBeginRow,fNameCol,fValueCol,fRows)
ffBeginRow=1
ffValueCol=2
ffRows=18
insertValue(floatFile,'HNB',ffBeginRow,ffValueCol,ffRows,adict)


adict.clear()
beginRow=0
Rows=13
iValueCol+=1
fname='/home/zy/codes/Python/xls/VBSPECCPU.xlsx'
adict=getXLSX(fname,sheetname,beginRow,nameCol,valueCol,Rows)
insertValue(intFile,'VB',iBeginRow,iValueCol,Rows,adict)

fBeginRow=0
fRows=16
fNameCol=7
fValueCol=9
adict=getXLSX(fname,sheetname,fBeginRow,fNameCol,fValueCol,fRows)
ffBeginRow=1
ffValueCol+=1
ffRows=17
insertValue(floatFile,'VB',ffBeginRow,ffValueCol,ffRows,adict)


adict.clear()
beginRow=1
Rows=14
iValueCol+=1
fname='/home/zy/codes/Python/xls/Xen+SPECCPU.xlsx'
adict=getXLSX(fname,sheetname,beginRow,nameCol,valueCol,Rows)
insertValue(intFile,'Xen',iBeginRow,iValueCol,Rows,adict)

fBeginRow=1
fRows=18
fNameCol=5
fValueCol=7
adict=getXLSX(fname,sheetname,fBeginRow,fNameCol,fValueCol,fRows)
ffBeginRow=1
ffValueCol+=1
ffRows=18
insertValue(floatFile,'Xen',ffBeginRow,ffValueCol,ffRows,adict)


adict.clear()
beginRow=0
Rows=13
iValueCol+=1
fname='/home/zy/codes/Python/xls/VNBSPECCPU.xlsx'
adict=getXLSX(fname,sheetname,beginRow,nameCol,valueCol,Rows)
insertValue(intFile,'VNB',iBeginRow,iValueCol,Rows,adict)

fBeginRow=0
fRows=17
fNameCol=8
fValueCol=10
adict=getXLSX(fname,sheetname,fBeginRow,fNameCol,fValueCol,fRows)
ffBeginRow=1
ffValueCol+=1
ffRows=18
insertValue(floatFile,'VNB',ffBeginRow,ffValueCol,ffRows,adict)
#ws=xint.add_sheet('sheet1')
#wss=xfloat.add_sheet('sheet1')
#xfloat.save('/home/zy/codes/Python/xls/baseFloat.xlsx')
'''
fname = "/home/zy/codes/Python/xls/BSPECCPU——base.xlsx"
bk=xlrd.open_workbook(fname)
shxrange=range(bk.nsheets)
try:
    sh=bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" %fname
nrows=sh.nrows
ncols=sh.ncols
print "nrows %d ncols %d" %(nrows,ncols)

beginRows=3
nameCols=0
valueCols=2
name=''
value=0.0
Rows=41
adict={}
for i in range(beginRows,Rows):
    name=sh.cell_value(i,nameCols)
    value=float(sh.cell_value(i,valueCols))
    if adict.has_key(name)==False:
        adict[name]=value
    else:
        if adict[name]>value:
            adict[name]=value
keys=adict.keys()
keys.sort(reverse=False)
xint=Workbook()
#xfloat=Workbook()
ws=xint.add_sheet('sheet1')
ws.write(0,0,'name')
ws.write(0,1,'base')
i=1
for key in keys:
    ws.write(i,0,key)
    ws.write(i,1,adict[key])
    i+=1
xint.save('/home/zy/codes/Python/xls/baseInt.xlsx')
#ws=xint.add_sheet('sheet1')
#wss=xfloat.add_sheet('sheet1')
#xfloat.save('/home/zy/codes/Python/xls/baseFloat.xlsx')
'''