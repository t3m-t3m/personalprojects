import matplotlib.pyplot as plt
import numpy as np
import rules
import csv


from Variable import Variable
from MamdaniAlgorithm import MamdaniAlgorithm
from SugenoAlgorithm import SugenoAlgorithm


def main():

    mode = 4
    t = -30 # -4
    h = 0  # 21
    if mode == 1:
        # Графики для температуры
        x = list(range(-30, 31))
        y = list()
        for condition in rules.temp_conditions:
            y.append([])
            for variable in x:
                y[-1].append(condition.get_weight(variable))

        plt.subplot(1, 3, 1)
        plt.title('Температура')
        plt.xlabel('Temperature, t')
        plt.ylabel('P')
        plt.grid()
        plt.plot(x, y[0], 'b')
        plt.plot(x, y[1], 'g')
        plt.plot(x, y[2], 'r')

        # Графики для влажности
        x = list(range(0, 101))
        y = list()
        for condition in rules.hum_conditions:
            y.append([])
            for variable in x:
                y[-1].append(condition.get_weight(variable))

        plt.subplot(1, 3, 2)
        plt.title('Влажность')
        plt.xlabel('Humidity, %')
        plt.ylabel('P')
        plt.grid()
        plt.plot(x, y[0], 'y')
        plt.plot(x, y[1], 'g')
        plt.plot(x, y[2], 'r')

        # Графики для описания погоды
        y = list()
        for condition in rules.desc_conditions:
            y.append([])
            for variable in x:
                y[-1].append(condition.get_weight(variable))

        colors = [
            'black',
            'red',
            'orange',
            'yellow',
            'green',
            'lightseagreen',
            'aqua',
            'dodgerblue',
            'blue',
            'violet',
            'purple',
            'lightpink',
        ]

        plt.subplot(1, 3, 3)
        plt.title('Описания погоды')
        plt.xlabel('Number of people, N')
        plt.ylabel('P')
        plt.grid()
        i = 0
        for var_list in y:
            plt.plot(x, var_list, colors[i])
            i += 1

        plt.show()

    elif mode == 2:
        mamdani_alg = MamdaniAlgorithm(rules.rules)
        var = Variable(t, h)
        mamdani_alg.classify(var)

        x = list(range(0, 101))
        result = mamdani_alg.variable.result
        P = mamdani_alg.variable.P
        answer = max(var.terms_dict, key=var.terms_dict.get)

        plt.title(f'Mamdani: {answer} погода\n'
                  f'({result}: {P})')
        plt.xlabel('N')
        plt.ylabel('P')
        plt.grid()

        for term, weight in var.terms_dict.items():
            if weight > 0:
                y = list()
                for condition in rules.desc_conditions:
                    if condition.term == term:
                        for element in x:
                            y.append(min(weight, condition.get_weight(element)))
                        plt.plot(x, y, color='red', linestyle='--', linewidth=1)

        y = list()
        for element in x:
            y.append(mamdani_alg.get_max_value(element))
        plt.plot(x, y, color='b', linewidth=2)
        plt.axvline(x=result, color='r', linewidth=2)
        plt.show()

    elif mode == 3:
        sugeno_alg = SugenoAlgorithm(rules.rules)
        var = Variable(t, h)
        sugeno_alg.classify(var)

        plt.title('Sugeno:')
        plt.xlabel('N')
        plt.ylabel('P')
        plt.grid()

        x = list(range(0, 101))
        for conclusion in sugeno_alg.default_conclusions:
            if conclusion.weight > 0:
                print(conclusion.term, conclusion.weight)
                for condition in rules.desc_conditions:
                    if conclusion.term == condition.term:
                        y = list()
                        for element in x:
                            y.append(min(conclusion.weight, condition.get_weight(element)))
                        plt.plot(x, y, color='red', linestyle='--', linewidth=1)

        plt.axvline(x=sugeno_alg.z0, color='r', linewidth=2)
        plt.show()

    elif mode == 4:  # Mamdani results csv
        with open('res/mamdani_results.csv', 'w', newline='') as csvfile:
            temperature = list()
            humidity = list()
            N = list()
            result = list()
            fieldnames = ['temperature', 'humidity', 'number of people', 'result']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for t in range(-30, 30, 1):
                for h in range(0, 101, 5):
                    var = Variable(t, h)
                    temperature.append(t)
                    humidity.append(h)
                    mamdani_alg = MamdaniAlgorithm(rules.rules)
                    N.append(round(mamdani_alg.classify(var), 2))
                    result.append(max(mamdani_alg.fuzzy_sets, key=mamdani_alg.fuzzy_sets.get))
                    writer.writerow({'temperature': t,
                                     'humidity': h,
                                     'number of people': N[-1],
                                     'result': result[-1]})
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.set_title('Mamdani scatter results')
            ax.plot_trisurf(np.array(temperature), np.array(humidity), np.array(N))
            plt.show()

    elif mode == 5:  # Sugeno results csv
        with open('res/sugeno_results.csv', 'w', newline='') as csvfile:
            temperature = list()
            humidity = list()
            N = list()
            result = list()
            fieldnames = ['temperature', 'humidity', 'number of people', 'result']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for t in range(-30, 30, 1):
                for h in range(0, 101, 5):
                    var = Variable(t, h)
                    sugeno_alg = SugenoAlgorithm(rules.rules)
                    temperature.append(t)
                    humidity.append(h)
                    N.append(round(sugeno_alg.classify(var), 2))
                    result.append(max(sugeno_alg.default_conclusions, key=sugeno_alg.default_conclusions.get))
                    writer.writerow({'temperature': t,
                                     'humidity': h,
                                     'number of people': N,
                                     'result': result})

            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.set_title('Sugeno scatter results')
            ax.plot_trisurf(np.array(temperature), np.array(humidity), np.array(N))
            plt.show()


if __name__ == '__main__':
    main()
