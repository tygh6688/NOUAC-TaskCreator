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
