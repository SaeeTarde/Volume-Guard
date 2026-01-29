import tkinter as tk
import random
import winsound


def show_cute_warning(volume, safe_volume):
    # 🎭 Random cute character
    character = random.choice(["🐱", "🐼", "🦊"])

    root = tk.Tk()
    root.title("Volume Guard")

    width, height = 300, 140

    # 📍 Center the window
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w // 2) - (width // 2)
    y = (screen_h // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")
    root.resizable(False, False)
    root.configure(bg="#fff7e6")

    # 🔝 Always on top
    root.attributes("-topmost", True)

    # 🌫️ Start fully transparent
    root.attributes("-alpha", 0.0)

    # 🔔 Soft alert sound
    winsound.MessageBeep(winsound.MB_ICONASTERISK)

    # 🧸 UI
    label1 = tk.Label(
        root,
        text=f"{character} Hey! Careful!",
        font=("Segoe UI", 20, "bold"),
        bg="#fff7e6"
    )
    label1.pack(pady=(15, 5))

    label2 = tk.Label(
        root,
        text=f"Headphones on 🎧\nVolume {volume}% → {safe_volume}%",
        font=("Segoe UI", 10),
        bg="#fff7e6"
    )
    label2.pack()

    # ✨ Fade-in animation
    def fade_in(alpha=0.0):
        alpha += 0.05
        root.attributes("-alpha", alpha)
        if alpha < 1.0:
            root.after(20, fade_in, alpha)
        else:
            # Start fade-out shortly after volume is lowered
            root.after(1200, fade_out)

    # 🌙 Fade-out animation
    def fade_out(alpha=1.0):
        alpha -= 0.05
        root.attributes("-alpha", alpha)
        if alpha > 0:
            root.after(20, fade_out, alpha)
        else:
            root.destroy()

    fade_in()
    root.mainloop()
