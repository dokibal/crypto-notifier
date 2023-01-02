REM upgrade pip
py -m pip install --upgrade pip
REM install virtualenv
py -m pip install --user virtualenv
REM create virtual environment venv
py -m venv venv
REM activate venv
.\env\Scripts\activate
REM print the location of python
where python
REM install packages using requirements.txt
py -m pip install -r requirements.txt