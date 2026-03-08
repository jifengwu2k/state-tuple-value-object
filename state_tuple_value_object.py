# Copyright (c) 2026 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
class StateTupleValueObject(object):
    def __eq__(self, other):
        return (
            isinstance(other, type(self))
            and self.get_state_tuple() == other.get_state_tuple()
        )

    def __hash__(self):
        return hash(self.get_state_tuple())

    def __reduce__(self):
        return type(self), self.get_state_tuple()

    def __repr__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join(map(repr, self.get_state_tuple()))
        )
    
    def get_state_tuple(self):
        raise NotImplementedError




