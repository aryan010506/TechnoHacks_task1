import tkinter as tk
from tkinter import messagebox

# Functions
def click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        history_listbox.insert(tk.END, f"{expression} = {result}")
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "❌ Cannot divide by zero.")
        clear()
    except Exception:
        messagebox.showerror("Input Error", "❌ Invalid expression.")
        clear()

def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    bg = "#ffffff" if not is_dark_mode else "#0f172a"
    fg = "#000000" if not is_dark_mode else "#ffffff"
    entry_bg = "#f0f0f0" if not is_dark_mode else "#1e293b"
    history_bg = "#f5f5f5" if not is_dark_mode else "#1e293b"
    btn_bg = "#e2e8f0" if not is_dark_mode else "#334155"
    operator_bg = "#3b82f6" if not is_dark_mode else "#2563eb"

    root.configure(bg=bg)
    entry.configure(bg=entry_bg, fg=fg)
    history_listbox.configure(bg=history_bg, fg=fg)
    clear_btn.configure(bg="#ef4444" if is_dark_mode else "#f87171", fg="white")
    theme_btn.configure(bg="#94a3b8" if is_dark_mode else "#cbd5e1", fg=fg)

    for btn, txt in zip(all_buttons, all_texts):
        btn.configure(bg=operator_bg if txt in ['+', '-', '*', '/', '='] else btn_bg, fg=fg)

# GUI setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg="#0f172a")
is_dark_mode = True

# Entry field
entry = tk.Entry(root, font=("Arial", 22), bg="#1e293b", fg="#ffffff", borderwidth=0, relief=tk.FLAT, justify="right")
entry.pack(padx=20, pady=20, ipady=15, fill="x")

# History panel
history_listbox = tk.Listbox(root, height=5, font=("Arial", 12), bg="#1e293b", fg="#ffffff", borderwidth=0)
history_listbox.pack(padx=20, pady=(0, 10), fill="both")

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

all_buttons = []
all_texts = []

for row in buttons:
    frame = tk.Frame(root, bg="#0f172a")
    frame.pack(expand=True, fill="both", padx=10, pady=5)
    for btn_text in row:
        if btn_text == "=":
            btn = tk.Button(frame, text=btn_text, font=("Arial", 18), bg="#2563eb", fg="white",
                            command=calculate, relief=tk.FLAT)
        else:
            btn = tk.Button(frame, text=btn_text, font=("Arial", 18), bg="#334155", fg="white",
                            command=lambda txt=btn_text: click(txt), relief=tk.FLAT)
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        all_buttons.append(btn)
        all_texts.append(btn_text)

# Clear & Theme Buttons
clear_btn = tk.Button(root, text="Clear", font=("Arial", 16), bg="#dc2626", fg="white", command=clear, relief=tk.FLAT)
clear_btn.pack(fill="x", padx=20, pady=(5, 2))

theme_btn = tk.Button(root, text="Toggle Theme", font=("Arial", 14), bg="#94a3b8", fg="#ffffff", command=toggle_theme, relief=tk.FLAT)
theme_btn.pack(fill="x", padx=20, pady=(2, 10))

# Keyboard support
def on_key(event):
    if event.keysym == 'Return':
        calculate()
    elif event.keysym == 'BackSpace':
        entry.delete(len(entry.get())-1)
    elif event.char in '0123456789+-*/.':
        entry.insert(tk.END, event.char)

root.bind("<Key>", on_key)

root.mainloop()
