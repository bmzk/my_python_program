::@echo off
set frompath=C:\Users\asd\Desktop
set floder="IronPython"
:: 设置日期相关变量
set year=%date:~0,4%
set month=%date:~5,2%
set day=%date:~8,2%
set hour=%date:~10,2%
set minute=%date:~12,2%
set topath=c:\%year%年%month%月%day%日\%hour%时%minute%分
:: 判断路径是否存在
:: 若路径存在且为目录 , 则无需任何处理	
xcopy C:\Users\asd\Desktop\IronPython\*.* c:\%year%年%month%月%day%日\%hour%时%minute%分\ /E/y


if exist %topath% (
	if exist %topath%\ (exit) 
	else (xcopy C:\Users\asd\Desktop\IronPython\*.* c:\work\%year%年%month%月%day%日\%hour%时%minute%分\ /E/y)
) 
xcopy C:\Users\asd\Desktop\IronPython\*.* c:\work\ /E/y
