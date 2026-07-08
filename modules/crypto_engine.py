"""
RSA Cryptography Engine with Base64 Encoding
Educational tool for understanding RSA key relationships and Base64 encoding
"""

import base64
import logging
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend


class CryptoEngine:
    """Main cryptography engine for RSA operations and Base64 encoding"""

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Key size constants
    KEY_SIZE_2048 = 2048
    KEY_SIZE_4096 = 4096

    @staticmethod
    def generate_rsa_keypair(key_size=2048):
        """
        Generate RSA key pair (public and private keys)
        
        Args:
            key_size: RSA key size in bits (2048 or 4096 recommended)
            
        Returns:
            tuple: (private_key_pem, public_key_pem) as bytes
        """
        try:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=key_size,
                backend=default_backend()
            )
            public_key = private_key.public_key()

            # Serialize to PEM format
            private_pem = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )

            public_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            CryptoEngine.logger.info(f"Generated RSA keypair with {key_size}-bit key")
            return private_pem, public_pem
        except Exception as e:
            CryptoEngine.logger.error(f"Error generating RSA keypair: {str(e)}")
            raise

    @staticmethod
    def derive_public_from_private(private_key_pem):
        """
        Derive public key from private key (ONLY possible for private keys)
        This demonstrates that: Private Key → Public Key (possible)
        
        Args:
            private_key_pem: Private key in PEM format (bytes or str)
            
        Returns:
            bytes: Public key in PEM format
        """
        try:
            if isinstance(private_key_pem, str):
                private_key_pem = private_key_pem.encode()

            private_key = serialization.load_pem_private_key(
                private_key_pem,
                password=None,
                backend=default_backend()
            )
            public_key = private_key.public_key()

            public_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            CryptoEngine.logger.info("Successfully derived public key from private key")
            return public_pem
        except Exception as e:
            CryptoEngine.logger.error(f"Error deriving public key: {str(e)}")
            raise ValueError("Invalid private key format")

    @staticmethod
    def validate_private_key(private_key_pem):
        """
        Validate if provided key is a valid private key
        
        Args:
            private_key_pem: Private key in PEM format (bytes or str)
            
        Returns:
            bool: True if valid private key, False otherwise
        """
        try:
            if isinstance(private_key_pem, str):
                private_key_pem = private_key_pem.encode()

            serialization.load_pem_private_key(
                private_key_pem,
                password=None,
                backend=default_backend()
            )
            return True
        except Exception:
            return False

    @staticmethod
    def validate_public_key(public_key_pem):
        """
        Validate if provided key is a valid public key
        
        Args:
            public_key_pem: Public key in PEM format (bytes or str)
            
        Returns:
            bool: True if valid public key, False otherwise
        """
        try:
            if isinstance(public_key_pem, str):
                public_key_pem = public_key_pem.encode()

            serialization.load_pem_public_key(
                public_key_pem,
                backend=default_backend()
            )
            return True
        except Exception:
            return False

    @staticmethod
    def get_key_info(key_pem):
        """
        Extract information about a key
        
        Args:
            key_pem: Key in PEM format (bytes or str)
            
        Returns:
            dict: Key information (size, type, etc.)
        """
        try:
            if isinstance(key_pem, str):
                key_pem = key_pem.encode()

            # Try to load as private key first
            try:
                private_key = serialization.load_pem_private_key(
                    key_pem,
                    password=None,
                    backend=default_backend()
                )
                return {
                    'type': 'Private Key',
                    'key_size': private_key.key_size,
                    'format': 'RSA',
                    'valid': True
                }
            except Exception:
                pass

            # Try to load as public key
            try:
                public_key = serialization.load_pem_public_key(
                    key_pem,
                    backend=default_backend()
                )
                return {
                    'type': 'Public Key',
                    'key_size': public_key.key_size,
                    'format': 'RSA',
                    'valid': True
                }
            except Exception:
                pass

            return {'type': 'Unknown', 'valid': False}
        except Exception as e:
            CryptoEngine.logger.error(f"Error getting key info: {str(e)}")
            return {'type': 'Error', 'valid': False}


class Base64Manager:
    """Manages Base64 encoding and decoding operations"""

    logger = logging.getLogger(__name__)

    @staticmethod
    def encode_to_base64(data):
        """
        Encode data to Base64
        
        Args:
            data: Input data (bytes or str)
            
        Returns:
            str: Base64 encoded string
        """
        try:
            if isinstance(data, str):
                data = data.encode('utf-8')

            encoded = base64.b64encode(data).decode('utf-8')
            Base64Manager.logger.info("Successfully encoded data to Base64")
            return encoded
        except Exception as e:
            Base64Manager.logger.error(f"Error encoding to Base64: {str(e)}")
            raise

    @staticmethod
    def decode_from_base64(data):
        """
        Decode data from Base64
        
        Args:
            data: Base64 encoded data (bytes or str)
            
        Returns:
            bytes: Decoded data
        """
        try:
            if isinstance(data, str):
                data = data.encode('utf-8')

            # Remove any whitespace
            data = b''.join(data.split())

            decoded = base64.b64decode(data)
            Base64Manager.logger.info("Successfully decoded Base64 data")
            return decoded
        except Exception as e:
            Base64Manager.logger.error(f"Error decoding Base64: {str(e)}")
            raise ValueError("Invalid Base64 format")

    @staticmethod
    def encode_key_to_base64(key_pem):
        """
        Encode a PEM key to Base64
        
        Args:
            key_pem: Key in PEM format (bytes or str)
            
        Returns:
            str: Base64 encoded key
        """
        try:
            return Base64Manager.encode_to_base64(key_pem)
        except Exception as e:
            Base64Manager.logger.error(f"Error encoding key: {str(e)}")
            raise

    @staticmethod
    def decode_base64_to_key(base64_key):
        """
        Decode a Base64 key back to PEM format
        
        Args:
            base64_key: Base64 encoded key (bytes or str)
            
        Returns:
            str: Key in PEM format
        """
        try:
            decoded = Base64Manager.decode_from_base64(base64_key)
            pem_key = decoded.decode('utf-8')
            return pem_key
        except Exception as e:
            Base64Manager.logger.error(f"Error decoding Base64 key: {str(e)}")
            raise ValueError("Invalid Base64 key format")


class RSAEncryption:
    """RSA encryption and decryption operations"""

    logger = logging.getLogger(__name__)

    @staticmethod
    def encrypt_message(plaintext, public_key_pem):
        """
        Encrypt message using RSA public key
        
        Args:
            plaintext: Message to encrypt (str or bytes)
            public_key_pem: Public key in PEM format (bytes or str)
            
        Returns:
            bytes: Encrypted message
        """
        try:
            if isinstance(plaintext, str):
                plaintext = plaintext.encode('utf-8')
            if isinstance(public_key_pem, str):
                public_key_pem = public_key_pem.encode()

            public_key = serialization.load_pem_public_key(
                public_key_pem,
                backend=default_backend()
            )

            ciphertext = public_key.encrypt(
                plaintext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            RSAEncryption.logger.info("Successfully encrypted message")
            return ciphertext
        except Exception as e:
            RSAEncryption.logger.error(f"Encryption error: {str(e)}")
            raise ValueError(f"Encryption failed: {str(e)}")

    @staticmethod
    def decrypt_message(ciphertext, private_key_pem):
        """
        Decrypt message using RSA private key
        
        Args:
            ciphertext: Encrypted message (bytes)
            private_key_pem: Private key in PEM format (bytes or str)
            
        Returns:
            str: Decrypted message
        """
        try:
            if isinstance(private_key_pem, str):
                private_key_pem = private_key_pem.encode()

            private_key = serialization.load_pem_private_key(
                private_key_pem,
                password=None,
                backend=default_backend()
            )

            plaintext = private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            RSAEncryption.logger.info("Successfully decrypted message")
            return plaintext.decode('utf-8')
        except Exception as e:
            RSAEncryption.logger.error(f"Decryption error: {str(e)}")
            raise ValueError(f"Decryption failed: {str(e)}")

    @staticmethod
    def sign_message(message, private_key_pem):
        """
        Create digital signature for a message
        
        Args:
            message: Message to sign (str or bytes)
            private_key_pem: Private key in PEM format (bytes or str)
            
        Returns:
            bytes: Digital signature
        """
        try:
            if isinstance(message, str):
                message = message.encode('utf-8')
            if isinstance(private_key_pem, str):
                private_key_pem = private_key_pem.encode()

            private_key = serialization.load_pem_private_key(
                private_key_pem,
                password=None,
                backend=default_backend()
            )

            signature = private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            RSAEncryption.logger.info("Successfully created digital signature")
            return signature
        except Exception as e:
            RSAEncryption.logger.error(f"Signing error: {str(e)}")
            raise ValueError(f"Signing failed: {str(e)}")

    @staticmethod
    def verify_signature(message, signature, public_key_pem):
        """
        Verify digital signature using public key
        
        Args:
            message: Original message (str or bytes)
            signature: Digital signature (bytes)
            public_key_pem: Public key in PEM format (bytes or str)
            
        Returns:
            bool: True if signature is valid, False otherwise
        """
        try:
            if isinstance(message, str):
                message = message.encode('utf-8')
            if isinstance(public_key_pem, str):
                public_key_pem = public_key_pem.encode()

            public_key = serialization.load_pem_public_key(
                public_key_pem,
                backend=default_backend()
            )

            public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            RSAEncryption.logger.info("Signature verification successful")
            return True
        except Exception as e:
            RSAEncryption.logger.error(f"Signature verification failed: {str(e)}")
            return False
