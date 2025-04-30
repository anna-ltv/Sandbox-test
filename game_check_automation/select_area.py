import time
import mss
from PIL import Image, ImageTk
import tkinter as tk

time.sleep(2)


def get_user_selected_area():
    def on_mouse_down(event):
        nonlocal start_x, start_y
        start_x, start_y = event.x, event.y

    def on_mouse_up(event):
        nonlocal end_x, end_y
        end_x, end_y = event.x, event.y
        root.quit()

    def on_mouse_drag(event):
        nonlocal start_x, start_y
        canvas.delete("selection")
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", tag="selection")

    # Capture the screen
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = Image.frombytes('RGB', (screenshot.width, screenshot.height), screenshot.rgb)

    # Create a Tkinter window with the screenshot
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)  # Ensure the window is on top
    canvas = tk.Canvas(root, width=img.width, height=img.height)
    canvas.pack()
    img_tk = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

    start_x = start_y = end_x = end_y = 0
    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)
    canvas.bind("<B1-Motion>", on_mouse_drag)

    root.mainloop()
    root.destroy()

    width = end_x - start_x
    height = end_y - start_y
    return (start_x, start_y, width, height)

if __name__ == "__main__":
    # Test the function if this script is run directly
    selected_area = get_user_selected_area()
    print(f"Selected area: {selected_area}")