# LED Matrix management for binary calculator
import tkinter as tk
from PIL import Image, ImageTk
from config import *

class LEDMatrix:
    def __init__(self, canvas):
        self.canvas = canvas
        self.glow_image = None
        self.glow_photo = None
        self.led_items = []  # Store all LED canvas items
        self.load_glow_image()
        
    def load_glow_image(self):
        """Load and resize the glow image"""
        try:
            self.glow_image = Image.open("images/glow.png")
            self.glow_image = self.glow_image.resize((LED_GLOW_SIZE, LED_GLOW_SIZE), Image.Resampling.LANCZOS)
            self.glow_photo = ImageTk.PhotoImage(self.glow_image)
        except Exception as e:
            print(f"Error loading glow image: {e}")
    
    def clear_all_leds(self):
        """Clear all LED glow effects"""
        for item in self.led_items:
            self.canvas.delete(item)
        self.led_items.clear()
    
    def update_led_row(self, row_num, binary_value, num_bits=8):
        """Update a specific row of LEDs based on binary value"""
        # Clear existing LEDs for this row first
        self.clear_row_leds(row_num)
        
        # Get Y position for this row
        if row_num == 1:
            y_pos = LED_ROW1_Y
        elif row_num == 2:
            y_pos = LED_ROW2_Y
        elif row_num == 3:
            y_pos = LED_ROW3_Y
        elif row_num == 4:
            y_pos = LED_ROW4_Y
        else:
            return
        
        # Convert to binary string with proper padding
        binary_str = format(binary_value, f'0{num_bits}b')
        
        # Create LEDs for each bit
        for i, bit in enumerate(binary_str):
            if bit == '1':
                x_pos = LED_X_START + (i * LED_SPACING)
                if self.glow_photo:
                    led_item = self.canvas.create_image(
                        x_pos, y_pos, 
                        image=self.glow_photo, 
                        tags=f"led_row_{row_num}"
                    )
                    self.led_items.append(led_item)
    
    def clear_row_leds(self, row_num):
        """Clear LEDs for a specific row"""
        self.canvas.delete(f"led_row_{row_num}")
        # Remove deleted items from our tracking list
        self.led_items = [item for item in self.led_items 
                         if self.canvas.type(item) != ""]
    
    def update_display(self, operand_a, operand_b, result):
        """Update the entire LED matrix display without offset (for initial setup)"""
        self.update_display_with_offset(operand_a, operand_b, result, 0, 0)
    
    def update_display_with_offset(self, operand_a, operand_b, result, offset_x, offset_y):
        """Update the entire LED matrix display with position offset"""
        # Store current state for position updates
        self._current_state = (operand_a, operand_b, result)
        
        # Clear all existing LEDs first
        self.clear_all_leds()
        
        # Update operand A (row 1)
        self._update_led_row_with_offset(1, operand_a, 8, offset_x, offset_y)
        
        # Update operand B (row 2) 
        self._update_led_row_with_offset(2, operand_b, 8, offset_x, offset_y)
        
        # Update result lower 8 bits (row 3)
        result_low = result & 0xFF
        self._update_led_row_with_offset(3, result_low, 8, offset_x, offset_y)
        
        # Update result upper 8 bits (row 4)
        result_high = (result >> 8) & 0xFF
        self._update_led_row_with_offset(4, result_high, 8, offset_x, offset_y)
    
    def update_positions(self, offset_x, offset_y):
        """Update LED positions when image moves"""
        # Use the stored state and update with new offset
        if hasattr(self, '_current_state'):
            operand_a, operand_b, result = self._current_state
            self.update_display_with_offset(operand_a, operand_b, result, offset_x, offset_y)
    
    def _update_led_row_with_offset(self, row_num, binary_value, num_bits, offset_x, offset_y):
        """Update a specific row of LEDs with position offset"""
        # Get Y position for this row
        if row_num == 1:
            y_pos = LED_ROW1_Y + offset_y
        elif row_num == 2:
            y_pos = LED_ROW2_Y + offset_y
        elif row_num == 3:
            y_pos = LED_ROW3_Y + offset_y
        elif row_num == 4:
            y_pos = LED_ROW4_Y + offset_y
        else:
            return
        
        # Convert to binary string with proper padding
        binary_str = format(binary_value, f'0{num_bits}b')
        
        # Create LEDs for each bit
        for i, bit in enumerate(binary_str):
            if bit == '1':
                x_pos = LED_X_START + (i * LED_SPACING) + offset_x
                if self.glow_photo:
                    led_item = self.canvas.create_image(
                        x_pos, y_pos, 
                        image=self.glow_photo, 
                        tags=f"led_row_{row_num}"
                    )
                    self.led_items.append(led_item)
