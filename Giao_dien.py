import tkinter as tk
root = tk.Tk()
root.geometry("1200x800")
root.title("Hai bàn cờ 8×8")
ban_co=["Hậu"]*8+[""]*56
cell_size = 60  # Kích thước mỗi ô vuông (px)
# Frame bàn cờ 1
frame1 = tk.Frame(root, width=cell_size*8, height=cell_size*8+50)
frame1.grid(row=0, column=0, padx=30, pady=30)
label1=tk.Label(frame1,text="Bàn cỡ ban đầu",fg="black", font=("Arial", 16, "bold"))
label1.place(x=0,y=0)
# Frame bàn cờ 2
frame2 = tk.Frame(root, width=cell_size*8, height=cell_size*8)
frame2.grid(row=0, column=1, padx=30, pady=30)
def color(i,j):
    if (i%2==1 and j%2==0) or (i%2==0 and j%2==1):
        return "green"
    else:
        return "white"
buttons1 = []
for i in range(8):
    for j in range(8):
        btn = tk.Button(frame1, text="", font=("Arial", 16, "bold"),bg=color(i,j))
        btn.place(x=j*cell_size, y=i*cell_size+50, width=cell_size, height=cell_size)
        buttons1.append(btn)

buttons2 = []
for i in range(8):
    for j in range(8):
        btn2 = tk.Button(frame2, text=ban_co[i*8+j], font=("Arial", 16, "bold"),bg=color(i,j))
        btn2.place(x=j*cell_size, y=i*cell_size, width=cell_size, height=cell_size)
        buttons2.append(btn2)

root.mainloop()
