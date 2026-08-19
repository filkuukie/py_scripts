from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image
import os
import sv_ttk

root = Tk()
root.title('WEBPgone')
root.iconbitmap("icon.ico")
root.minsize(width=300, height=220)
root.maxsize(width=300, height=235)
root.resizable(False, False)
frm = ttk.Frame(root, padding=10)

sv_ttk.set_theme('dark')

var1 = StringVar()
jpg = ['JPEG', '.jpg']
png = ['PNG', '.png']
bmp = ['BMP', '.bmp']
text='To convert image(s) please choose your target format file and click the button.'

ttk.Radiobutton(root, text = "JPEG", variable = var1, value = jpg).pack(pady=2)
ttk.Radiobutton(root, text = "PNG", variable = var1, value = png).pack(pady=2)
ttk.Radiobutton(root, text = "BMP", variable = var1, value = bmp).pack(pady=2)
label = ttk.Label(root, text=text, font=("Arial", 13), wraplength=290).pack(pady=10)

def convert_webp_to_jpg(text):
    aformat=var1.get()
    if aformat:
        pass    
    else:
        text="You should choose a file format first."
        label = ttk.Label(root, text=text).pack()
        raise ValueError
    ifi=fd.askopenfilenames(filetypes=[("Webp file", "*.webp")], parent=root, title='Choose *.webp files')
    fs=fd.askdirectory(parent=root, title='Choose output folder')
    for i in ifi:
        try:       
            if not os.path.exists(i):
                raise FileNotFoundError
                text=f"Input file '{i}' does not exist."
                label = ttk.Label(frm, text=text).pack()
            
            with Image.open(i) as img:
                if img.mode == 'CMYK':
                    img = img.convert('RGB')

                output_file = fs+'/'+str(i.split("/")[-1].split(".")[0])+aformat.split(" ")[-1]
                img.save(output_file, aformat.split(" ")[0], quality=95)

                text="Conversion successful!"
                label = ttk.Label(frm, text=text).pack()

        except (FileNotFoundError, IOError) as e:
            text=f"Error converting image: {e} for file {i}" 
            label = ttk.Label(frm, text=text).pack()


ttk.Button(root, text="Process", command= lambda:convert_webp_to_jpg(text)).pack(pady=5)

root.mainloop()
