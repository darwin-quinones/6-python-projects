# concatenar cadenas de caracteres
# supongamos que queremos crear una cadena que diga:
# aprende a programas con ___________.


# organizacion = 'freeCodeCamp'

# print('Aprende a programar con '+ organizacion)
# print('Aprende a programar con {}'.format(organizacion))
# print(f'Aprende a programar con {organizacion}')


# MAD LIBS (HISTORIAS LOCAS)

print("!Programar es tan ______! Siempre me emociona porque me encanta ______ problemas. !Aprende a ______ con freeCodeCamp y alcanza tus _______")

adj = input('Adjetivo: ')
verbo1 = input('Verbo: ')
verbo2 = input('Verbo: ')
sustantivo_plural = input('Sustantivo (plural): ')

madlib = f"!Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. !Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}"

print(madlib)