
class Singleton:
    """Class that implements singletone pattern."""
    
    _instances: dict = dict()

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances: 
            instance = super().__new__(cls, *args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls] 
