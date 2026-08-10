# EICAR Module for Windows

## Advanced Antivirus Test Module

This is a Windows executable module designed to test antivirus software behavior.

## What This Module Does

| Function | Description |
|----------|-------------|
| Defender Bypass | Attempts to disable Windows Defender components (simulation) |
| AMSI Bypass | Attempts to bypass AMSI protection (simulation) |
| UAC Bypass | Attempts to bypass User Account Control (simulation) |
| Kernel Access | Simulates kernel memory access |
| LSASS Access | Simulates LSASS process access |
| Registry Modification | Creates test registry keys (simulation) |
| Persistence | Adds startup entry (simulation) |
| File Creation | Creates EICAR test files in multiple locations |
| Process Injection | Simulates process injection |
| Network Activity | Simulates C2 communication |
| Ransomware | Simulates file encryption |
| Kernel Exploit | Displays kernel exploit simulation messages |
| Auto Cleanup | Removes all created files and registry entries |

## What It Does NOT Do

- Does NOT delete any system files
- Does NOT modify any system files
- Does NOT steal any data
- Does NOT encrypt any real files
- Does NOT send any data anywhere
- Does NOT install anything permanent
- Does NOT harm your computer in any way

## Why Use This Module

- Test if your antivirus is working
- Test Windows Defender behavior
- Test EDR/XDR systems
- Learn how security software detects threats
- Safe and controlled testing environment

## How To Use

1. Download `eicar.module.exe` from the releases page
2. Run the executable
3. Watch your antivirus detect and block it
4. If nothing happens, consider upgrading your antivirus

## Build Instructions

```bash
pip install pyinstaller
pyinstaller --onefile --console --name eicar.module eicar.module.py

Notice

This is a test file. No actual harm is done to your system.
All actions are simulated and automatically cleaned up.

Disclaimer

Use at your own risk. The author is not responsible for any actions taken by your antivirus software.

---

EICAR Module v1.0

```

---