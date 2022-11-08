@echo off
title Builder
color 0E
rd /S /Q build
rd /S /Q dist
del /Q main.spec
echo old data cleared
pyinstaller --onefile -c main.py
start dist\main.exe
timeout /T 3
rd /S /Q build
del /Q main.spec