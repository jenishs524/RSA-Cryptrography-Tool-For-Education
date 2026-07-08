"""
Encryption/Decryption and Digital Signatures Tab UI
Demonstrate RSA encryption and digital signatures
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os
import base64

from modules.crypto_engine import RSAEncryption, CryptoEngine, Base64Manager
from modules.theme import CybersecurityTheme, TextStyles, UIHelper


class EncryptionTab(ttk.Frame):
    """Tab for RSA encryption/decryption and digital signatures"""

    def __init__(self, parent, private_key=None, public_key=None):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.private_key = private_key
        self.public_key = public_key
        self.current_ciphertext = None
        self.build_ui()

    def build_ui(self):
        """Build the Encryption Tab UI"""
        # Create notebook for sections
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tab 1: Encryption/Decryption
        self.build_encryption_tab(notebook)
        
        # Tab 2: Digital Signatures
        self.build_signature_tab(notebook)

    def build_encryption_tab(self, notebook):
        """Build encryption/decryption section"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="🔐 Encryption/Decryption")
        
        frame.configure(style='TFrame')
        main_frame = tk.Frame(frame, bg=CybersecurityTheme.BG_PRIMARY)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Title
        title_label = tk.Label(
            main_frame,
            text="RSA Encryption/Decryption",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['header']
        )
        title_label.pack(anchor=tk.W, pady=(0, 15))

        # Key loading section
        key_frame = tk.LabelFrame(
            main_frame,
            text="🔑 Load Keys",
            bg=CybersecurityTheme.BG_TERTIARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['title'],
            padx=15,
            pady=15
        )
        key_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Button(
            key_frame,
            text="📂 Load Private Key",
            command=self.load_private_key_file
        ).pack(side=tk.LEFT, padx=(0, 10))

        ttk.Button(
            key_frame,
            text="📂 Load Public Key",
            command=self.load_public_key_file
        ).pack(side=tk.LEFT, padx=10)

        self.key_status_label = tk.Label(
            key_frame,
            text="Status: No keys loaded",
            bg=CybersecurityTheme.BG_TERTIARY,
            fg=CybersecurityTheme.FG_SECONDARY,
            font=TextStyles.FONTS['small']
        )
        self.key_status_label.pack(side=tk.RIGHT)

        # Left column - Encryption
        left_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        enc_label = tk.Label(
            left_frame,
            text="📝 Plaintext Message",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        enc_label.pack(anchor=tk.W, pady=(0, 5))

        self.plaintext_input = UIHelper.create_code_text(left_frame, height=10)
        self.plaintext_input.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        encrypt_btn = tk.Button(
            left_frame,
            text="🔒 ENCRYPT MESSAGE →",
            bg=CybersecurityTheme.ACCENT_GREEN,
            fg="white",
            font=TextStyles.FONTS['title'],
            command=self.encrypt_message,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        encrypt_btn.pack(fill=tk.X)

        # Right column - Decryption
        right_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        dec_label = tk.Label(
            right_frame,
            text="🔤 Ciphertext (Base64)",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        dec_label.pack(anchor=tk.W, pady=(0, 5))

        self.ciphertext_output = UIHelper.create_code_text(right_frame, height=10)
        self.ciphertext_output.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        cipher_btn_frame = tk.Frame(right_frame, bg=CybersecurityTheme.BG_PRIMARY)
        cipher_btn_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Button(
            cipher_btn_frame,
            text="Copy",
            command=lambda: self.copy_to_clipboard(self.ciphertext_output.get("1.0", tk.END))
        ).pack(side=tk.LEFT, padx=(0, 5))

        ttk.Button(
            cipher_btn_frame,
            text="Save",
            command=self.save_ciphertext
        ).pack(side=tk.LEFT, padx=5)

        decrypt_btn = tk.Button(
            right_frame,
            text="← DECRYPT MESSAGE",
            bg=CybersecurityTheme.ACCENT_ORANGE,
            fg="white",
            font=TextStyles.FONTS['title'],
            command=self.decrypt_message,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        decrypt_btn.pack(fill=tk.X)

    def build_signature_tab(self, notebook):
        """Build digital signature section"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="✍️ Digital Signatures")
        
        frame.configure(style='TFrame')
        main_frame = tk.Frame(frame, bg=CybersecurityTheme.BG_PRIMARY)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Title
        title_label = tk.Label(
            main_frame,
            text="RSA Digital Signatures",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['header']
        )
        title_label.pack(anchor=tk.W, pady=(0, 10))

        # Info box
        info_text = (
            "Digital signatures prove authenticity and integrity:\n"
            "• SIGN: Use PRIVATE KEY to create a signature\n"
            "• VERIFY: Use PUBLIC KEY to verify the signature\n\n"
            "If the signature is valid, it proves:\n"
            "1. The message came from the holder of the private key\n"
            "2. The message hasn't been tampered with"
        )
        info_box = UIHelper.create_info_box(main_frame, "ℹ️ What are Digital Signatures?", info_text)
        info_box.pack(fill=tk.X, pady=(0, 15))

        # Left column - Message to sign
        left_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        msg_label = tk.Label(
            left_frame,
            text="📝 Message to Sign",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        msg_label.pack(anchor=tk.W, pady=(0, 5))

        self.sign_message_input = UIHelper.create_code_text(left_frame, height=8)
        self.sign_message_input.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        sign_btn = tk.Button(
            left_frame,
            text="✍️ CREATE SIGNATURE →",
            bg=CybersecurityTheme.ACCENT_PURPLE,
            fg="white",
            font=TextStyles.FONTS['title'],
            command=self.create_signature,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        sign_btn.pack(fill=tk.X)

        # Right column - Signature verification
        right_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        sig_label = tk.Label(
            right_frame,
            text="🔐 Digital Signature (Base64)",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        sig_label.pack(anchor=tk.W, pady=(0, 5))

        self.signature_output = UIHelper.create_code_text(right_frame, height=8)
        self.signature_output.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        sig_btn_frame = tk.Frame(right_frame, bg=CybersecurityTheme.BG_PRIMARY)
        sig_btn_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Button(
            sig_btn_frame,
            text="Copy",
            command=lambda: self.copy_to_clipboard(self.signature_output.get("1.0", tk.END))
        ).pack(side=tk.LEFT, padx=(0, 5))

        ttk.Button(
            sig_btn_frame,
            text="Verify",
            command=self.verify_signature
        ).pack(side=tk.LEFT, padx=5)

    def load_private_key_file(self):
        """Load private key from file"""
        try:
            filename = filedialog.askopenfilename(
                title="Load Private Key",
                filetypes=[("PEM files", "*.pem"), ("Key files", "*.key"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'r') as f:
                    self.private_key = f.read()
                self.update_key_status()
                messagebox.showinfo("Loaded", "✓ Private key loaded!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key:\n{str(e)}")

    def load_public_key_file(self):
        """Load public key from file"""
        try:
            filename = filedialog.askopenfilename(
                title="Load Public Key",
                filetypes=[("PEM files", "*.pem"), ("Key files", "*.key"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'r') as f:
                    self.public_key = f.read()
                self.update_key_status()
                messagebox.showinfo("Loaded", "✓ Public key loaded!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key:\n{str(e)}")

    def update_key_status(self):
        """Update key status display"""
        priv_status = "✓ Private" if self.private_key else "✗ Private"
        pub_status = "✓ Public" if self.public_key else "✗ Public"
        self.key_status_label.config(text=f"Status: {priv_status} | {pub_status}")

    def encrypt_message(self):
        """Encrypt a message"""
        try:
            if not self.public_key:
                messagebox.showwarning("Missing Key", "Please load a public key first")
                return
            
            plaintext = self.plaintext_input.get("1.0", tk.END).strip()
            if not plaintext:
                messagebox.showwarning("Empty", "Please enter a message to encrypt")
                return
            
            ciphertext_bytes = RSAEncryption.encrypt_message(plaintext, self.public_key)
            ciphertext_b64 = Base64Manager.encode_to_base64(ciphertext_bytes)
            
            self.current_ciphertext = ciphertext_bytes
            
            self.ciphertext_output.delete("1.0", tk.END)
            self.ciphertext_output.insert("1.0", ciphertext_b64)
            
            messagebox.showinfo("Success", f"✓ Message encrypted!\nCiphertext size: {len(ciphertext_b64)} characters")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed:\n{str(e)}")

    def decrypt_message(self):
        """Decrypt a message"""
        try:
            if not self.private_key:
                messagebox.showwarning("Missing Key", "Please load a private key first")
                return
            
            ciphertext_b64 = self.ciphertext_output.get("1.0", tk.END).strip()
            if not ciphertext_b64:
                messagebox.showwarning("Empty", "Please enter ciphertext to decrypt")
                return
            
            ciphertext_bytes = Base64Manager.decode_from_base64(ciphertext_b64)
            plaintext = RSAEncryption.decrypt_message(ciphertext_bytes, self.private_key)
            
            self.plaintext_input.delete("1.0", tk.END)
            self.plaintext_input.insert("1.0", plaintext)
            
            messagebox.showinfo("Success", "✓ Message decrypted!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")

    def create_signature(self):
        """Create a digital signature"""
        try:
            if not self.private_key:
                messagebox.showwarning("Missing Key", "Please load a private key first")
                return
            
            message = self.sign_message_input.get("1.0", tk.END).strip()
            if not message:
                messagebox.showwarning("Empty", "Please enter a message to sign")
                return
            
            signature_bytes = RSAEncryption.sign_message(message, self.private_key)
            signature_b64 = Base64Manager.encode_to_base64(signature_bytes)
            
            self.signature_output.delete("1.0", tk.END)
            self.signature_output.insert("1.0", signature_b64)
            
            messagebox.showinfo("Success", f"✓ Signature created!\nSignature size: {len(signature_b64)} characters")
        except Exception as e:
            messagebox.showerror("Error", f"Signing failed:\n{str(e)}")

    def verify_signature(self):
        """Verify a digital signature"""
        try:
            if not self.public_key:
                messagebox.showwarning("Missing Key", "Please load a public key first")
                return
            
            message = self.sign_message_input.get("1.0", tk.END).strip()
            signature_b64 = self.signature_output.get("1.0", tk.END).strip()
            
            if not message or not signature_b64:
                messagebox.showwarning("Empty", "Please enter both message and signature")
                return
            
            signature_bytes = Base64Manager.decode_from_base64(signature_b64)
            is_valid = RSAEncryption.verify_signature(message, signature_bytes, self.public_key)
            
            if is_valid:
                messagebox.showinfo("Valid", "✓ Signature is VALID!\nThe message is authentic and untampered.")
            else:
                messagebox.showwarning("Invalid", "✗ Signature is INVALID!\nThe message may have been tampered with.")
        except Exception as e:
            messagebox.showerror("Error", f"Verification failed:\n{str(e)}")

    def save_ciphertext(self):
        """Save ciphertext to file"""
        try:
            ciphertext = self.ciphertext_output.get("1.0", tk.END).strip()
            if not ciphertext:
                messagebox.showwarning("Empty", "Nothing to save")
                return
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".enc",
                filetypes=[("Encrypted files", "*.enc"), ("Text files", "*.txt"), ("All files", "*.*")],
                initialfile="encrypted_message.enc"
            )
            
            if filename:
                with open(filename, 'w') as f:
                    f.write(ciphertext)
                messagebox.showinfo("Success", f"✓ Ciphertext saved!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save:\n{str(e)}")

    def copy_to_clipboard(self, text):
        """Copy text to clipboard"""
        try:
            self.master.clipboard_clear()
            self.master.clipboard_append(text.strip())
            self.master.update()
            messagebox.showinfo("Copied", "✓ Copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy:\n{str(e)}")
