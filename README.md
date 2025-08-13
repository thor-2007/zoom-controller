# Zoom Controller

A Zoom Controller I programmed because I have bad eyesight and found FPS shooter games unfair.
Made with **Tkinter** and **Python**.

---
## Optional:

## Creating an Executable (.exe)

If you want to run this project without installing Python, you can create a standalone executable using **PyInstaller**.

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Navigate to the Project Directory

```bash
cd path/to/zoom_controller
```

### 3. Build the Executable

```bash
pyinstaller --onefile --windowed --icon=icon.ico zoom_controller.py
```

**Options explained:**

* `--onefile` → bundle everything into a single `.exe` file
* `--windowed` / `-w` → run without a console window (for GUI apps)
* `--icon=icon.ico` → set a custom icon
* `--add-data "source;destination"` → include extra files or folders

### 4. Locate the Output

After building, your `.exe` will be in the `dist/` folder inside your project directory.

### 5. Test the Executable

Run the `.exe` to confirm it works as expected.
