from my_class import MyClass
from my_class2 import MyClass2
from base_class import BaseClass
from derived_class import DerivedClass

if __name__ == '__main__':
    
    # simple class object and call
    obj = MyClass()
    obj.print_text('sample class')
    print('-'*100)
    # class with properties and overloaded method
    obj2 = MyClass2()
    # normal method call
    obj2.process(10,'green')
    # overload call
    obj2.proces()
    print('-'*100)
    # inheritance
    child_obj = DerivedClass()
    child_obj.process()
    child_obj.base_method()
    child_obj.derived_method()