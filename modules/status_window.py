import tkinter as tk
from tkinter import ttk

class StatusWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = None
        self.operand_a_binary_var = tk.StringVar()
        self.operand_a_decimal_var = tk.StringVar()
        self.operand_b_binary_var = tk.StringVar()
        self.operand_b_decimal_var = tk.StringVar()
        self.result_binary_var = tk.StringVar()
        self.result_decimal_var = tk.StringVar()
        
    def show_window(self):
        """Show the status window"""
        if self.window is None or not self.window.winfo_exists():
            self.create_window()
        else:
            self.window.lift()
            self.window.focus()
            
    def create_window(self):
        """Create the status window"""
        self.window = tk.Toplevel(self.parent)
        self.window.title("States")
        self.window.geometry("450x130")
        self.window.resizable(False, False)
        
        # Make window stay on top
        self.window.attributes('-topmost', True)
        
        # Create main frame with centering
        main_frame = ttk.Frame(self.window, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for centering
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        
        # Headers (centered)
        ttk.Label(main_frame, text="", width=12).grid(row=0, column=0)
        ttk.Label(main_frame, text="Binary", font=('Arial', 11, 'bold')).grid(row=0, column=1, padx=10)
        ttk.Label(main_frame, text="Decimal", font=('Arial', 11, 'bold')).grid(row=0, column=2, padx=10)
        
        # Operand A
        ttk.Label(main_frame, text="Operand A:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=3)
        ttk.Label(main_frame, textvariable=self.operand_a_binary_var, font=('Courier', 10)).grid(row=1, column=1, padx=10, pady=3)
        ttk.Label(main_frame, textvariable=self.operand_a_decimal_var, font=('Arial', 10)).grid(row=1, column=2, padx=10, pady=3)
        
        # Operand B
        ttk.Label(main_frame, text="Operand B:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=3)
        ttk.Label(main_frame, textvariable=self.operand_b_binary_var, font=('Courier', 10)).grid(row=2, column=1, padx=10, pady=3)
        ttk.Label(main_frame, textvariable=self.operand_b_decimal_var, font=('Arial', 10)).grid(row=2, column=2, padx=10, pady=3)
        
        # Result
        ttk.Label(main_frame, text="Result, O/P:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky=tk.W, pady=3)
        ttk.Label(main_frame, textvariable=self.result_binary_var, font=('Courier', 10)).grid(row=3, column=1, padx=10, pady=3)
        ttk.Label(main_frame, textvariable=self.result_decimal_var, font=('Arial', 10)).grid(row=3, column=2, padx=10, pady=3)
        
        # Initial data load
        self.refresh_data()
        
        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def refresh_data(self):
        """Refresh the displayed data"""
        try:
            from button_functions import get_calculator_state
            operand_a, operand_b, result = get_calculator_state()
            
            # Update operand A
            self.operand_a_binary_var.set(f"{format(operand_a, '08b')}")
            self.operand_a_decimal_var.set(f"{operand_a}")
            
            # Update operand B
            self.operand_b_binary_var.set(f"{format(operand_b, '08b')}")
            self.operand_b_decimal_var.set(f"{operand_b}")
            
            # Update result
            self.result_binary_var.set(f"{format(result, '016b')}")
            self.result_decimal_var.set(f"{result}")
            
        except Exception as e:
            print(f"Error refreshing status data: {e}")
            
    def on_close(self):
        """Handle window close"""
        self.window.destroy()
        self.window = None