from Variable import Variable


class SugenoAlgorithm:
    def __init__(self, rules):
        self._rules = list()
        for rule in rules:
            self._rules.append(rule)

    @property
    def variable(self):
        return self._variable

    def classify(self, x):
        self._fuz_agg_acc_defuz(x)
        return self._z0

    def _fuz_agg_acc_defuz(self, x):
        self._variable = x
        alphas = list()
        conclusions = list()
        # self._default_conclusions = list()
        self._default_conclusions = dict()
        for rule in self._rules:
            temp_condition = rule.condition_temp
            hum_condition = rule.condition_hum
            # self._default_conclusions.append(rule.return_conclusion(x))
            conclusion = rule.return_conclusion(x)
            self._default_conclusions[conclusion.term] = conclusion.weight
            if temp_condition.get_weight(x.temperature) < hum_condition.get_weight(x.humidity):
                alphas.append(temp_condition.get_weight(x.temperature))
                conclusions.append(alphas[-1] * x.temperature +
                                   x.humidity)
            else:
                alphas.append(temp_condition.get_weight(x.humidity))
                conclusions.append(x.temperature +
                                   alphas[-1] * x.humidity)
        self._z0 = sum([0.2 * conclusions[i] for i in range(len(alphas))]) / sum(alphas)
        # self._z0 = sum([0.20 * conclusions[i] for i in range(len(alphas))]) / sum(alphas)
        # self._P = sum([alphas[i] * conclusions[i] for i in range(len(alphas))]) / sum(conclusions)
        # print(self._z0)

    @property
    def default_conclusions(self):
        return self._default_conclusions

    @property
    def z0(self):
        return self._z0

    @property
    def P(self):
        return self._P
