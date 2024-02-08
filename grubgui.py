import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Barebone Builder")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="Build", command=self.build_kernel)
        self.build_button.pack(pady=5)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_kernel)
        self.run_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="add file", command=self.copy_file)
        self.copy_button.pack(pady=5)
        self.new_button = tk.Button(self.root, text="new project", command=self.new_file)
        self.new_button.pack(pady=5)

    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        
        self.text_area.delete(1.0, tk.END)
 
        
        if 0==0:
            f1=open("./grub.cfg","a")
            ff="""\n}"""
            
            #f1.write(ff)
            f1.close()
        
        self.execute_command("mv -f ./grub.cfg ./file/isodir/boot/grub/",True) 
        self.execute_command("grub-mkrescue -o myos.iso ./file/isodir",True)
    def run_kernel(self):
        self.text_area.delete(1.0, tk.END)
        self.execute_command("qemu-system-x86_64 -serial msmouse -cdrom myos.iso",True)


    def copy_file(self):
        #self.text_area.delete(1.0, tk.END)
        filename = tk.filedialog.askopenfilename(title="Select file")
        if filename:
            f1=open("./grub.cfg","a")
            ff="""menuentry \"$1\" {
	 multiboot /boot/$1 \n}\n"""
            fn=filename
            l=True
            while l:
                fnn=fn.find("/")
                if fnn<0:
                    break
                else:
                    fnn+=1
                    fn=fn[fnn:]
            print(fn)
            ff=ff.replace("$1",fn)
            f1.write(ff)
            f1.close()
	

            self.execute_command(('grub-file --is-x86-multiboot  "$1" ' ).replace("$1",filename),True)
            self.execute_command(('cp -f "$1"  ./file/isodir/boot/').replace("$1",filename),True)
            
            self.text_area.insert(tk.END, f"File {filename} copied \n",True)
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        
        if 0==0:
            self.execute_command("mkdir -p ./file/isodir/boot/grub",False)
            self.execute_command('rm -f ./file/isodir/boot/*.bin',False)
            self.execute_command('rm -f ./file/isodir/boot/grub/*.cfg',False)
            self.execute_command('rm -f ./*.cfg',False)
            self.execute_command("mkdir -p ./file/isodir/boot/grub",True)
            #self.execute_command("cp /tmp/kernel.bin ./file/isodir/boot/kernel.bin",True)
            self.execute_command("cp ./file/grub.cfg ./file/isodir/boot/grub/grub.cfg",True)
            self.execute_command("cp -f ./file/grub.txt ./grub.cfg",True)
            self.text_area.insert(tk.END, f"new project \n",True)


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
