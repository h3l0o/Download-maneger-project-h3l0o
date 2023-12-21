import tkinter as tk
from pySmartDL import SmartDL
from tkinter import ttk
from urllib.request import Request, urlopen


class MainProgramme:

    def __init__(self):
        self.destination = 'C:\\Users\\lansi\\Downloads'
        self.root = tk.Tk()
        self.geometry = self.root.geometry('350x400')
        self.title = self.root.title("IDM")
        self.url = 'https://example.com/file.zip'
        self.obj = SmartDL(self.url, dest=self.destination)

        self.text = tk.StringVar()
        self.text.set(self.url)
        self.url1 = None

        self.entry = tk.Entry(self.root, width=40, textvariable=self.text)
        self.d_button = tk.Button(self.root, text="Download", command=self.download)
        self.p_button = tk.Button(self.root, text="pause", command=self.pause)
        self.r_button = tk.Button(self.root, text="resume", command=self.resume, width=20)
        # TODO
        self.Progress = ttk.Progressbar(self.root, length=100, mode="determinate")
        # TODO
        self.entry.pack(pady=10)
        self.d_button.pack(pady=10)
        self.p_button.pack(side="right", padx=70)
        self.r_button.pack(side="left", padx=60, pady=70)
        self.Progress.pack()

        def erase_example_text(event):
            if self.text.get() == self.url:
                self.text.set('')

        self.entry.bind('<Button-1>', erase_example_text)

        self.root.mainloop()

    def pause(self):
        if self.obj and not self.obj.isFinished():
            self.obj.pause()

    def resume(self):
        if self.obj and not self.obj.isFinished():
            self.obj.unpause()



    def progress(self):

        for i in range(100):
            self.Progress['value'] = i + 1
            self.root.update_idletasks()
            self.root.after(1)

    def download(self):
        url1 = self.entry.get()
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = Request(url1, headers=headers)
        handler = urlopen(req)
        self.obj = SmartDL(url1, self.destination, fix_urls=True, progress_bar=True)
        self.obj.start(blocking=False)


MainProgramme()
