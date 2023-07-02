class MetaSingleton(type):

    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass

log_1 = Logger()
print(f"log 1: {id(log_2)}")

log_2 = Logger()
print(f"log 1: {id(log_2)}")