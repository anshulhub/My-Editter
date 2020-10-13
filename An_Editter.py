import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, messagebox, filedialog
import os
win = tk.Tk()
win.title("An Editter")
win.geometry("700x700")

# ********************************************* Main Menu ************************************************
main_menu = tk.Menu()

#INSERTING IMAGES
file = tk.Menu(main_menu,tearoff=False)
new_icon = tk.PhotoImage(file="icons/new.png")
open_icon = tk.PhotoImage(file="icons/open.png")
save_icon = tk.PhotoImage(file="icons/save.png")
save_as_icon = tk.PhotoImage(file="icons/save_as.png")
exit_icon = tk.PhotoImage(file="icons/exit.png")


edit = tk.Menu(main_menu,tearoff=False)
copy_icon = tk.PhotoImage(file="icons/copy.png")
paste_icon = tk.PhotoImage(file="icons/paste.png")
cut_icon = tk.PhotoImage(file="icons/cut.png")
find_icon = tk.PhotoImage(file="icons/find.png")

view = tk.Menu(main_menu,tearoff=False)
tool_bar_icon = tk.PhotoImage(file="icons/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons/status_bar.png")


color=tk.Menu(main_menu,tearoff=False)
light_default_icon=tk.PhotoImage(file="icons/light_default.png")
light_plus_icon=tk.PhotoImage(file="icons/light_plus.png")
dark_icon=tk.PhotoImage(file="icons/dark.png")

theme_choice=tk.StringVar()
color_icon=(light_default_icon,light_plus_icon,dark_icon)

color_dict={
    "Light Default":('#000000','#ffffff'),  #here there is text color and backgrund color
    "Light Plus":('#474747','#e0e0e0'),
    "Dark":('#c4c4c4','#2d2d2d')
}


#******cascades******
main_menu.add_cascade(label="Files",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Colors",menu=color)
# ***********************************************End of Main menu*******************************************
#***********************************************************************************************************


# *********************************************Tool bar************************************************
tool_bar=ttk.Label(win)
tool_bar.pack(side=tk.TOP,fill=tk.X)

#font box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_combo=ttk.Combobox(tool_bar,width=25,state="readonly",textvariable=font_family)
font_combo['values']=font_tuple
font_combo.grid(row=0,column=0,padx=4)
font_combo.current(font_tuple.index('Arial'))

#size box
size_var=tk.IntVar()
size_combo=ttk.Combobox(tool_bar,width=15,textvariable=size_var,state="readonly")
size_combo['values']=tuple(range(5,50,3))
size_combo.grid(row=0,column=1,padx=4)
size_combo.current(3)

#now creating all the buttons
bold_icon=tk.PhotoImage(file='icons/bold.png')
italic_icon=tk.PhotoImage(file='icons/italic.png')
underline_icon=tk.PhotoImage(file='icons/underline.png')
font_color_icon=tk.PhotoImage(file='icons/font_color.png')
align_left_icon=tk.PhotoImage(file='icons/align_left.png')
align_right_icon=tk.PhotoImage(file='icons/align_right.png')
align_center_icon=tk.PhotoImage(file='icons/align_center.png')

bold_button=ttk.Button(tool_bar,image=bold_icon)
bold_button.grid(row=0,column=2,padx=4)

italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=4)

underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=4)

font_color_button=ttk.Button(tool_bar,image=font_color_icon)
font_color_button.grid(row=0,column=5,padx=4)

align_left_button=ttk.Button(tool_bar,image=align_left_icon)
align_left_button.grid(row=0,column=6,padx=4)

align_center_button=ttk.Button(tool_bar,image=align_center_icon)
align_center_button.grid(row=0,column=7,padx=4)

align_right_button=ttk.Button(tool_bar,image=align_right_icon)
align_right_button.grid(row=0,column=8,padx=4)
# ***********************************************End of Tool bar******************************************
#*********************************************************************************************************


# *********************************************Text Editor************************************************
text_editor=tk.Text(win)
text_editor.config(wrap='word',relief=tk.FLAT)
text_editor.focus_set()

scroll_bar=tk.Scrollbar(win)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functionalities
current_font_family="Arial"
current_font_size=12

def change_font(win):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_size(win):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_combo.bind('<<ComboboxSelected>>',change_font)
size_combo.bind('<<ComboboxSelected>>',change_size)

#****************buttons functionality
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_button.configure(command=change_bold)

#italic functionality
def change_italic():
    italic=tk.font.Font(font=text_editor['font'])
    if italic.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if italic.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
italic_button.configure(command=change_italic)

#underline functionality
def change_underline():
    underline=tk.font.Font(font=text_editor['font'])
    if underline.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if underline.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_button.configure(command=change_underline)

#color functionality
def color_change():
    color=tk.colorchooser.askcolor()
    text_editor.configure(fg=color[1])
font_color_button.configure(command=color_change)

#now we will do allignment
def left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
align_left_button.configure(command=left)

def center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
align_center_button.configure(command=center)

def right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
align_right_button.configure(command=right)

text_editor.configure(font=("Arial",12))
# # ***********************************************End of Text editor******************************************
#************************************************************************************************************


#************************************************Status bar***************************************************
status_bar=ttk.Label(win,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters= len(text_editor.get(1.0,'end-1c')) 
        status_bar.config(text=f"Characters:{characters}  Words : {words} ")
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)
#************************************************End of status bar********************************************
#*************************************************************************************************************


# ************************************************Main menu functionality***********************************
url=''          #variable

#new functionality
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)
#file new command
file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl+N",command=new_file)

#open functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select File",filetypes=(("Text files","*.txt"),("All files","*.*")))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return 
    win.title(os.path.basename(url))
#open command
file.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl+O",command=open_file)
file.add_separator()

#functionality to save a file
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as wf:
                wf.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
            content=text_editor.get(1.0,tk.END)    
            url.write(content)
            url.close()
    except:
        return
#save command
file.add_command(label="Save",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)

#save as functionality
def save_as(event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
        content=text_editor.get(1.0,tk.END)
        url.write(content)
        url.close()
    except:
        return
#save as command
file.add_command(label="Save As",image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_as)
file.add_separator()

#Exit command functionality
def exit_fun(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel("Warningg!!","Do you want to save your file!!?")
            if mbox is True:
                if url:
                    content=str(text_editor.get(1.0,tk.END))
                    with open(url,'w',encoding='utf-8') as wf:
                        wf.write(content)
                        win.destroy()
                else:
                    url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
                    content2=text_editor.get(1.0,tk.END)    
                    url.write(content2)
                    url.close()
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return
#exit command
file.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl+Z",command=exit_fun)


#edit commands adding functionality
#find functionality
def find_func(event=None):

    def find():
        word=find_input.get()
        text_editor.tag_remove("match",'1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
            
    def replace():
        word=find_input.get()
        replace_content=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_content)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialog=tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title("Find")
    find_dialog.resizable(0,0)

    find_frame=ttk.Labelframe(find_dialog,text="Find/Replace")
    find_frame.pack(pady=20)

    ##labels
    text_find_label=ttk.Label(find_frame,text="Find: ")
    text_replace_label=ttk.Label(find_frame,text="Replace")
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    ##entry boxes
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #bottons
    find_button=ttk.Button(find_frame,text="Find",command=find)
    replace_button=ttk.Button(find_frame,text="Replace",command=replace)
    find_button.grid(row=2,column=0,padx=4,pady=4)
    replace_button.grid(row=2,column=1,padx=4,pady=4)



edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_separator()

edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find_func)

#view checkbuttons

show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

view.add_checkbutton(label="Status Bar",onvalue=True,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)
view.add_checkbutton(label="Tool bar",image=tool_bar_icon,onvalue=True,offvalue=False,variable=show_toolbar,compound=tk.LEFT,command=hide_toolbar)

#color Theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color , bg_color = color_tuple[0] ,color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count=0
for i in color_dict:
    color.add_radiobutton(label=i,image=color_icon[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count += 1


# ********************************************End of Main Menu Functionality*********************************
win.config(menu=main_menu)

#binding shortcut keys
win.bind('<Control-n>',new_file)
win.bind('<Control-o>',open_file)
win.bind('<Control-s>',save_file)
win.bind('<Control-Alt-s>',save_as)
win.bind('<Control-f>',find_func)
win.bind('<Control-q>',exit_fun)

win.mainloop()
