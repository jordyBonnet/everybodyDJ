# everybod**DJ**
is a free app on Heroku to let people tell a DJ what song they would like to hear

## Getting started
create your new project folder
as usual and create a virtual env also

## pip installs
```
pip install dash
pip install gunicorn
```
to update the requirements
```
pip freeze > requirements.txt
```

## PythonEverywhere


mkvirtualenv myvirtualenv --python=/usr/bin/python3.8
cd everybodyDJ§
pip install -r requirements.txt


[Active.ps1 issue with powershell](https://support.enthought.com/hc/en-us/articles/360058403072-Windows-error-activate-ps1-cannot-be-loaded-because-running-scripts-is-disabled-UnauthorizedAccess-):<br>
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
