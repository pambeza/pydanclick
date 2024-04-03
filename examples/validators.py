from typing import List

import click
from pydantic import BaseModel

from pydanclick import from_pydantic


class CustomSubModel(BaseModel):
    sub_values: List[str]


class CustomModel(BaseModel):
    values: List[int]
    sub_model: CustomSubModel


@click.command()
@from_pydantic(
    CustomModel, validators={"values": lambda x: map(int, x.split(",")), "sub_model.sub_values": lambda x: x.split(",")}
)
def test(custom_model: CustomModel):
    click.echo(custom_model.model_dump_json(indent=2))


if __name__ == "__main__":
    test()
