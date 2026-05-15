@echo off
setlocal
title NorCuts

:: UI Language: en_US = English, ar_SA = Arabic
:: To run in Arabic:  set VIRALS_LANGUAGE=ar_SA
:: To run in English: set VIRALS_LANGUAGE=en_US
set VIRALS_LANGUAGE=en_US

cd /d "%~dp0"
call .venv\Scripts\activate.bat
python main_improved.py
echo.
pause
