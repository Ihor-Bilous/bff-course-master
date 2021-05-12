from collections import defaultdict
from typing import Any, Dict, Type

_repository: Dict[Any, Dict[Any, Any]] = defaultdict(dict)

_authors = [
    {
        "id": "1",
        "first_name": "Loreth Anne",
        "last_name": "White",
        "born": "South Africa",
    },
    {
        "id": "2",
        "first_name": "Lisa",
        "last_name": "Regan",
        "born": "USA",
    },
    {
        "id": "3",
        "first_name": "Ty",
        "last_name": "Patterson",
        "born": "USA",
    },
    {
        "id": "4",
        "first_name": "Sue",
        "last_name": "Burke",
        "born": "USA",
    },
    {
        "id": "5",
        "first_name": "Aliya",
        "last_name": "Whiteley",
        "born": "UK",
    },
    {
        "id": "6",
        "first_name": "Yoon Ha",
        "last_name": "Lee",
        "born": "USA",
    },
]


class Repository:
    @staticmethod
    def all(model_type: Any) -> Any:
        return _repository[model_type].values()

    @staticmethod
    def get_by_id(model_type: Any, id: Any) -> Any:
        return _repository[model_type].get(id)

    @staticmethod
    def add(model_instance: Any) -> None:
        model_repo = _repository[type(model_instance)]
        if not _repository:
            _repository[type(model_instance)] = {}
        model_repo[getattr(model_instance, "id")] = model_instance

    @staticmethod
    def remove(model_instance: Any) -> None:
        del _repository[type(model_instance)][getattr(model_instance, "id")]

    @staticmethod
    def get_max_id(model_type: Any) -> Any:
        return max([getattr(item, "id") for _, item in _repository[model_type].items()])


def init_db(db: Type[Repository]) -> None:
    from app.api.schemas import AuthorInDBBase

    for author in _authors:
        db.add(AuthorInDBBase.parse_obj(author))
