import os
import ecdsa
import hashlib
import base58
import requests
import bitcoin
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Function to generate a private key
def generate_private_key():
    return os.urandom(32)

# Function to convert a private key to WIF format
def private_key_to_wif(private_key):
    extended_key = b"\x80" + private_key
    checksum = hashlib.sha256(hashlib.sha256(extended_key).digest()).digest()[:4]
    return base58.b58encode(extended_key + checksum)

# Function to convert a private key to a public key
def private_key_to_public_key(private_key):
    signing_key = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    return bytes.fromhex("04") + verifying_key.to_string()

# Function to check balance from blockchain API
def check_balance():
    try:
        private_key = generate_private_key()
        wif_private_key = private_key_to_wif(private_key).decode()
        public_key = private_key_to_public_key(private_key).hex()
        address = bitcoin.pubkey_to_address(public_key)
        
        response = requests.get("https://blockchain.info/balance", params={"active": address})
        response.raise_for_status()
        data = response.json()
        final_balance = data[address]["final_balance"]
        
        result_text = (
            f"WIF Private Key: {wif_private_key}\n"
            f"Public Key: {public_key}\n"
            f"Address: {address}\n"
            f"Balance: {final_balance}\n"
        )
        result_box.delete(1.0, tk.END)  # Clear previous results
        result_box.insert(tk.END, result_text)
        
        if final_balance != 0:
            with open('FoundAddress.txt', 'a') as f:
                f.write(f"{wif_private_key}\n")
            result_box.insert(tk.END, "Donate to HCMLXOX: bc1qk5tpd68l4gfj6uzkq7u0l998dzvzyjpzhgpvnm\n")
        else:
            with open('log.txt', 'a') as f:
                f.write(f"{wif_private_key}\n")
    except Exception as e:
        messagebox.showerror("Error", "Please check your network connection")
        print(e)

# Function to handle button click event
def on_check_balance():
    check_balance()

# Create the main window
root = tk.Tk()
root.title("Bitcoin Roulette")

# Create and place widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a label to display the banner text
banner_text = (
    "░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░       ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓████████▓▒░ \n"
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░        \n"
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░        \n"
    "░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓██████▓▒░    ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓██████▓▒░   \n"
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░        \n"
    "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓█▓▒░        \n"
    "░▒▓███████▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓████████▓▒░  ░▒▓█▓▒░      ░▒▓█▓▒░   ░▒▓████████▓▒░ \n"
)

banner_label = tk.Label(root, text=banner_text, font=('Courier', 8), justify='center')
banner_label.pack()

check_balance_button = tk.Button(frame, text="Spin!!!", command=on_check_balance)
check_balance_button.pack()

result_box = scrolledtext.ScrolledText(frame, width=100, height=15)
result_box.pack(pady=10)

# Run the application
root.mainloop()