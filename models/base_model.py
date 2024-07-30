"""
The base model class module
"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model of the air-bnb storage model"""
    id: str
    # created_at

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()

    def __str__(self):
        """returns human readable representation of the BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the BaseModel instance"""
        return self.__dict__



# newObj = BaseModel()

# print(f"first time printing: {newObj.__str__()}")

# newObj.save()

# print(f"second time printing: {newObj.__str__()}")