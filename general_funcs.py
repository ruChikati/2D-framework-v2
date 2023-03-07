
import json
import math

import pygame


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


def write_json(path, data, indent=1):
    with open(path, 'x') as f:
        f.write(json.dumps(data, indent=indent))


def read_json(path):
    with open(path, 'r') as f:
        data = f.read()
    data = json.loads(data)
    return data


def sum_list(list_: list, sort=True) -> list:
    """:returns: sub-sums of a given list of numbers"""
    return_list = []
    for i in range(len(list_)):
        return_list.append(sum(list_[:i + 1]))
    if sort:
        return_list.sort()
    return return_list


def string_of_(var):
    """:returns: string of the name of the given variable"""
    return f'{var=}'.split('=')[0]


def get_key(val, dict: dict):
    """:returns: the corresponding key to a given value in O(n) time, else None"""
    for key, value in dict.items():
        if val == value:
            return key
    return


def unique_vals(obj):
    """Removes duplicates of any type from a list in O(n^2)"""
    for val in obj:
        if obj.count(val) > 1:
            first_i = obj.index(val)
            while True:
                try:
                    del obj[obj.index(val)]
                except ValueError:
                    obj.insert(first_i, val)
                    break
    return obj


def single_true(iterable):
    """Checks if an iterable has "exactly one True element in it"""
    iterator = iter(iterable)
    has_true = any(iterator)
    has_another_true = any(iterator)
    return has_true and not has_another_true


def prime_generator(end):
    for n in range(2, end):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            yield n


def is_prime(n):
    if n <= 3:
        return n > 1
    if not (n % 2 and n % 3):
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def swap_colour(surf, old_colour, new_colour):
    """Swaps one colour for a new one on a pygame.Surface"""
    surf = surf.copy()
    surf.set_colorkey(old_colour)
    swap_surf = pygame.Surface(surf.get_width(), surf.get_height())
    swap_surf.fill(new_colour)
    swap_surf.blit(surf, (0, 0))
    return swap_surf


def colored_text(r, g, b, text):
    return f'\033[38;2;{r};{g};{b}m{text} \033[38;2;255;255;255m'


def centre_blit(source, surf, dest=(0, 0)):
    """Blits the centre of source onte surf at dest"""
    surf.blit(source, (dest[0] - source.get_width() // 2, dest[1] - source.get_height() // 2))


def centre_of_rect(rect):
    return rect.x + rect.w // 2, rect.y + rect.h // 2


def normalize(num, val):
    if num > val:
        num -= val
    elif num < val:
        num += val
    elif num == val:
        num = 0
    return num


def normalize_list(lst):
    """Normalizes all values in a list"""
    minimum, maximum = min(lst), max(lst)
    for i, val in enumerate(lst):
        if maximum - minimum:
            lst[i] = (val - minimum) / (maximum - minimum)
        else:
            lst[i] = val - minimum
    return lst


def sum_of_lists(big_list):
    return_list = []
    for small_list in big_list:
        return_list += small_list
    return return_list


def gcd(a, b):
    while b:
        a, b = b, a % b
    return max(a, -a)


def lcm(a, b):
    return a * b // gcd(a, b)


def angle2(point1, point2):
    """:returns: angle made between the line passing through point1 and point2 and the x-axis, in radians"""
    if not point2[0] - point1[0]:
        return 0
    return math.atan2((point2[1] - point1[1]), (point2[0] - point1[0]))


def magnitude(point):
    """:returns: the magnitude of an n-dimensional point"""
    return sum(val ** 2 for val in point) ** 0.5


def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


def clip(surf, x, y, w, h):
    handle_surf = surf.copy()
    handle_surf.set_clip(pygame.Rect(x, y, w, h))
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def clip_rect(surf, rect):
    handle_surf = surf.copy()
    handle_surf.set_clip(rect)
    image = surf.subsurface(handle_surf.get_clip())
    return image.copy()


def two_point_rect(point1, point2):
    return pygame.Rect(min(point1[0], point2[0]), min(point1[1], point2[1]), max(point1[0], point2[0]) - min(point1[0], point2[0]), max(point1[1], point2[1]) - min(point1[1], point2[1]))


class Vector2:

    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1:
            if not isinstance(args[0], (tuple, list)):
                raise IndexError('Vector2s take 2 int/floats or a list/tuple')
            self.x, self.y = args[0]
        else:
            raise IndexError('Vector2s take 2 int/floats or a list/tuple')

    def __add__(self, other):
        if isinstance(other, (list, tuple)) and len(other) == 2:
            return Vector2(other[0] + self.x, other[1] + self.y)
        elif isinstance(other, Vector2):
            return Vector2(other.x + self.x, other.y + self.y)
        else:
            raise TypeError('Only lists, tuples (of length 2) and Vector2s can be added to a Vector2')

    def __sub__(self, other):
        if isinstance(other, (list, tuple)) and len(other) == 2:
            return Vector2(other[0] - self.x, other[1] - self.y)
        elif isinstance(other, Vector2):
            return Vector2(other.x - self.x, other.y - self.y)
        else:
            raise TypeError('Only lists, tuples (of length 2) and Vector2s can be subtracted from a Vector2')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        elif isinstance(other, (list, tuple)) and len(other) == 2:
            return self.x * other[0] + self.y * other[1]
        elif isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError('Vector2 can only be multiplied by lists, tuples (of length 2), int, floats and Vector2s')

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        elif isinstance(other, (list, tuple)) and len(other) == 2:
            return self.x / other[0] + self.y / other[1]
        elif isinstance(other, Vector2):
            return self.x / other.x + self.y / other.y
        else:
            raise TypeError('Vector2 can only be divided by lists, tuples (of length 2), int, floats and Vector2s')

    def __getitem__(self, item):
        if -1 < item < 2:
            return self.y if item else self.x
        else:
            raise IndexError('Vector2 index out of range: 0 or 1, index is ' + str(item))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > 1 or self.n < 0:
            raise StopIteration
        self.n += 1
        return self.y if self.n else self.x

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return True if self.x and self.y else False

    def __eq__(self, other):
        if isinstance(other, (list, tuple)) and len(other) == 2:
            return (self.x, self.y) == (other[0], other[1])
        elif isinstance(other, Vector2):
            return (self.x, self.y) == (other.x, other.y)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Vector2):
            return abs(self) > abs(other)
        if len(other) == 2:
            return self.magnitude() > magnitude(other)
        else:
            raise TypeError('Cannot compare Vector2 with type ', type(other), ' of length ', len(other))

    def __ge__(self, other):
        if isinstance(other, Vector2):
            return abs(self) >= abs(other)
        if len(other) == 2:
            return self.magnitude() >= magnitude(other)
        else:
            raise TypeError('Cannot compare Vector2 with type ', type(other), ' of length ', len(other))

    def __lt__(self, other):
        if isinstance(other, Vector2):
            return abs(self) < abs(other)
        if len(other) == 2:
            return self.magnitude() < magnitude(other)
        else:
            raise TypeError('Cannot compare Vector2 with type ', type(other), ' of length ', len(other))

    def __le__(self, other):
        if isinstance(other, Vector2):
            return abs(self) <= abs(other)
        if len(other) == 2:
            return self.magnitude() <= magnitude(other)
        else:
            raise TypeError('Cannot compare Vector2 with type ', type(other), ' of length ', len(other))

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __invert__(self):
        return Vector2(self.y, self.x)

    def __str__(self):
        return f'{self.x},{self.y}'

    def __repr__(self):
        return f'Vector2(x: {self.x}, y: {self.y})'

    def __contains__(self, item):
        return item in (self.x, self.y)

    def __len__(self):
        return self.magnitude()

    def magnitude(self):
        return abs(self)

    def normalized(self):
        return Vector2(normalize_list([self.x, self.y]))

    def cross(self, vec):
        if isinstance(vec, (list, tuple)):
            if len(vec) == 2:
                return self.x * vec[1] - self.y * vec[0]
            else:
                raise TypeError('can only cross with a Vector2')
        if isinstance(vec, Vector2):
            return self.x * vec.y - self.y * vec.x
        else:
            raise TypeError('can only cross with a Vector2 or a list/tuple')


I2 = Vector2(1, 0)
J2 = Vector2(0, 1)


class Vector3:

    def __init__(self, *args):
        if len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        elif len(args) == 1:
            if not isinstance(args[0], (tuple, list)):
                raise IndexError('Vector3s take 3 int/floats or a list/tuple')
            self.x, self.y, self.z = args[0]
        else:
            raise IndexError('Vector3s take 3 int/floats or a list/tuple')

    def __add__(self, other):
        if isinstance(other, (list, tuple)) and len(other) == 3:
            return Vector3(other[0] + self.x, other[1] + self.y, other[2] + self.z)
        elif isinstance(other, Vector3):
            return Vector3(other.x + self.x, other.y + self.y, other.z + self.z)
        else:
            raise TypeError('Only lists, tuples (of length 3) and Vector3s can be added to a Vector3')

    def __sub__(self, other):
        if isinstance(other, (list, tuple)) and len(other) == 3:
            return Vector3(other[0] + self.x, other[1] + self.y, other[2] + self.z)
        elif isinstance(other, Vector3):
            return Vector3(other.x - self.x, other.y - self.y, other.z + self.z)
        else:
            raise TypeError('Only lists, tuples (of length 3) and Vector3s can be subtracted from a Vector3')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, (list, tuple)) and len(other) == 3:
            return self.x * other[0] + self.y * other[1] + self.z * other[2]
        elif isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError('Vector3 can only be multiplied by lists, tuples (of length 3), int, floats and Vector2s')

    def __getitem__(self, item):
        if -1 < item < 3:
            if item == 0:
                return self.x
            elif item == 1:
                return self.y
            elif item == 2:
                return self.z
        else:
            raise IndexError('Vector3s only have x, y, z attributes, index is ' + str(item))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > 2 or self.n < 0:
            raise StopIteration
        if self.n == 0:
            self.n += 1
            return self.x
        elif self.n == 1:
            self.n += 1
            return self.y
        elif self.n == 2:
            self.n += 1
            return self.z

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __bool__(self):
        return True if self.x and self.y and self.z else False

    def __eq__(self, other):
        if isinstance(other, (list, tuple)) and len(other) == 3:
            return (self.x, self.y, self.z) == (other[0], other[1], other[2])
        elif isinstance(other, Vector3):
            return (self.x, self.y, self.z) == (other.x, other.y, other.z)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Vector3):
            return abs(self) > abs(other)
        if len(other) == 3:
            return self.magnitude() > magnitude(other)
        else:
            raise TypeError('Cannot compare Vector3 with type ', type(other), ' of length ', len(other))

    def __ge__(self, other):
        if isinstance(other, Vector3):
            return abs(self) >= abs(other)
        if len(other) == 3:
            return self.magnitude() >= magnitude(other)
        else:
            raise TypeError('Cannot compare Vector3 with type ', type(other), ' of length ', len(other))

    def __lt__(self, other):
        if isinstance(other, Vector3):
            return abs(self) < abs(other)
        if len(other) == 3:
            return self.magnitude() < magnitude(other)
        else:
            raise TypeError('Cannot compare Vector3 with type ', type(other), ' of length ', len(other))

    def __le__(self, other):
        if isinstance(other, Vector3):
            return abs(self) <= abs(other)
        if len(other) == 3:
            return self.magnitude() <= magnitude(other)
        else:
            raise TypeError('Cannot compare Vector3 with type ', type(other), ' of length ', len(other))

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __str__(self):
        return f'{self.x},{self.y},{self.z}'

    def __repr__(self):
        return f'Vector3(x: {self.x}, y: {self.y}, z: {self.z})'

    def __contains__(self, item):
        return item in self.x, self.y, self.z

    def __len__(self):
        return abs(self)

    def cross(self, vec):
        if isinstance(vec, (list, tuple)):
            if len(vec) == 3:
                return Vector3(self.y * vec[2] - self.z * vec[1], self.z * vec[0] - self.x * vec[2], self.x * vec[1] - self.x * vec[0])
            else:
                raise TypeError('can only cross with a Vector3')
        if isinstance(vec, Vector3):
            return Vector3(self.y * vec.z - self.z * vec.y, self.z * vec.x - self.x * vec.z, self.x * vec.y - self.y * vec.x)
        else:
            raise TypeError('can only cross with a Vector3 or a list/tuple')

    def magnitude(self):
        return abs(self)

    def normalized(self):
        return normalize_list([self.x, self.y, self.z])


I3 = Vector3(1, 0, 0)
J3 = Vector3(0, 1, 0)
K3 = Vector3(0, 0, 1)
