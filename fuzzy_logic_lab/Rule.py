from Condition import Condition
from Conclusion import Conclusion


class Rule:

    _condition_temp = Condition
    _condition_hum = Condition
    _term = ''

    def __init__(self, condition_temp, condition_hum, term):
        self._condition_temp = condition_temp
        self._condition_hum = condition_hum
        self._term = term

    @property
    def condition_temp(self):
        return self._condition_temp

    @property
    def condition_hum(self):
        return self._condition_hum

    def return_conclusion(self, x):
        weight = min(self._condition_temp.get_weight(x.temperature),
                     self._condition_hum.get_weight(x.humidity))
        return Conclusion(x, self._term, weight)
