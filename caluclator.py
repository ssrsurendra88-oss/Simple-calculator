import tkinter as tk


def on_button_click(event):
  text = event.widget["text"]

  if text == "=":
    try:
      result = eval(entry.get())
      entry.delete(0, tk.END)
      entry.insert(tk.END, str(result))
    except Exception:
      entry.delete(0, tk.END)
      entry.insert(tk.END, "Error")
  elif text == "C":
    entry.delete(0, tk.END)
  else:
    entry.insert(tk.END, text)


# Window Setup
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")

# Entry Display
entry = tk.Entry(
    root, font=("Segoe UI", 20), justify="right", bd=10, insertwidth=2
)
entry.pack(fill="both", padx=10, pady=10)

# Button Layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
  row_frame = tk.Frame(frame)
  row_frame.pack(expand=True, fill="both")
  for btn_text in row:
    btn = tk.Button(
        row_frame, text=btn_text, font=("Segoe UI", 16), relief="groove"
    )
    btn.pack(side="left", expand=True, fill="both")
    btn.bind("<Button-1>", on_button_click)

root.mainloop()