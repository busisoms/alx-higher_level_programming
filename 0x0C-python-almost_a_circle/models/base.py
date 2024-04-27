import json
""" Defines Base Class """


class Base:
    """
    Base class for other classes.

    Attributes:
        __nb_objects (int): Represents the number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int): Optional. The identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to be converted.

        Returns:
            str: JSON representation of the list of dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        elif isinstance(list_dictionaries[0], dict):
            return json.dumps(list_dictionaries)
        else:
            dict_list = [obj.to_dictionary() for obj in list_dictionaries]
            return json.dumps(dict_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a file in JSON format.

        Args:
            list_objs (list): List of objects to be saved.
        """
        filename = f"{cls.__name__}.json"
        json_rep = cls.to_json_string(list_objs)

        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None or not list_objs:
                f.write("[]")
            else:
                f.write(json_rep)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): JSON string to be converted.

        Returns:
            list: List of dictionaries.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            dictionary (dict): Dictionary containing attributes.

        Returns:
            Base: An instance with attributes set from the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(2, 1, 4, 3, 0)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1, 4, 1, 1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = f"{cls.__name__}.json"

        with open(filename, mode="r", encoding="utf-8") as f:
            content = f.read()
            if not content:
                return []
            else:
                list_rep = cls.from_json_string(content)
                instance = [cls.create(**i) for i in list_rep]

        return instance
