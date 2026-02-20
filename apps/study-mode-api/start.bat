@echo off
REM Clean startup script for Study Mode API
REM Kills existing processes and starts fresh

echo ============================================================
echo STUDY MODE API - CLEAN STARTUP
echo ============================================================

REM Kill any Python processes on port 8000
echo [Cleanup] Killing existing processes...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    echo [Cleanup] Killing PID %%a
    taskkill /F /PID %%a 2>nul
)

REM Also kill stray python processes
taskkill /F /IM python.exe 2>nul

REM Wait for cleanup
timeout /t 2 /nobreak >nul

REM Start the server
echo [Startup] Starting server...
cd /d %~dp0src
set PYTHONUNBUFFERED=1
python -m uvicorn study_mode_api.main:app --host 127.0.0.1 --port 8000 --log-level info
