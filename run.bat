@echo off
call E:\automationteststore\.venv\Scripts\activate.bat
rem pytest -s -v -m "sanity" --html E:\automationteststore\reports\report.html --browser chrome 
rem pytest -s -v -m "regression" --html E:\automationteststore\reports\report.html --browser chrome 
rem pytest -s -v -m "sanity and regression" --html E:\automationteststore\reports\report.html --browser chrome 
pytest -s -v -m "sanity or regression" --html E:\automationteststore\reports\report.html --browser chrome 
pause