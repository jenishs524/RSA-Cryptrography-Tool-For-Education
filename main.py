"""
RSA Cryptography Educational Tool
Main Application
Professional desktop application for learning RSA cryptography and Base64 encoding
"""

import tkinter as tk
from tkinter import ttk, messagebox
import os

from modules.theme import CybersecurityTheme, TextStyles
from ui.key_generation_tab import KeyGenerationTab
from ui.base64_tab import Base64Tab
from ui.educational_demo_tab import EducationalDemoTab
from ui.encryption_tab import EncryptionTab


class RSACryptoApp:
    """Main application class"""

    def __init__(self, root):
        self.root = root
        self.root.title("RSA Cryptography Educational Tool")
        self.root.geometry("1400x800")
        self.root.minsize(1000, 600)
        
        # Configure theme
        CybersecurityTheme.configure_tkinter_theme(root)
        
        # Set icon if available
        try:
            # Try to set a window icon if it exists
            pass
        except Exception:
            pass
        
        self.current_private_key = None
        self.current_public_key = None
        
        self.build_ui()

    def build_ui(self):
        """Build the main application UI"""
        # Header
        self.build_header()
        
        # Main content area with tabs
        self.build_tabs()
        
        # Footer
        self.build_footer()

    def build_header(self):
        """Build application header"""
        header_frame = tk.Frame(self.root, bg=CybersecurityTheme.ACCENT_BLUE)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        
        # Logo and title
        content_frame = tk.Frame(header_frame, bg=CybersecurityTheme.ACCENT_BLUE)
        content_frame.pack(fill=tk.X, padx=20, pady=15)
        
        title_label = tk.Label(
            content_frame,
            text="🔐 RSA Cryptography Educational Tool",
            bg=CybersecurityTheme.ACCENT_BLUE,
            fg="white",
            font=('Courier New', 18, 'bold')
        )
        title_label.pack(side=tk.LEFT)
        
        subtitle_label = tk.Label(
            content_frame,
            text="Learn RSA, Base64, Encryption & Digital Signatures",
            bg=CybersecurityTheme.ACCENT_BLUE,
            fg="white",
            font=('Courier New', 10)
        )
        subtitle_label.pack(side=tk.LEFT, padx=(20, 0))

    def build_tabs(self):
        """Build main tabbed interface"""
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        # Tab 1: Key Generation
        self.key_gen_tab = KeyGenerationTab(
            notebook,
            on_key_generated_callback=self.on_keys_generated
        )
        notebook.add(self.key_gen_tab, text="🔑 Key Generation")
        
        # Tab 2: Base64 Operations
        self.base64_tab = Base64Tab(notebook)
        notebook.add(self.base64_tab, text="📊 Base64 Encode/Decode")
        
        # Tab 3: Educational Demo
        self.edu_tab = EducationalDemoTab(notebook)
        notebook.add(self.edu_tab, text="📚 Educational Demo")
        
        # Tab 4: Encryption
        self.enc_tab = EncryptionTab(
            notebook,
            private_key=self.current_private_key,
            public_key=self.current_public_key
        )
        notebook.add(self.enc_tab, text="🔒 Encryption")

    def build_footer(self):
        """Build application footer"""
        footer_frame = tk.Frame(self.root, bg=CybersecurityTheme.BG_SECONDARY, relief=tk.SOLID, bd=1)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_content = tk.Frame(footer_frame, bg=CybersecurityTheme.BG_SECONDARY)
        footer_content.pack(fill=tk.X, padx=20, pady=10)
        
        # Left section
        info_label = tk.Label(
            footer_content,
            text="💡 Tip: Start with 'Key Generation' tab to create RSA keys, then explore encryption!",
            bg=CybersecurityTheme.BG_SECONDARY,
            fg=CybersecurityTheme.FG_SECONDARY,
            font=TextStyles.FONTS['small']
        )
        info_label.pack(side=tk.LEFT)
        
        # Right section
        btn_frame = tk.Frame(footer_content, bg=CybersecurityTheme.BG_SECONDARY)
        btn_frame.pack(side=tk.RIGHT)
        
        ttk.Button(
            btn_frame,
            text="ℹ️ About",
            command=self.show_about
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(
            btn_frame,
            text="⚙️ Help",
            command=self.show_help
        ).pack(side=tk.LEFT)

    def on_keys_generated(self, private_key, public_key):
        """Callback when keys are generated"""
        self.current_private_key = private_key
        self.current_public_key = public_key
        self.enc_tab.private_key = private_key
        self.enc_tab.public_key = public_key
        self.enc_tab.update_key_status()

    def show_about(self):
        """Show about dialog"""
        about_text = """
RSA CRYPTOGRAPHY EDUCATIONAL TOOL
Version 1.0

A professional learning tool to understand:
• RSA asymmetric cryptography
• Public and private key concepts
• Base64 encoding and decoding
• RSA encryption and decryption
• Digital signatures and verification

KEY PRINCIPLES:
✓ Public Key → Private Key: IMPOSSIBLE (mathematically proven)
✓ Private Key → Public Key: EASY (automatic derivation)
✓ Base64: ENCODING (not encryption)
✓ RSA: SECURE when using 2048-bit+ keys

USAGE:
1. Start with "Key Generation" to create RSA keys
2. Try "Base64" tab to understand encoding
3. Read "Educational Demo" for concepts
4. Use "Encryption" to practice RSA operations

SECURITY WARNING:
⚠️ This is an EDUCATIONAL tool
⚠️ Do NOT use for production security
⚠️ Always keep private keys secret
⚠️ Use established cryptographic libraries for real applications

© 2024 - Educational Purpose Only
        """
        messagebox.showinfo("About", about_text)

    def show_help(self):
        """Show help dialog"""
        help_text = """
GETTING STARTED:

1️⃣ KEY GENERATION TAB
   • Select key size (2048-bit recommended)
   • Click "Generate New Key Pair"
   • Keys are automatically displayed in PEM format
   • Both keys are Base64 encoded for transport

2️⃣ BASE64 TAB
   • Enter text and click "Encode to Base64"
   • See how binary becomes text
   • Decode to reverse the process
   • Remember: Base64 is NOT encryption!

3️⃣ EDUCATIONAL DEMO TAB
   • Learn how RSA works mathematically
   • Understand why Private ← Public is impossible
   • Read about computational complexity
   • Get historical factorization data

4️⃣ ENCRYPTION TAB
   • Load your RSA key pair
   • Encrypt messages with public key
   • Only private key can decrypt
   • Try digital signatures with verification

KEY CONCEPTS:

RSA SECURITY:
Based on Integer Factorization Problem
n = p × q (p, q are huge secret primes)
Finding p and q from n is computationally hard
This is why 2048-bit RSA is secure

KEY DERIVATION:
✓ Private → Public: Mathematically straightforward
✗ Public → Private: Mathematically impossible
  (would require factoring a 2048-bit number = ~trillion years)

ENCODING vs ENCRYPTION:
• Encoding: Format conversion (PEM ↔ Base64)
• Encryption: Scrambles data with a key for security

DIGITAL SIGNATURES:
• Sign: Use private key to create signature
• Verify: Use public key to verify signature
• Proves authenticity and integrity

PRACTICAL TIPS:
• Use 2048-bit keys minimum for security
• Never share your private key
• Base64 keys are safe to share (use encryption for actual messages)
• Always verify digital signatures from trusted sources
        """
        messagebox.showinfo("Help", help_text)


def main():
    """Main entry point"""
    root = tk.Tk()
    app = RSACryptoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
