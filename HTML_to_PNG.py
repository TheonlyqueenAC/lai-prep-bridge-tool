#!/usr/bin/env python3
"""
Convert HTML cascade visualization to publication-ready image for MDPI Viruses LaTeX manuscript
Requires: selenium, pillow, and Chrome/Firefox WebDriver
"""

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import time


def html_to_png_highres(html_path, output_path, width=3800, height=2800, scale=2):
    """
    Convert HTML file to high-resolution PNG suitable for publication

    Parameters:
    -----------
    html_path : str
        Path to the HTML file
    output_path : str
        Path for output PNG file
    width : int
        Viewport width in pixels (default 3800 for 2x scale)
    height : int
        Viewport height in pixels (default 2800 for 2x scale)
    scale : int
        Device scale factor (2 or 3 for retina/high-DPI)
    """

    # Set up Chrome options for headless rendering
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'--window-size={width},{height}')
    chrome_options.add_argument(f'--force-device-scale-factor={scale}')

    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Load HTML file
        html_file = f'file://{os.path.abspath(html_path)}'
        print(f"Loading HTML from: {html_file}")
        driver.get(html_file)

        # Wait for rendering
        time.sleep(3)

        # Take screenshot
        print(f"Capturing screenshot at {width}x{height} with {scale}x scaling...")
        driver.save_screenshot(output_path)

        # Verify and report DPI
        img = Image.open(output_path)
        actual_width, actual_height = img.size

        # Calculate effective DPI at journal column width
        # MDPI single column: ~3.35 inches, two-column: ~7 inches
        dpi_single_column = actual_width / 7.0  # Full page width
        dpi_two_column = actual_width / 3.35  # Single column width

        print(f"\nOutput image specifications:")
        print(f"  Dimensions: {actual_width} x {actual_height} pixels")
        print(f"  File size: {os.path.getsize(output_path) / 1024 / 1024:.2f} MB")
        print(f"  Effective DPI at full page width (7\"): {dpi_single_column:.0f} DPI")
        print(f"  Effective DPI at single column (3.35\"): {dpi_two_column:.0f} DPI")

        if dpi_single_column >= 300:
            print(f"  ✓ Meets 300 DPI requirement for full page width")
        else:
            print(f"  ⚠ Below 300 DPI for full page - increase width or scale")

        # Set DPI metadata
        img.save(output_path, dpi=(300, 300))
        print(f"\n✓ Saved to: {output_path}")

    finally:
        driver.quit()


def main():
    """Convert the circular cascade comparison HTML to publication-ready PNG"""

    # Input and output paths
    input_html = 'circular-cascade-comparison.html'
    output_png = 'figures/figure1_circular_cascade_comparison.png'

    # Create output directory
    os.makedirs('figures', exist_ok=True)

    # Check if input exists
    if not os.path.exists(input_html):
        print(f"Error: {input_html} not found!")
        print("Please ensure the HTML file is in the current directory.")
        return

    print("=" * 70)
    print("Converting HTML to Publication-Ready PNG for MDPI Viruses")
    print("=" * 70)

    # Convert at 2x scale (3800x2800) for high DPI
    html_to_png_highres(
        html_path=input_html,
        output_path=output_png,
        width=3800,
        height=2800,
        scale=2
    )

    print("\n" + "=" * 70)
    print("NEXT STEPS:")
    print("=" * 70)
    print("1. Review the generated figure: figures/figure1_circular_cascade_comparison.png")
    print("2. Verify text is readable when zoomed to actual print size")
    print("3. Copy the LaTeX code from latex_figure_instructions.tex")
    print("4. Place PNG in your LaTeX project's figures/ directory")
    print("5. Compile manuscript and check figure rendering")
    print("\nFor alternative formats:")
    print("  - PDF: Use print-to-PDF from Chrome for vector graphics")
    print("  - TIFF: Convert PNG using: convert input.png -compress lzw output.tiff")
    print("=" * 70)


if __name__ == '__main__':
    # Check dependencies
    try:
        import selenium
        from PIL import Image

        main()
    except ImportError as e:
        print("Missing required package!")
        print("\nInstall dependencies with:")
        print("  pip install selenium pillow")
        print("  # Also install ChromeDriver: https://chromedriver.chromium.org/")
        print(f"\nError: {e}")