@echo off
:: UI Language: en_US = English, ar_SA = Arabic
:: To run in Arabic:  set VIRALS_LANGUAGE=ar_SA
:: To run in English: set VIRALS_LANGUAGE=en_US
set VIRALS_LANGUAGE=en_US
call .venv\Scripts\activate.bat
python webui\app.py
pause
