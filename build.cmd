@echo off
title Builder
color 0E
rd /S /Q build
rd /S /Q dist
del /Q main.spec
echo old data cleared
pyinstaller --onefile --icon=icon.ico -c main.py
pyinstaller --onefile --icon=icon.ico -c guildCreator.py
pyinstaller --onefile -c uri.py
start dist\
rem start "starting..." /D "./dist/" main.exe
rem timeout /T 3
rd /S /Q build
del /Q *.spec