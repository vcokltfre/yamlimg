from pydantic import BaseModel


class Pixel(BaseModel):
    x: int
    y: int
    r: int
    g: int
    b: int
    a: int


class YAMLImg(BaseModel):
    version: int
    width: int
    height: int
    data: list[Pixel]
