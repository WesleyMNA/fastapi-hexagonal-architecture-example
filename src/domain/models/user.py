class User:
    id: int
    name: str
    email: str

    def __init__(self, _id, name, email):
        self.id = _id
        self.name = name
        self.email = email