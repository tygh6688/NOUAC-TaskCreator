# NOUAC TaskCreator (NTC)
> **Must Run As Administrator • NO UAC • Auto Run On Logon • Highest Privileges**
> **必须以管理员身份运行 • 无UAC弹窗 • 登录自动启动 • 最高权限运行**

A lightweight Windows utility to create privileged scheduled tasks with one-click desktop shortcuts, eliminating UAC prompts for background applications.

一款轻量级 Windows 工具，用于创建最高权限计划任务，并自动生成桌面一键快捷方式，彻底消除后台程序的 UAC 提示。

---

## ✨ Features | 功能特点
- Admin-only execution / 强制管理员运行
- Logon trigger / 登录自动触发
- Highest privileges / 最高权限运行（无UAC）
- Power-agnostic / 无视电源限制
- One-click shortcuts / 一键快捷方式
- Win10/Win11 compatible / 系统兼容

---

## 📋 Requirements | 系统要求
- Windows 10 / 11
- Python 3.7+
- Must run as administrator / 必须以管理员身份运行

---

## 🛠️ Installation | 安装依赖
```bash
pip install pywin32 winshell
