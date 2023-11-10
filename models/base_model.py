#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id: str = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.name = None
        self.my_number = None
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        class_attr = self.__dict__
        filtered_class_attr = dict()

        filtered_class_attr["updated_at"]: str = self.updated_at
        filtered_class_attr["created_at"]: str = self.created_at

        for key in class_attr:
            if class_attr[key] is not None:
                filtered_class_attr[key] = class_attr[key]
        filtered_class_attr["__class__"] = self.__class__.__name__

        return filtered_class_attr


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
# print(my_model)
print("***** \n")
my_model.save()
# print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
