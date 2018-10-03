@echo off
set time = 10
for /l %%i in (1,1,%time%) do (
    echo counter:%%i%
)
echo %time%
pause