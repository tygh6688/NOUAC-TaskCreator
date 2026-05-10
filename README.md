# NOUAC TaskCreator (NTC)
> **Must Run As Administrator • NO UAC • Auto Run On Logon • Highest Privileges**

A lightweight Windows utility to create **privileged scheduled tasks** with one-click desktop shortcuts, eliminating UAC prompts for background applications.

---

## ✨ Features
- **Admin-only execution**: Enforced admin check at startup
- **Logon trigger**: Tasks run automatically when the user logs in
- **Highest privileges**: Tasks execute with elevated permissions (no UAC popups)
- **Power-agnostic**: Ignores battery/power conditions for laptops
- **One-click shortcuts**: Auto-generates desktop shortcuts to launch tasks instantly
- **Win10/11 compatible**: Built for modern Windows task scheduler

---

## 📋 Requirements
- Windows 10 / Windows 11
- Python 3.7+
- Run the program **AS ADMINISTRATOR** (critical for task creation)

---

## 🛠️ Installation
Install required dependencies first:
```bash
pip install pywin32 winshell
```

---

## 🚀 Usage
Download the attached NOUAC-TaskCreator.exe  
Right-click the file and select Run as administrator  
Select any executable .exe application  
The program will automatically create a system scheduled task and a desktop shortcut

---

## ⚙️ Task Configuration
| Setting | English Description |
|---------|---------------------|
| Trigger | On user logon |
| Privilege | Highest available system authority |
| Power Restriction | No battery or power limitations |
| Compatibility | Windows 10 / Windows 11 |
| Shortcut Command | schtasks /run /tn "TaskName" |

---

## ⚠️ Important Notes
The program must be run as administrator, otherwise task creation will fail.  
Bypass UAC prompts by using Windows highest-privilege scheduled task mechanism.  
A desktop shortcut is automatically generated for manual one-click startup at any time.

---

## 📄 License
MIT License - Free to use, modify, and distribute, provided the original copyright notice is retained.
