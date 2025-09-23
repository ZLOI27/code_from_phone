@dataclass

def to_Klass(data: dict):
    klass = Klass()
    for key, value in data.items():
        setattr(klass, key, value)
    return klass
