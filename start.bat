:: Activate Virtual Enviroment
@ECHO Step #1 - Generate Python Enviroment ...
@for /f "delims=" %%a in ('ver ^| findstr /v "linux"') do @set myvar=%%a
@echo %myvar%|find "Windows">nul && python -m venv env || echo python3 -m venv env
@ECHO Step #1 - Done

@ECHO Step #2 - Activating Virtual Environment ...
@CD env/Scripts && activate && CD ../.. && ECHO Step #2 - Done && ECHO Step #3 - Isntalling Requirements ... && pip3 install -r requirements.txt && ECHO Step #3 - Done