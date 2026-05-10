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

## 🚀 使用说明
下载附件中的 NOUAC-TaskCreator.exe 文件
右键点击该文件，选择 “以管理员身份运行”
选择任意可执行的.exe 应用程序
程序将自动创建系统计划任务和桌面快捷方式

---

## ⚙️ 任务配置详情
| 配置项 | 说明 |
|--------|------|
| 触发条件 | 用户登录系统时 |
| 运行权限 | 系统最高可用权限 |
| 电源限制 | 无电池或电源限制 |
| 系统兼容性 | Windows 10 / Windows 11 |
| 快捷方式命令 | schtasks /run /tn "TaskName" |

---

## ⚠️ 重要说明
必须以管理员身份运行程序，否则无法创建任务。
通过 Windows 最高权限计划任务机制，绕过 UAC 弹窗。
系统会自动生成桌面快捷方式，可随时手动一键启动。

---

## 📄 License | 开源协议
MIT License - Free to use, modify, and distribute, provided the original copyright notice is retained.
MIT 许可证 - 可免费使用、修改、分发，仅需保留原始版权声明。
