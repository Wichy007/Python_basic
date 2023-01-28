import tkinter as tk

def multiply_function():
    input = int(entry_box.get())
    if input == 0:
        output_label.configure(text='ไม่คิด')
        return

    output = ''

    for i in range(1, 13):
        output += str(input) + 'x' + str(i) + '=' + str(input*i) + '\n'

    output_label.configure(text=output)
    title_label.configure(text='สูตรคูณแม่' + ' ' + str(input))

def clear_entry_box():
    title_label.configure(text = "20")




window = tk.Tk()
window.title('JustPython')
window.minsize(400, 400)

title_label = tk.Label(master=window, text='สูตรคูณแม่')
title_label.pack(pady=20)
#title_label.place(x=20, y=20)

entry_box = tk.Entry(master=window)
entry_box.pack(pady=20)

go_button = tk.Button(master=window, text='ได้แก่', command=multiply_function)
go_button.pack()
go_button.place(x=120,y=140)

clear_button = tk.Button(master=window, text='ล้าง', command=clear_entry_box)
#clear_button.pack(side=tk.RIGHT, expand=True)
clear_button.pack()
clear_button.place(x=250,y=140)


output_label = tk.Label(master=window)
output_label.pack(side=tk.BOTTOM)

window.mainloop()

