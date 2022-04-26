import tkinter as tk


# Handle the waiting time
def handle_wait(event):
    global event_id
    if event_id is not None: # same goes for this ;)
        root.after_cancel(event_id)
    event_id = root.after(deadline, clear_text)


def clear_text():
    writing_sec.delete('1.0', tk.END)


event_id = None  # I do not fully understand how it works.
# I stumbled upon it on a post in stackoverflow and somehow made it work here.
# if you know you can share in comments
deadline = 11000
root = tk.Tk()
root.geometry('800x400')
root.config(padx=20, pady=20)
root.title('Disappearing Text App')

prompt = tk.Label(text="Don't Stop if you don't want your work to disappear!", font=('ubuntu', 16, 'bold'))
prompt.place(x=100, y=20)

x1 = tk.Label(text='Some Text :', font=('ubuntu', 14, 'bold'))
x1.place(x=100, y=100)

writing_sec = tk.Text(width=47, height=10, font=('ubuntu', 11))
writing_sec.focus()
writing_sec.place(x=250, y=100)
# checks if something is typed and then executes the given func.
writing_sec.bind('<Key>', handle_wait)

root.mainloop()
