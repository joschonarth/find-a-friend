from unittest.mock import MagicMock
from sqlalchemy.orm.exc import NoResultFound
import pytest
from src.models.sqlite.repositories.people_repository import PeopleRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = MagicMock()

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = MagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_person():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)

    repo.insert_person("João", "Otávio", 20, 2)

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_insert_person_error():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)

    mock_connection.session.add.side_effect = Exception("Insert failed")

    with pytest.raises(Exception):
        repo.insert_person("João", "Otávio", 20, 2)

    mock_connection.session.rollback.assert_called_once()
