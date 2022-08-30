str = 'Incluso quien no sepa nada de latín se da cuenta de inmediato de que se trata de la lengua de los antiguos romanos. Pero, quien sepa algo de latín constatará, tras algunos infructuosos intentos, que este montón de palabras no se puede traducir, al menos no completamente. Y es que entre las verdaderas palabras en latín se mezclan algunas invenciones que aparentan tener un origen romano.'

str = (str.split(' '))
str = len(a)
acumulado = 0
for a in str:
    if a == 'a':
        acumulado = acumulado + 1



print(acumulado)


