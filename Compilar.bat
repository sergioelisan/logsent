@echo off
echo [COMPILANDO VERSAO PADRAO]
c:\Python26\python.exe setup.py py2exe


echo [ORGANIZANDO DIRETORIOS]
mkdir LogSent

copy  /y    dist\*.* __Dist__\
xcopy /y /e build    __Build__\
xcopy /y /e __Dist__ LogSent\

rar a LogSent.rar LogSent\
move LogSent.rar  __Release__\

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q LogSent

echo [COMPILANDO COM GUI]
c:\Python26\python.exe setupgui.py py2exe


echo [ORGANIZANDO DIRETORIOS]
mkdir LogSentXP

copy  /y    dist\*.*    __DistGUI__\
xcopy /y /e build       __BuildGUI__\
xcopy /y /e __DistGUI__ LogSentXP\

rar a LogSentXP.rar LogSentXP\ LogSentXP\__Images__\ LogSentXP\Gui\__Fonts__\
move  LogSentXP.rar __Release__\

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q LogSentXP


echo [ORGANIZANDO PROJETO]
rar a LogSentProject.rar *.* .settings\ __DistGUI__\ __BuildGUI__\ __Build__\ __Dist__\ __Docs__\ __Images__\ __Tests__\ Eval\ Gui\ Gui\__Fonts__\ Logic\ Util\ Wiri\
move LogSentProject.rar __Backup__\

echo.
echo.
echo "[FIM]"
echo.
echo.
pause