import matplotlib.pyplot as plt
import random
import math
import numpy as np
from scipy import integrate

# Triangulo de Sierpinski
class Exercise1(object):

    def __init__(self):
        pass

    def f1(self, x, y):
        return x / 2, y / 2

    def f2(self, x, y):
        return x / 2 + 0.5, y / 2

    def f3(self, x, y):
        return x / 2 + 0.25, y / 2 + 0.5

    def execute(self):
        x = random.random()
        y = random.random()
        p1 = 0.33
        p2 = 0.33
        #p3 = 1 - p1 - p2
        n = 100000
        plt.plot(x, y, 'k.')
        for _ in range(n):
            r = random.random()
            if r < p1:
                x, y = self.f1(x, y)
            elif r < p1 + p2:
                x, y = self.f2(x, y)
            else:
                x, y = self.f3(x, y)
            plt.plot(x, y, 'k.')
        plt.show()

# Creation of fractal
class Exercise2(object):

    def __init__(self):
        pass

    def f1(self, x, y):
        return (x*0.85 + y*0.04), (x*-0.04 + y*0.85 + 1.6)

    def f2(self, x, y):
        return (-0.15*x + 0.28*y), (x*0.26 + y*0.24 + 0.44)

    def f3(self, x, y):
        return (x*0.2 + y*-0.26), (x*0.23 + y*0.22 + 1.6)

    def f4(self, x, y):
        return (x*0 + y*0), (x*0 + y*0.16)

    def execute(self):
        x = random.random()
        y = random.random()
        p1 = 0.85
        p2 = 0.07
        p3 = 0.07
        #p4 = 1 - p1 - p2 - p3
        n = 100000
        plt.plot(x, y, 'k.')
        for _ in range(n):
            r = random.random()
            if r < p1:
                x, y = self.f1(x, y)
            elif r < p1 + p2:
                x, y = self.f2(x, y)
            elif r < p1 + p2 + p3:
                x, y = self.f3(x, y)
            else:
                x, y = self.f4(x, y)
            plt.plot(x, y, 'k.')
        plt.show()

class Exercise3(object):

    def __init__(self):
        pass

    def rng1(self, n):
        return (5**5) * ((n-1) % (2**35 - 1))

    def rng2(self, n):
        return (7**5) * ((n-1) % (2**31 - 1))

    def percentage_bar(self, actual, total, max_percentage, top, bottom):
        percentage = 100 * (actual / int(total))
        percentage_relative = 100 * (percentage / max_percentage)
        bar = '*' * int(percentage_relative) + '-' * int(100 - int(percentage_relative))
        print(f"\n{bottom} - {top} |{bar}| ({percentage:.2f}% = {actual})")

    def  mean(self, data):
        return sum(data) / len(data)

    def variance(self, data):
        mean = self.mean(data)
        return sum([(x - mean)**2 for x in data]) / len(data)

    def standard_deviation(self, data):
        return self.variance(data) ** 0.5

    def execute(self, rng):
        ns = [100, 5000, 100000]
        for n in ns:
            r = []
            for i in range(1, n+1):
                if rng == 1:
                    r.append(self.rng1(r[i-2] if i > 2 else 1))
                elif rng == 2:
                    r.append(self.rng2(r[i-2] if i > 2 else 1))
                else:
                    r.append(random.random())
            print(f"\nResultados para n = {n} del generador {rng}")
            # normalizando los valores
            if max(r) > 1:
                max_value = max(r)
                r = [x / max_value for x in r]
            # separando los valores en 10 bins (intervalos) entre 0 y 1
            between_ranges = [{ "bottom": bottom/10,
                                "top": top/10,
                                "values": [x for x in r if (bottom/10 <= x < top/10) or (top/10 == 1 and x == 1)]
                            } for bottom, top in zip(range(0, 10), range(1, 11))]
            # estadisticas de iteracion
            mean = self.mean(r)
            variance = self.variance(r)
            mean_percentages = [(100 * len(between_range["values"]) / int(n)) for between_range in between_ranges]
            print(f"Media de valores: {mean} - Desviación Estándar de valores: {self.standard_deviation(r)} - Desviación Estándar de Porcentajes: {self.standard_deviation(mean_percentages)}")
            # estadisticas de cada bin
            for between_range in between_ranges:
                count = len(between_range["values"])
                mean = self.mean(between_range["values"])
                min_value = min(between_range["values"])
                max_value = max(between_range["values"])
                self.percentage_bar(count, n, max(mean_percentages), between_range['bottom'], between_range['top'])
                print(f"μ={mean} - min={min_value} - max={max_value}")

# Aproximacion de integral con metodo de Monte Carlo
class Exercise4(object):

    def __init__(self):
        pass

    # Integral original
    def fo(self, x):
        return math.e**(-x**2)

    # Integral transformada a limites 0 y 1
    def ft(self, x):
        return (math.e**(-((x**2) / ((1-x)**2)))) / ((1 - x)**2)

    def execute(self):
        ns = [100, 10000, 100000]
        a = 0
        b = 1.8
        limit_x = 50
        for n in ns:
            print(f"\nResultado de la integral aproximada para para n = {n}")
            # para la funcion original
            x = np.random.uniform(-limit_x, limit_x, n)
            y = np.random.uniform(a, b, n)
            inside_points = []
            outside_points = []
            for i in range(n):
                if y[i] <= self.fo(x[i]):
                    inside_points.append((x[i], y[i]))
                else:
                    outside_points.append((x[i], y[i]))
            # graficando puntos
            plt.plot([x for x, y in outside_points], [y for x, y in outside_points], color='red', marker='.', linestyle='none')
            plt.plot([x for x, y in inside_points], [y for x, y in inside_points], color='blue', marker='.', linestyle='none')
            # graficando linea
            line = np.linspace(-limit_x, limit_x, 1000)
            plt.plot(line, self.fo(line), 'k-')
            # calculando integral
            integral = (b - a) * (limit_x * 2) * (len(inside_points) / n)
            print(f"Integral original: {integral}")
            plt.title(f"Integral original")
            plt.show()

            # Para la funcion transformada
            # puntos aleatorios
            x = np.random.uniform(-limit_x, limit_x, n)
            y = np.random.uniform(a, b, n)
            inside_points = []
            outside_points = []
            for i in range(n):
                if y[i] <= self.ft(x[i]):
                    inside_points.append((x[i], y[i]))
                else:
                    outside_points.append((x[i], y[i]))
            # graficando puntos
            plt.plot([x for x, y in outside_points], [y for x, y in outside_points], color='red', marker='.', linestyle='none')
            plt.plot([x for x, y in inside_points], [y for x, y in inside_points], color='blue', marker='.', linestyle='none')
            # graficando linea
            line = np.linspace(-limit_x, limit_x, 1000)
            plt.plot(line, self.ft(line), 'k-')
            # calculando integral
            integral = (b - a) * (limit_x) * (len(inside_points) / n)
            print(f"Integral transformada aproximada (x2): {integral * 2}")
            plt.title(f"Integral transformada")
            plt.show()

# Aproximacion de integral con metodo de Monte Carlo
class Exercise5(object):

    def __init__(self):
        pass

    def f1o(self, x):
        return 1-math.e**(-2*x)

    def f2o(self, x):
        return math.e**(-x)

    def ft(self, u, v):
        return (math.e**-((u/(1-u)) + (v/(1-v)))) / (((1-u)**2) * ((1-v)**2))

    def execute(self):
        ns = [100, 10000, 100000]
        a = 0
        b = 0.25
        limit_x = 10
        for n in ns:
            print(f"\nResultado de la integral aproximada para para n = {n}")
            # puntos aleatorios
            x = np.random.uniform(0, limit_x, n)
            y = np.random.uniform(a, b, n)
            inside_points = []
            outside_points = []
            for i in range(n):
                if y[i] <= self.f1o(x[i]) + self.f2o(x[i]) - 1:
                    inside_points.append((x[i], y[i]))
                else:
                    outside_points.append((x[i], y[i]))
            # graficando puntos
            plt.plot([x for x, y in outside_points], [y for x, y in outside_points], color='red', marker='.', linestyle='none')
            plt.plot([x for x, y in inside_points], [y for x, y in inside_points], color='blue', marker='.', linestyle='none')
            # graficando linea
            line = np.linspace(0, limit_x, 1000)
            plt.plot(line, self.f2o(line) + self.f1o(line) - 1, 'k-')
            plt.show()
            # calculando integral
            integral = (b - a) * (limit_x) * (len(inside_points) / n)
            print(f"Integral aproximada: {integral}")


exercise1 = Exercise1()
exercise2 = Exercise2()
exercise3 = Exercise3()
exercise4 = Exercise4()
exercise5 = Exercise5()
#exercise1.execute()
#exercise2.execute()
#exercise3.execute(2)
#exercise4.execute()
exercise5.execute()