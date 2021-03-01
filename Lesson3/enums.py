from enum import Enum


class Things(Enum):
    banana = 1
    apple = 2
    house = 3
    bedroom = 4

    @classmethod
    def is_fruit(cls, enum_val):
        return True if enum_val in {cls.banana, cls.apple} else False

    @classmethod
    def is_house_thing(cls, enum_val):
        return True if enum_val in {cls.house, cls.bedroom} else False


if __name__ == '__main__':
    print("Demonstrate enum")
    thing = Things.banana
    print(f'Enum: {thing}, value:{thing.value}, name: {thing.name}')
    print(f'{thing} is fruit:{Things.is_fruit(thing)}')
    print(f'{thing} is house thing:{Things.is_house_thing(thing)}')

    print(f'finding enum: by value:{Things(3)}, by name:{Things["house"]}')

    # this lines will cause Exception Things.values(), Things.keys()
    enum_items = {item.name: item.value for item in Things}
    print(f'items as dict: {enum_items}')

