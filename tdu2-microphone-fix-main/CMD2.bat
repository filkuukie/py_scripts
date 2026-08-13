@echo off
cd %SystemRoot%\System32
set "program_name=TestDrive2.exe"
:check_program

tasklist /FI "imagename eq %program_name%" | find /i "%program_name%" >nul 2>&1
if %errorlevel% == 1 (
  echo Waiting...
  timeout /t <wait_time_not_running> /nobreak  
  goto check_program
) else (
  echo "%program_name% is running, continuing..."
  goto continue
)

:continue
Set "[Key]=HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone"
For /F "tokens=3" %%# in ('Reg Query "%[Key]%" /v Value') Do (Set "[Data]=%%#")
If "%[Data]%"=="Allow" (REG Add "%[Key]%" /V Value /T REG_SZ /D Deny /F & Set "[M]=disabled")

TIMEOUT /T 10 /nobreak
Set "[Key]=HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\microphone"
For /F "tokens=3" %%# in ('Reg Query "%[Key]%" /v Value') Do (Set "[Data]=%%#")
If "%[Data]%"=="Deny" (REG Add "%[Key]%" /V Value /T REG_SZ /D Allow /F & Set "[M]=enabled")

taskkill /F /IM UpLauncher.exe
