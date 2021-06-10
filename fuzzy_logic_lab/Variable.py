class Variable:
    _temperature = 0.0
    _humidity = 0
    terms_dict = dict()

    def __init__(self, temperature, humidity):
        self._temperature = temperature
        self._humidity = humidity

    def set_result(self, result, P):
        self._result = result
        self._P = P

    @property
    def result(self):
        return self._result

    @property
    def P(self):
        return self._P

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity
