# Configuration and constants
import numpy as np

# Display settings
INITIAL_ZOOM = 0.62  # Change this to adjust initial zoom level
MOVE_SPEED = 20      # How fast arrow keys move the image

# Button settings
BUTTON_SIZE = 20     # Square buttons (in pixels)
BUTTON_WIDTH_CHARS = max(1, BUTTON_SIZE // 10)  # Convert pixels to character width
BUTTON_HEIGHT_CHARS = max(1, BUTTON_SIZE // 15)  # Convert pixels to character height

# Window settings
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# LED Matrix settings
LED_GLOW_SIZE = 200        # Size of the glow effect (square)
LED_SPACING = 68          # Spacing between each LED
LED_X_START = 785         # X position of the first LED (all LEDs align vertically)
LED_ROW1_Y = 315          # Y position of row 1 (operand A)
LED_ROW2_Y = 450          # Y position of row 2 (operand B) 
LED_ROW3_Y = 750          # Y position of row 3 (result bits 0-7)
LED_ROW4_Y = 885          # Y position of row 4 (result bits 8-15)

# Button positions - adjust these coordinates to position buttons on your circuit
BUTTON_POSITIONS = {
    'del_row1': (615, 356),
    'del_row2': (615, 447),
    'append_1_row1': (1456, 356),
    'append_0_row1': (1547, 356),
    'append_1_row2': (1456, 447),
    'append_0_row2': (1547, 447),
    'del_output': (1547, 902),
    'not_output': (615, 902),
    'and_op': (728, 629),
    'or_op': (819, 629),
    'xor_op': (910, 629),
    'mod_op': (1001, 629),
    'add_op': (1092, 629),
    'div_op': (1183, 629),
    'sub_op': (1274, 629),
    'mult_op': (1365, 629)
}
