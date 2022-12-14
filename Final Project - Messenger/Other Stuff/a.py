import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root)
scrolly = tk.Scrollbar(root, orient='vertical', command=canvas.yview)

# display labels in the canvas
for i in range(10):
    label = tk.Label(canvas, text='label %i' % i)
    canvas.create_window(0, i*50, anchor='nw', window=label, height=50)

canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrolly.set)

canvas.pack(fill='both', expand=True, side='left')
scrolly.pack(fill='y', side='right')

root.mainloop()