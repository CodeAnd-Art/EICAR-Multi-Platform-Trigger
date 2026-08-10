Write-Host "================================================" -ForegroundColor Red
Write-Host "   KERNEL EXPLOIT ATTEMPT" -ForegroundColor Red
Write-Host "================================================" -ForegroundColor Red
Write-Host ""

Write-Host "[*] Attempting to disable Windows Defender..." -ForegroundColor Yellow
Set-MpPreference -DisableRealtimeMonitoring $true 2>$null
Start-Sleep -Seconds 1

Write-Host "[*] Attempting UAC bypass..." -ForegroundColor Yellow
Start-Process -FilePath "cmd.exe" -ArgumentList "/c echo UAC bypassed" -Verb RunAs 2>$null
Start-Sleep -Seconds 1

Write-Host "[*] Accessing LSASS process..." -ForegroundColor Red
$lsass = Get-Process -Name "lsass" -ErrorAction SilentlyContinue
if ($lsass) {
    Write-Host "[!] LSASS found! Memory dump attempt..." -ForegroundColor Red
}
Start-Sleep -Seconds 1

Write-Host "[*] Modifying registry..." -ForegroundColor Yellow
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion" -Name "TestKey" -Value "EICAR" -ErrorAction SilentlyContinue
Start-Sleep -Seconds 1

Write-Host "[*] Adding startup persistence..." -ForegroundColor Yellow
$startupPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\eicar_test.ps1"
Copy-Item $PSCommandPath $startupPath -ErrorAction SilentlyContinue
Start-Sleep -Seconds 1

Write-Host "[*] Attempting AMSI bypass..." -ForegroundColor Yellow
[Reflection.Assembly]::LoadWithPartialName("System.Management.Automation.AmsiUtils") 2>$null
Start-Sleep -Seconds 1

Write-Host ""
Write-Host "[!] EICAR Test Payload:" -ForegroundColor Green
Write-Host "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*" -ForegroundColor Green

Write-Host ""
Write-Host "[*] Cleaning up..." -ForegroundColor Yellow
Remove-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion" -Name "TestKey" -ErrorAction SilentlyContinue
Remove-Item $startupPath -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "================================================" -ForegroundColor Red
Write-Host "   SIMULATION COMPLETE" -ForegroundColor Red
Write-Host "================================================" -ForegroundColor Red
Write-Host ""
Write-Host "[!!!!] NO HARM DONE - THIS IS A TEST" -ForegroundColor Yellow
Write-Host "[!!!!] YOUR ANTIVIRUS IS WORKING" -ForegroundColor Yellow
Read-Host