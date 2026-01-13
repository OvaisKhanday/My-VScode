import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import filedialog
import os


root = tk.Tk()
root.title("Visual Studio Remake")
root.geometry("450x450")
root.configure(bg='#252526')


image = PhotoImage(file="icons/vscode.png")
root.iconphoto(True, image)

def open_file_in_new_tab():
    # Open a file
    # Create a tab
    # Put the text of file in TEXT widget
    # Append the tab on notebook
    content = ''
    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="D:\\teaching\\Python\\L1\\File Handling", # Start in the root directory (change as needed)
        filetypes=(
            ("Code & Text files", "*.py *.txt *.java *.csv *.css *.js *.ts *.json"),
            ("Python files", "*.py"),
            ("Text files", "*.txt"),
        )
    )


    if file_path:
        print("Selected file:", file_path)
    # You can now use the file_path variable with Python's open() function
    try:
        f = open(file_path, 'r')
        content = f.read()
        print("\nFile content:")
        print(content)
    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


    tab = tk.Frame(notebook)
    textarea = tk.Text(tab, width=300, height='300',  bg="#003763", fg="white", font="Consolas",insertbackground="white")
    textarea.pack(padx=10,pady=10)
    textarea.insert(tk.END, content)
    file_name = file_path.split('/')[-1]
    notebook.add(tab, text=file_name)
    notebook.select(tab)



    if file_path:
        print("Selected file:", file_path)
    # You can now use the file_path variable with Python's open() function
    try:
        f = open(file_path, 'r')
        content = f.read()
        print("\nFile content:")
        print(content)
    except FileNotFoundError:
        print(f"Error: The file was not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_new_tab():
    untitled_tab = tk.Frame(notebook)
    tk.Text(untitled_tab, width=300, height='300', bg="#252526", fg="white", font="Consolas",insertbackground="white").pack(padx=10,pady=10)
    notebook.add(untitled_tab, text='untitled')
    notebook.select(untitled_tab)

def close_current_tab():
    current_tab = notebook.select()
    if current_tab:
        notebook.forget(current_tab)


notebook = ttk.Notebook(root)
sidebar = tk.Frame(root, width=120, bg="#252526")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

btn_file = tk.Button(sidebar, text="📁", font=("Arial", 20), bg="#252526", fg="white")
btn_file.pack(pady=10, padx=10)

btn_search = tk.Button(sidebar, text="🔍", font=("Arial", 20), bg="#252526", fg="white")
btn_search.pack(pady=10, padx=10)

btn_settings = tk.Button(sidebar, text="⚙️", font=("Arial", 20), bg="#252526", fg="white")
btn_settings.pack(pady=10, padx=10)

btn_bugs = tk.Button(sidebar, text="🐞", font=("Arial", 20), bg="#252526", fg="white")
btn_bugs.pack(pady=10, padx=10)

btn_close = tk.Button(sidebar, text="❌", font=("Arial", 20), bg="#252526", fg="white", command=close_current_tab)
btn_close.pack(pady=10, padx=10)

# -----------------------------------------








menuBar = tk.Menu(root)


fileMenu = tk.Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New', command=create_new_tab)
fileMenu.add_command(label='Open', command=open_file_in_new_tab)
fileMenu.add_command(label='Close Tab', command=close_current_tab)

fileMenu.add_command(label='Save')
fileMenu.add_command(label='Save As')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.destroy)
menuBar.add_cascade(label='File', menu=fileMenu)




untitled_tab = tk.Frame(notebook)


tk.Text(untitled_tab, width=300, height='300', bg="#252526", fg="white", font="Consolas",insertbackground="white").pack(padx=10,pady=10)


notebook.add(untitled_tab, text='untitled')
notebook.pack(expand=1, fill="both", side=tk.LEFT)





root.config(menu = menuBar)
root.mainloop()
