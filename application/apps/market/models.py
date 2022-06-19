from orm_converter.tortoise_to_django import ConvertedModel
from tortoise import Tortoise, fields
from tortoise.models import Model


class ExampleModel(Model, ConvertedModel):
    name = fields.CharField(max_length=255)

    class Meta:
        abstract = True
        table = "example"


def register_models() -> None:
    Tortoise.init_models(
        models_paths=["apps.market.models"],
        app_label="market",
        _init_relations=False,
    )
