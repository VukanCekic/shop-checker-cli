class Book:

    def __init__(self, id, name,
                 category, date_added):
        self.id = id
        self.name = name
        self.category = category
        self.date_added = date_added

    def __repr__(self) -> str:
        return f"({self.id}, {self.name}, {self.category}, {self.date_added})"

    def __getitem__(self, key: str):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value
