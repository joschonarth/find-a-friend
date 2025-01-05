from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Fluffy", type="Cat", id=10),
            PetsTable(name="Buddy", type="Dog", id=11)
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    excepted_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                { "name": "Fluffy", "type": "Cat", "id": 10 },
                { "name": "Buddy", "type": "Dog", "id": 11 }
            ]
        }
    }

    assert response == excepted_response
