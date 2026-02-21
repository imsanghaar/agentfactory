@echo off
REM Progress API - Quick Start Script for Windows
REM This script starts the Progress API server

echo ========================================
echo Progress API - Starting Server
echo ========================================
echo.

REM Check if .env file exists
if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo.
    echo IMPORTANT: Edit .env to configure your database connection
    echo Default config uses SQLite for easy setup
    echo.
)

REM Check if Python environment is available
where uv >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: uv is not installed or not in PATH
    echo Install uv from: https://docs.astral.sh/uv/getting-started/installation/
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing dependencies...
uv sync --quiet

echo.
echo ========================================
echo Starting Progress API on port 8002
echo ========================================
echo.
echo Server will start at: http://localhost:8002
echo Health check: http://localhost:8002/health
echo.
echo Press Ctrl+C to stop the server
echo.

REM Start the server
uv run uvicorn progress_api.main:app --reload --port 8002
