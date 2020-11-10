# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:20:48 2020

@author: lynn
"""

import tkinter as tk
import asymcrypt
import ctypes
import pyperclip
root = tk.Tk()
root.geometry("400x240")#size of the window
top = tk.Frame(root)
bottom = tk.Frame(root)
top.pack(side=tk.TOP, anchor = tk.W)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
help_text = '''
Welcome to 1nQQrypt: the encryption and decryption program!

1nQQrypt is a program that uses asymmetric encryption. This makes text almost impossible to be decrypted without keys after encryption. Thus, you can definitely trust this program.

For any encryption and decyption, private and public keys are needed. Therefore, before doing any encryption and decryption, please generate keys, or transfer the keys into the same folder as the program first.
 
To encrypt text, type your text in (or paste it), and press the encrypt button.

To decrypt text, copy and paste the encrypted text in and press the decrypt button.

Please notice, if the encrypted text is still unrecognisable after decryption, it is because the private and public keys and not correct.

If nothing happens after the encrypt or decrypt button is pressed, please check if the private and public key files are in the same folder as the program.

If any bug or problem is noticed, or any further help is needed, please contact the email 2036306003@qq.com.

Please don't duplicate the program and send it to others without its author, Adam Li's permission.

Thank you for using 1nQQrypt and have a nice day!
'''
def encode():#encode function
    data=textE.get("1.0","end")
    encrypted = asymcrypt.encrypt_data(data,'my_public_key_file.pem', out_format = 'base64')
    textE.delete("1.0","end")
    textE.insert(tk.INSERT, encrypted)
    ctypes.windll.user32.MessageBoxW(0, "Message Encoded", "1nQQrypt", 1)
    encrypted = textE.get("1.0","end")
    pyperclip.copy(encrypted)
    
def decode():#decode function
    my_bytes = textE.get("1.0","end")
    encrypted = my_bytes.encode('ascii')
    original_message = asymcrypt.decrypt_data(encrypted,'my_private_key_file.pem', in_format = 'base64')
    ctypes.windll.user32.MessageBoxW(0, "Message Decoded", "1nQQrypt", 1)
    textE.delete("1.0","end")
    textE.insert(tk.INSERT, original_message)

def key_gen():
    asymcrypt.generate_keys('my_private_key_file.pem','my_public_key_file.pem')
    ctypes.windll.user32.MessageBoxW(0, "Private and public keys generated successfully", "1nQQrypt", 1)
    
def gethelp():
    textE.delete("1.0","end")
    textE.insert(tk.INSERT, help_text)
 

#set text
textE=tk.Text(root, width=35, height=15)

#encode button render
encodeOp = tk.Button(root, height=1, width=9, text="Encode", 
                    command = encode)
encodeOp.pack(in_=top, side=tk.LEFT)
#decode button render
decodeOp = tk.Button(root, height=1, width=9, text="Decode", 
                    command = decode)
decodeOp.pack(in_=top, side=tk.LEFT)
#key gen button render
genOp = tk.Button(root, height=1, width=9, text="Key gen", 
                    command = key_gen)
genOp.pack(in_=top, side=tk.LEFT)
#help button render
helpOp = tk.Button(root, height=1, width=9, text="Help", 
                    command = gethelp)
helpOp.pack(in_=top, side=tk.LEFT)

# Vertical (y) Scroll Bar
scroll = tk.Scrollbar(root)
scroll.config(command=textE.yview)
textE.config(yscrollcommand=scroll.set)
#scrollbar render
scroll.pack(in_=bottom, side=tk.RIGHT, fill=tk.Y)
textE.pack(in_=bottom, side=tk.LEFT, fill=tk.BOTH, expand=True)


root.title("1nQQrypt")

root.mainloop()
