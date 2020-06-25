@echo off
chcp 65001
::要备份的文件夹的路径
set frompath="C:\Users\asd\Desktop\IronPython"
::要备份的文件夹的名字
set floder=p11952
::备份的位置
set topath=c:

set currentDate=%date:~3,4%年%date:~8,2%月-备份
set currentTime=%date:~3,4%-%date:~8,2%-%date:~11,2%___%time:~0,2%-%time:~3,2%-%time:~6,2%-备份
echo.%currentDate%
echo.%currentTime%
::set tdate=%date:~0,4%year%date:~5,2%-%date:~8,2%day
::set baktime=%time:~0,2%时%time:~3,2%分%time:~6,2%秒-备份-y
::xcopy %frompath%\*.* %topath%\%YY%年%MM%月%DD\%日\%h%时%m%分%s%秒\%floder%\ /E/y
xcopy %frompath%\*.* %topath%\%currentDate%\%currentTime%\%floder%\ /E/y

::运行结束后cmd不自动关闭
::set Year=%date:~3,4%
::set MM=%date:~8,2%
::set DD=%date:~11,2%
::set h=%time:~0,2%
::set m=%time:~3,2%
::set s=%time:~6,2%
::echo.%Year%
::echo.%MM%
::echo.%DD%
::echo.%h%
::echo.%m%
::echo.%s%
::pause

