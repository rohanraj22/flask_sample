from base_class import BaseClass

class DerivedClass(BaseClass):
    def __int__(self):
        print('derived class constructor')
    
    def process(self):
        print('derived class process')

    def derived_method(self):
        print('derived only method')