import sys
from random import randrange
# from tkinter import Tk, Label, Buttontk.
import tkinter as tk
from tkinter import *
from tkinter import EW, N, NSEW, NW, filedialog as fd
from pathlib import Path

from config.app_cfg import Theme_dark, Theme_wp, Theme_pink, Theme_grey, Theme_psycho, Theme_style, App_font, Theme_dark_green
from library.file_manager import Files, process_list_of_path, unzip_file

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
    def __init__(self):
        
        self.root = tk.Tk()
        self.Theme = Theme_wp
        # color settings
        self.BG_COLOR = self.Theme.BG_COLOR.value
        self.FG_COLOR = self.Theme.FG_COLOR.value
        self.BT_COLOR = self.Theme.BT_COLOR.value
        self.TXT_BG_COLOR = self.Theme.TXT_BG_COLOR.value
        self.TXT_FG_COLOR = self.Theme.TXT_FG_COLOR.value

        self.TXT_FONT_1 = App_font.TXT_FONT_1.value
        self.TXT_FONT_2 = App_font.TXT_FONT_2.value

        # setting GUI
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

        # Menu
        self.menubar = tk.Menu (self.root, bg=self.BG_COLOR, fg=self.FG_COLOR, tearoff=0)
        self.filemenu = tk.Menu(self.menubar, bg=self.BG_COLOR, fg=self.FG_COLOR, tearoff=0)
        self.filemenu.add_command(label="White-purple", command=self.theme_wp)
        self.filemenu.add_command(label="Dark", command=self.theme_dark)
        self.filemenu.add_command(label="Pink", command=self.theme_pink)
        self.filemenu.add_command(label="Green", command=self.theme_dark_green)
        self.filemenu.add_command(label="Grey", command=self.theme_grey)
        self.filemenu.add_command(label="Ugly 1", command=self.theme_psycho)
        self.filemenu.add_command(label="Ugly 2", command=self.theme_style)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="Color", menu=self.filemenu)

        self.root.config(menu=self.menubar)

        # setting frame 1
        self.frame_1 = tk.Frame(self.root, bg=self.BG_COLOR)
        self.frame_1.grid(column=0, row=0, padx=10, pady=5, sticky=NSEW)

        # Frame 1
        # Row 0
        self.import_dir_button = tk.Button(
            self.frame_1,
            text="Select source directory",
            command=self.select_files,
            bg=self.BT_COLOR,
            fg=self.TXT_BG_COLOR
        )
        self.import_dir_button.grid(column=0, row=0, sticky=tk.EW, pady=5)

        # Row 1
        self.extract_dir_button = tk.Button(
            self.frame_1,
            text="Select extraction directory",
            command=self.select_extract_directory,
            bg=self.BT_COLOR,
            fg=self.TXT_BG_COLOR
        )
        self.extract_dir_button.grid(column=0, row=1, sticky=tk.EW, pady=5)

        # Row 2
        self.extract_button = tk.Button(
            self.frame_1,
            text="Extract all",
            command=self.exctract_file,
            bg=self.BT_COLOR,
            fg=self.TXT_BG_COLOR
        )
        self.extract_button.grid(column=0, row=2, sticky=tk.EW, pady=5)

        # Row 3
        self.close_button = tk.Button(
            self.frame_1,
            text="Close",
            command=self.root.quit,
            bg=self.BT_COLOR,
            fg=self.TXT_BG_COLOR,
        )
        self.close_button.grid(column=0, row=3, sticky=tk.EW, pady=5)
 

        # Setting frame 2
        self.frame_2 = tk.Frame(self.root, bg=self.BG_COLOR)
        self.frame_2.grid(column=1, row=0, padx=10, pady=5, sticky=NSEW)

        # Row 0
        self.label_nbr_imported_file = tk.Label(
            self.frame_2,
            textvariable=self.nbr_of_files,
            bg=self.BG_COLOR,
            fg=self.TXT_FG_COLOR
        )
        self.label_nbr_imported_file.grid(column=0, row=0, sticky=tk.W, pady=7)
        # Row 0
        self.label_files = tk.Label(
            self.frame_2,
            text="file(s) selected",
            bg=self.BG_COLOR,
            fg=self.TXT_FG_COLOR
        )
        self.label_files.grid(column=1, row=0, sticky=tk.W, pady=7)
        # Row 1
        self.extract_dir_label = tk.Label(
            self.frame_2,
            textvariable=self.extract_directory,
            bg=self.BG_COLOR,
            fg=self.TXT_FG_COLOR
        )
        self.extract_dir_label.grid(columnspan=2, row=1, sticky=tk.W, pady=7)
        # Row 1
        self.extract_label = tk.Label(
            self.frame_2,
            textvariable=self.nbr_of_processed_files,
            bg=self.BG_COLOR,
            fg=self.TXT_FG_COLOR
        )
        self.extract_label.grid(column=0, row=2, sticky=tk.W, pady=7)
        # Row 2        
        self.label_processed_files = tk.Label(
            self.frame_2,
            text="file(s) unziped",
            bg=self.BG_COLOR,
            fg=self.TXT_FG_COLOR
        )
        self.label_processed_files.grid(column=1, row=2, sticky=tk.W, pady=7)
        # Row 3 -> ToDo add progressbar...
        self.finished_label = tk.Label(
            self.frame_2,
            textvariable=self.finised,
            bg=self.BG_COLOR,
            fg=self.TXT_FG_COLOR
        )
        self.finished_label.grid(columnspan=2, row=3, sticky=tk.W, pady=7)

        self.root.mainloop()


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
        self.extract_directory.set(path)


    def theme_dark(self):
        self.Theme = Theme_dark
        self.apply_theme()

    def theme_pink(self):
        self.Theme = Theme_pink
        self.apply_theme()

    def theme_wp(self):
        self.Theme = Theme_wp
        self.apply_theme()

    def theme_dark_green(self):
        self.Theme = Theme_dark_green
        self.apply_theme()

    def theme_grey(self):
        self.Theme = Theme_grey
        self.apply_theme()

    def theme_psycho(self):
        self.Theme = Theme_psycho
        self.apply_theme()

    def theme_style(self):
        self.Theme = Theme_style
        self.apply_theme()


    def apply_theme(self):
        
        self.root.config(
            bg=self.Theme.BG_COLOR.value
        )

        self.menubar.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.FG_COLOR.value
        )
        
        self.filemenu.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.FG_COLOR.value
        )

        self.frame_1.config(
            bg=self.Theme.BG_COLOR.value
        )

        self.import_dir_button.config(
            bg=self.Theme.BT_COLOR.value,
            fg=self.Theme.TXT_BG_COLOR.value
        )

        self.extract_dir_button.config(
            bg=self.Theme.BT_COLOR.value,
            fg=self.Theme.TXT_BG_COLOR.value
        )  

        self.extract_button.config(
            bg=self.Theme.BT_COLOR.value,
            fg=self.Theme.TXT_BG_COLOR.value
        )
        
        self.close_button.config(
            bg=self.Theme.BT_COLOR.value,
            fg=self.Theme.TXT_BG_COLOR.value
        )
        

        self.frame_2.config(
            bg=self.Theme.BG_COLOR.value
        )
        
        self.label_nbr_imported_file.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.TXT_FG_COLOR.value
        )
        
        self.label_files.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.TXT_FG_COLOR.value
        )
                
        self.extract_dir_label.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.TXT_FG_COLOR.value
        )
                
        self.extract_label.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.TXT_FG_COLOR.value
        )
                
        self.label_processed_files.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.TXT_FG_COLOR.value
        )
                
        self.finished_label.config(
            bg=self.Theme.BG_COLOR.value,
            fg=self.Theme.TXT_FG_COLOR.value
        )
           

if __name__ == "__main__":
    my_gui = App()