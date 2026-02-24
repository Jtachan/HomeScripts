"""This script will return the color code of a selected pixel on your screen.

The color is returned in both formats RGB and hexadecimal.

Requires
--------
pip install pillow pynput

Examples
--------
    ```
    Click anywhere on the screen to get the pixel color. Press Ctrl+C to stop.
    Position : (945, 320)
    RGB       : (34, 139, 34)
    Hex       : #228B22
    ```
"""

from PIL import ImageGrab
from pynput import mouse


def get_pixel_rgb_color(x: int, y: int) -> tuple[int, int, int]:
    """Extracts the RGB color of the pressed pixel at coordinates `(x, y)`.

    Parameters
    ----------
    x, y: int
        Coordinates of the selected pixel, defined w.r.t. the primary monitor.
        These coordinates might be negative depending on which monitor is the
        selected pixel.
    """
    screenshot = ImageGrab.grab(all_screens=True)
    bbox = screenshot.getbbox()
    adj_coords = x - (bbox[0] if bbox else 0), y - (bbox[1] if bbox else 0)
    return screenshot.getpixel(adj_coords)


def on_mouse_click(x: int, y: int, _button: mouse.Button, pressed: bool) -> bool:
    """Callback for the mouse listener."""
    if pressed:
        rgb = get_pixel_rgb_color(x, y)
        hex_color = f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"
        print(
            f"Pixel coords (w.r.t. primary monitor): {(x, y)}\n"
            f"RGB code: {rgb}\n"
            f"Hex code: {hex_color}"
        )

    # After the first click, the function returns 'False' stopping the thread.
    return not pressed


if __name__ == "__main__":
    print("Click anywhere on the screen to get the pixel color.")
    with mouse.Listener(on_click=on_mouse_click) as listener:
        listener.join()
