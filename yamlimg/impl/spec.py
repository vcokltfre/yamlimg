from pydantic import BaseModel


class Pixel(BaseModel):
    x: int
    y: int
    r: int = 0
    g: int = 0
    b: int = 0
    a: int = 0


class YAMLImg(BaseModel):
    version: int
    width: int
    height: int
    data: list[Pixel]
