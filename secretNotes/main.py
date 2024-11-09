# All modules imported into Tkinter and base64
from tkinter import *
from tkinter import messagebox
import base64

# Properties
FONT = ("Helvetica", 12, "bold")
BG_COLOR = "#1A1A1D"
TEXT_COLOR = "#C0C0C0"
ENTRY_BG_COLOR = "#333333"
BUTTON_COLOR = "#6C0F0F"
BUTTON_TEXT_COLOR = "#E0E0E0"

# Window
window = Tk()
window.config(padx=20, pady=20, bg=BG_COLOR)
window.minsize(width=600, height=700)
window.title("Secret Notes")

# İmage
image = PhotoImage(file="TopSecret.png")
image_label = Label(window, image=image, bg=BG_COLOR)
image_label.pack(padx=10, pady=10)

# Title label and entry
notes_label = Label(window, text="Enter Your Title", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
title_entry = Entry(window, width=40, bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, font=FONT)
notes_label.pack(padx=10, pady=10)
title_entry.pack(padx=10, pady=10)

# Notes label and text
notes_label = Label(window, text="Enter Your Secret Note", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
notes_text = Text(window, width=50, height=15, bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, font=FONT)
notes_label.pack(padx=10, pady=10)
notes_text.pack(padx=10, pady=10)

# Password label and entry
password_label = Label(window, text="Enter Your Password", font=FONT, bg=BG_COLOR, fg=TEXT_COLOR)
password_entry = Entry(window, width=40, bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, font=FONT, show="*")
password_label.pack(padx=10, pady=10)
password_entry.pack(padx=10, pady=10)


# Encrypt and Decrypt
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


# Save and Encrypt button
def save_encrypt():
    # Save File
    title = title_entry.get()
    secret_note_content = notes_text.get("1.0", END)
    password = password_entry.get()
    if len(title) == 0 or len(secret_note_content) == 0 or len(password) == 0:
        messagebox.showwarning(title='Error', message='Please Enter the Requested İnformation')
    else:
        # Encrypt File
        content_encrypt = encode(password, secret_note_content)
        try:
            with open("MySecretNotes.txt", 'a') as fp:
                fp.write(f"\n{title}\n{content_encrypt}")
        except FileNotFoundError:
            with open("MySecretNotes.txt", 'w') as fp:
                fp.write(f"\n{title}\n{content_encrypt}")
        finally:
            title_entry.delete(0, END)
            notes_text.delete("1.0", END)
            password_entry.delete(0, END)


save_encrypt_button = Button(window, text="Save and Encrypt", command=save_encrypt, bg=BUTTON_COLOR,
                             fg=BUTTON_TEXT_COLOR, font=FONT)
save_encrypt_button.pack(padx=10, pady=10)


# Decrypt button
def decrypt():
    title = title_entry.get()
    secret_note_content = notes_text.get("1.0", END)
    password = password_entry.get()
    if len(secret_note_content) == 0 or len(password) == 0:
        messagebox.showwarning(title='Error', message='Please Enter the Requested İnformation')
    else:
        # Decrypt File
        try:
            content_decrypt = decode(password, secret_note_content)
            notes_text.delete("1.0", END)
            notes_text.insert("1.0", content_decrypt)
        except:
            messagebox.showerror(title='Error', message='Please Enter Encrypted Text')


decrypt_button = Button(window, text="Decrypt", command=decrypt, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, font=FONT)
decrypt_button.pack(padx=10, pady=10)
# Mainloop
window.mainloop()
