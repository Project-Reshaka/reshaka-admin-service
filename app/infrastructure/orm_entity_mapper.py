from typing import TypeVar, Optional, Type

TEntity = TypeVar("TEntity")
TModel = TypeVar("TModel")

class OrmEntityMapper:
    @staticmethod
    def to_entity(model: Optional[TModel], entity_class: Type[TEntity]) -> Optional[TEntity]:
        if model is None:
            return None
        data = {
            k: v
            for k, v in model.__dict__.items()
            if not k.startswith("_") and not callable(v)
        }

        return entity_class(**data)

    @staticmethod
    def to_model(entity: TEntity, model_cls: Type[TModel]) -> TModel:
        data = {
            k: v
            for k, v in entity.__dict__.items()
            if not k.startswith("_") and not callable(v)
        }
        return model_cls(**data)