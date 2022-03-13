from __future__ import annotations

from PIL import Image
from yaml import SafeLoader, dump, load

from .spec import YAMLImg


def image_to_yaml(img: Image.Image) -> str:
    data: dict[str, int | list[dict[str, int]]] = {
        "version": 1,
        "width": img.width,
        "height": img.height,
    }

    pixels: list[dict[str, int]] = []

    for x in range(img.width):
        for y in range(img.height):
            pixel: tuple[int, int, int, int] = img.getpixel((x, y))  # type: ignore
            pixels.append(
                {
                    "x": x,
                    "y": y,
                    "r": pixel[0],
                    "g": pixel[1],
                    "b": pixel[2],
                    "a": pixel[3] if len(pixel) > 3 else 255,
                }
            )

    data["data"] = pixels

    return dump(data, default_flow_style=False)


def yaml_to_image(yaml: str) -> Image.Image:
    data = load(yaml, SafeLoader)
    img = YAMLImg(**data)

    if img.version != 1:
        raise ValueError("Unsupported version")

    image = Image.new("RGBA", (img.width, img.height))

    for pixel in img.data:
        image.putpixel((pixel.x, pixel.y), (pixel.r, pixel.g, pixel.b, pixel.a))

    return image
