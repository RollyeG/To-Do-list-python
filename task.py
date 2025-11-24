class Task:
    def __init__(self, name: str, priority: int, completion: bool = False):
        self.name = name
        self.priority = priority
        self.completion = completion
    
    def to_dict(self):
        return {
            "name": self.name,
            "priority": self.priority,
            "completion": self.completion
        }

    @classmethod
    def from_dict(cls, data: dict):
        # crea un Task a partir de un dict
        return cls(
            data["name"],
            data["priority"],
            data["completion"]
        )