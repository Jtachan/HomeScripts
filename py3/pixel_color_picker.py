"""Script that returns the color code of a selected pixel on your screen.

The color is returned in both formats RGB and hexadecimal.
The script also considers only the primary monitor.

Requires
--------
pip install pillow pynput

Instructions
------------
1. Run the script via `python ./py3/pixel_color_picker.py`
2. Use your mouse to point and left-click on your primary monitor at the color you are interested.
        After clicking, the color will be displayed via terminal (see the example below).
3. The program will run indefinitely, allowing you to click as many times as you want to pick the color.
4. Stop the program by pressing 'ESC'.

Examples
--------
    ```
    Click anywhere on the screen to get the pixel color.
    Press ESC to stop the program.

    Position : (945, 320)
    RGB       : (34, 139, 34)
    Hex       : #228B22
    ```
"""

from PIL import ImageGrab
from pynput import keyboard, mouse


def get_pixel_rgb_color(x: int, y: int) -> tuple[int, int, int]:
    """Extracts the RGB color of the pressed pixel at coordinates `(x, y)`.

    Parameters
    ----------
    x, y: int
        Coordinates of the selected pixel, defined w.r.t. the primary monitor.
        These coordinates might be negative depending on which monitor is the
        selected pixel.
    """
    screenshot = ImageGrab.grab()
    return screenshot.getpixel((x, y))


def on_mouse_click(x: int, y: int, _button: mouse.Button, pressed: bool):
    """Callback for the mouse listener."""
    if pressed:
        if x < 0 or y < 0:
            print("Pixel is not from the primary monitor")
            return

        rgb = get_pixel_rgb_color(x, y)
        hex_color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        print(
            f"Pixel coords (w.r.t. primary monitor): {(x, y)}\n"
            f"RGB code: {rgb}\n"
            f"Hex code: {hex_color}"
        )


if __name__ == "__main__":

    def on_keyboard_press(key: keyboard.Key) -> bool:
        """Function to allow stopping the program if 'ESC' is pressed."""
        if key == keyboard.Key.esc:
            mouse_listener.stop()
            return False
        return True

    print(
        "Click anywhere on the screen to get the pixel color.\nPress 'ESC' to stop the program."
    )

    mouse_listener = mouse.Listener(on_click=on_mouse_click)
    key_listener = keyboard.Listener(on_press=on_keyboard_press)

    mouse_listener.start()
    key_listener.start()

    mouse_listener.join()
    key_listener.join()
