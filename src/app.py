import sys
from random import randrange
# from tkinter import Tk, Label, Buttontk.
import tkinter as tk
from tkinter import EW, N, NSEW, NW, filedialog as fd
from pathlib import Path

from config.app_cfg import App_color, App_font
from modules.file_manager import Files, process_list_of_path, unzip_file

home = str(Path.home())

# setting the path separator for linux and mac ( / ) or windows ( \\ )
if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
    print(f"Your os is {sys.platform}\nand your home directory is {home}")
    separator = "/"
elif sys.platform == "win32":
    print(f"Your os is {sys.platform}\nand your home directory is {home}")
    separator = "\\"
else:
    print("System not supported.")
    quit()

class App:
    def __init__(self, root):
        # color settings
        self.BG_COLOR = App_color.BG_COLOR.value
        self.FG_COLOR = App_color.FG_COLOR.value
        self.BT_COLOR = App_color.BT_COLOR.value
        self.TXT_COLOR = App_color.TXT_COLOR.value

        self.TXT_FONT_1 = App_font.TXT_FONT_1.value
        self.TXT_FONT_2 = App_font.TXT_FONT_2.value

        # setting GUI
        self.root = root
        self.root.title("Multi-zip extractor")
        # self.root.geometry("400x200")
        self.root.config(bg=self.BG_COLOR)
        self.root.columnconfigure(0,weight=1)
        self.root.columnconfigure(1,weight=5)

        # setting variables
        self.path_desktop = home+f"{separator}Desktop"

        self.nbr_of_files = tk.IntVar()
        self.nbr_of_files.set(0)

        self.nbr_of_processed_files = tk.IntVar()
        self.nbr_of_processed_files.set(0)

        self.file_list = Files
        
        self.extract_directory = tk.StringVar()
        self.extract_directory.set(self.path_desktop)

        self.finised = tk.StringVar()

        self.frame_1 = tk.Frame(self.root, bg=self.BG_COLOR)
        self.frame_1.grid(column=0, row=0, padx=10, pady=5, sticky=NSEW)

        self.frame_2 = tk.Frame(self.root, bg=self.BG_COLOR)
        self.frame_2.grid(column=1, row=0, padx=10, pady=5, sticky=NSEW)
        # self.frame_2 = frame(self.root)

        # F1 buttons
        # setting search button at row 0
        self.load_button = tk.Button(
            self.frame_1,
            text="Select source directory", 
            command=self.select_files, 
            bg=self.BT_COLOR, 
            fg=self.BG_COLOR
        ).grid(column=0, row=0, sticky=tk.EW, pady=5)

        # setting search button at row 1
        self.extract_dir_button = tk.Button(
            self.frame_1,
            text="Select extraction directory", 
            command=self.select_extract_directory, 
            bg=self.BT_COLOR, 
            fg=self.BG_COLOR
        ).grid(column=0, row=1, sticky=tk.EW, pady=5)

        self.extract_button = tk.Button(
            self.frame_1,
            text="Extract all", 
            command=self.exctract_file, 
            bg=self.BT_COLOR, 
            fg=self.BG_COLOR
        ).grid(column=0, row=2, sticky=tk.EW, pady=5)

        # setting quit button at row 3
        self.close_button = tk.Button(
            self.frame_1,
            text="Close", 
            command=self.root.quit, 
            bg=self.BT_COLOR, 
            fg=self.BG_COLOR
        ).grid(column=0, row=3, sticky=tk.EW, pady=5)
 
        # F2 text and textvariable
        
        self.label_load_directory = tk.Label(
            self.frame_2,
            textvariable=self.nbr_of_files, 
            bg=self.BG_COLOR, 
            fg=self.FG_COLOR
        ).grid(column=0, row=0, sticky=tk.W, pady=7)
        
        self.label_files = tk.Label(
            self.frame_2,
            text="file(s) selected", 
            bg=self.BG_COLOR, 
            fg=self.FG_COLOR
        ).grid(column=1, row=0, sticky=tk.W, pady=7)

        self.extract_dir_label = tk.Label(
            self.frame_2,
            textvariable=self.extract_directory, 
            bg=self.BG_COLOR, 
            fg=self.FG_COLOR
        ).grid(columnspan=2, row=1, sticky=tk.W, pady=7)

        self.extract_label = tk.Label(
            self.frame_2,
            textvariable=self.nbr_of_processed_files, 
            bg=self.BG_COLOR, 
            fg=self.FG_COLOR
        ).grid(column=0, row=2, sticky=tk.W, pady=7)
        
        self.label_processed_files = tk.Label(
            self.frame_2,
            text="file(s) unziped", 
            bg=self.BG_COLOR, 
            fg=self.FG_COLOR
        ).grid(column=1, row=2, sticky=tk.W, pady=7)

        self.finished_label = tk.Label(
            self.frame_2,
            textvariable=self.finised, 
            bg=self.BG_COLOR, 
            fg=self.FG_COLOR
        ).grid(columnspan=2, row=3, sticky=tk.W, pady=7)

    def select_files(self):
        file_type = [('zip file', '*.zip')]
        path_tuple = fd.askopenfilenames(
            title="Select files...",
            filetypes=file_type,
            initialdir=self.path_desktop
        )
        self.nbr_of_files.set(len(path_tuple))
        self.file_list = process_list_of_path(path_tuple)
        self.frame_2.update_idletasks()
        # print(f"> selected dir: {self.file_list }")

    def exctract_file(self):
        for file in self.file_list.list:
            unzip_file(file.path, self.extract_directory.get()+separator+file.file_name)
            self.nbr_of_processed_files.set(self.nbr_of_processed_files.get()+1)
            self.finised.set(self.finised.get()+'. ')
            self.frame_2.update_idletasks()
        self.finised.set(f"Finished! {self.nbr_of_processed_files.get()}/{self.nbr_of_files.get()} processed.")

    def select_extract_directory(self):
        path = fd.askdirectory(
            title="Load from",
            initialdir=self.path_desktop
        )
        # print(f"> selected dir: {path}")
        self.extract_directory.set(path)

if __name__ == "__main__":
    root = tk.Tk()
    my_gui = App(root)
    root.mainloop()
