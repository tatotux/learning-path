from sys import platlibdir
import exs25

frase="Hola Gente Bienvenidos a Python"

palabras=exs25.break_words(frase)

print(palabras[0])

acomodado=exs25.sort_words(frase)

print(acomodado)

frase="Hola Gente Bienvenidos a Python"

print(exs25.print_first_word(frase.split(" ")))

frase="Hola Gente Bienvenidos a Python"

print(exs25.print_last_word(frase.split(" ")))

frase="Hola Gente Bienvenidos a Python"

print(exs25.sort_sentence(frase))

frase="Hola Gente Bienvenidos a Python"

print(exs25.print_first_and_last(frase))

frase="Hola Gente Bienvenidos a Python"

print(exs25.print_first_and_last_sorted(frase))

