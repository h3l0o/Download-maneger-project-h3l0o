import requests
import tkinter as tk


class MainProgramme:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('350x400')
        self.root.title('Download master')
        self.url = "https://example.com/file.zip"  # Default URL

        self.text = tk.StringVar()
        self.text.set(self.url)

        self.entry = tk.Entry(self.root, width=40, textvariable=self.text)
        self.button = tk.Button(self.root, width=10, command=self.download, text="Download")

        self.entry.pack()
        self.button.pack(pady=50)

        def erase_example_text(event):
            if self.text.get() == self.url:
                self.text.set('')

        self.entry.bind('<Button-1>', erase_example_text)

        self.root.mainloop()

    def download(self):
        url = self.text.get()
        if url:
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    file_name = url.split('/')[-1]
                    with open(file_name, 'wb') as f:
                        f.write(response.content)
                    print(f"Download successful: {file_name}")
                else:
                    print("Download failed. Status code:", response.status_code)
            except requests.RequestException as e:
                print("Download failed:", e)
                
    # TODO
    def pause(self):
        pass

    # TODO
    def resume(self):
        pass


MainProgramme()
