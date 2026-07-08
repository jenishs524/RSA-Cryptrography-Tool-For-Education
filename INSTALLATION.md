# Installation Guide - RSA Cryptography Educational Tool

## System Requirements

- **OS**: Windows, Linux, or macOS
- **Python**: 3.8 or higher
- **RAM**: Minimum 512 MB
- **Disk Space**: ~100 MB (including dependencies)
- **Display**: 1000x600 minimum resolution

## Step-by-Step Installation

### Option 1: Windows (Recommended)

#### Step 1: Install Python
1. Download Python 3.11 from https://www.python.org/downloads/
2. Run the installer
3. ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click Install

#### Step 2: Verify Python Installation
Open Command Prompt and run:
```cmd
python --version
pip --version
```

You should see version numbers (e.g., Python 3.11.0)

#### Step 3: Download the Application
- Download the RSA_Crypto_Edu_Tool folder
- Extract to a convenient location (e.g., C:\Users\YourName\Desktop\)

#### Step 4: Install Dependencies
```cmd
cd path\to\RSA_Crypto_Edu_Tool
pip install -r requirements.txt
```

#### Step 5: Run the Application
```cmd
python main.py
```

Or double-click `run_setup.py` if you want an automatic setup.

---

### Option 2: Linux (Ubuntu/Debian)

#### Step 1: Install Python and Tkinter
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk
```

#### Step 2: Verify Installation
```bash
python3 --version
pip3 --version
```

#### Step 3: Download and Navigate
```bash
cd path/to/RSA_Crypto_Edu_Tool
```

#### Step 4: Install Dependencies
```bash
pip3 install -r requirements.txt
```

Or with user flag (if you don't have sudo access):
```bash
pip3 install --user -r requirements.txt
```

#### Step 5: Run the Application
```bash
python3 main.py
```

---

### Option 3: Kali Linux

#### Step 1: Update System
```bash
sudo apt update
sudo apt upgrade
```

#### Step 2: Install Dependencies
```bash
sudo apt install python3 python3-pip python3-tk python3-dev libssl-dev
```

#### Step 3: Install Python Requirements
```bash
cd path/to/RSA_Crypto_Edu_Tool
pip3 install -r requirements.txt
```

#### Step 4: Run the Application
```bash
python3 main.py
```

---

### Option 4: macOS

#### Step 1: Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Python
```bash
brew install python3
```

#### Step 3: Install Tkinter
```bash
brew install python-tk@3.11
```

#### Step 4: Navigate and Install
```bash
cd path/to/RSA_Crypto_Edu_Tool
pip3 install -r requirements.txt
```

#### Step 5: Run the Application
```bash
python3 main.py
```

---

## Creating an Executable (.exe) for Windows

### Using PyInstaller

#### Step 1: Install PyInstaller
```cmd
pip install pyinstaller
```

#### Step 2: Create Single-File Executable
```cmd
cd path\to\RSA_Crypto_Edu_Tool
pyinstaller --onefile --windowed --name "RSA_Crypto_Tool" --add-data "modules:modules" --add-data "ui:ui" main.py
```

#### Step 3: Locate Executable
The .exe file will be in:
```
dist/RSA_Crypto_Tool.exe
```

#### Step 4: (Optional) Create Installer
For distribution, use NSIS:
1. Install NSIS from http://nsis.sourceforge.net/
2. Create a .nsi script
3. Build the installer

---

## Creating a Standalone Package

### Windows - Directory Bundle
```cmd
pyinstaller --windowed --name "RSA_Crypto_Tool" --add-data "modules:modules" --add-data "ui:ui" main.py
cd dist/RSA_Crypto_Tool
# Create shortcut to RSA_Crypto_Tool.exe
```

### Linux - AppImage
```bash
pip install appimagetool
# ... (requires more complex setup)
```

---

## Troubleshooting Installation

### Problem: "pip: command not found"
**Solution**: Reinstall Python with "Add to PATH" enabled

### Problem: "No module named 'tkinter'"
**Windows**: Tkinter is included with Python
**Linux**: 
```bash
sudo apt install python3-tk
```
**macOS**:
```bash
brew install python-tk@3.11
```

### Problem: "ModuleNotFoundError: No module named 'cryptography'"
**Solution**:
```bash
pip install --upgrade cryptography
# or
pip3 install --upgrade cryptography
```

### Problem: "Could not find Tkinter"
**Solution**: Reinstall Python and select "tcl/tk and IDLE" during installation

### Problem: Application starts but shows blank window
**Solution**: Try running in a terminal to see error messages
```bash
python main.py  # See actual error
```

### Problem: "Permission denied" on Linux
**Solution**: Make file executable
```bash
chmod +x main.py
python3 main.py
```

---

## Verifying Installation

Run this test to verify everything works:

```python
python3 << 'EOF'
from modules.crypto_engine import CryptoEngine, Base64Manager
from modules.theme import CybersecurityTheme

# Test key generation
private, public = CryptoEngine.generate_rsa_keypair(2048)
print("✓ Key generation works")

# Test Base64
encoded = Base64Manager.encode_to_base64(b"test")
print("✓ Base64 works")

# Test key derivation
derived = CryptoEngine.derive_public_from_private(private)
print("✓ Key derivation works")

print("\n✅ Installation verified!")
EOF
```

---

## Updating the Application

### To Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### To Get Latest Cryptography Library
```bash
pip install --upgrade cryptography
```

---

## Uninstalling

### Windows
1. Delete the RSA_Crypto_Edu_Tool folder
2. (Optional) Uninstall Python from Control Panel

### Linux/macOS
```bash
rm -rf path/to/RSA_Crypto_Edu_Tool
pip uninstall cryptography pycryptodome
```

---

## Docker Setup (Advanced)

Create a `Dockerfile` in the project directory:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV DISPLAY=:0
CMD ["python3", "main.py"]
```

Build and run:
```bash
docker build -t rsa-crypto-tool .
docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix rsa-crypto-tool
```

---

## CI/CD and Automated Testing

### GitHub Actions Example
Create `.github/workflows/test.yml`:

```yaml
name: Test RSA Crypto Tool

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10', '3.11']
    
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m py_compile main.py modules/*.py ui/*.py
```

---

## Performance Optimization

### For Older Computers
1. Use 2048-bit keys instead of 4096-bit
2. Close other applications
3. Allocate more system RAM
4. Use SSD instead of HDD

### For Better Performance
1. Use 4096-bit keys for stronger security
2. Upgrade Python to latest version
3. Install cryptography with pre-built wheels
4. Use PyPy for faster execution (advanced)

---

## Support and Help

- **README.md**: Full documentation
- **QUICKSTART.md**: Fast setup guide
- **In-app Help**: ⚙️ Help button in application
- **Educational Demo Tab**: Comprehensive tutorials

---

## Security Notes

⚠️ **Important**:
- This is an EDUCATIONAL tool, not production security software
- For real cryptographic security, use established frameworks
- Never use these keys for actual sensitive data
- Always keep backups of important keys in secure locations

---

## License and Attribution

This tool is for educational purposes only.
See LICENSE file for terms and conditions.

---

**Installation complete! You're ready to learn RSA cryptography! 🔐**
