from __future__ import annotations

from PIL import Image
from yaml import SafeLoader, load

from .spec import YAMLImg


def image_to_yaml(img: Image.Image) -> str:
    data = f"version: 1\nwidth: {img.width}\nheight: {img.height}\ndata:\n"

    pixels: list[str] = []

    for x in range(img.width):
        for y in range(img.height):
            pixel: tuple[int, int, int, int] = img.getpixel((x, y))  # type: ignore
            pixels.append(
                "\n".join(
                    [
                        p
                        for p in [
                            f"- x: {x}",
                            f"  y: {y}",
                            f"  r: {pixel[0]}" if pixel[0] != 0 else "",
                            f"  g: {pixel[1]}" if pixel[1] != 0 else "",
                            f"  b: {pixel[2]}" if pixel[2] != 0 else "",
                            f"  a: {pixel[3]}" if len(pixel) == 4 and pixel[3] != 0 else "",
                        ]
                        if p
                    ]
                )
                + "\n"
            )

    data += "".join(pixels)
    return data


def yaml_to_image(yaml: str) -> Image.Image:
    data = load(yaml, SafeLoader)
    img = YAMLImg(**data)

    if img.version != 1:
        raise ValueError("Unsupported version")

    image = Image.new("RGBA", (img.width, img.height))

    for pixel in img.data:
        image.putpixel((pixel.x, pixel.y), (pixel.r, pixel.g, pixel.b, pixel.a))

    return image
