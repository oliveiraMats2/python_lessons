class Singleton(object):
    instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f"object created {cls.instance}")

        return cls.instance


s_1 = Singleton()

print(f"Instance 1: {id(s_1)}")

s_2 = Singleton()

print(f"Instance 2: {id(s_2)}")
