# YAMLImg

A way to store images in YAML.

I made this after seeing [Roadcrosser's JSON-G](https://github.com/Roadcrosser/JSON-G) because it was too inspiring to ignore this opportunity.

![Lint](https://github.com/vcokltfre/yamlimg/actions/workflows/lint.yml/badge.svg)

## Installation

```sh
pip install yamlimg
```

or from GitHub

```sh
pip install git+https://github.com/vcokltfre/yamlimg
```

## Usage

Dumping an image:

```sh
yamlimg dump <image> [--output=output.yaml]
```

Loading an image:

```sh
yamlimg load <image> [--output=image.png]
```

Using the programmatic API:

```py
from PIL import Image
from yamlimg import yaml_to_image, image_to_yaml

# Open an image
image = Image.open("image.png")

# Convert the image to yaml
yaml = image_to_yaml(image)

# Convert the yaml back to an image
image = yaml_to_image(yaml)
```

## Note

There is no point in using this. It was made as a joke and I implore you not to ever actually use this for anything other than a joke.
