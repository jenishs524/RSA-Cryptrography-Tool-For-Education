"""
Base64 Encode/Decode Tab UI
Demonstrate Base64 encoding and decoding
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import os

from modules.crypto_engine import Base64Manager
from modules.theme import CybersecurityTheme, TextStyles, UIHelper


class Base64Tab(ttk.Frame):
    """Tab for Base64 encoding and decoding operations"""

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.build_ui()

    def build_ui(self):
        """Build the Base64 Tab UI"""
        # Title
        title_frame = tk.Frame(self, bg=CybersecurityTheme.BG_PRIMARY)
        title_frame.pack(fill=tk.X, padx=20, pady=(20, 10))
        
        title_label = tk.Label(
            title_frame,
            text="📊 Base64 Encode/Decode",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['header']
        )
        title_label.pack(anchor=tk.W)

        # Main content
        main_frame = tk.Frame(self, bg=CybersecurityTheme.BG_PRIMARY)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Information box
        info_text = (
            "Base64 is a binary-to-text encoding scheme that represents binary data in ASCII string format.\n"
            "It's NOT encryption - the data can be easily decoded by anyone.\n"
            "Base64 uses 64 characters: A-Z, a-z, 0-9, +, / and = for padding."
        )
        info_box = UIHelper.create_info_box(main_frame, "ℹ️ What is Base64?", info_text)
        info_box.pack(fill=tk.X, pady=(0, 15))

        # Left column - Encoding
        left_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        encode_label = tk.Label(
            left_frame,
            text="📝 Input Text / Binary",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        encode_label.pack(anchor=tk.W, pady=(0, 5))

        self.input_text = UIHelper.create_code_text(left_frame, height=12)
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        input_btn_frame = tk.Frame(left_frame, bg=CybersecurityTheme.BG_PRIMARY)
        input_btn_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Button(
            input_btn_frame,
            text="📂 Load from File",
            command=self.load_input_file
        ).pack(side=tk.LEFT, padx=(0, 5))

        ttk.Button(
            input_btn_frame,
            text="Clear",
            command=lambda: self.input_text.delete("1.0", tk.END)
        ).pack(side=tk.LEFT, padx=5)

        # Encode button
        encode_btn = tk.Button(
            left_frame,
            text="🔄 ENCODE TO BASE64 →",
            bg=CybersecurityTheme.ACCENT_GREEN,
            fg="white",
            font=TextStyles.FONTS['title'],
            command=self.encode_text,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        encode_btn.pack(fill=tk.X)

        # Right column - Decoding
        right_frame = tk.Frame(main_frame, bg=CybersecurityTheme.BG_PRIMARY)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0))

        decode_label = tk.Label(
            right_frame,
            text="🔤 Base64 Output",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['title']
        )
        decode_label.pack(anchor=tk.W, pady=(0, 5))

        self.output_text = UIHelper.create_code_text(right_frame, height=12)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        output_btn_frame = tk.Frame(right_frame, bg=CybersecurityTheme.BG_PRIMARY)
        output_btn_frame.pack(fill=tk.X, pady=(0, 10))

        ttk.Button(
            output_btn_frame,
            text="Copy",
            command=lambda: self.copy_to_clipboard(self.output_text.get("1.0", tk.END))
        ).pack(side=tk.LEFT, padx=(0, 5))

        ttk.Button(
            output_btn_frame,
            text="Save",
            command=self.save_output
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            output_btn_frame,
            text="Clear",
            command=lambda: self.output_text.delete("1.0", tk.END)
        ).pack(side=tk.LEFT, padx=5)

        # Decode button
        decode_btn = tk.Button(
            right_frame,
            text="← DECODE FROM BASE64",
            bg=CybersecurityTheme.ACCENT_ORANGE,
            fg="white",
            font=TextStyles.FONTS['title'],
            command=self.decode_text,
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        decode_btn.pack(fill=tk.X)

        # Bottom section - Additional tools
        bottom_frame = tk.Frame(self, bg=CybersecurityTheme.BG_PRIMARY)
        bottom_frame.pack(fill=tk.X, padx=20, pady=(20, 10))

        tools_label = tk.Label(
            bottom_frame,
            text="🛠️ Additional Tools",
            bg=CybersecurityTheme.BG_PRIMARY,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['title']
        )
        tools_label.pack(anchor=tk.W, pady=(0, 10))

        tools_frame = tk.Frame(bottom_frame, bg=CybersecurityTheme.BG_TERTIARY, relief=tk.FLAT, bd=1)
        tools_frame.pack(fill=tk.X)

        ttk.Button(
            tools_frame,
            text="Convert Key PEM to Base64",
            command=self.convert_pem_to_base64
        ).pack(fill=tk.X, padx=10, pady=10)

        ttk.Button(
            tools_frame,
            text="Convert Base64 to Key PEM",
            command=self.convert_base64_to_pem
        ).pack(fill=tk.X, padx=10, pady=(0, 10))

    def encode_text(self):
        """Encode input text to Base64"""
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Empty", "Please enter text to encode")
                return
            
            encoded = Base64Manager.encode_to_base64(text)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", encoded)
            
            # Show statistics
            stats = f"\n\n[INFO] Original size: {len(text)} bytes | Encoded size: {len(encoded)} bytes"
            self.output_text.insert(tk.END, stats)
            
            messagebox.showinfo("Success", "✓ Text encoded to Base64!")
        except Exception as e:
            messagebox.showerror("Error", f"Encoding failed:\n{str(e)}")

    def decode_text(self):
        """Decode Base64 text"""
        try:
            text = self.output_text.get("1.0", tk.END).strip()
            if not text:
                messagebox.showwarning("Empty", "Please enter Base64 to decode")
                return
            
            # Remove info lines
            if "[INFO]" in text:
                text = text.split("\n\n[INFO]")[0]
            
            decoded = Base64Manager.decode_from_base64(text).decode('utf-8', errors='replace')
            
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert("1.0", decoded)
            
            messagebox.showinfo("Success", "✓ Base64 decoded!")
        except Exception as e:
            messagebox.showerror("Error", f"Decoding failed:\n{str(e)}")

    def load_input_file(self):
        """Load file content for encoding"""
        try:
            filename = filedialog.askopenfilename(
                title="Select file to encode",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                self.input_text.delete("1.0", tk.END)
                self.input_text.insert("1.0", content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")

    def save_output(self):
        """Save encoded/decoded output to file"""
        try:
            content = self.output_text.get("1.0", tk.END).strip()
            if not content:
                messagebox.showwarning("Empty", "Nothing to save")
                return
            
            # Remove info lines for saving
            if "[INFO]" in content:
                content = content.split("\n\n[INFO]")[0]
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                initialfile="base64_output.txt"
            )
            
            if filename:
                with open(filename, 'w') as f:
                    f.write(content)
                messagebox.showinfo("Success", f"✓ Saved to:\n{os.path.basename(filename)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save:\n{str(e)}")

    def convert_pem_to_base64(self):
        """Convert PEM file to Base64 encoding"""
        try:
            filename = filedialog.askopenfilename(
                title="Select PEM file",
                filetypes=[("PEM files", "*.pem"), ("Key files", "*.key"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'r') as f:
                    pem_content = f.read()
                
                encoded = Base64Manager.encode_to_base64(pem_content)
                
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert("1.0", encoded)
                
                messagebox.showinfo("Success", "✓ PEM converted to Base64!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert:\n{str(e)}")

    def convert_base64_to_pem(self):
        """Convert Base64 back to PEM format"""
        try:
            base64_text = self.output_text.get("1.0", tk.END).strip()
            if not base64_text:
                messagebox.showwarning("Empty", "Please enter Base64 content")
                return
            
            # Remove info lines
            if "[INFO]" in base64_text:
                base64_text = base64_text.split("\n\n[INFO]")[0]
            
            pem_content = Base64Manager.decode_base64_to_key(base64_text)
            
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert("1.0", pem_content)
            
            messagebox.showinfo("Success", "✓ Base64 converted to PEM!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert:\n{str(e)}")

    def copy_to_clipboard(self, text):
        """Copy text to clipboard"""
        try:
            # Remove info lines
            if "[INFO]" in text:
                text = text.split("\n\n[INFO]")[0]
            
            self.master.clipboard_clear()
            self.master.clipboard_append(text.strip())
            self.master.update()
            messagebox.showinfo("Copied", "✓ Copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy:\n{str(e)}")
