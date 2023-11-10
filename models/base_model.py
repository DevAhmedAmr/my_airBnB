class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = None
        self.my_number = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) created_at: {} updated_at: {} {}".format(
            self.__class__.__name__,
            self.id,
            self.created_at.isoformat(),
            self.updated_at.isoformat(),
            self.__dict__,
        )

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        class_attr = self.__dict__
        filtered_class_attr = {}

        # Convert created_at and updated_at to ISO format strings
        filtered_class_attr["created_at"] = self.created_at.isoformat()
        filtered_class_attr["updated_at"] = self.updated_at.isoformat()

        # Include only non-None values and non-default values
        for key, value in class_attr.items():
            if value is not None and value != "default_value":
                filtered_class_attr[key] = value

        # Add the __class__ key with the class name
        filtered_class_attr["__class__"] = self.__class__.__name__

        return filtered_class_attr


# Example usage:
base_model_instance = BaseModel()
print(str(base_model_instance))
result_dict = base_model_instance.to_dict()
print(result_dict)
