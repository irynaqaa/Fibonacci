from pydantic import BaseModel, ValidationError

class InputData(BaseModel):
    id: int
    name: str
    description: str


def validate_input_data_pydantic(data):
    try:
        input_data = InputData(**data)
        return input_data
    except ValidationError as e:
        print(e)