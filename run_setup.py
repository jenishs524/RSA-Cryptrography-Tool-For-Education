#!/usr/bin/env python3
"""
Quick Start Script for RSA Crypto Educational Tool
Run this to set up and launch the application
"""

import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("🔐 RSA CRYPTOGRAPHY EDUCATIONAL TOOL - SETUP")
    print("=" * 60)
    print()

    # Check Python version
    print("✓ Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    print()

    # Check if requirements are installed
    print("✓ Checking dependencies...")
    try:
        import cryptography
        print(f"✓ cryptography {cryptography.__version__} installed")
    except ImportError:
        print("⚠ cryptography not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])

    try:
        import Crypto
        print(f"✓ pycryptodome installed")
    except ImportError:
        print("⚠ pycryptodome not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pycryptodome"])

    print()
    print("✓ All dependencies are installed!")
    print()

    # Launch application
    print("=" * 60)
    print("🚀 Launching RSA Cryptography Educational Tool...")
    print("=" * 60)
    print()

    try:
        import main
        main.main()
    except Exception as e:
        print(f"❌ Error launching application: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
