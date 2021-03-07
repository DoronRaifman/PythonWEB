def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass:
    pass


c1 = MyClass()
c2 = MyClass()


print(f'c1={c1}')
print(f'c2={c2}')


