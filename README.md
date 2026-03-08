# `state-tuple-value-object`

A simple Python base class for immutable objects whose value is determined by a state tuple.

## Features

- **Equality (`==`)** via `__eq__` 
- **Hashing** via `__hash__` for use in sets and as dictionary keys
- **Pickle support** via `__reduce__`
- **Readable representation** via `__repr__` for easier debugging
- Compatible with **Python 2+**
- Less dynamic features than `attrs` or `dataclasses`

## Usage

1. Inherit from `StateTupleValueObject`
2. Implement `get_state_tuple(self)` to return the state as a tuple
3. Benefit from automated equality, hashing, pickling, and representation

```python
from state_tuple_value_object import StateTupleValueObject


class Point(StateTupleValueObject):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_state_tuple(self):
        return (self.x, self.y)


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 == p2)  # True
print(hash(p1) == hash(p2))  # True
print(p1)        # Point(1, 2)
print(p1 == p3)  # False

my_set = {p1, p2, p3}
print(my_set)  # {Point(1, 2), Point(3, 4)}
```

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
