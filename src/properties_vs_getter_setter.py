from datetime import date

'''
https://realpython.com/python-getter-setter/
usage of properties in python:
    Use public attributes whenever appropriate, even if you expect the attribute to require functional behavior in the 
        future.
    Avoid defining setter and getter methods for your attributes. You can always turn them into properties if needed.
    Use properties when you need to attach behavior to attributes and keep using them as regular attributes in your code.
    Avoid side effects in properties because no one would expect operations like assignments to cause any side effects.
        make sure that the methods behind the property are fast and don’t cause side effects

!Only use properties when you need to add extra processing on top of a specific attribute!

A property is a special type of descriptor. However, regular descriptors are more powerful than properties and can be 
reused through different classes.

getter and setter methods may be better suited to deal with situations in which you need to:
    Run costly transformations on attribute access or mutation
    Take extra arguments and flags
    Use inheritance
    Raise exceptions related to attribute access and mutation
    Facilitate integration in heterogeneous development teams
'''


class Date:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = date.fromisoformat(value)


class Employee:
    birth_date = Date()
    start_date = Date()

    def __init__(self, name, birth_date, start_date):
        self.name = name
        self.birth_date = birth_date
        self.start_date = start_date

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.upper()


#The .__setattr__() and .__getattr__() methods
class Point:
    """
    Note that Point allows you to access the coordinates as public attributes.
    However, it stores them as non-public attributes. You can confirm this behavior with the built-in dir() function.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, name: str):
        """
        returns the coordinate represented by 'name'
        attribute’s final name will have an underscore preceding whatever you pass in name
        Python automatically calls .__getattr__() whenever you access an attribute of Point using the dot notation
        """
        return self.__dict__[f"_{name}"]

    def __setattr__(self, name, value):
        """
        adds or updates attributes
        Python calls .__setattr__() whenever you run an assignment operation on any attribute of the containing class
        """
        self.__dict__[f"_{name}"] = float(value)


#classical getter & setter
class Label:
    def __init__(self, text, font):
        self.set_text(text)
        self.font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value.upper()  # Attached behavior


def main():
    user = Employee("John", "2001-02-07", "2012-02-07")
    print("getting")
    print(user.name)
    print(user.birth_date)
    print("setting")
    user.name = "John Doe"
    print(user.name)
    #
    point = Point(21, 42)
    print(point.x)
    point.x = 84
    print(point.x)
    print(dir(point))#
    #
    label = Label("Fruits", "JetBrains Mono NL")
    print(label.get_text())
    label.set_text("Vegetables")
    print(label.get_text())


if __name__ == "__main__":
    main()