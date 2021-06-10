from scipy import integrate


from Variable import Variable
from rules import desc_conditions


class MamdaniAlgorithm:
    def __init__(self, rules):
        self._rules = list()
        for rule in rules:
            self._rules.append(rule)

    @property
    def variable(self):
        return self._variable

    def classify(self, x):
        self._fuzzification_aggregation_activisation(x)
        self._accumulation()
        result = self._defuzzification()
        P = self.get_max_value(result)
        self._variable.set_result(result, P)
        # print(result, ': ', P)
        # print(self._fuzzy_sets)
        return result

    def _fuzzification_aggregation_activisation(self, x):
        self._variable = x
        conclusions = list()
        for rule in self._rules:
            conclusions.append(rule.return_conclusion(x))
        for conclusion in conclusions:
            self._variable.terms_dict[conclusion.term] = \
                conclusion.get_activised_weight()

    def _accumulation(self):
        self._fuzzy_sets = dict()
        for term_name, term_weight in self._variable.terms_dict.items():
            if term_weight > 0:
                self._fuzzy_sets[term_name] = term_weight

    def _get_max_value_multi(self, x):
        result = 0.0
        for term, weight in self._fuzzy_sets.items():
            current_condition = None
            for condition in desc_conditions:
                if condition.term == term:
                    current_condition = condition
            result = max(result, min(current_condition.get_weight(x), weight))
        return result * x

    def get_max_value(self, x):
        result = 0.0
        for term, weight in self._fuzzy_sets.items():
            current_condition = None
            for condition in desc_conditions:
                if condition.term == term:
                    current_condition = condition
            result = max(result, min(current_condition.get_weight(x), weight))
        return result

    def _defuzzification(self):
        result = integrate.quad(self._get_max_value_multi, 0, 100)[0] / \
                 integrate.quad(self.get_max_value, 0, 100)[0]
        return result

    @property
    def fuzzy_sets(self):
        return self._fuzzy_sets
