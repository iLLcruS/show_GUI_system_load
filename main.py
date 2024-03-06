import tkinter as tk
import psutil

try:
    from GPUtil import showUtilization as gpu_util
except ImportError:
    gpu_util = lambda: "N/A"

def update_stats():
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    gpu_usage = gpu_util()
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    ram_label.config(text=f"RAM Usage: {ram_usage}%")
    gpu_label.config(text=f"GPU Usage: {gpu_usage}%")
    window.after(1000, update_stats)

window = tk.Tk()
window.title("System Monitor")

font_large = ('Helvetica', 16, 'bold')

cpu_label = tk.Label(window, text="CPU Usage: ", font=font_large)
cpu_label.pack()
ram_label = tk.Label(window, text="RAM Usage: ", font=font_large)
ram_label.pack()
gpu_label = tk.Label(window, text="GPU Usage: ", font=font_large)
gpu_label.pack()

window.geometry("+0+0")

window.attributes("-topmost", True)

update_stats()

window.mainloop()
