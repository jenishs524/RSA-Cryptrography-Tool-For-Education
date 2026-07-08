# 🔐 RSA Cryptography Educational Tool

A professional Python + Tkinter desktop application for learning RSA cryptography, Base64 encoding, encryption, and digital signatures.

## Features

### ✅ Core Features
- **RSA Key Generation**: Generate secure 2048-bit, 3072-bit, or 4096-bit RSA key pairs
- **Automatic Key Derivation**: When you load a private key, the public key is automatically derived
- **Base64 Encoding/Decoding**: Convert between binary and Base64 text format
- **RSA Encryption/Decryption**: Encrypt messages with public key, decrypt with private key
- **Digital Signatures**: Create and verify digital signatures using RSA
- **Key Management**: Import, export, and save keys in PEM format

### 📚 Educational Features
- **Comprehensive tutorials** explaining RSA concepts
- **Why private keys can't be reversed**: Detailed mathematical explanation
- **Factorization complexity**: Historical data on RSA breaking attempts
- **Encoding vs Encryption**: Clear distinction explained
- **Key relationship diagram**: Visual representation of cryptographic principles

### 🎨 Professional GUI
- Dark cybersecurity theme
- Intuitive tabbed interface
- Real-time status updates
- Comprehensive error handling
- Copy-to-clipboard functionality

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download
```bash
# If you have git
git clone <repository-url>
cd RSA_Crypto_Edu_Tool

# Or extract the ZIP file and navigate to the directory
cd RSA_Crypto_Edu_Tool
```

### Step 2: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Or manually install
pip install cryptography>=41.0.0
pip install pycryptodome>=3.19.0
```

### Step 3: Run the Application
```bash
python main.py
```

## Usage Guide

### 1. Key Generation Tab 🔑
1. Select key size (2048-bit recommended for security)
2. Click "Generate New Key Pair"
3. Both private and public keys are displayed in PEM format
4. Click "Show Base64" to see the Base64 encoded version
5. Save keys to files for later use

**Auto-Derivation**: When you load just a private key, the public key is automatically derived!

### 2. Base64 Encode/Decode Tab 📊
1. Enter text in the input field
2. Click "ENCODE TO BASE64" to convert to Base64
3. Click "DECODE FROM BASE64" to convert back
4. Use "Convert Key PEM to Base64" for key conversion

**Remember**: Base64 is ENCODING, not ENCRYPTION! Anyone can decode it.

### 3. Educational Demo Tab 📚
- **RSA Concepts**: Learn how RSA works mathematically
- **Key Relationships**: Understand Private → Public is possible, but Public → Private is impossible
- **Key Comparison**: Table comparing public vs private keys
- **Irreversibility**: Deep dive into why private keys can't be derived from public keys
- **Practical Demo**: Links to interactive demonstrations

### 4. Encryption Tab 🔒
1. Load your RSA key pair (or generate new one)
2. Enter a plaintext message
3. Click "ENCRYPT MESSAGE" (uses public key)
4. The ciphertext is displayed in Base64 format
5. Click "DECRYPT MESSAGE" (uses private key) to recover original message
6. Create and verify digital signatures

**Note**: Only the holder of the private key can decrypt messages encrypted with the public key!

## Key Principles (Important!)

### Private Key → Public Key: ✅ POSSIBLE
- Mathematically straightforward
- This tool does this automatically when you load a private key
- Based on extracting the public components

### Public Key → Private Key: ❌ IMPOSSIBLE
- No known algorithm exists in polynomial time
- Would require factoring a 2048-bit number
- **Estimated time with today's computers**: ~trillion years
- This is the foundation of RSA security

## Mathematical Background

### RSA Security Basis: Integer Factorization Problem
```
Given: n = p × q (where p and q are 1024-bit primes each)
Find: p and q
Problem: Computationally infeasible with known algorithms
```

### Key Sizes and Security
- **512-bit**: BROKEN (1999)
- **768-bit**: BROKEN (2009, took 3 years)
- **1024-bit**: WEAK (not recommended)
- **2048-bit**: SECURE (current standard)
- **4096-bit**: VERY SECURE (future-proof)

## Building an Executable (.exe)

### Using PyInstaller

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Create executable:
```bash
# For a single-file executable
pyinstaller --onefile --windowed --name "RSA_Crypto_Tool" main.py

# For a directory bundle (faster)
pyinstaller --windowed --name "RSA_Crypto_Tool" main.py
```

3. Executable location:
- Single file: `dist/RSA_Crypto_Tool.exe`
- Directory: `dist/RSA_Crypto_Tool/RSA_Crypto_Tool.exe`

### Running on Kali Linux

```bash
# Install Python and dependencies
sudo apt update
sudo apt install python3 python3-pip python3-tk

# Install cryptography libraries
pip3 install -r requirements.txt

# Run the application
python3 main.py
```

## File Structure

```
RSA_Crypto_Edu_Tool/
├── main.py                      # Main application entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This file
│
├── modules/                     # Core cryptography modules
│   ├── __init__.py
│   ├── crypto_engine.py         # RSA operations and Base64 handling
│   └── theme.py                 # GUI theme and styling
│
└── ui/                          # User interface components
    ├── __init__.py
    ├── key_generation_tab.py    # Key generation interface
    ├── base64_tab.py            # Base64 encoding/decoding interface
    ├── educational_demo_tab.py  # Educational content
    └── encryption_tab.py        # Encryption/decryption interface
```

## Code Quality

- ✅ Well-commented for learning purposes
- ✅ Modular and object-oriented design
- ✅ Comprehensive error handling
- ✅ Proper logging
- ✅ PEP 8 compliant
- ✅ No hardcoded values
- ✅ Real cryptographic principles (NO faking private key derivation!)

## Important Notes

### ⚠️ This is an Educational Tool
- **DO NOT USE FOR PRODUCTION SECURITY**
- This tool is designed for learning cryptographic concepts
- For real applications, use established security libraries and frameworks
- Consult security professionals for production implementations

### 🔒 Security Best Practices
- **Never share your private key** with anyone
- **Always back up your keys** in a secure location
- **Use 2048-bit minimum** for any security-critical application
- **Verify signatures** from trusted sources before trusting the data
- **Keep the tool updated** with the latest cryptography library versions

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'cryptography'"
**Solution**: 
```bash
pip install --upgrade cryptography
```

### Issue: "Tkinter not found" on Linux
**Solution**:
```bash
sudo apt install python3-tk
```

### Issue: Application won't start
**Solution**: Make sure you're in the correct directory and run:
```bash
python main.py  # on Windows
python3 main.py # on Linux/Mac
```

## Educational Content

The application includes detailed explanations of:
- **How RSA works**: Mathematical foundation and practical implementation
- **Key generation**: Step-by-step process of creating RSA keys
- **Asymmetric cryptography**: Why two different keys are needed
- **Public key infrastructure**: How to distribute and verify keys
- **Digital signatures**: Creating and verifying authenticity
- **Base64 encoding**: Why data needs to be converted to text format
- **Factorization complexity**: Why 2048-bit RSA is secure

## Contributing

Feel free to contribute improvements, bug fixes, or educational content!

## License

Educational Use Only - See LICENSE file for details

## References

- **RFC 3447**: PKCS #1 RSA Cryptography Specifications
- **NIST SP 800-131A**: Transitions: Recommendations for Transitioning the Use of Cryptographic Algorithms
- **OWASP**: Cryptographic Failure Prevention
- https://en.wikipedia.org/wiki/RSA_(cryptosystem)
- https://en.wikipedia.org/wiki/Integer_factorization

## Contact & Support

For issues, questions, or suggestions:
- Review the Educational Demo tab in the application
- Check the Help menu (⚙️ Help button)
- Consult the inline code comments

---

**Remember**: Security is only as strong as your keys. Keep your private keys secure! 🔐
