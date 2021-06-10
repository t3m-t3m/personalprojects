class Conclusion:
    _weight = 0

    def __init__(self, variable, term, weight, confidence_coefficient=1):
        self._variable = variable
        self._term = term
        self._weight = weight
        self._confidence_coefficient = confidence_coefficient

    @property
    def variable(self):
        return self._variable

    @property
    def term(self):
        return self._term

    @property
    def weight(self):
        return self._weight

    def get_activised_weight(self):
        return self._weight * self._confidence_coefficient
