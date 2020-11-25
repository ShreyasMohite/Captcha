from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha


class AllCaptcha:
    def __init__(self,root):
        self.root=root
        self.root.title("Captcha")
        self.root.geometry("400x300")
        self.root.iconbitmap("logo577.ico")
        self.root.resizable(0,0)


        inputs=StringVar()
        capt=StringVar()
        name=StringVar()



        def clear():
            inputs.set("")
            capt.set("Select Captcha")
            name.set("")

        
        def create_captcha():
            if inputs.get()!="":
                if capt.get()!="Select Captcha":
                    if name.get()!="":
                        if capt.get()=="Image":
                           image=ImageCaptcha()
                           data=image.generate(inputs.get())
                           image.write(inputs.get(),'{}.png'.format(name.get()))
                        if capt.get()=="Audio":
                           audio=AudioCaptcha()
                           data=audio.generate(inputs.get())
                           audio.write(inputs.get(),'{}.wav'.format(name.get()))
                        
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter name")
                else:
                    tkinter.messagebox.showerror("Error","Pleas Select Captcha")
            else:
                tkinter.messagebox.showerror("Error","Please Enter Inputs for Captcha")









        def on_enter1(e):
            but_create['background']="black"
            but_create['foreground']="cyan"  
        def on_leave1(e):
            but_create['background']="SystemButtonFace"
            but_create['foreground']="SystemButtonText"
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"






#=================frame=========================
        
        mainframe=Frame(self.root,width=400,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=394,height=250,relief="ridge",bd=3,bg="gray77")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=394,height=45,relief="ridge",bd=3,bg="gray77")
        secondframe.place(x=0,y=250)


#===================firstframe==============================#
        
        lab_enter_captcha_inputs=Label(firstframe,text="Enter Captcha Inputs",font=('times new roman',12),bg="gray77")
        lab_enter_captcha_inputs.place(x=130,y=5)

        ent_captcha=Entry(firstframe,width=30,font=('times new roman',14),relief="ridge",bd=3,textvariable=inputs)
        ent_captcha.place(x=50,y=30)

        Capt=['Image','Audio']
        Capt_combo=Combobox(firstframe,values=Capt,font=('arial',14),width=15,state="readonly",textvariable=capt)
        Capt_combo.set("Select Captcha")
        Capt_combo.place(x=100,y=100)

        lab_save=Label(firstframe,text="Enter Save Name",font=('times new roman',12),bg="gray77")
        lab_save.place(x=130,y=170)

        ent_name=Entry(firstframe,width=30,font=('times new roman',14),relief="ridge",bd=3,textvariable=name)
        ent_name.place(x=50,y=200)


#===================secondframe=============================#

        but_create=Button(secondframe,width=17,text="Create",font=('times new roman',12),cursor="hand2",command=create_captcha)
        but_create.place(x=10,y=3)
        but_create.bind("<Enter>",on_enter1)
        but_create.bind("<Leave>",on_leave1)



        but_clear=Button(secondframe,width=17,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=213,y=3)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#==========================================================#
        




if __name__ == "__main__":
    root=Tk()
    AllCaptcha(root)
    root.mainloop()