# 🎧 Volume Guard

A cute Windows utility that protects your ears by automatically lowering volume when headphones are connected.

## ✨ Features

- 🎧 Detects headphone connection
- 🔊 Warns if volume is above safe level
- 🐱🐼🦊 Cute animated notification
- 🔉 Auto-lowers volume
- 🐰 Custom app icon
- 🚀 Can run on startup

## 🛠️ Tech Stack

- Python
- pycaw (Windows audio control)
- Tkinter (UI)
- PyInstaller

## ▶️ How to Run (Source Code)

```bash
pip install -r requirements.txt
python main.py

Build EXE
pyinstaller --onefile --windowed --icon=icon.ico --name VolumeGuard main.py

🧠 Use Case

Protect ears from sudden loud sounds when plugging headphones 🎧
```
