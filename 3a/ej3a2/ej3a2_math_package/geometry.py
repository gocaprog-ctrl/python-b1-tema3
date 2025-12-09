# geometry.py


def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    area_square = side_length**2
    return area_square
    pass


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    area_rectangle = base_length * height
    return area_rectangle
    pass


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    area_triangle = (base_length*height)/2
    return area_triangle
    pass


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    pi = 3.14
    area_circle = pi*radius**2
    return area_circle
    pass
