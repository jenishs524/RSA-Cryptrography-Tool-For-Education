"""
GUI Theme and Utilities
Modern dark cybersecurity theme for Tkinter
"""

import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk


class CybersecurityTheme:
    """Modern dark cybersecurity theme colors and styling"""

    # Color palette
    BG_PRIMARY = "#0d1117"  # Dark background
    BG_SECONDARY = "#161b22"  # Slightly lighter background
    BG_TERTIARY = "#21262d"  # Panel background
    
    FG_PRIMARY = "#c9d1d9"  # Main text
    FG_SECONDARY = "#8b949e"  # Secondary text
    FG_MUTED = "#6e7681"  # Muted text
    
    ACCENT_GREEN = "#238636"  # Success/positive action
    ACCENT_BLUE = "#0969da"  # Primary action
    ACCENT_ORANGE = "#fb8500"  # Warning
    ACCENT_RED = "#da3633"  # Error/danger
    ACCENT_PURPLE = "#8957e5"  # Information
    
    BORDER_COLOR = "#30363d"
    
    @staticmethod
    def configure_tkinter_theme(root):
        """Apply theme to root window"""
        root.configure(bg=CybersecurityTheme.BG_PRIMARY)
        # Define custom styles using ttk.Style (accepts kwargs)
        style = ttk.Style()
        style.theme_use('clam')

        style.configure('TFrame', background=CybersecurityTheme.BG_PRIMARY)
        style.configure('TLabel', background=CybersecurityTheme.BG_PRIMARY,
                        foreground=CybersecurityTheme.FG_PRIMARY)
        style.configure('TLabelframe', background=CybersecurityTheme.BG_PRIMARY,
                        foreground=CybersecurityTheme.FG_PRIMARY)
        style.configure('TLabelframe.Label', background=CybersecurityTheme.BG_PRIMARY,
                        foreground=CybersecurityTheme.ACCENT_BLUE)
        style.configure('TButton', background=CybersecurityTheme.BG_TERTIARY,
                        foreground=CybersecurityTheme.FG_PRIMARY)
        style.map('TButton', background=[('active', CybersecurityTheme.ACCENT_BLUE)])
        style.configure('Accent.TButton', background=CybersecurityTheme.ACCENT_BLUE,
                        foreground='white')
        style.map('Accent.TButton', background=[('active', CybersecurityTheme.ACCENT_GREEN)])
        style.configure('TEntry', background=CybersecurityTheme.BG_TERTIARY,
                        foreground=CybersecurityTheme.FG_PRIMARY,
                        fieldbackground=CybersecurityTheme.BG_TERTIARY)
        style.configure('TNotebook', background=CybersecurityTheme.BG_PRIMARY)
        style.configure('TNotebook.Tab', background=CybersecurityTheme.BG_SECONDARY,
                        foreground=CybersecurityTheme.FG_PRIMARY)
        style.map('TNotebook.Tab', background=[('selected', CybersecurityTheme.ACCENT_BLUE)])


class TextStyles:
    """Text formatting styles"""

    FONTS = {
        'header': ('Courier New', 14, 'bold'),
        'title': ('Courier New', 12, 'bold'),
        'body': ('Courier New', 10),
        'mono': ('Courier New', 9),
        'small': ('Courier New', 8),
    }


class UIHelper:
    """Helper functions for UI construction"""

    @staticmethod
    def create_section_frame(parent, bg_color):
        """Create a styled section frame"""
        frame = tk.Frame(parent, bg=bg_color, relief=tk.FLAT, bd=1)
        return frame

    @staticmethod
    def create_code_text(parent, height=10, width=60):
        """Create a styled text widget for displaying code/keys"""
        from tkinter import scrolledtext
        text = scrolledtext.ScrolledText(
            parent,
            height=height,
            width=width,
            bg=CybersecurityTheme.BG_TERTIARY,
            fg=CybersecurityTheme.ACCENT_GREEN,
            font=TextStyles.FONTS['mono'],
            relief=tk.SOLID,
            bd=1,
            wrap=tk.WORD
        )
        return text

    @staticmethod
    def create_info_label(parent, text, fg_color=None, bg_color=None):
        """Create an info label"""
        if fg_color is None:
            fg_color = CybersecurityTheme.FG_SECONDARY
        if bg_color is None:
            bg_color = CybersecurityTheme.BG_PRIMARY

        label = tk.Label(
            parent,
            text=text,
            fg=fg_color,
            bg=bg_color,
            font=TextStyles.FONTS['small'],
            wraplength=300,
            justify=tk.LEFT
        )
        return label

    @staticmethod
    def create_info_box(parent, title, content, bg_color=None):
        """Create an information box"""
        if bg_color is None:
            bg_color = CybersecurityTheme.BG_TERTIARY

        box = tk.Frame(parent, bg=bg_color, relief=tk.FLAT, bd=1)
        
        title_label = tk.Label(
            box,
            text=title,
            bg=bg_color,
            fg=CybersecurityTheme.ACCENT_BLUE,
            font=TextStyles.FONTS['body'],
            anchor=tk.W
        )
        title_label.pack(fill=tk.X, padx=10, pady=(10, 5))
        
        content_label = tk.Label(
            box,
            text=content,
            bg=bg_color,
            fg=CybersecurityTheme.FG_SECONDARY,
            font=TextStyles.FONTS['small'],
            justify=tk.LEFT,
            wraplength=400,
            anchor=tk.NW
        )
        content_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        return box
