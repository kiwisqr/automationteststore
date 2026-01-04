@echo off
setlocal

REM Always run from the Jenkins workspace (the checked-out GitHub repo)
cd /d "%~dp0"

REM Activate venv that lives inside the repo (relative path)
call .venv\Scripts\activate.bat

REM Ensure reports dir exists (since you gitignored/deleted it)
if not exist reports mkdir reports
if not exist logs mkdir logs
if not exist screenshots mkdir screenshots

REM Run only from repo, and force pytest rootdir to avoid scanning C:\
pytest -m sanity -q test_cases --browser chrome --headless test_cases --rootdir="%CD%"

endlocal