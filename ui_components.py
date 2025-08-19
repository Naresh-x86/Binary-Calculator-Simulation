import tkinter as tk

class ToolTip:
    """Tooltip class for showing hover information on widgets"""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show)
        self.widget.bind("<Leave>", self.hide)

    def show(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 20
        y += self.widget.winfo_rooty() + 20
        
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(self.tooltip, text=self.text, background="yellow", 
                        relief="solid", borderwidth=1, font=("Arial", 8))
        label.pack()

    def hide(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

def create_button(root, text, command, width_chars, height_chars, tooltip_text):
    """Create a standardized button with tooltip"""
    button = tk.Button(
        root, 
        text=text, 
        width=width_chars, 
        height=height_chars, 
        relief='flat', 
        command=command, 
        font=('Arial', 6), 
        bg='#735348', 
        fg='#735348', 
        activebackground='#735348', 
        activeforeground='#735348'
    )
    ToolTip(button, tooltip_text)
    return button
