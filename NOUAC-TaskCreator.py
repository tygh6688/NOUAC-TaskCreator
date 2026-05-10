import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import tempfile
import ctypes
import winshell
from win32com.client import Dispatch

# ==============================================
# 程序名称：NOUAC TaskCreator (缩写：NTC)
# 核心说明：必须以管理员身份运行 | Must run as administrator
# 功能：创建登录启动、最高权限、无电源限制的计划任务 + 桌面快捷一键运行
# ==============================================

def is_admin():
    """检查程序是否以管理员权限运行"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# ====================== 主功能：创建计划任务 ======================
def create_scheduled_task():
    # 强制管理员权限检查
    if not is_admin():
        messagebox.showerror(
            "ERROR | 权限错误",
            "PROGRAM: NOUAC TaskCreator (NTC)\n\n"
            "ERROR: This program MUST run as ADMINISTRATOR!\n"
            "错误：本程序必须【以管理员身份运行】！"
        )
        return

    # 创建隐藏窗口
    root = tk.Tk()
    root.title("NOUAC TaskCreator | NTC - Must Run As Admin")
    root.withdraw()

    # 选择EXE
    exe_path = filedialog.askopenfilename(
        title="NOUAC TaskCreator (NTC) | 请选择EXE程序 - MUST RUN AS ADMIN",
        filetypes=[("Executable Program", "*.exe"), ("All Files", "*.*")]
    )

    if not exe_path:
        messagebox.showinfo("NTC", "No file selected. Program exit.")
        return

    # 生成任务名
    exe_name = os.path.splitext(os.path.basename(exe_path))[0]
    prefix = exe_name[:3] if len(exe_name) >= 3 else exe_name
    task_name = f"{prefix}NUAC"

    # XML任务配置：登录启动 + 最高权限 + 无电源限制 + Win10
    task_xml = f'''<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2026-05-10T00:00:00</Date>
    <Author>NOUAC_TaskCreator</Author>
    <URI>\\{task_name}</URI>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>{os.environ['USERDOMAIN']}\\{os.getlogin()}</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>"{exe_path}"</Command>
    </Exec>
  </Actions>
</Task>'''

    try:
        # 写入临时XML
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-16', suffix='.xml', delete=False) as f:
            f.write(task_xml)
            temp_xml = f.name

        # 创建任务
        cmd = [
            'schtasks', '/Create',
            '/TN', task_name,
            '/XML', temp_xml,
            '/F'
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        os.unlink(temp_xml)

        # 创建成功 → 创建桌面快捷方式
        if res.returncode == 0:
            ok, path = create_desktop_shortcut(task_name)
            if ok:
                messagebox.showinfo(
                    "NOUAC TaskCreator | SUCCESS",
                    f"✅ Task created successfully!\n"
                    f"✅ Desktop shortcut created!\n\n"
                    f"Task Name: {task_name}\n"
                    f"Shortcut: {path}\n\n"
                    f"Run on logon • Highest privileges • NO UAC\n"
                    f"Must run as administrator"
                )
            else:
                messagebox.showwarning("NTC", f"Task OK\nShortcut failed: {path}")
        else:
            messagebox.showerror("NTC ERROR", f"Task failed\n{res.stderr}")

    except Exception as e:
        messagebox.showerror("NTC ERROR", f"Exception: {str(e)}")

# ====================== 创建桌面快捷方式（winshell 纯原生，无VBS） ======================
def create_desktop_shortcut(task_name):
    try:
        desktop = winshell.desktop()
        lnk_path = os.path.join(desktop, f"{task_name}.lnk")

        if os.path.exists(lnk_path):
            os.remove(lnk_path)

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(lnk_path)
        shortcut.TargetPath = "cmd.exe"
        shortcut.Arguments = f'/c schtasks /run /tn "{task_name}"'
        shortcut.WorkingDirectory = r"C:\Windows\System32"
        shortcut.WindowStyle = 7
        shortcut.Description = f"NOUAC Run Task: {task_name}"
        shortcut.IconLocation = r"C:\Windows\System32\cmd.exe,0"
        shortcut.Save()

        return (True, lnk_path) if os.path.exists(lnk_path) else (False, "Shortcut not created")

    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    create_scheduled_task()
