import eel
eel.init('web')


@eel.expose
def dogon_calculator(win, lose, outcome):
    res = (float(win) + float(lose)) / (float(outcome) - 1)
    return "Следующая ставка: " + str(res)


eel.start('main.html', size=(800, 600))
