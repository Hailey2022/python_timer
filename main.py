import tkinter as tk
import datetime
import threading
import tkinter.messagebox as messagebox


class GUI:
    def __init__(self, master):
        self.task = 0
        self.master = master
        self.set_title()
        self.label = tk.Label(master, text="執行時間：")
        self.label.grid(row=0, column=0)

        now = datetime.datetime.now()

        self.year_entry = tk.Entry(master, width=5, justify="center")
        self.year_entry.insert(0, str(now.year))
        self.month_entry = tk.Entry(master, width=3, justify="center")
        self.month_entry.insert(0, str(now.month))
        self.day_entry = tk.Entry(master, width=3, justify="center")
        self.day_entry.insert(0, str(now.day))
        self.hour_entry = tk.Entry(master, width=3, justify="center")
        self.hour_entry.insert(0, str(now.hour))
        self.minute_entry = tk.Entry(master, width=3, justify="center")
        self.minute_entry.insert(0, str(now.minute))
        self.second_entry = tk.Entry(master, width=3, justify="center")
        self.second_entry.insert(0, str(now.second))

        self.year_entry.grid(row=0, column=1)
        tk.Label(master, text="年").grid(row=0, column=2)
        self.month_entry.grid(row=0, column=3)
        tk.Label(master, text="月").grid(row=0, column=4)
        self.day_entry.grid(row=0, column=5)
        tk.Label(master, text="日").grid(row=0, column=6)
        self.hour_entry.grid(row=0, column=7)
        tk.Label(master, text="時").grid(row=0, column=8)
        self.minute_entry.grid(row=0, column=9)
        tk.Label(master, text="分").grid(row=0, column=10)
        self.second_entry.grid(row=0, column=11)
        tk.Label(master, text="秒").grid(row=0, column=12)

        self.button = tk.Button(master, text="開始", command=self.start_timer)
        self.button.grid(row=2, column=0, columnspan=12)

    def set_title(self):
        if self.task == 0:
            title = "定時器"
        elif self.task > 0:
            title = f"定時器（{self.task})"
        else:
            title = "error"
        self.master.title(title)

    def start_timer(self):
        try:
            time_str = f"{self.year_entry.get()} {self.month_entry.get()} {self.day_entry.get()} {self.hour_entry.get()} {self.minute_entry.get()} {self.second_entry.get()}"
            execute_time = datetime.datetime.strptime(
                time_str, '%Y %m %d %H %M %S')
        except ValueError:
            messagebox.showerror("錯誤", "時間格式錯誤，請重新輸入")
            return
        delta = (execute_time - datetime.datetime.now()).total_seconds()
        if delta > 0:
            timer = threading.Timer(delta, self.execute)
            timer.start()
            self.task += 1
            self.set_title()
            print(f"提示：將在{execute_time} ({delta:.1f}秒)後執行")
        else:
            messagebox.showinfo("提示", "請輸入未來的時間")

    def execute(self):
        self.task -= 1
        self.set_title()
        messagebox.showinfo("提示", "時間到！")


root = tk.Tk()
gui = GUI(root)
root.mainloop()
