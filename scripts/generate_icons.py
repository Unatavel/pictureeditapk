"""Generate Android launcher icons from the source artwork."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "art" / "app-icon-source.jpg"
ART = ROOT / "art"
RES = ROOT / "app" / "src" / "main" / "res"

DENSITIES = {
    "mdpi": 1,
    "hdpi": 1.5,
    "xhdpi": 2,
    "xxhdpi": 3,
    "xxxhdpi": 4,
}


def circle_mask(size: int) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size - 1, size - 1), fill=255)
    return mask.filter(ImageFilter.SMOOTH)


def main() -> None:
    src = Image.open(SOURCE).convert("RGBA")
    src = src.resize((1024, 1024), Image.Resampling.LANCZOS)
    png_source = ART / "app-icon.png"
    src.save(png_source, "PNG")
    src.resize((512, 512), Image.Resampling.LANCZOS).save(ART / "play-icon-512.png", "PNG")

    for name, scale in DENSITIES.items():
        folder = RES / f"mipmap-{name}"
        folder.mkdir(parents=True, exist_ok=True)

        legacy = src.resize((int(48 * scale), int(48 * scale)), Image.Resampling.LANCZOS)
        legacy.save(folder / "ic_launcher.png", "PNG")

        size = int(48 * scale)
        round_icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        round_icon.paste(legacy, (0, 0))
        round_icon.putalpha(circle_mask(size))
        round_icon.save(folder / "ic_launcher_round.png", "PNG")

        foreground = src.resize((int(108 * scale), int(108 * scale)), Image.Resampling.LANCZOS)
        foreground.save(folder / "ic_launcher_foreground.png", "PNG")


if __name__ == "__main__":
    main()
