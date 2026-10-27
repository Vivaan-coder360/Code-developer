import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @staticmethod
    def _validate_dimensions(**dimensions):
        for dimension_name, value in dimensions.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(f"{dimension_name} must be a number")
            if not math.isfinite(value) or value <= 0:
                raise ValueError(f"{dimension_name} must be a positive finite number")

    @abstractmethod
    def calculate_measurements(self):
        raise NotImplementedError

    def draw(self):
        print(self.name)


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self._validate_dimensions(side=side)
        self.side = side

    def calculate_area(self):
        return self.side ** 2

    def calculate_perimeter(self):
        return 4 * self.side

    def calculate_measurements(self):
        return {
            "area": self.calculate_area(),
            "perimeter": self.calculate_perimeter(),
        }


class Circle(Shape):
    def __init__(self, name, diameter):
        super().__init__(name)
        self._validate_dimensions(diameter=diameter)
        self.diameter = diameter

    def calculate_circumference(self):
        return math.pi * self.diameter

    def calculate_area(self):
        return math.pi * self.diameter ** 2 / 4

    def calculate_measurements(self):
        return {
            "area": self.calculate_area(),
            "circumference": self.calculate_circumference(),
        }


class Triangle(Shape):
    def __init__(self, name, base, height, side_a, side_b):
        super().__init__(name)
        self._validate_dimensions(
            base=base,
            height=height,
            side_a=side_a,
            side_b=side_b,
        )
        if (
            side_a + side_b <= base
            or side_a + base <= side_b
            or side_b + base <= side_a
        ):
            raise ValueError("The three side lengths must form a valid triangle")

        semiperimeter = (base + side_a + side_b) / 2
        heron_area = math.sqrt(
            semiperimeter
            * (semiperimeter - base)
            * (semiperimeter - side_a)
            * (semiperimeter - side_b)
        )
        if not math.isclose(
            base * height / 2,
            heron_area,
            rel_tol=1e-9,
            abs_tol=1e-9,
        ):
            raise ValueError("height must match the supplied triangle side lengths")

        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b

    def calculate_perimeter(self):
        return self.base + self.side_a + self.side_b

    def calculate_area(self):
        return self.base * self.height / 2

    def calculate_measurements(self):
        return {
            "area": self.calculate_area(),
            "perimeter": self.calculate_perimeter(),
        }


class Cube(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self._validate_dimensions(side=side)
        self.side = side

    def calculate_surface_area(self):
        return 6 * self.side ** 2

    def calculate_volume(self):
        return self.side ** 3

    def calculate_measurements(self):
        return {
            "surface_area": self.calculate_surface_area(),
            "volume": self.calculate_volume(),
        }


class Sphere(Shape):
    def __init__(self, name, diameter):
        super().__init__(name)
        self._validate_dimensions(diameter=diameter)
        self.diameter = diameter

    def calculate_surface_area(self):
        return math.pi * self.diameter ** 2

    def calculate_volume(self):
        return math.pi * self.diameter ** 3 / 6

    def calculate_measurements(self):
        return {
            "surface_area": self.calculate_surface_area(),
            "volume": self.calculate_volume(),
        }


class Pyramid(Shape):
    def __init__(self, name, base_length, base_width, height):
        super().__init__(name)
        self._validate_dimensions(
            base_length=base_length,
            base_width=base_width,
            height=height,
        )
        self.base_length = base_length
        self.base_width = base_width
        self.height = height

    def calculate_volume(self):
        return self.base_length * self.base_width * self.height / 3

    def calculate_surface_area(self):
        length_slant_height = math.sqrt(
            self.height ** 2 + (self.base_width / 2) ** 2
        )
        width_slant_height = math.sqrt(
            self.height ** 2 + (self.base_length / 2) ** 2
        )
        base_area = self.base_length * self.base_width
        length_faces_area = 0.5 * self.base_length * length_slant_height
        width_faces_area = 0.5 * self.base_width * width_slant_height
        return base_area + length_faces_area + width_faces_area

    def calculate_measurements(self):
        return {
            "surface_area": self.calculate_surface_area(),
            "volume": self.calculate_volume(),
        }


class Cone(Shape):
    def __init__(self, name, diameter, height):
        super().__init__(name)
        self._validate_dimensions(diameter=diameter, height=height)
        self.diameter = diameter
        self.height = height

    def calculate_volume(self):
        return math.pi * self.diameter ** 2 * self.height / 12

    def calculate_surface_area(self):
        radius = self.diameter / 2
        slant_height = math.sqrt(radius ** 2 + self.height ** 2)
        return math.pi * radius * (radius + slant_height)

    def calculate_measurements(self):
        return {
            "surface_area": self.calculate_surface_area(),
            "volume": self.calculate_volume(),
        }


class ShapeCollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self):
        choice = input(
            "Choose a shape (square, circle, triangle, cube, sphere, pyramid, cone): "
        ).strip().lower()

        if not choice:
            print("No shape selected.")
            return

        if choice not in {
            "square",
            "circle",
            "triangle",
            "cube",
            "sphere",
            "pyramid",
            "cone",
        }:
            print("That shape isn't available.")
            return

        name = input("Shape name: ").strip()
        try:
            if choice == "square":
                side = float(input("Side length: "))
                shape = Square(name, side)
            elif choice == "circle":
                diameter = float(input("Diameter: "))
                shape = Circle(name, diameter)
            elif choice == "triangle":
                base = float(input("Base length: "))
                height = float(input("Height: "))
                side_a = float(input("First other side length: "))
                side_b = float(input("Second other side length: "))
                shape = Triangle(name, base, height, side_a, side_b)
            elif choice == "cube":
                side = float(input("Side length: "))
                shape = Cube(name, side)
            elif choice == "sphere":
                diameter = float(input("Diameter: "))
                shape = Sphere(name, diameter)
            elif choice == "pyramid":
                base_length = float(input("Base length: "))
                base_width = float(input("Base width: "))
                height = float(input("Enter height: "))
                shape = Pyramid(name, base_length, base_width, height)
            elif choice == "cone":
                diameter = float(input("Diameter: "))
                height = float(input("Height: "))
                shape = Cone(name, diameter, height)
        except (TypeError, ValueError) as error:
            print(f"Could not add shape: {error}")
            return

        self.shapes.append(shape)
        print(f"Added {shape.name}.")

    def list_shapes(self):
        if not self.shapes:
            print("There are no shapes yet.")
            return

        print("Available shapes:")
        for index, shape in enumerate(self.shapes, start=1):
            print(f"{index}. {shape.name} ({type(shape).__name__})")

    def choose_shape(self):
        if not self.shapes:
            print("There are no shapes yet.")
            return None

        self.list_shapes()
        try:
            number = int(input("Choose a shape number: "))
        except ValueError:
            print("Enter a valid number.")
            return None

        if number < 1 or number > len(self.shapes):
            print("That shape number doesn't exist.")
            return None

        return self.shapes[number - 1]

    def show_all_measurements(self):
        if not self.shapes:
            print("There are no shapes yet.")
            return

        for index, shape in enumerate(self.shapes, start=1):
            print(f"{index}. {shape.name}: {shape.calculate_measurements()}")

    def remove_shape(self):
        shape = self.choose_shape()
        if shape is None:
            return

        self.shapes.remove(shape)
        print(f"Removed {shape.name}.")

    def show_shape_measurements(self):
        shape = self.choose_shape()
        if shape is None:
            return
        print(shape.calculate_measurements())

    def draw_shape(self):
        shape = self.choose_shape()
        if shape is None:
            return
        shape.draw()

    def run_menu(self):
        while True:
            print("\n1. Add shape")
            print("2. List shapes")
            print("3. Show all measurements")
            print("4. Show shape measurements")
            print("5. Draw shape")
            print("6. Remove shape")
            print("7. Exit")

            action = input("Choose an action: ").strip()

            if action == "1":
                self.add_shape()
            elif action == "2":
                self.list_shapes()
            elif action == "3":
                self.show_all_measurements()
            elif action == "4":
                self.show_shape_measurements()
            elif action == "5":
                self.draw_shape()
            elif action == "6":
                self.remove_shape()
            elif action == "7":
                print("Goodbye!")
                break
            else:
                print("That action isn't available.")


if __name__ == "__main__":
    collection = ShapeCollection()
    collection.run_menu()
