can you make a readme? for
(linuxgui code)
#!/usr/bin/env python3
import os
import shutil
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog, scrolledtext
import psutil
from time import time
import sys
import platform
import json
import glob

# ========== RED CYBERPUNK THEME ==========
BG_COLOR = "#120a0a"           # Dark red-black
FG_COLOR = "#ff0033"           # Red accent
BTN_COLOR = "#cc0000"          # Red button
BTN_ACTIVE_BG = "#ff3333"      # Bright red on press
PROGRESS_BG = "#330000"        # Dark red progress bar background
TAB_BG = "#221111"             # Slightly lighter than BG for tabs
TAB_ACTIVE = "#cc0000"         # Active tab color
TERMINAL_BG = "#110000"        # Very dark red for terminal
TERMINAL_FG = "#ff3366"        # Pink-red terminal text
TERMINAL_CURSOR = "#ffffff"    # White cursor
GLOW_COLOR = "#ff0066"         # Pink-red glow effect

# ========== MAIN WINDOW ==========
root = tk.Tk()
root.title("C00lgui v2.0 - CyberPanel [RED EDITION]")
root.configure(bg=BG_COLOR)
root.geometry("900x700")

style = ttk.Style()
style.theme_use('clam')
style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
style.configure("TNotebook.Tab", background=TAB_BG, foreground=FG_COLOR, padding=[15,5], font=('Courier New', 10, 'bold'), borderwidth=0)
style.map("TNotebook.Tab", background=[("selected", TAB_ACTIVE)], foreground=[("selected", "white")])
style.configure("red.Horizontal.TProgressbar", troughcolor=PROGRESS_BG, background=FG_COLOR, thickness=20)

def create_glow(event):
    event.widget.config(highlightbackground=GLOW_COLOR, highlightcolor=GLOW_COLOR, highlightthickness=2)
def remove_glow(event):
    event.widget.config(highlightbackground=BG_COLOR, highlightcolor=BG_COLOR, highlightthickness=0)

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# ========== TAB 1: DASHBOARD ==========
dash_tab = ttk.Frame(notebook)
notebook.add(dash_tab, text="Dashboard")
header_frame = tk.Frame(dash_tab, bg=BG_COLOR)
header_frame.pack(fill='x', pady=(10,20))
tk.Label(header_frame, text="SYSTEM DASHBOARD", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 16, "bold")).pack(side='left', padx=20)
grid_frame = tk.Frame(dash_tab, bg=BG_COLOR)
grid_frame.pack(fill='both', expand=True, padx=20, pady=10)
cpu_frame = tk.Frame(grid_frame, bg=BG_COLOR, bd=2, relief='groove', highlightbackground=FG_COLOR)
cpu_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
tk.Label(cpu_frame, text="CPU", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12, "bold")).pack()
cpu_var = tk.StringVar()
tk.Label(cpu_frame, textvariable=cpu_var, bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
cpu_progress = ttk.Progressbar(cpu_frame, orient='horizontal', style="red.Horizontal.TProgressbar")
cpu_progress.pack(fill='x', padx=5, pady=5)
ram_frame = tk.Frame(grid_frame, bg=BG_COLOR, bd=2, relief='groove', highlightbackground=FG_COLOR)
ram_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)
tk.Label(ram_frame, text="RAM", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12, "bold")).pack()
ram_var = tk.StringVar()
tk.Label(ram_frame, textvariable=ram_var, bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
ram_progress = ttk.Progressbar(ram_frame, orient='horizontal', style="red.Horizontal.TProgressbar")
ram_progress.pack(fill='x', padx=5, pady=5)
storage_frame = tk.Frame(grid_frame, bg=BG_COLOR, bd=2, relief='groove', highlightbackground=FG_COLOR)
storage_frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)
tk.Label(storage_frame, text="STORAGE", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12, "bold")).pack()
storage_var = tk.StringVar()
tk.Label(storage_frame, textvariable=storage_var, bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
storage_progress = ttk.Progressbar(storage_frame, orient='horizontal', style="red.Horizontal.TProgressbar")
storage_progress.pack(fill='x', padx=5, pady=5)
net_frame = tk.Frame(grid_frame, bg=BG_COLOR, bd=2, relief='groove', highlightbackground=FG_COLOR)
net_frame.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
tk.Label(net_frame, text="NETWORK", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12, "bold")).pack()
net_var = tk.StringVar()
tk.Label(net_frame, textvariable=net_var, bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
sys_frame = tk.Frame(grid_frame, bg=BG_COLOR, bd=2, relief='groove', highlightbackground=FG_COLOR)
sys_frame.grid(row=2, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)
tk.Label(sys_frame, text="SYSTEM INFO", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12, "bold")).pack()
uptime_var = tk.StringVar()
tk.Label(sys_frame, textvariable=uptime_var, bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
temp_var = tk.StringVar()
tk.Label(sys_frame, textvariable=temp_var, bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
os_var = tk.StringVar()
tk.Label(sys_frame, textvariable=os_var, bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
grid_frame.columnconfigure(0, weight=1)
grid_frame.columnconfigure(1, weight=1)
grid_frame.rowconfigure(0, weight=1)
grid_frame.rowconfigure(1, weight=1)
grid_frame.rowconfigure(2, weight=1)

# ========== TAB 2: WINE HQ ==========
wine_tab = ttk.Frame(notebook)
notebook.add(wine_tab, text="Wine HQ")
wine_frame = tk.Frame(wine_tab, bg=BG_COLOR)
wine_frame.pack(fill='both', expand=True, padx=20, pady=20)
wine_status = tk.StringVar()
wine_version = tk.StringVar()
status_frame = tk.Frame(wine_frame, bg=BG_COLOR)
status_frame.pack(pady=20)
tk.Label(status_frame, text="WINE STATUS:", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 14, "bold")).pack(side='left')
tk.Label(status_frame, textvariable=wine_status, bg=BG_COLOR, fg="white", font=("Courier New", 14)).pack(side='left', padx=10)
btn_frame = tk.Frame(wine_frame, bg=BG_COLOR)
btn_frame.pack(pady=20)
def check_wine():
    try:
        result = subprocess.run(["wine", "--version"], capture_output=True, text=True)
        version = result.stdout.strip() if result.stdout else result.stderr.strip()
        wine_status.set("ACTIVE")
        wine_version.set(f"Version: {version}")
        return True
    except:
        wine_status.set("INACTIVE")
        wine_version.set("Not installed")
        return False
def install_wine():
    if messagebox.askyesno("Install Wine", "Wine is not installed. Install it now?"):
        try:
            subprocess.run(["sudo", "apt", "update"], check=True)
            subprocess.run(["sudo", "apt", "install", "-y", "wine"], check=True)
            messagebox.showinfo("Success", "Wine installed successfully!")
            check_wine()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install Wine:\n{e}")
def run_exe():
    if not check_wine():
        messagebox.showerror("Error", "Wine is not installed!")
        return
    file_path = filedialog.askopenfilename(title="Select an EXE file", filetypes=[("Windows Executable", "*.exe")])
    if file_path:
        try:
            subprocess.Popen(["wine", file_path])
            messagebox.showinfo("Running", f"Running {file_path} with Wine.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run the exe:\n{e}")
def create_wine_prefix():
    path = filedialog.askdirectory(title="Select Wine Prefix Location")
    if path:
        try:
            os.environ["WINEPREFIX"] = path
            subprocess.run(["wine", "wineboot"], check=True)
            messagebox.showinfo("Success", f"Wine prefix created at {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create prefix:\n{e}")
buttons = [
    ("Check Wine", check_wine),
    ("Install Wine", install_wine),
    ("Run EXE", run_exe),
    ("Create Prefix", create_wine_prefix)
]
for text, cmd in buttons:
    btn = tk.Button(btn_frame, text=text, command=cmd, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 12, "bold"), relief='raised', bd=3)
    btn.pack(side='left', padx=10, ipadx=10, ipady=5)
    btn.bind("<Enter>", create_glow)
    btn.bind("<Leave>", remove_glow)
version_frame = tk.Frame(wine_frame, bg=BG_COLOR)
version_frame.pack(pady=10)
tk.Label(version_frame, textvariable=wine_version, bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12)).pack()

# ========== TAB 3: TERMINAL ==========
term_tab = ttk.Frame(notebook)
notebook.add(term_tab, text="Terminal")
term_frame = tk.Frame(term_tab, bg=BG_COLOR)
term_frame.pack(fill='both', expand=True, padx=10, pady=10)
term_output = scrolledtext.ScrolledText(term_frame, bg=TERMINAL_BG, fg=TERMINAL_FG, insertbackground=TERMINAL_CURSOR, font=("Courier New", 12), wrap=tk.WORD)
term_output.pack(fill='both', expand=True)
term_output.insert(tk.END, "C00lgui Terminal v2.0 [RED EDITION] - Type commands below\n")
term_output.insert(tk.END, "=====================================================\n\n")
cmd_frame = tk.Frame(term_frame, bg=BG_COLOR)
cmd_frame.pack(fill='x', pady=(10,0))
tk.Label(cmd_frame, text=">", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12)).pack(side='left')
cmd_entry = tk.Entry(cmd_frame, bg=TERMINAL_BG, fg=TERMINAL_FG, insertbackground=TERMINAL_CURSOR, font=("Courier New", 12), relief='sunken', bd=3)
cmd_entry.pack(side='left', fill='x', expand=True, padx=5)
cmd_entry.bind("<Return>", lambda e: execute_command())
def execute_command():
    command = cmd_entry.get()
    if not command:
        return
    term_output.insert(tk.END, f"> {command}\n")
    term_output.see(tk.END)
    cmd_entry.delete(0, tk.END)
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        if stdout:
            term_output.insert(tk.END, stdout + "\n")
        if stderr:
            term_output.insert(tk.END, f"Error: {stderr}\n", "error")
    except Exception as e:
        term_output.insert(tk.END, f"Failed to execute: {str(e)}\n", "error")
    term_output.see(tk.END)
term_output.tag_config("error", foreground="#ff6666")
term_btn_frame = tk.Frame(term_frame, bg=BG_COLOR)
term_btn_frame.pack(fill='x', pady=(10,0))
def clear_terminal():
    term_output.delete(1.0, tk.END)
tk.Button(term_btn_frame, text="Clear", command=clear_terminal, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 10, "bold")).pack(side='left', padx=5)

# ========== TAB 4: NERD STATS ==========
nerd_tab = ttk.Frame(notebook)
notebook.add(nerd_tab, text="Nerd Stats")
nerd_frame = tk.Frame(nerd_tab, bg=BG_COLOR)
nerd_frame.pack(fill='both', expand=True, padx=10, pady=10)
nerd_text = tk.Text(nerd_frame, bg=TERMINAL_BG, fg=TERMINAL_FG, font=("Courier New", 10), wrap=tk.WORD, padx=10, pady=10)
nerd_text.pack(fill='both', expand=True)
scrollbar = tk.Scrollbar(nerd_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
nerd_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=nerd_text.yview)
def get_nerd_stats():
    try:
        nerd_text.delete(1.0, tk.END)
        nerd_text.insert(tk.END, "=== SYSTEM INFORMATION ===\n", "header")
        nerd_text.insert(tk.END, f"OS: {platform.system()} {platform.release()}\n")
        nerd_text.insert(tk.END, f"Hostname: {platform.node()}\n")
        nerd_text.insert(tk.END, f"Processor: {platform.processor()}\n\n")
        nerd_text.insert(tk.END, "=== CPU DETAILS ===\n", "header")
        nerd_text.insert(tk.END, f"Cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count()} logical\n")
        nerd_text.insert(tk.END, f"Frequency: {psutil.cpu_freq().current:.2f} MHz\n")
        nerd_text.insert(tk.END, f"Load: {psutil.getloadavg()}\n\n")
        nerd_text.insert(tk.END, "=== MEMORY DETAILS ===\n", "header")
        mem = psutil.virtual_memory()
        nerd_text.insert(tk.END, f"Total: {mem.total//(1024**3)} GB\n")
        nerd_text.insert(tk.END, f"Available: {mem.available//(1024**3)} GB\n")
        nerd_text.insert(tk.END, f"Used: {mem.used//(1024**3)} GB ({mem.percent}%)\n")
        nerd_text.insert(tk.END, f"Swap: {psutil.swap_memory().used//1024**2}/{psutil.swap_memory().total//1024**2} MB\n\n")
        nerd_text.insert(tk.END, "=== STORAGE DETAILS ===\n", "header")
        partitions = psutil.disk_partitions()
        for part in partitions:
            usage = psutil.disk_usage(part.mountpoint)
            nerd_text.insert(tk.END, f"{part.device} -> {part.mountpoint} ({part.fstype})\n")
            nerd_text.insert(tk.END, f"  Total: {usage.total//(1024**3)} GB, Used: {usage.percent}%\n")
        nerd_text.insert(tk.END, "\n")
        nerd_text.insert(tk.END, "=== NETWORK DETAILS ===\n", "header")
        net = psutil.net_io_counters()
        nerd_text.insert(tk.END, f"Bytes Sent: {net.bytes_sent//1024} KB\n")
        nerd_text.insert(tk.END, f"Bytes Received: {net.bytes_recv//1024} KB\n")
        try:
            nerd_text.insert(tk.END, "\n=== SENSORS ===\n", "header")
            temps = psutil.sensors_temperatures()
            for name, entries in temps.items():
                nerd_text.insert(tk.END, f"{name}:\n")
                for entry in entries:
                    nerd_text.insert(tk.END, f"  {entry.label}: {entry.current}°C\n")
        except:
            pass
        nerd_text.tag_config("header", foreground=FG_COLOR, font=("Courier New", 10, "bold"))
    except Exception as e:
        nerd_text.insert(tk.END, f"Error getting stats: {str(e)}")
refresh_btn = tk.Button(nerd_frame, text="Refresh Stats", command=get_nerd_stats, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 12, "bold"))
refresh_btn.pack(pady=10)
refresh_btn.bind("<Enter>", create_glow)
refresh_btn.bind("<Leave>", remove_glow)

# ========== TAB 5: LINUX APPS (CROSTINI, CUSTOM UNINSTALL) ==========
def get_linux_desktop_apps():
    app_files = glob.glob("/usr/share/applications/*.desktop") + glob.glob(os.path.expanduser("~/.local/share/applications/*.desktop"))
    apps = []
    for f in app_files:
        name, exec_line, icon = None, None, None
        with open(f, "r", encoding="utf-8", errors="replace") as fd:
            for line in fd:
                if line.startswith("Name="):
                    name = line.split("=",1)[1].strip()
                elif line.startswith("Exec="):
                    exec_line = line.split("=",1)[1].strip().split(" ")[0]
                elif line.startswith("Icon="):
                    icon = line.split("=",1)[1].strip()
        if name and exec_line:
            apps.append({"name": name, "exec": exec_line, "desktopfile": f})
    return apps

linuxapps_tab = ttk.Frame(notebook)
notebook.add(linuxapps_tab, text="Linux Apps")
linuxapps_frame = tk.Frame(linuxapps_tab, bg=BG_COLOR)
linuxapps_frame.pack(fill='both', expand=True, padx=20, pady=20)
tk.Label(linuxapps_frame, text="Search & select Linux apps to uninstall:", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 14, "bold")).pack(pady=10)
search_var = tk.StringVar()
app_listbox = tk.Listbox(linuxapps_frame, selectmode='single', bg=TERMINAL_BG, fg=TERMINAL_FG, font=("Courier New", 12), height=16)
app_listbox.pack(fill='both', expand=True, pady=10)
def refresh_app_list():
    linuxapps_tab.all_apps = get_linux_desktop_apps()
    filter_linux_apps()
def filter_linux_apps(*args):
    query = search_var.get().lower()
    app_listbox.delete(0, tk.END)
    for app in linuxapps_tab.all_apps:
        if query in app["name"].lower():
            app_listbox.insert(tk.END, app["name"])
search_bar = tk.Entry(linuxapps_frame, textvariable=search_var, bg=TERMINAL_BG, fg=FG_COLOR, font=("Courier New", 12))
search_bar.pack(fill='x', pady=(0,10))
search_var.trace_add("write", filter_linux_apps)
refresh_app_list()

def uninstall_selected_linux_app():
    selection = app_listbox.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Select an app to uninstall.")
        return
    selected_name = app_listbox.get(selection[0])
    app_obj = next((a for a in linuxapps_tab.all_apps if a["name"] == selected_name), None)
    if not app_obj:
        messagebox.showerror("Error", "App not found!")
        return
    exec_cmd = app_obj["exec"]
    desktopfile = app_obj["desktopfile"]
    uninstall_options = tk.Toplevel(root)
    uninstall_options.title(f"Uninstall: {selected_name}")
    uninstall_options.configure(bg=BG_COLOR)
    uninstall_options.geometry("450x220")
    tk.Label(uninstall_options, text=f"Uninstall options for {selected_name}:", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 13, "bold")).pack(pady=12)
    tk.Label(uninstall_options, text=f"Exec command: {exec_cmd}\nDesktop file: {desktopfile}", bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack()
    def try_package_uninstall():
        result = subprocess.run(f"apt list --installed | grep -i '{exec_cmd}'", shell=True, stdout=subprocess.PIPE, text=True)
        if result.stdout:
            pkg_name = result.stdout.split('/')[0]
            subprocess.run(f"sudo apt remove --purge -y {pkg_name}", shell=True)
            messagebox.showinfo("Done", f"Uninstalled: {selected_name} ({pkg_name})")
        else:
            result2 = subprocess.run(f"flatpak list | grep -i '{exec_cmd}'", shell=True, stdout=subprocess.PIPE, text=True)
            if result2.stdout:
                flatpak_id = result2.stdout.split()[0]
                subprocess.run(f"flatpak uninstall -y {flatpak_id}", shell=True)
                messagebox.showinfo("Done", f"Uninstalled Flatpak app: {selected_name} ({flatpak_id})")
            else:
                messagebox.showerror("Not Found", f"Could not identify apt or flatpak package for: {selected_name}")
        uninstall_options.destroy()
        refresh_app_list()
    tk.Button(uninstall_options, text="Uninstall with apt/flatpak", command=try_package_uninstall, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 11, "bold")).pack(pady=6)
    def delete_desktop_file():
        if messagebox.askyesno("Delete Desktop Entry", f"Delete launcher icon ONLY?\n({desktopfile})"):
            try:
                os.remove(desktopfile)
                messagebox.showinfo("Done", "Desktop entry deleted.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
            uninstall_options.destroy()
            refresh_app_list()
    tk.Button(uninstall_options, text="Delete Desktop Entry Only", command=delete_desktop_file, bg="#444", fg="white", activebackground="#666", font=("Courier New", 11, "bold")).pack(pady=6)
    app_folder = None
    if exec_cmd.startswith('/') and os.path.exists(exec_cmd):
        app_folder = os.path.dirname(exec_cmd)
        if exec_cmd.lower().endswith('.appimage'):
            app_folder = exec_cmd
    if app_folder and os.path.exists(app_folder):
        def delete_app_folder():
            if messagebox.askyesno("Delete App Files", f"Delete app files/folder?\n({app_folder})"):
                try:
                    if os.path.isdir(app_folder):
                        shutil.rmtree(app_folder)
                    else:
                        os.remove(app_folder)
                    messagebox.showinfo("Done", "App files deleted.")
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                uninstall_options.destroy()
                refresh_app_list()
        tk.Button(uninstall_options, text="Delete App Files/Folder", command=delete_app_folder, bg="#990000", fg="white", activebackground="#cc2222", font=("Courier New", 11, "bold")).pack(pady=6)
    else:
        tk.Label(uninstall_options, text="No app folder found (custom/manual install may need manual deletion)", bg=BG_COLOR, fg="#ff6666", font=("Courier New", 10)).pack(pady=6)
    tk.Button(uninstall_options, text="Cancel", command=uninstall_options.destroy, bg="#333", fg="white", font=("Courier New", 11)).pack(pady=8)

tk.Button(linuxapps_frame, text="Uninstall Selected", command=uninstall_selected_linux_app, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 12, "bold")).pack(pady=10)

# ========== TAB 6: WINE APPS (UNINSTALL WINDOWS PROGRAMS) ==========
wineapps_tab = ttk.Frame(notebook)
notebook.add(wineapps_tab, text="Wine Apps")
wineapps_frame = tk.Frame(wineapps_tab, bg=BG_COLOR)
wineapps_frame.pack(fill='both', expand=True, padx=20, pady=20)
tk.Label(wineapps_frame, text="Manage Windows apps installed via Wine:", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 14, "bold")).pack(pady=10)
def run_wine_uninstaller():
    try:
        subprocess.Popen(["wine", "uninstaller"])
    except Exception as e:
        messagebox.showerror("Error", f"Could not open Wine Uninstaller:\n{str(e)}")
tk.Button(wineapps_frame, text="Open Wine Uninstaller", command=run_wine_uninstaller, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 12, "bold")).pack(pady=10)
tk.Label(wineapps_frame, text="(This opens Wine's Add/Remove Programs window. Use it to uninstall your Windows apps.)", bg=BG_COLOR, fg="white", font=("Courier New", 10)).pack(pady=10)

# ========== TAB 7: COMMANDS ==========
cmd_tab = ttk.Frame(notebook)
notebook.add(cmd_tab, text="Commands")
cmd_main_frame = tk.Frame(cmd_tab, bg=BG_COLOR)
cmd_main_frame.pack(fill='both', expand=True, padx=20, pady=20)
cmd_header = tk.Label(cmd_main_frame, text="QUICK COMMANDS", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 16, "bold"))
cmd_header.pack(pady=(0, 20))
def execute_quick_command(command, description):
    if messagebox.askyesno("Confirm Command", f"Do you want to run this command?\n\nDescription: {description}\nCommand: {command}\n\n⚠️  This will execute with system privileges if needed."):
        try:
            progress_window = tk.Toplevel(root)
            progress_window.title("Executing Command...")
            progress_window.configure(bg=BG_COLOR)
            progress_window.geometry("400x150")
            progress_window.transient(root)
            progress_window.grab_set()
            progress_window.geometry("+%d+%d" % (root.winfo_rootx() + 250, root.winfo_rooty() + 200))
            tk.Label(progress_window, text="Executing Command...", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12, "bold")).pack(pady=20)
            progress_bar = ttk.Progressbar(progress_window, mode='indeterminate', style="red.Horizontal.TProgressbar")
            progress_bar.pack(fill='x', padx=20, pady=10)
            progress_bar.start()
            status_label = tk.Label(progress_window, text=f"Running: {command}", bg=BG_COLOR, fg="white", font=("Courier New", 10))
            status_label.pack(pady=10)
            root.update()
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            progress_bar.stop()
            progress_window.destroy()
            result_window = tk.Toplevel(root)
            result_window.title("Command Result")
            result_window.configure(bg=BG_COLOR)
            result_window.geometry("600x400")
            result_window.transient(root)
            if process.returncode == 0:
                tk.Label(result_window, text="✅ COMMAND EXECUTED SUCCESSFULLY", bg=BG_COLOR, fg="#00ff00", font=("Courier New", 12, "bold")).pack(pady=10)
            else:
                tk.Label(result_window, text="❌ COMMAND FAILED", bg=BG_COLOR, fg="#ff6666", font=("Courier New", 12, "bold")).pack(pady=10)
            result_frame = tk.Frame(result_window, bg=BG_COLOR)
            result_frame.pack(fill='both', expand=True, padx=10, pady=10)
            result_text = scrolledtext.ScrolledText(result_frame, bg=TERMINAL_BG, fg=TERMINAL_FG, font=("Courier New", 10), wrap=tk.WORD)
            result_text.pack(fill='both', expand=True)
            result_text.insert(tk.END, f"Command: {command}\n")
            result_text.insert(tk.END, f"Return Code: {process.returncode}\n")
            result_text.insert(tk.END, "=" * 50 + "\n\n")
            if stdout:
                result_text.insert(tk.END, "STDOUT:\n")
                result_text.insert(tk.END, stdout + "\n\n")
            if stderr:
                result_text.insert(tk.END, "STDERR:\n")
                result_text.insert(tk.END, stderr + "\n")
            tk.Button(result_window, text="Close", command=result_window.destroy, bg=BTN_COLOR, fg="white", font=("Courier New", 10, "bold")).pack(pady=10)
        except Exception as e:
            try:
                progress_window.destroy()
            except:
                pass
            messagebox.showerror("Error", f"Failed to execute command:\n{str(e)}")
canvas = tk.Canvas(cmd_main_frame, bg=BG_COLOR, highlightthickness=0)
scrollbar_cmd = ttk.Scrollbar(cmd_main_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar_cmd.set)
commands = {
    "SYSTEM UPDATE & MAINTENANCE": [
        ("Update Package List", "sudo apt update", "Updates the package repository list"),
        ("Upgrade System", "sudo apt upgrade -y", "Upgrades all installed packages"),
        ("Full System Upgrade", "sudo apt full-upgrade -y", "Performs a complete system upgrade"),
        ("Clean Package Cache", "sudo apt autoremove && sudo apt autoclean", "Removes unused packages and cleans cache"),
        ("Fix Broken Packages", "sudo apt --fix-broken install", "Attempts to fix broken package dependencies"),
    ],
    "SYSTEM INFORMATION": [
        ("System Info", "neofetch || screenfetch || uname -a", "Display detailed system information"),
        ("Disk Usage", "df -h", "Show disk space usage"),
        ("Memory Usage", "free -h", "Display memory usage"),
        ("Process List", "ps aux", "List all running processes"),
        ("Network Interfaces", "ip addr show", "Show network interface information"),
        ("System Uptime", "uptime", "Show system uptime and load"),
    ],
    "NETWORK TOOLS": [
        ("Ping Google", "ping -c 4 google.com", "Test internet connectivity"),
        ("Network Speed Test", "curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3", "Test internet speed"),
        ("Show Open Ports", "sudo netstat -tulpn", "Display open network ports"),
        ("WiFi Networks", "nmcli dev wifi list", "Scan for available WiFi networks"),
        ("Public IP", "curl ifconfig.me", "Show your public IP address"),
    ],
    "FILE SYSTEM": [
        ("List Directory", "ls -la", "List files in current directory with details"),
        ("Disk Space", "du -sh * | sort -hr", "Show directory sizes sorted by size"),
        ("Find Large Files", "find / -type f -size +100M 2>/dev/null | head -20", "Find files larger than 100MB"),
        ("Check File System", "sudo fsck -f /", "Check file system for errors (USE WITH CAUTION)"),
    ],
    "DEVELOPMENT TOOLS": [
        ("Install Git", "sudo apt install git -y", "Install Git version control"),
        ("Install Python3 Pip", "sudo apt install python3-pip -y", "Install Python package manager"),
        ("Install Node.js", "curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - && sudo apt-get install -y nodejs", "Install Node.js and npm"),
        ("Install Docker", "curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh", "Install Docker"),
        ("Install VS Code", "wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/ && sudo sh -c 'echo \"deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main\" > /etc/apt/sources.list.d/vscode.list' && sudo apt update && sudo apt install code -y", "Install Visual Studio Code"),
    ],
    "SECURITY": [
        ("Install UFW Firewall", "sudo apt install ufw -y && sudo ufw enable", "Install and enable UFW firewall"),
        ("Check Failed Logins", "sudo grep 'Failed password' /var/log/auth.log | tail -10", "Show recent failed login attempts"),
        ("List Sudo Users", "getent group sudo", "Show users with sudo privileges"),
        ("Update Security Patches", "sudo unattended-upgrade", "Install security updates"),
    ],
    "MULTIMEDIA": [
        ("Install VLC", "sudo apt install vlc -y", "Install VLC media player"),
        ("Install GIMP", "sudo apt install gimp -y", "Install GIMP image editor"),
        ("Install Audacity", "sudo apt install audacity -y", "Install Audacity audio editor"),
        ("Install OBS Studio", "sudo apt install obs-studio -y", "Install OBS Studio for streaming/recording"),
    ],
    "GAMING": [
        ("Install Steam", "wget -O steam.deb https://steamcdn-a.akamaihd.net/client/installer/steam.deb && sudo dpkg -i steam.deb && sudo apt-get install -f -y", "Install Steam gaming platform"),
        ("Install Lutris", "sudo apt install lutris -y", "Install Lutris gaming platform"),
        ("Install GameMode", "sudo apt install gamemode -y", "Install GameMode for better gaming performance"),
    ]
}
for category, cmd_list in commands.items():
    category_frame = tk.Frame(scrollable_frame, bg=BG_COLOR)
    category_frame.pack(fill='x', pady=(20, 10))
    tk.Label(category_frame, text=category, bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 14, "bold")).pack(anchor='w')
    separator = tk.Frame(scrollable_frame, height=2, bg=FG_COLOR)
    separator.pack(fill='x', pady=(0, 10))
    buttons_frame = tk.Frame(scrollable_frame, bg=BG_COLOR)
    buttons_frame.pack(fill='x', padx=20, pady=(0, 10))
    for i, (name, command, description) in enumerate(cmd_list):
        btn = tk.Button(buttons_frame, text=name, command=lambda cmd=command, desc=description: execute_quick_command(cmd, desc), bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 10, "bold"), relief='raised', bd=2, wraplength=200, justify='center')
        row = i // 3
        col = i % 3
        btn.grid(row=row, column=col, padx=5, pady=5, sticky='ew', ipadx=10, ipady=5)
        btn.bind("<Enter>", create_glow)
        btn.bind("<Leave>", remove_glow)
        buttons_frame.columnconfigure(col, weight=1)
canvas.pack(side="left", fill="both", expand=True)
scrollbar_cmd.pack(side="right", fill="y")
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
canvas.bind_all("<MouseWheel>", _on_mousewheel)
custom_frame = tk.Frame(cmd_main_frame, bg=BG_COLOR)
custom_frame.pack(fill='x', pady=20, side='bottom')
tk.Label(custom_frame, text="CUSTOM COMMAND:", bg=BG_COLOR, fg=FG_COLOR, font=("Courier New", 12, "bold")).pack(anchor='w')
custom_entry_frame = tk.Frame(custom_frame, bg=BG_COLOR)
custom_entry_frame.pack(fill='x', pady=5)
custom_cmd_entry = tk.Entry(custom_entry_frame, bg=TERMINAL_BG, fg=TERMINAL_FG, font=("Courier New", 11), relief='sunken', bd=3)
custom_cmd_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
def execute_custom_command():
    command = custom_cmd_entry.get().strip()
    if command:
        execute_quick_command(command, "Custom command entered by user")
        custom_cmd_entry.delete(0, tk.END)
custom_btn = tk.Button(custom_entry_frame, text="Execute", command=execute_custom_command, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 10, "bold"))
custom_btn.pack(side='right')
custom_btn.bind("<Enter>", create_glow)
custom_btn.bind("<Leave>", remove_glow)
custom_cmd_entry.bind("<Return>", lambda e: execute_custom_command())
custom_cmds_file = "custom_cmds.json"
def load_custom_cmds():
    try:
        with open(custom_cmds_file, "r") as f:
            return json.load(f)
    except:
        return []
def save_custom_cmds(cmds):
    with open(custom_cmds_file, "w") as f:
        json.dump(cmds, f)
custom_cmds = load_custom_cmds()
def add_custom_cmd_button():
    name = simpledialog.askstring("Command Name", "Button name?")
    cmd = simpledialog.askstring("Command", "System command?")
    if name and cmd:
        custom_cmds.append({"name": name, "cmd": cmd})
        save_custom_cmds(custom_cmds)
        render_custom_cmd_buttons()
def render_custom_cmd_buttons():
    for widget in custom_buttons_frame.winfo_children():
        widget.destroy()
    for item in custom_cmds:
        btn = tk.Button(custom_buttons_frame, text=item["name"], command=lambda c=item["cmd"]: execute_quick_command(c, f"Custom: {c}"), bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 10, "bold"))
        btn.pack(side='left', padx=5, pady=5)
        btn.bind("<Enter>", create_glow)
        btn.bind("<Leave>", remove_glow)
custom_buttons_frame = tk.Frame(cmd_main_frame, bg=BG_COLOR)
custom_buttons_frame.pack(fill='x', pady=(10,0))
tk.Button(cmd_main_frame, text="Add Custom Command Button", command=add_custom_cmd_button, bg=BTN_COLOR, fg="white", activebackground=BTN_ACTIVE_BG, font=("Courier New", 10, "bold")).pack(pady=5)
render_custom_cmd_buttons()

def get_disk_usage():
    usage = shutil.disk_usage('/')
    percent = usage.used / usage.total * 100
    return percent, usage.free // (2**30)
def update_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_var.set(f"Usage: {cpu_percent}%")
    cpu_progress['value'] = cpu_percent
    mem = psutil.virtual_memory()
    ram_percent = mem.percent
    ram_var.set(f"Usage: {ram_percent}% ({mem.used//(1024**2)}/{mem.total//(1024**2)} MB)")
    ram_progress['value'] = ram_percent
    disk_percent, free_gb = get_disk_usage()
    storage_var.set(f"Usage: {disk_percent:.1f}% ({free_gb} GB free)")
    storage_progress['value'] = disk_percent
    net = psutil.net_io_counters()
    net_var.set(f"▲ {net.bytes_sent//1024} KB ▼ {net.bytes_recv//1024} KB")
    uptime = int(time() - psutil.boot_time())
    hours, remainder = divmod(uptime, 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime_var.set(f"Uptime: {hours}h {minutes}m {seconds}s")
    try:
        temp = psutil.sensors_temperatures().get('coretemp', [{}])[0].current
        temp_var.set(f"CPU Temp: {temp}°C" if temp else "")
    except:
        temp_var.set("")
    os_var.set(f"{platform.system()} {platform.release()}")
    if disk_percent > 90:
        storage_progress.configure(style="red.Horizontal.TProgressbar")
    else:
        storage_progress.configure(style="red.Horizontal.TProgressbar")
    root.after(2000, update_system_info)

check_wine()
update_system_info()
get_nerd_stats()

def focus_terminal():
    notebook.select(term_tab)
    cmd_entry.focus()
term_shortcut = tk.Button(root, text="TERMINAL", command=focus_terminal, bg="#660000", fg=FG_COLOR, font=("Courier New", 10, "bold"), relief='raised', bd=2)
term_shortcut.pack(side='bottom', anchor='se', padx=10, pady=10)
term_shortcut.bind("<Enter>", create_glow)
term_shortcut.bind("<Leave>", remove_glow)

root.mainloop()