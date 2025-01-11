from pprint import pprint
import inspect


def introspection_info(obj):
    attributes = dir(obj)
    metods = [method for method in attributes if callable(getattr(obj, method))]
    return {'type': type(obj).__name__,
            'attributes': attributes,
            'metods': metods,
            'module': inspect.getmodule(obj)
            }


class MyClass:
    pass


obj = MyClass()

number_info = introspection_info(42)
pprint(number_info)

