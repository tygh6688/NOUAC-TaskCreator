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
```

---

## 🚀 Usage | 使用方法
Download the attached NOUAC-TaskCreator.exe
Right-click → Run as administrator
Select any .exe application
The task and shortcut will be created automatically
下载附件中的 NOUAC-TaskCreator.exe
右键文件 → 以管理员身份运行
选择任意需要自启的 exe 程序
程序自动创建计划任务和桌面快捷方式

---

## ⚙️ Task Configuration | 任务配置详情
表格
Setting	English Description	中文说明
Trigger	On user logon	用户登录系统时
Privilege	Highest available	系统最高可用权限
Power Restriction	None	无电池 / 电源限制
Compatibility	Windows 10 / 11	兼容 Win10 / Win11
Shortcut Command	schtasks /run /tn "TaskName"	双击快捷方式即可立即执行任务

---

## ⚠️ Important Notes | 重要说明
Must run as administrator, otherwise task creation will fail
Auto skip UAC popup via system highest privilege schedule task
Desktop shortcut auto created for one-click manual run
必须以管理员身份启动程序，否则无法创建高权限任务
通过系统最高权限计划任务机制，实现无 UAC 弹窗后台自启
自动生成桌面快捷方式，随时可以双击手动启动程序

---

## 📄 License | 开源协议
MIT License - Free to use, modify, and distribute, provided the original copyright notice is retained.
MIT 许可证 - 可免费使用、修改、分发，仅需保留原始版权声明。
