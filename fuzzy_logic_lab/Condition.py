class Condition:
    def __init__(self, term, a, b, c=None, d=None, f_type=None):
        self._term = term
        self._a, self._b, self._c, self._d = a, b, c, d
        self._f_type = f_type

    @property
    def term(self):
        return self._term

    def get_constants(self):
        return self._a, self._b, self._c, self._d

    def get_weight(self, x):
        if self._c is not None and self._d is not None:
            return max(min((x - self._a)/(self._b - self._a),
                           1,
                           (self._d - x)/(self._d - self._c)),
                       0)
        elif self._f_type == 'lup':
            return max(min((x - self._a)/(self._b - self._a), 1), 0)
        elif self._f_type == 'ldown':
            return max(min((self._b - x) / (self._b - self._a), 1), 0)
