from PIL import Image
from typer import Typer, echo

from ..impl import image_to_yaml, yaml_to_image

app = Typer()


@app.command(name="dump")
def dump(image: str, output: str = "image.yaml") -> None:
    img = Image.open(image)

    with open(output, "w") as f:
        f.write(image_to_yaml(img))

    echo(f"Dumped image to {output}")


@app.command(name="load")
def load(image: str, output: str = "image.png") -> None:
    with open(image) as f:
        yaml = f.read()

    img = yaml_to_image(yaml)
    img.save(output)

    echo(f"Loaded image from {image}")
