from PIL import Image, ImageDraw
import os

def create_placeholder_images():
    assets_dir = "aulas/assets/images"
    os.makedirs(assets_dir, exist_ok=True)

    # 1. Background (Dark Blue)
    bg = Image.new('RGB', (1920, 1080), color='#0f172a') # Slate 900
    draw = ImageDraw.Draw(bg)
    # Draw some "matrix" style lines
    for i in range(0, 1920, 40):
        draw.line([(i, 0), (i, 1080)], fill='#1e293b', width=1)
    bg.save(f"{assets_dir}/parallax_bg.png")
    print(f"Created {assets_dir}/parallax_bg.png")

    # 2. Middle Layer (Floating Elements)
    mid = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(mid)
    # Draw some squares/circles
    draw.rectangle([200, 200, 400, 400], fill=(56, 189, 248, 128)) # Sky blue semi-transparent
    draw.ellipse([1500, 100, 1700, 300], fill=(255, 215, 0, 128)) # Gold semi-transparent
    draw.rectangle([800, 500, 900, 600], fill=(56, 189, 248, 100), outline='white', width=2)
    mid.save(f"{assets_dir}/parallax_mid.png")
    print(f"Created {assets_dir}/parallax_mid.png")

    # 3. Foreground (Bottom Wave)
    fg = Image.new('RGBA', (1920, 1080), (0, 0, 0, 0))
    draw = ImageDraw.Draw(fg)
    # Draw a bottom wave/shape
    draw.polygon([(0, 900), (1920, 800), (1920, 1080), (0, 1080)], fill='#1e293b')
    draw.line([(0, 900), (1920, 800)], fill='#38bdf8', width=5)
    fg.save(f"{assets_dir}/parallax_fg.png")
    print(f"Created {assets_dir}/parallax_fg.png")

if __name__ == "__main__":
    create_placeholder_images()
