# 🚀 SETUP & RUN INSTRUCTIONS

Quick and easy setup instructions for all platforms.

## 📋 File Checklist

Verify these files are present:
```
✅ main.py
✅ run_setup.py
✅ requirements.txt
✅ README.md
✅ QUICKSTART.md
✅ INSTALLATION.md
✅ USER_GUIDE.md
✅ PROJECT_SUMMARY.md
✅ modules/crypto_engine.py
✅ modules/theme.py
✅ ui/key_generation_tab.py
✅ ui/base64_tab.py
✅ ui/educational_demo_tab.py
✅ ui/encryption_tab.py
```

All 16 files present? ✅ You're ready!

---

## 🪟 WINDOWS SETUP

### Method 1: Simple (Recommended)

1. **Download Python**
   - Go to https://www.python.org/downloads/
   - Download Python 3.11 (latest)
   - Run installer
   - ⚠️ CHECK "Add Python to PATH"
   - Click Install

2. **Open Command Prompt**
   - Press `Win + R`
   - Type `cmd`
   - Press Enter

3. **Navigate to folder**
   ```cmd
   cd C:\path\to\RSA_Crypto_Edu_Tool
   ```

4. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

5. **Run application**
   ```cmd
   python main.py
   ```

### Method 2: Automatic (Extra Easy)

1. Download Python and add to PATH
2. Double-click `run_setup.py`
3. Wait for dependencies to install
4. Application launches automatically!

### Troubleshooting Windows

**"Python not found"**:
- Reinstall Python with "Add to PATH" checked

**"pip not found"**:
- Use `python -m pip` instead of `pip`

**Permission denied**:
- Run Command Prompt as Administrator

---

## 🐧 LINUX SETUP

### Ubuntu / Debian

1. **Update system**
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. **Install Python and Tkinter**
   ```bash
   sudo apt install python3 python3-pip python3-tk
   ```

3. **Navigate to folder**
   ```bash
   cd path/to/RSA_Crypto_Edu_Tool
   ```

4. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

5. **Run application**
   ```bash
   python3 main.py
   ```

### Fedora / RHEL / CentOS

1. **Install dependencies**
   ```bash
   sudo dnf install python3 python3-pip python3-tkinter
   ```

2. **Navigate and run**
   ```bash
   cd path/to/RSA_Crypto_Edu_Tool
   pip3 install -r requirements.txt
   python3 main.py
   ```

### Arch Linux

1. **Install packages**
   ```bash
   sudo pacman -S python python-pip tk
   ```

2. **Navigate and run**
   ```bash
   cd path/to/RSA_Crypto_Edu_Tool
   pip install -r requirements.txt
   python main.py
   ```

### Linux Troubleshooting

**"tkinter not found"**:
```bash
# Ubuntu/Debian:
sudo apt install python3-tk

# Fedora:
sudo dnf install python3-tkinter

# Arch:
sudo pacman -S tk
```

**"permission denied"**:
```bash
chmod +x main.py
python3 main.py
```

---

## 🔒 KALI LINUX SETUP

### Complete Setup

```bash
# 1. Update Kali
sudo apt update
sudo apt upgrade -y

# 2. Install dependencies
sudo apt install -y python3 python3-pip python3-tk python3-dev libssl-dev

# 3. Navigate to application
cd path/to/RSA_Crypto_Edu_Tool

# 4. Install Python requirements
pip3 install -r requirements.txt

# 5. Run the application
python3 main.py
```

### Quick Copy-Paste Version

```bash
sudo apt update && sudo apt install -y python3 python3-pip python3-tk && cd RSA_Crypto_Edu_Tool && pip3 install -r requirements.txt && python3 main.py
```

### Using in Kali Labs

```bash
# If running in Kali inside VirtualBox
# Make sure to enable 3D acceleration or try:
export GDK_SCALE=2
python3 main.py
```

---

## 🍎 MACOS SETUP

### Using Homebrew (Recommended)

1. **Install Homebrew** (if not installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python**
   ```bash
   brew install python3
   ```

3. **Python 3 comes with Tkinter**
   - No separate install needed for Tkinter

4. **Navigate to folder**
   ```bash
   cd path/to/RSA_Crypto_Edu_Tool
   ```

5. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Run application**
   ```bash
   python3 main.py
   ```

### Manual Setup (No Homebrew)

1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. Tkinter is included with Python on macOS
4. Follow same steps as above

### macOS Troubleshooting

**"command not found: python3"**:
```bash
# Add to ~/.zshrc or ~/.bash_profile
export PATH="/usr/local/opt/python3/bin:$PATH"
```

**Tkinter issues**:
```bash
# Reinstall Python with Tkinter
brew reinstall python3
```

---

## 🐳 DOCKER SETUP (Advanced)

### 1. Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install Tkinter
RUN apt-get update && apt-get install -y python3-tk libcairo2-dev

# Copy application
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Set display for GUI
ENV DISPLAY=:0

CMD ["python3", "main.py"]
```

### 2. Build and Run

```bash
# Build image
docker build -t rsa-crypto-tool .

# Run container (with X11 forwarding for GUI)
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY rsa-crypto-tool
```

---

## 🏗️ CREATING EXECUTABLE

### Windows .exe

1. **Install PyInstaller**
   ```cmd
   pip install pyinstaller
   ```

2. **Create single-file executable**
   ```cmd
   pyinstaller --onefile --windowed --name "RSA_Crypto_Tool" --add-data "modules:modules" --add-data "ui:ui" main.py
   ```

3. **Find executable**
   ```
   dist/RSA_Crypto_Tool.exe
   ```

4. **Double-click to run!**

### Linux Binary

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "RSA_Crypto_Tool" --add-data "modules:modules" --add-data "ui:ui" main.py
./dist/RSA_Crypto_Tool
```

---

## 🧪 VERIFY INSTALLATION

Run this to check everything works:

```bash
python3 << 'EOF'
print("Testing RSA Crypto Tool...")

from modules.crypto_engine import CryptoEngine, Base64Manager
print("✓ Imports successful")

private_key, public_key = CryptoEngine.generate_rsa_keypair(2048)
print("✓ Key generation works")

encoded = Base64Manager.encode_to_base64(b"test")
decoded = Base64Manager.decode_from_base64(encoded)
print("✓ Base64 operations work")

print("\n✅ Installation verified - Ready to launch!")
EOF
```

---

## 🚀 QUICK START COMMANDS

### Copy-Paste for Your Platform

**Windows (Command Prompt)**:
```cmd
cd C:\path\to\RSA_Crypto_Edu_Tool
pip install -r requirements.txt
python main.py
```

**Linux/Mac**:
```bash
cd path/to/RSA_Crypto_Edu_Tool
pip3 install -r requirements.txt
python3 main.py
```

**Kali Linux**:
```bash
sudo apt install python3-tk
cd path/to/RSA_Crypto_Edu_Tool
pip3 install -r requirements.txt
python3 main.py
```

---

## 💡 AFTER INSTALLATION

1. **First Launch**
   - Application opens with dark theme
   - You see 4 tabs at the bottom

2. **Next Steps**
   - Read QUICKSTART.md (2-min read)
   - Go to Key Generation tab
   - Generate a test key pair
   - Explore each tab

3. **Learning Path**
   - Spend 10 mins on each tab
   - Read Educational Demo thoroughly
   - Try encryption examples
   - Complete exercises in USER_GUIDE.md

---

## 🆘 COMMON ISSUES

| Problem | Solution |
|---------|----------|
| "Python not found" | Install Python from python.org |
| "pip not found" | Use `python -m pip` |
| "tkinter not found" | Install python3-tk package |
| "ModuleNotFoundError" | Run `pip install -r requirements.txt` |
| "Permission denied" | Run as Administrator (Windows) or with `sudo` (Linux) |
| Application freezes | Wait 2-3 seconds (key generation takes time) |

---

## 📞 GETTING HELP

1. **Read QUICKSTART.md** - Fast answers
2. **Check USER_GUIDE.md** - Detailed help
3. **Review README.md** - Full documentation
4. **Click Help ⚙️** - In-app guidance
5. **Visit code comments** - Implementation details

---

## ✅ YOU'RE READY!

After following these steps, you'll have:
- ✅ Python installed
- ✅ Dependencies installed
- ✅ Application ready to launch
- ✅ All documentation available
- ✅ Educational content accessible

**Enjoy learning RSA cryptography! 🔐**

---

## 📝 NOTES

- Application requires internet connection only for dependency installation
- All cryptographic operations are local (nothing shared online)
- Keys are only stored where YOU choose to save them
- This is educational software, not for production use

---

**Questions? Check the documentation files included in the project!**
