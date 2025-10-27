from pathlib import Path
from typing import Optional, Sequence

import click

from config import CONVERSION_CHARACTERS
from converter import image_to_ascii, load_font


@click.command()
@click.option(
    "--image-path",
    "-i",
    default=str(Path(__file__).parents[1] / "images" / "angry_bird.jpg"),
    help='Path or URL of the image to convert. You can also use "clip" or "clipboard" to paste the value directly from the clipboard.',
)
@click.option(
    "--size",
    "-s",
    default=None,
    type=(int, int),
    help="Size of the output ASCII art (width, height). If not provided, the original image size is used.",
)
@click.option(
    "--charset",
    "-c",
    default=CONVERSION_CHARACTERS,
    type=click.STRING,
    help="Characters to use for ASCII art. If not provided, a default charset is used.",
)
@click.option(
    "--fix-scaling/--no-fix-scaling",
    default=True,
    help="Whether to fix the aspect ratio scaling for ASCII characters.",
)
@click.option(
    "--scale",
    default=1.0,
    type=float,
    help="Scaling factor for the output ASCII art size.",
)
@click.option(
    "--sharpness",
    default=1.0,
    type=float,
    help="Sharpness factor to enhance image details.",
)
@click.option(
    "--brightness",
    default=1.0,
    type=float,
    help="Brightness factor to adjust image brightness.",
)
@click.option(
    "--sort-chars/--no-sort-chars",
    default=False,
    help="Whether to sort the charset by character brightness.",
)
@click.option(
    "--colorful/--no-colorful",
    default=False,
    help="Whether to use colored characters in the ASCII art.",
)
@click.option(
    "--font-str",
    default=None,
    type=str,
    help="Font file to use for character brightness calculation (default: monos.ttf).",
)
@click.option(
    "--font-size",
    default=20,
    type=int,
    help="Font size to use for character brightness calculation.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
    help="Enable verbose output.",
)
def main(
    image_path: str,
    size: Optional[tuple[int, int]] = None,
    charset: Optional[Sequence[str]] = None,
    fix_scaling: bool = True,
    scale: float | tuple[float, float] = 1,
    sharpness: float = 1,
    brightness: float = 1,
    sort_chars: bool = False,
    colorful: bool = False,
    font_str: Optional[str] = None,
    font_size: int = 20,
    verbose: bool = False,
) -> None:
    if font_str is None:
        font_str = "monos.ttf"

    if font_size <= 0:
        font_size = 20

    font = load_font(font_str, font_size)
    if verbose:
        click.echo(f"Reading image from: {image_path}")
        click.echo(f"Output size: {size}")
        click.echo(f"Charset: {charset}")
        click.echo(f"Fix scaling: {fix_scaling}")
        click.echo(f"Scale: {scale}")
        click.echo(f"Sharpness: {sharpness}")
        click.echo(f"Brightness: {brightness}")
        click.echo(f"Sort chars: {sort_chars}")
        click.echo(f"Colorful: {colorful}")

    ascii_art = image_to_ascii(
        image_path,
        size,
        charset,
        fix_scaling,
        scale,
        sharpness,
        brightness,
        sort_chars,
        colorful,
        font=font,
    )
    click.echo(ascii_art)
    return None


if __name__ == "__main__":
    main()
