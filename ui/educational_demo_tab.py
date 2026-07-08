"""
Educational Demo Tab UI
Learn RSA concepts, key relationships, and why private keys can't be derived
"""

import tkinter as tk
from tkinter import ttk, messagebox
from modules.crypto_engine import CryptoEngine
from modules.theme import CybersecurityTheme, TextStyles, UIHelper


class EducationalDemoTab(ttk.Frame):
    """Tab for educational content about RSA and cryptography"""

    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style='TFrame')
        self.build_ui()

    def build_ui(self):
        """Build the Educational Demo UI"""
        # Create notebook for sections
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tab 1: RSA Concepts
        self.build_rsa_concepts_tab(notebook)
        
        # Tab 2: Key Relationships
        self.build_key_relationships_tab(notebook)
        
        # Tab 3: Public vs Private Key
        self.build_key_comparison_tab(notebook)
        
        # Tab 4: Why Private Keys Can't Be Derived
        self.build_irreversibility_tab(notebook)
        
        # Tab 5: Practical Demo
        self.build_practical_demo_tab(notebook)

    def build_rsa_concepts_tab(self, notebook):
        """Build RSA Concepts section"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="📚 RSA Concepts")
        
        frame.configure(style='TFrame')
        
        canvas = tk.Canvas(frame, bg=CybersecurityTheme.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=CybersecurityTheme.BG_PRIMARY)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Content
        content_frame = tk.Frame(scrollable_frame, bg=CybersecurityTheme.BG_PRIMARY)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        sections = [
            ("🔐 What is RSA?", 
             "RSA (Rivest-Shamir-Adleman) is an asymmetric cryptographic algorithm that uses a pair of keys:\n"
             "• PUBLIC KEY: Can be shared with anyone\n"
             "• PRIVATE KEY: Must be kept secret\n\n"
             "Data encrypted with public key can ONLY be decrypted with private key."),
            
            ("🔑 How RSA Works",
             "1. Two large prime numbers (p, q) are multiplied: n = p × q\n"
             "2. Public exponent (e) and private exponent (d) are calculated\n"
             "3. Public key = (n, e)\n"
             "4. Private key = (n, d)\n"
             "5. Encryption: C = M^e mod n\n"
             "6. Decryption: M = C^d mod n"),
            
            ("💡 The Mathematical Foundation",
             "RSA Security relies on the DIFFICULTY of factoring large numbers.\n\n"
             "Given n = p × q where p and q are huge primes:\n"
             "• Finding p and q from n is computationally infeasible\n"
             "• This makes it impossible to derive d (private exponent) from e (public exponent)\n"
             "• Therefore: It's impossible to reverse Public Key → Private Key\n\n"
             "2048-bit RSA requires factoring a 2048-bit number with modern computers.\n"
             "This would take TRILLIONS of years with current technology!"),
            
            ("🎯 Key Sizes",
             "• 512-bit: BROKEN (factored in 1999)\n"
             "• 768-bit: BROKEN (factored in 2009, took 3 years)\n"
             "• 1024-bit: WEAK (not recommended for new systems)\n"
             "• 2048-bit: SECURE (standard for today)\n"
             "• 4096-bit: VERY SECURE (for high-security applications)\n\n"
             "This tool uses 2048-bit+ keys for education."),
        ]

        for title, content in sections:
            box = UIHelper.create_info_box(content_frame, title, content, CybersecurityTheme.BG_TERTIARY)
            box.pack(fill=tk.X, pady=10)

        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

    def build_key_relationships_tab(self, notebook):
        """Build Key Relationships section"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="🔗 Key Relationships")
        
        frame.configure(style='TFrame')
        
        canvas = tk.Canvas(frame, bg=CybersecurityTheme.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=CybersecurityTheme.BG_PRIMARY)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(scrollable_frame, bg=CybersecurityTheme.BG_PRIMARY)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Direction indicators
        directions = [
            ("✅ POSSIBLE: Private Key → Public Key",
             "If you have the PRIVATE KEY, you can ALWAYS derive the PUBLIC KEY.\n"
             "Mathematical formula: PublicKey = PrivateKey.public_key()\n\n"
             "This is what the Key Generation tab does automatically!\n"
             "When you load/generate a private key, the tool derives the public key.\n"
             "This is FAST and REVERSIBLE (mathematically).",
             CybersecurityTheme.ACCENT_GREEN),
            
            ("❌ IMPOSSIBLE: Public Key → Private Key",
             "If you ONLY have the PUBLIC KEY, you CANNOT derive the PRIVATE KEY.\n"
             "There is NO mathematical formula to reverse this.\n\n"
             "Why? Because the relationship depends on factorization:\n"
             "n = p × q (where p and q are secret large primes)\n"
             "Without knowing p and q, you cannot calculate the private exponent d.\n"
             "And factoring n with p,q > 1024 bits is computationally infeasible.",
             CybersecurityTheme.ACCENT_RED),
        ]

        for title, content, color in directions:
            direction_box = tk.Frame(content_frame, bg=color, relief=tk.FLAT, bd=2)
            direction_box.pack(fill=tk.X, pady=10)
            
            title_label = tk.Label(
                direction_box,
                text=title,
                bg=color,
                fg="white",
                font=TextStyles.FONTS['title'],
                anchor=tk.W
            )
            title_label.pack(fill=tk.X, padx=15, pady=(10, 5))
            
            content_label = tk.Label(
                direction_box,
                text=content,
                bg=color,
                fg="white" if color == CybersecurityTheme.ACCENT_RED else CybersecurityTheme.BG_PRIMARY,
                font=TextStyles.FONTS['body'],
                justify=tk.LEFT,
                wraplength=600,
                anchor=tk.NW
            )
            content_label.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))

        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

    def build_key_comparison_tab(self, notebook):
        """Build Public vs Private Key comparison"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="🔐 Key Comparison")
        
        frame.configure(style='TFrame')
        
        content = tk.Frame(frame, bg=CybersecurityTheme.BG_PRIMARY)
        content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Comparison table
        headers = ["Property", "Public Key", "Private Key"]
        
        comparison_data = [
            ["Visibility", "Can be shared publicly", "Must be kept secret"],
            ["Usage in Encryption", "Used to ENCRYPT messages", "Used to DECRYPT messages"],
            ["Usage in Signatures", "Used to VERIFY signatures", "Used to CREATE signatures"],
            ["Derivation from Other", "Cannot be derived from private key", "Can be derived from private key"],
            ["Reverse Derivation", "Cannot derive private key from public", "N/A"],
            ["Compromise Risk", "Low (public knowledge)", "CRITICAL if compromised"],
            ["Key Size", "Same as private key", "Same as public key"],
            ["Format", "X.509 SubjectPublicKeyInfo (PEM)", "PKCS#8 (PEM)"],
        ]

        # Create table using frames
        table_frame = tk.Frame(content, bg=CybersecurityTheme.BG_PRIMARY)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        for i, header in enumerate(headers):
            cell = tk.Label(
                table_frame,
                text=header,
                bg=CybersecurityTheme.ACCENT_BLUE,
                fg="white",
                font=TextStyles.FONTS['title'],
                relief=tk.SOLID,
                bd=1,
                padx=15,
                pady=10
            )
            cell.grid(row=0, column=i, sticky="nsew", padx=1, pady=1)

        # Rows
        for row_idx, row_data in enumerate(comparison_data, 1):
            for col_idx, cell_data in enumerate(row_data):
                bg_color = CybersecurityTheme.BG_TERTIARY if row_idx % 2 == 0 else CybersecurityTheme.BG_SECONDARY
                fg_color = CybersecurityTheme.ACCENT_ORANGE if col_idx == 0 else CybersecurityTheme.FG_PRIMARY
                
                cell = tk.Label(
                    table_frame,
                    text=cell_data,
                    bg=bg_color,
                    fg=fg_color,
                    font=TextStyles.FONTS['small'],
                    relief=tk.SOLID,
                    bd=1,
                    padx=15,
                    pady=8,
                    justify=tk.LEFT,
                    wraplength=250,
                    anchor=tk.W
                )
                cell.grid(row=row_idx, column=col_idx, sticky="nsew", padx=1, pady=1)

        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=1)
        table_frame.grid_columnconfigure(2, weight=1)

    def build_irreversibility_tab(self, notebook):
        """Build Why Private Keys Can't Be Derived section"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="🔒 Irreversibility")
        
        frame.configure(style='TFrame')
        
        canvas = tk.Canvas(frame, bg=CybersecurityTheme.BG_PRIMARY, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg=CybersecurityTheme.BG_PRIMARY)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(scrollable_frame, bg=CybersecurityTheme.BG_PRIMARY)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        content_sections = [
            ("🚫 Why It's Impossible",
             "The security of RSA depends on the Integer Factorization Problem:\n"
             "Given n = p × q (where p and q are unknown large primes),\n"
             "finding p and q is computationally hard.\n\n"
             "To reverse a public key, you would need to:\n"
             "1. Factor n into its prime components p and q\n"
             "2. Calculate Euler's totient: φ(n) = (p-1)(q-1)\n"
             "3. Find the private exponent d using extended Euclidean algorithm\n\n"
             "Step 1 is the bottleneck - it's COMPUTATIONALLY INFEASIBLE."),
            
            ("⏱️ Computational Complexity",
             "Factoring a 2048-bit number:\n"
             "• Best known algorithm: General Number Field Sieve (GNFS)\n"
             "• Time estimate: ~2^110 operations\n"
             "• On a computer doing 10^9 operations/second: ~2^78 seconds\n"
             "• Conversion: OVER 9 TRILLION YEARS\n\n"
             "Note: By the time you finish reading this, RSA-2048 is STILL not broken!\n"
             "This is why modern security relies on RSA."),
            
            ("🔬 Factorization History",
             "RSA FACTORIZATION ACHIEVEMENTS (as of 2024):\n\n"
             "• 576-bit (174 digits): 3 months - 2003\n"
             "• 640-bit (193 digits): 2 years - 2005\n"
             "• 768-bit (232 digits): 3 years - 2009 (RSA-768)\n"
             "• 896-bit: Not yet broken\n"
             "• 1024-bit and above: Not broken with known methods\n\n"
             "The jump from 768-bit to 1024-bit shows the exponential difficulty.\n"
             "2048-bit is considered secure for at least the next 20-30 years."),
            
            ("⚠️ Real-World Implications",
             "✓ You can safely share your PUBLIC KEY\n"
             "✓ Anyone can use it to send encrypted messages only you can read\n"
             "✓ Anyone can verify your digital signatures\n"
             "✗ If someone gets your PRIVATE KEY, your security is compromised\n"
             "✗ They can decrypt all messages meant for you\n"
             "✗ They can forge your digital signatures\n"
             "✗ They can impersonate you\n\n"
             "NEVER share your private key with anyone!"),
        ]

        for title, content in content_sections:
            box = UIHelper.create_info_box(content_frame, title, content, CybersecurityTheme.BG_TERTIARY)
            box.pack(fill=tk.X, pady=10)

        canvas.pack(side="left", fill=tk.BOTH, expand=True)
        scrollbar.pack(side="right", fill="y")

    def build_practical_demo_tab(self, notebook):
        """Build Practical Demo section"""
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="💻 Practical Demo")
        
        frame.configure(style='TFrame')
        
        content_frame = tk.Frame(frame, bg=CybersecurityTheme.BG_PRIMARY)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Demo description
        demo_box = UIHelper.create_info_box(
            content_frame,
            "🧪 Interactive Demonstration",
            "This demo shows how to:\n"
            "1. Generate RSA key pair\n"
            "2. Automatically derive public key from private key\n"
            "3. Understand why reversing is impossible\n\n"
            "Click buttons below to see the concepts in action!",
            CybersecurityTheme.BG_TERTIARY
        )
        demo_box.pack(fill=tk.X, pady=(0, 20))

        # Demo buttons frame
        buttons_frame = tk.Frame(content_frame, bg=CybersecurityTheme.BG_PRIMARY)
        buttons_frame.pack(fill=tk.X, pady=10)

        ttk.Button(
            buttons_frame,
            text="📖 Go to Key Generation Tab",
            command=lambda: self.show_message(
                "KEY GENERATION DEMO",
                "1. Click 'Key Generation' tab\n"
                "2. Choose key size (2048-bit recommended)\n"
                "3. Click 'Generate New Key Pair'\n"
                "4. Both public and private keys will be generated\n"
                "5. Try loading just the private key and see the public key auto-derive!"
            )
        ).pack(fill=tk.X, pady=5)

        ttk.Button(
            buttons_frame,
            text="📊 Go to Base64 Tab",
            command=lambda: self.show_message(
                "BASE64 ENCODING DEMO",
                "1. Click 'Base64 Encode/Decode' tab\n"
                "2. Type any message in the input field\n"
                "3. Click 'ENCODE TO BASE64'\n"
                "4. Notice how the binary data is converted to text\n"
                "5. Click 'DECODE FROM BASE64' to reverse it\n\n"
                "Important: Base64 is ENCODING, not ENCRYPTION!\n"
                "Anyone can decode Base64 back to the original."
            )
        ).pack(fill=tk.X, pady=5)

        ttk.Button(
            buttons_frame,
            text="🔐 Go to Encryption Tab",
            command=lambda: self.show_message(
                "ENCRYPTION DEMO",
                "1. Click 'Encryption' tab\n"
                "2. Generate or load a key pair\n"
                "3. Enter a message to encrypt\n"
                "4. Click 'Encrypt' (uses public key)\n"
                "5. Only the private key can decrypt it!\n"
                "6. Try decrypting with the private key\n\n"
                "This demonstrates why keeping the private key secret is critical."
            )
        ).pack(fill=tk.X, pady=5)

        # Key concepts summary
        summary_box = UIHelper.create_info_box(
            content_frame,
            "🎓 Key Concepts Summary",
            "ENCODING: Converting data format (PEM ↔ Base64)\n"
            "          Not for security, just for transport/storage\n\n"
            "ENCRYPTION: Making data unreadable without the key\n"
            "            Only private key can decrypt public-key encrypted data\n\n"
            "DIGITAL SIGNATURE: Proving authenticity and integrity\n"
            "                   Only private key can sign, anyone can verify with public key\n\n"
            "RSA SECURITY: Based on factorization difficulty\n"
            "              2048-bit RSA is secure for 20+ years",
            CybersecurityTheme.BG_TERTIARY
        )
        summary_box.pack(fill=tk.X, pady=(20, 0))

    def show_message(self, title, message):
        """Show info message"""
        messagebox.showinfo(title, message)
