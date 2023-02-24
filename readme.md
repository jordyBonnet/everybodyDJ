# everybod**DJ**
Webapp deployed on pythoneverywhere

[http://jordyb.pythonanywhere.com/](http://jordyb.pythonanywhere.com/)

## Getting started
create your new project folder
as usual and create a virtual env also

Then follow [this tutorial](https://www.youtube.com/watch?v=WOWVat5BgM4&t=552s)
[joint doc](https://drive.google.com/file/d/1HtJcu3ZWsDYEIv8srod16z4jD4HEeHuH/view)

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

mkvirtualenv myvirtualenv --python=/usr/bin/python3.10
cd everybodyDJ
pip install -r requirements.txt

## update code
commit push on github with virtual studio code
then in the bash command of PythonEverywhere write
```
cd everybodyDJ
```
Then
```
Git pull
```

If message: "Your local changes to the following files would be overwritten by merge: songs.db"<br>
do
```
git reset --hard origin/main
```

[Active.ps1 issue with powershell](https://support.enthought.com/hc/en-us/articles/360058403072-Windows-error-activate-ps1-cannot-be-loaded-because-running-scripts-is-disabled-UnauthorizedAccess-):<br>
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
