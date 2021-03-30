class MyClass2:

    colour = 'red'
    count = 10    

    def __init__(self):
        print('constructor')
        print('colour : ' + self.colour)
        print('count : ' + str(self.count))
    
    # overload
    def proces(self):
        print('this is the overload')
        print('colour : ' + self.colour)
        print('count : ' + str(self.count))

    def process(self,number,color):
        number = int(number)
        # local method call
        self.process_colour(color)
        # update the local property
        self.count +=  int(number)
        print('processing complete')


    
    def process_colour(self,color):
        self.colour = color
        print('process_colour complete')
