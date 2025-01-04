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

def test_get_person_success():
    mock_connection = MockConnection()
    repo = PeopleRepository(mock_connection)

    mock_person = MagicMock()
    mock_person.first_name = "João"
    mock_person.last_name = "Otávio"
    mock_person.pet_name = "max"
    mock_person.pet_type = "dog"

    mock_connection.session.query.return_value \
        .outerjoin.return_value \
        .filter.return_value \
        .with_entities.return_value \
        .one.return_value = mock_person

    person = repo.get_person(1)

    assert person.first_name == "João"
    assert person.last_name == "Otávio"
    assert person.pet_name == "max"
    assert person.pet_type == "dog"

def test_get_person_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PeopleRepository(mock_connection)

    person = repo.get_person(999)
    assert person is None
