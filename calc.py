from sympy import *

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.widgets import *



x_min = -10

x_max = 10

y_min = -10

y_max = 10

x = symbols("x")

formula = "x^2"

ftc_array = np.arange(-3, 5, 0.1)



def convert_func(formula):

    simplified = sympify(formula)

    return simplified



def convert_der(formula):

    simplified = sympify(formula)

    der = derive(1, simplified)

    return der



def convert_sec_der(formula):

    simplified = sympify(formula)

    sec_der = derive(2, simplified)

    return sec_der



def derive(degree, func):

    if degree == 0:

        return func

    func = (func.subs(x, x + 0.00001) - func) / 0.00001

    return derive(degree - 1, func)



def relative_extrema(xvals, func):

    der_func = derive(1, func)

    if der_func == 0:

        return []
    
    print(der_func)
    print(str(der_func))
    result = solveset(der_func, x, domain=Interval(x_min, x_max))

    if isinstance(result, ConditionSet):

        return []

    return result



def POI(xvals, func):

    der_func = derive(2, func)

    if der_func == 0:

        return []

    result = solveset(der_func, x, domain=Interval(x_min, x_max))

    if isinstance(result, ConditionSet):

        return []

    return result



def hole_get(formula):

    test = sympify(formula, evaluate=false)

    n, d = fraction(test)

    n_zeros = solveset(n, x, domain=Interval(x_min, x_max))

    d_zeros = solveset(d, x, domain=Interval(x_min, x_max))

    intersect_zeros = n_zeros.intersect(d_zeros)

    intersect_x = list(intersect_zeros)

    return intersect_x



def crit_get(simplified):

    crit_num = list(relative_extrema(xvals, simplified))



    final_crit = []



    for val in crit_num:

        below = der.subs(x, val - 0.00001)

        above = der.subs(x, val + 0.00001)

        if (below > 0 and above < 0):

            final_crit.append(val)

        elif (below < 0 and above > 0):

            final_crit.append(val)

        else:

            continue

    return final_crit



def POI_get(simplified):

    POI_num = list(POI(xvals, simplified))



    final_POI = []

    for val in POI_num:

        below = sec_der.subs(x, val - 0.00001)

        above = sec_der.subs(x, val + 0.00001)

        if (below > 0 and above < 0):

            final_POI.append(val)

        elif (below < 0 and above > 0):

            final_POI.append(val)

        else:

            continue

    return final_POI



def crit_graph(simplified):

    crit_y = []

    for val in final_crit:

        crit_y.append(simplified.subs(x, val))

    return crit_y



def POI_graph(simplified):

    POI_y = []

    for val in final_POI:

        POI_y.append(simplified.subs(x, val))

    return POI_y



def hole_graph(simplified):

    intersect_y = []

    for val in intersect_x:

        intersect_y.append(simplified.subs(x, val))

    return intersect_y



def func_graph(simplified):

    y = []

    for val in xvals:

        y.append(simplified.subs(x, val))

    return y



def der_graph(der):

    der_y = []

    for val in xvals:

        der_y.append(der.subs(x, val))

    return der_y



def sec_der_graph(sec_der):

    sec_der_y = []

    for val in xvals:

        sec_der_y.append(sec_der.subs(x, val))

    return sec_der_y



# Define function and range



test = sympify(formula, evaluate=false)

n, d = fraction(test)

n_zeros = solveset(n, x, domain=Interval(x_min, x_max))

d_zeros = solveset(d, x, domain=Interval(x_min, x_max))

intersect_zeros = n_zeros.intersect(d_zeros)

intersect_x = list(intersect_zeros)



converted = sympify(formula, evaluate=false)

simplified = sympify(formula)

lambda_simpl = lambdify(x, simplified, "numpy")



xvals = np.arange(x_min, x_max, 0.1)

yvals = lambda_simpl(ftc_array)



y = lambdify(x, simplified, "numpy")

der = derive(1, simplified)

sec_der = derive(2, simplified)

y_prime = lambdify(x, derive(1, simplified), "numpy")

y_doubleprime = lambdify(x, derive(2, simplified), "numpy")



crit_num = list(relative_extrema(xvals, simplified))



final_crit = []



for val in crit_num:

    below = der.subs(x, val - 0.00001)

    above = der.subs(x, val + 0.00001)

    if (below > 0 and above < 0):

        final_crit.append(val)

    elif (below < 0 and above > 0):

        final_crit.append(val)

    else:

        continue



POI_num = list(POI(xvals, simplified))



final_POI = []

for val in POI_num:

    below = sec_der.subs(x, val - 0.00001)

    above = sec_der.subs(x, val + 0.00001)

    if (below > 0 and above < 0):

        final_POI.append(val)

    elif (below < 0 and above > 0):

        final_POI.append(val)

    else:

        continue



crit_y = []

POI_y = []

intersect_y = []

for val in final_crit:

    crit_y.append(simplified.subs(x, val))

for val in final_POI:

    POI_y.append(simplified.subs(x, val))

for val in intersect_x:

    intersect_y.append(simplified.subs(x, val))



y = []

der_y = []

sec_der_y = []

for val in xvals:

    y.append(simplified.subs(x, val))

    der_y.append(der.subs(x, val))

    sec_der_y.append(sec_der.subs(x, val))



fig, axx = plt.subplots()



ax = plt.gca()

ax.spines['top'].set_color('none')

ax.spines['bottom'].set_position('zero')

ax.spines['left'].set_position('zero')

ax.spines['right'].set_color('none')



p1, = plt.plot(xvals, y, label='y', color='tab:blue', visible = False, zorder=0)

p2, = plt.plot(xvals, der_y, label='1st Deriv', color='crimson', visible = False, zorder=2)

p3, = plt.plot(xvals, sec_der_y, label='2nd Deriv', color='tab:green', visible = False, zorder=3)

p4 = plt.scatter(final_crit, crit_y, label='extrema', color='tab:orange', visible=False, zorder=4)

p5 = plt.scatter(final_POI, POI_y, label='POI', color='deeppink', visible = False, zorder=5)

p6 = plt.scatter(intersect_x, intersect_y, marker='$O$', label='holes', color='purple', visible = False, zorder=6)

p7 = plt.fill_between(ftc_array, yvals, visible = False, zorder=1, alpha = 0.3)

plt.axis([x_min, x_max, y_min, y_max])

graphs = [p1, p2, p3, p4, p5, p6, p7]



#ax.legend()

# plt.title("title")



plt.subplots_adjust(left=0.27, bottom=0.05, right=0.95, top=0.88)



labels = ["Function", "1st Deriv", "2nd Deriv", "Extrema", "POI", "Holes", "FTC"]

activated = [False, False, False, False, False, False, False]

button_field = plt.axes([0.03, 0.6, 0.17, 0.3])

check_button = CheckButtons(button_field, labels, activated)



def set_visible(label):

    index = labels.index(label)

    graphs[index].set_visible(not graphs[index].get_visible())

    plt.draw()

    fig.canvas.flush_events()



check_button.on_clicked(set_visible)



def submit(input):

    simplified = convert_func(input)

    p1.set_ydata(func_graph(simplified))

    p2.set_ydata(der_graph(convert_der(input)))

    p3.set_ydata(sec_der_graph(convert_sec_der(input)))

    plt.draw()

    fig.canvas.flush_events()



axbox = plt.axes([0.132, 0.92, 0.818, 0.05])

text_box = TextBox(axbox, "Function:")

text_box.on_submit(submit)



plt.show()



#Need to make it work for all functions

#Need to add removable discontinuities

#Need to add FTC

#Need to fix axis

#Maybe add GUI (optional)