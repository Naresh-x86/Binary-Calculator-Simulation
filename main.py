import tkinter as tk
from PIL import Image, ImageTk
from config import *
from ui_components import create_button
from button_functions import *
from led_matrix import LEDMatrix

# Create window
root = tk.Tk()
root.title("Binary Calculator Circuit Simulator")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)

# Create canvas
canvas = tk.Canvas(root, bg='black', highlightthickness=0)
canvas.place(x=0, y=0, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# Initialize LED Matrix
led_matrix = LEDMatrix(canvas)

# Load and resize image
image = Image.open("images/circuit_light.png")
original_width, original_height = image.size
new_width = int(original_width * INITIAL_ZOOM)
new_height = int(original_height * INITIAL_ZOOM)
resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized_image)

# Place image on canvas
image_x = 0
image_y = 0
image_item = canvas.create_image(image_x, image_y, anchor='nw', image=photo)

# Core movement and positioning logic
def move_image(event):
    global image_x, image_y
    
    # Calculate movement limits
    min_x = WINDOW_WIDTH - new_width   # Left edge of image at right edge of canvas
    max_x = 0                          # Right edge of image at left edge of canvas
    min_y = WINDOW_HEIGHT - new_height # Top edge of image at bottom edge of canvas
    max_y = 0                          # Bottom edge of image at top edge of canvas
    
    # Move based on arrow key
    if event.keysym == 'Up':
        image_y = min(image_y + MOVE_SPEED, max_y)
    elif event.keysym == 'Down':
        image_y = max(image_y - MOVE_SPEED, min_y)
    elif event.keysym == 'Left':
        image_x = min(image_x + MOVE_SPEED, max_x)
    elif event.keysym == 'Right':
        image_x = max(image_x - MOVE_SPEED, min_x)
    
    # Update image position
    canvas.coords(image_item, image_x, image_y)
    
    # Update button positions to move with the image
    update_button_positions()

def update_button_positions():
    """Update all button positions relative to the image offset"""
    for button_name, (orig_x, orig_y) in BUTTON_POSITIONS.items():
        new_x = orig_x + image_x
        new_y = orig_y + image_y
        canvas.coords(button_items[button_name], new_x, new_y)
    
    # Update LED positions as well
    update_led_positions()

def update_led_positions():
    """Update LED positions to move with the image"""
    led_matrix.update_positions(image_x, image_y)

def update_led_display():
    """Update the LED matrix display with current calculator state"""
    operand_a, operand_b, result = get_calculator_state()
    # Always update with current image offset to maintain consistent positioning
    led_matrix.update_display_with_offset(operand_a, operand_b, result, image_x, image_y)

def create_button_with_led_update(root, text, command, width_chars, height_chars, tooltip):
    """Create a button that updates LEDs after executing its command"""
    def wrapped_command():
        command()  # Execute original command
        update_led_display()  # Update LED display
    
    return create_button(root, text, wrapped_command, width_chars, height_chars, tooltip)

# Button creation and setup
buttons = {}
button_items = {}  # Store canvas window item references

# Button definitions with their properties
button_definitions = [
    ('del_row1', "DEL", del_row1, "Delete Row 1 (Clear first 8-bit input)"),
    ('del_row2', "DEL", del_row2, "Delete Row 2 (Clear second 8-bit input)"),
    ('append_1_row1', "1", append_1_row1, "Append 1 to Row 1"),
    ('append_0_row1', "0", append_0_row1, "Append 0 to Row 1"),
    ('append_1_row2', "1", append_1_row2, "Append 1 to Row 2"),
    ('append_0_row2', "0", append_0_row2, "Append 0 to Row 2"),
    ('del_output', "DEL", del_output, "Delete All Output (Clear result)"),
    ('not_output', "NOT", not_output, "NOT Operation (Bitwise NOT)"),
    ('and_op', "AND", and_op, "AND Operation (Bitwise AND)"),
    ('or_op', "OR", or_op, "OR Operation (Bitwise OR)"),
    ('xor_op', "XOR", xor_op, "XOR Operation (Bitwise XOR)"),
    ('mod_op', "MOD", mod_op, "MOD Operation (Modulo)"),
    ('add_op', "+", add_op, "ADD Operation"),
    ('div_op', "/", div_op, "DIV Operation (Division)"),
    ('sub_op', "-", sub_op, "SUB Operation (Subtraction)"),
    ('mult_op', "*", mult_op, "MULT Operation (Multiplication)")
]

# Create all buttons
for button_id, text, command, tooltip in button_definitions:
    buttons[button_id] = create_button_with_led_update(root, text, command, BUTTON_WIDTH_CHARS, BUTTON_HEIGHT_CHARS, tooltip)
    button_items[button_id] = canvas.create_window(
        BUTTON_POSITIONS[button_id][0], 
        BUTTON_POSITIONS[button_id][1], 
        window=buttons[button_id]
    )

# Initialize LED display with all zeros
update_led_display()

# Bind arrow keys
root.bind('<Key>', move_image)
root.focus_set()

# Start the application
root.mainloop()