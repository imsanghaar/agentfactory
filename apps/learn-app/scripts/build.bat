@echo off
REM Build script for Windows

cd /d "%~dp0.."

REM Increase heap size for OG image generation
set NODE_OPTIONS=--max-old-space-size=4096

npx docusaurus build
