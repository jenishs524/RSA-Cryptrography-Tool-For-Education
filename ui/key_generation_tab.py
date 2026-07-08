"""
Key Generation Tab UI
Generate and manage RSA key pairs
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os

from modules.crypto_engine import CryptoEngine, Base64Manager
from modules.theme import CybersecurityTheme, TextStyles, UIHelper


class KeyGenerationTab(ttk.Frame):
    """Tab for generating and managing RSA key pairs"""

    def __init__(self, parent, on_key_generated_callback=None):
        super().__init__(parent)
        self.on_key_generated = on_key_generated_callback
        
        self.current_private_key = None
        self.current_public_key = None
        self.current_private_key_base64 = None
        self.current_public_key_base64 = None
        
        self.configure(style='TFrame')
        self.build_ui()

    def build_ui(self):
        """Build the Key Generation UI"""
        # Title
        title_frame = tk.Frame(self, bg=CybersecurityTheme.BG_PRIMARY)
        title_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        title_label = tk.Label(
            title_frame,
            text="🔐 RSA Key Generation",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['header']
        )
        title_label.pack(anchor=tk.W)

        # Main content
        main_frame = tk.Frame(self, bg=CybersecurityTheme.BG_PRIMARY)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Left column - Key generation settings
        left_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Key size selection
        size_frame = tk.LabelFrame(
            left_frame,
            text="Key Configuration",
            bg=CybersecurityTheme.BG_TERTIARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['title'],
            padx=15,
            pady=15
        )
        size_frame.pack(fill=tk.X, pady=(0, 10))

        tk.Label(
            size_frame,
            text="Select Key Size (bits):",
            bg=CybersecurityTheme.BG_TERTIARY,
            fg=CybersecurityTheme.FG_PRIMARY,
            font=TextStyles.FONTS['body']
        ).pack(anchor=tk.W, pady=(0, 10))

        self.key_size_var = tk.StringVar(value="2048")
        for size in ["2048", "3072", "4096"]:
            rb = tk.Radiobutton(
                size_frame,
                text=f"{size} bits (recommended: 2048+)",
                variable=self.key_size_var,
                value=size,
                bg=CybersecurityTheme.BG_TERTIARY,
                fg=CybersecurityTheme.FG_PRIMARY,
                selectcolor=CybersecurityTheme.ACCENT_BLUE,
                font=TextStyles.FONTS['body']
            )
            rb.pack(anchor=tk.W, pady=5)

        # Generate button
        ttk.Button(
            size_frame,
            text="🔑 Generate New Key Pair",
            command=self.generate_keypair
        ).pack(fill=tk.X, pady=(15, 0))

        # Import section
        import_frame = tk.LabelFrame(
            left_frame,
            text="Import Existing Key",
            bg=CybersecurityTheme.BG_TERTIARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['title'],
            padx=15,
            pady=15
        )
        import_frame.pack(fill=tk.X, pady=(10, 0))

        ttk.Button(
            import_frame,
            text="📂 Load Private Key from File",
            command=self.import_private_key
        ).pack(fill=tk.X, pady=(0, 10))

        ttk.Button(
            import_frame,
            text="📂 Load Public Key from File",
            command=self.import_public_key
        ).pack(fill=tk.X)

        # Right column - Key display
        right_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        # Private Key section
        priv_label = tk.Label(
            right_frame,
            text="Private Key (PEM Format)",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        priv_label.pack(anchor=tk.W, pady=(0, 5))

        self.private_key_text = UIHelper.create_code_text(right_frame, height=8)
        self.private_key_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        priv_btn_frame = tk.Frame(right_frame, bg=CybersecurityTheme.BG_PRIMARY)
        priv_btn_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Button(
            priv_btn_frame,
            text="Copy",
            command=lambda: self.copy_to_clipboard(self.private_key_text.get("1.0", tk.END))
        ).pack(side=tk.LEFT, padx=(0, 5))

        ttk.Button(
            priv_btn_frame,
            text="Save",
            command=self.save_private_key
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            priv_btn_frame,
            text="Show Base64",
            command=lambda: self.show_base64_key(self.current_private_key_base64, "Private Key")
        ).pack(side=tk.LEFT, padx=5)

        # Public Key section
        pub_label = tk.Label(
            right_frame,
            text="Public Key (PEM Format)",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        pub_label.pack(anchor=tk.W, pady=(0, 5))

        self.public_key_text = UIHelper.create_code_text(right_frame, height=8)
        self.public_key_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        pub_btn_frame = tk.Frame(right_frame, bg=CybersecurityTheme.BG_PRIMARY)
        pub_btn_frame.pack(fill=tk.X)

        ttk.Button(
            pub_btn_frame,
            text="Copy",
            command=lambda: self.copy_to_clipboard(self.public_key_text.get("1.0", tk.END))
        ).pack(side=tk.LEFT, padx=(0, 5))

        ttk.Button(
            pub_btn_frame,
            text="Save",
            command=self.save_public_key
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            pub_btn_frame,
            text="Show Base64",
            command=lambda: self.show_base64_key(self.current_public_key_base64, "Public Key")
        ).pack(side=tk.LEFT, padx=5)

    def generate_keypair(self):
        """Generate a new RSA key pair"""
        try:
            key_size = int(self.key_size_var.get())
            
            # Disable button during generation
            for widget in self.winfo_children():
                if isinstance(widget, tk.Frame):
                    for w in widget.winfo_children():
                        if isinstance(w, tk.Frame):
                            for btn in w.winfo_children():
                                if isinstance(btn, ttk.Button):
                                    btn.configure(state='disabled')
            
            self.master.update()
            
            private_key_pem, public_key_pem = CryptoEngine.generate_rsa_keypair(key_size)
            
            self.current_private_key = private_key_pem.decode('utf-8')
            self.current_public_key = public_key_pem.decode('utf-8')
            
            # Encode to Base64
            self.current_private_key_base64 = Base64Manager.encode_key_to_base64(private_key_pem)
            self.current_public_key_base64 = Base64Manager.encode_key_to_base64(public_key_pem)
            
            # Display keys
            self.private_key_text.delete("1.0", tk.END)
            self.private_key_text.insert("1.0", self.current_private_key)
            
            self.public_key_text.delete("1.0", tk.END)
            self.public_key_text.insert("1.0", self.current_public_key)
            
            # Re-enable buttons
            for widget in self.winfo_children():
                if isinstance(widget, tk.Frame):
                    for w in widget.winfo_children():
                        if isinstance(w, tk.Frame):
                            for btn in w.winfo_children():
                                if isinstance(btn, ttk.Button):
                                    btn.configure(state='normal')
            
            messagebox.showinfo("Success", f"✓ Generated {key_size}-bit RSA key pair successfully!")
            
            if self.on_key_generated:
                self.on_key_generated(self.current_private_key, self.current_public_key)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate keys:\n{str(e)}")

    def import_private_key(self):
        """Import private key from file"""
        try:
            filename = filedialog.askopenfilename(
                title="Load Private Key",
                filetypes=[("PEM files", "*.pem"), ("Key files", "*.key"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'r') as f:
                    key_content = f.read()
                
                # Validate
                if CryptoEngine.validate_private_key(key_content):
                    self.current_private_key = key_content
                    self.current_private_key_base64 = Base64Manager.encode_key_to_base64(key_content)
                    
                    self.private_key_text.delete("1.0", tk.END)
                    self.private_key_text.insert("1.0", key_content)
                    
                    # Auto-derive public key
                    try:
                        public_key_pem = CryptoEngine.derive_public_from_private(key_content)
                        self.current_public_key = public_key_pem.decode('utf-8')
                        self.current_public_key_base64 = Base64Manager.encode_key_to_base64(public_key_pem)
                        
                        self.public_key_text.delete("1.0", tk.END)
                        self.public_key_text.insert("1.0", self.current_public_key)
                        
                        messagebox.showinfo("Success", "✓ Private key loaded!\n✓ Public key automatically derived!")
                    except Exception as e:
                        messagebox.showerror("Error", f"Could not derive public key:\n{str(e)}")
                else:
                    messagebox.showerror("Error", "Invalid private key format")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key:\n{str(e)}")

    def import_public_key(self):
        """Import public key from file"""
        try:
            filename = filedialog.askopenfilename(
                title="Load Public Key",
                filetypes=[("PEM files", "*.pem"), ("Key files", "*.key"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'r') as f:
                    key_content = f.read()
                
                # Validate
                if CryptoEngine.validate_public_key(key_content):
                    self.current_public_key = key_content
                    self.current_public_key_base64 = Base64Manager.encode_key_to_base64(key_content)
                    
                    self.public_key_text.delete("1.0", tk.END)
                    self.public_key_text.insert("1.0", key_content)
                    
                    messagebox.showinfo(
                        "Public Key Loaded",
                        "✓ Public key loaded successfully!\n\n"
                        "📌 Note: Private key cannot be derived from public key.\n"
                        "This is the foundation of RSA security!"
                    )
                else:
                    messagebox.showerror("Error", "Invalid public key format")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key:\n{str(e)}")

    def save_private_key(self):
        """Save private key to file"""
        if not self.current_private_key:
            messagebox.showwarning("Empty", "No private key to save")
            return
        
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".pem",
                filetypes=[("PEM files", "*.pem"), ("Key files", "*.key"), ("All files", "*.*")],
                initialfile="private_key.pem"
            )
            
            if filename:
                with open(filename, 'w') as f:
                    f.write(self.current_private_key)
                messagebox.showinfo("Success", f"✓ Private key saved to:\n{os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save key:\n{str(e)}")

    def save_public_key(self):
        """Save public key to file"""
        if not self.current_public_key:
            messagebox.showwarning("Empty", "No public key to save")
            return
        
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".pem",
                filetypes=[("PEM files", "*.pem"), ("Key files", "*.key"), ("All files", "*.*")],
                initialfile="public_key.pem"
            )
            
            if filename:
                with open(filename, 'w') as f:
                    f.write(self.current_public_key)
                messagebox.showinfo("Success", f"✓ Public key saved to:\n{os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save key:\n{str(e)}")

    def show_base64_key(self, base64_key, key_type):
        """Show Base64 encoded key in a new window"""
        if not base64_key:
            messagebox.showwarning("Empty", f"No {key_type} to display")
            return
        
        window = tk.Toplevel(self.master)
        window.title(f"{key_type} - Base64 Encoded")
        window.geometry("700x400")
        window.configure(bg=CybersecurityTheme.BG_PRIMARY)
        
        title = tk.Label(
            window,
            text=f"{key_type} (Base64 Encoded)",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['title']
        )
        title.pack(padx=10, pady=(10, 5))
        
        text_widget = UIHelper.create_code_text(window, height=15, width=80)
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_widget.insert("1.0", base64_key)
        text_widget.configure(state='disabled')
        
        btn_frame = tk.Frame(window, bg=CybersecurityTheme.BG_PRIMARY)
        btn_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        
        ttk.Button(
            btn_frame,
            text="Copy Base64",
            command=lambda: self.copy_to_clipboard(base64_key)
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Button(
            btn_frame,
            text="Save to File",
            command=lambda: self.save_base64_key(base64_key, key_type)
        ).pack(side=tk.LEFT, padx=5)

    def save_base64_key(self, base64_key, key_type):
        """Save Base64 encoded key to file"""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("Base64 files", "*.b64"), ("All files", "*.*")],
                initialfile=f"{key_type.lower().replace(' ', '_')}_base64.txt"
            )
            
            if filename:
                with open(filename, 'w') as f:
                    f.write(base64_key)
                messagebox.showinfo("Success", f"✓ Base64 key saved to:\n{os.path.basename(filename)}")
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
