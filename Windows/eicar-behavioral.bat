@echo off
title SYSTEM BREACH
color 0c
cls

echo ===============================================
echo    SYSTEM COMPROMISE DETECTED
echo ===============================================
echo.

REM 1. Privilege Escalation
echo [*] Attempting privilege escalation...
whoami /groups | find "S-1-16-12288" > nul
if %errorlevel%==0 (
    echo [*] Admin privileges detected!
) else (
    echo [*] Attempting to elevate privileges...
)
timeout /t 2 /nobreak > nul

REM 2. UAC Bypass
echo [*] Attempting UAC bypass...
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemCheck" /t REG_SZ /d "%0" /f > nul 2>&1
timeout /t 2 /nobreak > nul

REM 3. Disable Defender
echo [*] Attempting to disable Windows Defender...
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d 1 /f > nul 2>&1
timeout /t 2 /nobreak > nul

REM 4. Access LSASS
echo [*] Accessing LSASS process...
tasklist | find "lsass.exe" > nul
if %errorlevel%==0 (
    echo [*] LSASS process found!
)
timeout /t 2 /nobreak > nul

REM 5. Kernel Access
echo [*] Attempting kernel memory access...
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" /v "DisablePagingExecutive" /t REG_DWORD /d 1 /f > nul 2>&1
timeout /t 2 /nobreak > nul

REM 6. Registry Modification
echo [*] Modifying registry...
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ShowSuperHidden" /t REG_DWORD /d 0 /f > nul 2>&1
timeout /t 2 /nobreak > nul

REM 7. Startup Persistence
echo [*] Adding startup persistence...
copy "%0" "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\system_check.bat" > nul 2>&1
timeout /t 2 /nobreak > nul

REM 8. EICAR Payload
echo.
echo [!] EICAR Test Payload executing...
echo X5O!P%%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
echo.

REM 9. Cleanup (Simulation)
echo [*] Cleaning up simulated activity...
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemCheck" /f > nul 2>&1
reg delete "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /f > nul 2>&1
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v "ShowSuperHidden" /f > nul 2>&1
del "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\system_check.bat" > nul 2>&1

echo ===============================================
echo    SIMULATION COMPLETE
echo ===============================================
echo.
echo [!!!!] NO HARM DONE - THIS IS A TEST
echo [!!!!] YOUR ANTIVIRUS IS WORKING
echo.
pause