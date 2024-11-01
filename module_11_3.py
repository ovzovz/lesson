from inspect import getmodule

class MyClass():
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def method_1(self):
        pass

    def method_2(self):
        pass

def introspection_info(obj):
    info={}
    info['type'] = type(obj)
    info['attributes']= [attr_name for attr_name
                  in dir(obj) if not 'method' in str(getattr(obj, attr_name))]
        #{attr_name: getattr(obj, attr_name) for attr_name in dir(obj) if not 'method' in str(getattr(obj, attr_name))}
    info['methods'] = [attr_name for attr_name
                  in dir(obj) if 'method' in str(getattr(obj, attr_name))]
    info['module'] = getmodule(obj)
    return info

number_info = introspection_info(42)
print(number_info)

example = MyClass(2345,'abc')
print(introspection_info(example))

