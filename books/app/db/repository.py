from collections import defaultdict
from typing import Any, Dict, Type

_repository: Dict[Any, Dict[Any, Any]] = defaultdict(dict)

_books = [
    {
        "id": "1",
        "title": "Semiosis: A Novel",
        "pages": 333,
        "author_id": "4",
        "genres": [
            "Novel",
            "Science Fiction",
            "Space opera",
            "Hard science fiction",
        ],
    },
    {
        "id": "2",
        "title": "The Loosening Skin",
        "pages": 132,
        "author_id": "5",
        "genres": ["Science Fiction"],
    },
    {
        "id": "3",
        "title": "Ninefox Gambit",
        "pages": 384,
        "author_id": "6",
        "genres": ["Novel", "Science Fiction"],
    },
    {
        "id": "4",
        "title": "Raven Stratagem",
        "pages": 400,
        "author_id": "6",
        "genres": ["Science Fiction", "Fantasy Fiction"],
    },
    {
        "id": "5",
        "title": "Revenant Gun",
        "pages": 466,
        "author_id": "6",
        "genres": ["Science Fiction", "Adventure fiction"],
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
    from app.api.schemas import BookInDBBase

    for book in _books:
        db.add(BookInDBBase.parse_obj(book))
