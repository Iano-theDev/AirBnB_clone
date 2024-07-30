"""
The base model class module
"""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model of the air-bnb storage model"""
    def __init__(self, *args, **kwargs):
        if not kwargs: 
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)

    def __str__(self):
        """returns human readable representation of the BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the BaseModel instance"""
        bmDict = self.__dict__
        bmDict['__class__'] = self.__class__.__name__
        bmDict["created_at"] = bmDict["created_at"].isoformat()
        if ('updated_at' in bmDict):
            bmDict["updated_at"] = bmDict["updated_at"].isoformat()
        return bmDict



# newObj = BaseModel()

# print(f"first time printing: {newObj.__str__()}")

# newObj.save()

# print(f"second time printing: {newObj.__str__()}")

# bm = BaseModel()
# bm.save()
# print(type(bm.created_at))
# print(bm.to_dict())

# bm = BaseModel()
# bm.updated_at = datetime.utcnow()
# d_json = bm.to_dict()
# print(type(d_json))
# print(type(d_json['id']))
# print(type(d_json['created_at']))
# print(type(d_json['__class__']))
# print(d_json['__class__'])

