REM This script clears the cache of all ever installed python packages

:: Clearing all the cache for pip
pip cache purge

:: Checking whether 'uv' is installed and clearing all its cache if needed
@echo OFF
where uv >nul 2>&1

if %ERRORLEVEL% == 0 (
    @echo ON
    uv clean
)