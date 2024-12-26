import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd


def extract_and_rename_pdfs(input_pdf, output_dir, names):
    reader = PyPDF2.PdfReader(input_pdf)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for page_num in range(len(reader.pages)):
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[page_num])
        output_path = os.path.join(output_dir, f"{names[page_num]}.pdf")
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

    messagebox.showinfo("Success", "Proses ekstraksi dan rename selesai.")


def select_input_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    input_pdf_var.set(file_path)


def select_output_dir():
    dir_path = filedialog.askdirectory()
    output_dir_var.set(dir_path)


def start_extraction():
    input_pdf = input_pdf_var.get()
    output_dir = output_dir_var.get()

    if not input_pdf or not output_dir:
        messagebox.showerror("Error", "Silakan pilih file PDF dan direktori output.")
        return

    names = name_listbox.get(0, tk.END)  # Get all names from the listbox
    if len(names) == 0:
        messagebox.showerror("Error", "Daftar nama tidak boleh kosong.")
        return

    extract_and_rename_pdfs(input_pdf, output_dir, names)


def add_name():
    new_name = name_entry.get().strip()
    if new_name:
        name_listbox.insert(tk.END, new_name)
        name_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Nama tidak boleh kosong.")


def remove_name():
    selected_indices = name_listbox.curselection()
    if selected_indices:
        for index in reversed(selected_indices):
            name_listbox.delete(index)
    else:
        messagebox.showwarning("Warning", "Silakan pilih nama yang ingin dihapus.")


def import_names():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if not file_path:
        return

    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            names = df.iloc[:, 0].dropna().tolist()  # Assuming names are in the first column
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
            names = df.iloc[:, 0].dropna().tolist()  # Assuming names are in the first column

        # Clear the current list and add new names
        name_listbox.delete(0, tk.END)
        for name in names:
            name_listbox.insert(tk.END, name)

        messagebox.showinfo("Success", f"{len(names)} nama berhasil diimpor.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengimpor nama: {str(e)}")


def download_template():
    # Create a DataFrame with only the header "Name"
    template_data = {
        "Name": []
    }

    df = pd.DataFrame(template_data)

    # Create a new window for format selection
    format_window = tk.Toplevel(root)
    format_window.title("Pilih Format Template")

    tk.Label(format_window, text="Pilih format untuk mengunduh template:").pack(padx=10, pady=10)

    def download_csv():
        template_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile="template-extract-rename.csv",
                                                     filetypes=[("CSV Files", "*.csv")])
        if template_path:
            try:
                df.to_csv(template_path, index=False)
                messagebox.showinfo("Success", "Template CSV berhasil diunduh.")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal mengunduh template: {str(e)}")
        format_window.destroy()

    def download_xlsx():
        template_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                     initialfile="template-extract-rename.xlsx",
                                                     filetypes=[("Excel Files", "*.xlsx")])
        if template_path:
            try:
                df.to_excel(template_path, index=False)
                messagebox.showinfo("Success", "Template XLSX berhasil diunduh.")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal mengunduh template: {str(e)}")
        format_window.destroy()

    tk.Button(format_window, text="Download as CSV", command=download_csv).pack(padx=10, pady=5)
    tk.Button(format_window, text="Download as XLSX", command=download_xlsx).pack(padx=10, pady=5)


def toggle_theme():
    current_theme = root.option_get('theme', 'light')

    if current_theme == 'light':
        # Switch to dark theme
        root.configure(bg="#2E2E2E")
        for widget in root.winfo_children():
            widget.configure(bg="#2E2E2E")  # Set background color
            # Set foreground color only if the widget supports it
            if isinstance(widget, (tk.Button, tk.Label, tk.Entry)):
                widget.configure(fg="white")
        theme_button.config(text="Switch to Light Mode")
        root.option_add('*TButton*highlightBackground', '#2E2E2E')
        root.option_add('theme', 'dark')  # Update the theme state
    else:
        # Switch to light theme
        root.configure(bg="#f0f0f0")
        for widget in root.winfo_children():
            widget.configure(bg="#f0f0f0")  # Set background color
            # Set foreground color only if the widget supports it
            if isinstance(widget, (tk.Button, tk.Label, tk.Entry)):
                widget.configure(fg="black")
        theme_button.config(text="Switch to Dark Mode")
        root.option_add('theme', 'light')  # Update the theme state

    # Toggle the theme state
    current_theme = 'dark' if root.option_get('theme', 'light') == 'light' else 'light'
    root.option_add('theme', current_theme)


# Create the main window
root = tk.Tk()
root.title("PDF Extractor and Renamer")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Variables to hold file paths
input_pdf_var = tk.StringVar()
output_dir_var = tk.StringVar()

# Create and place widgets using frames for better organization
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Input PDF File:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(frame_input, textvariable=input_pdf_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_input, text="Browse", command=select_input_pdf).grid(row=0, column=2, padx=10, pady=10)

tk.Label(frame_input, text="Output Directory:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(frame_input, textvariable=output_dir_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(frame_input, text="Browse", command=select_output_dir).grid(row=1, column=2, padx=10, pady=10)

# Name management section
frame_names = tk.Frame(root, bg="#f0f0f0")
frame_names.pack(pady=10)

tk.Label(frame_names, text="Daftar Nama:", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10)
name_listbox = tk.Listbox(frame_names, width=50, height=10)
name_listbox.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame_names, text="Nama Baru:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(frame_names, width=50)
name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(frame_names, text="Tambah Nama", command=add_name).grid(row=2, column=1, padx=10, pady=5)
tk.Button(frame_names, text="Hapus Nama", command=remove_name).grid(row=2, column=2, padx=10, pady=5)
tk.Button(frame_names, text="Impor Nama", command=import_names).grid(row=2, column=0, padx=10, pady=5)
tk.Button(frame_names, text="Download Template", command=download_template).grid(row=3, column=0, padx=10, pady=5)

# Start extraction button
tk.Button(root, text="Start Extraction", command=start_extraction, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(
    pady=20)

# ... [rest of your code above]

# Theme toggle button
theme_button = tk.Button(root, text="Switch to Dark Mode", command=toggle_theme, bg="#007BFF", fg="white")
theme_button.pack(pady=10)

# Set initial theme
toggle_theme()  # Call this to set the initial theme based on the default

# Start the GUI event loop
root.mainloop()

