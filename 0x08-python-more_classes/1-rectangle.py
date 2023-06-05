class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle. Defaults to 0.
            height (int): The height of the new rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return (
            "{'_Rectangle__height': " + str(self.__height) +
            ", '_Rectangle__width': " + str(self.__width) + "}"
        )


my_rectangle = Rectangle(2, 4)
print(my_rectangle)  # Output: {'_Rec__he': 4, '_Rec__width': 2}

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)  # Output: {'_Rec__height': 3, '_Rec__width': 10}
