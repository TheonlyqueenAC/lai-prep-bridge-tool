# Fixed: HTML to PNG Converter Script

## What Was Wrong

On line 48 of the original script, there was a syntax error in the file path construction:

**Original (broken):**
```python
html_file = {/Users/acdmbpmax/Documents/GitHub/lai-prep-bridge-tool/circular.html)}'
```

**Fixed:**
```python
html_file = f'file://{os.path.abspath(html_path)}'
```

The original line had:
- Incorrect use of curly braces `{` instead of proper f-string syntax
- Mismatched brackets (`)` instead of `}`)
- Extra single quote at the end
- Hardcoded path instead of using the `html_path` parameter

## How to Use

1. **Install dependencies:**
   ```bash
   pip install selenium pillow
   ```

2. **Install ChromeDriver:**
   - Download from: https://chromedriver.chromium.org/
   - Or use: `brew install chromedriver` (macOS with Homebrew)
   - Or use: `apt-get install chromium-chromedriver` (Ubuntu/Debian)

3. **Run the script:**
   ```bash
   python html_to_png_converter.py
   ```

   The script will:
   - Look for `circular-cascade-comparison.html` in the current directory
   - Create a `figures/` directory
   - Generate a high-resolution PNG at `figures/figure1_circular_cascade_comparison.png`

## Output Specifications

- **Resolution:** 3800 x 2800 pixels
- **Scale:** 2x (retina quality)
- **DPI:** 300 DPI metadata (suitable for publication)
- **Target:** MDPI Viruses journal submission

## Alternative Approaches

If you encounter issues with Selenium/ChromeDriver, you can also:

1. **Use Chrome Print-to-PDF:**
   - Open the HTML in Chrome
   - Press Ctrl+P (Cmd+P on Mac)
   - Select "Save as PDF"
   - This preserves vector graphics

2. **Convert PNG to TIFF (if journal requires):**
   ```bash
   convert figure1_circular_cascade_comparison.png -compress lzw output.tiff
   ```
