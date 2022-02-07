# str.replace(shablon zamena i [max count])- 
# zamena stroki po shablonu, po umolchaniu probel
# s = 'hello world'
# result = s.replace('lo', 'dnf', 2)
# print(result)
# str.split(simvol)

# s = '#summer#top'
# print(s.split('#'))

# s.isdigit() - proveryaet stroku chtoby ona sostoyala tolko iz chidel
# s = '123'
# print(s.isdigit())

# s.isalpha() - sostoit li stroka tolko iz bukv
# s = 'hello'
# print(s.isalpha())

# s. isalnum() - sostoit li stroka tolka iz cifr ili bukv
# s = 'world3'
# print(s.isalnum())

# s. islower() proverka na to chtoby vse simvoly stroki byli v nijnem registre
# s = 'hello'
# print(s.islower())

# s.isupper() proverke na verhnie registr
# s = 'HELLO WORLD'
# print(isupper())
# s.isspace() proverkana neotobrajaemye simvoly
# s = '      / n'
# print(s.isspace())

# # s.istitle() nachinautsya li slova v stroke s zaglavnoi bukvy
# s = 'Helo World'
# print(s.istitle())

# s.upper() preobrazovanie stroki k verhnemu registru
# s = 'hello world'
# print(s.upper())
# s = input('enter hello: ')
# print(s.upper())

# s.lower()
# s = input (' ENTER SOME ')
# print(s.islower())

# s.startswith(str) nachinaetsya li stroka s kakogo libo shablona
# s = 'heloo world'
# print(s.startswith('hello'))
# input() -> '3' .startswith()


#s.endswith() - proveryaet zakanchivaetsya li stroka na opredelennyi shablon
# s = 'hello world'
# print(s.endswith('d'))

# s. capitalize( perevodit pervyi simvol v verhnie v verhnii registr a wse ostalnoe v nijnie)
# s = 'hello World'
# print(s.capitalize())
# # print(s.title()) privodit kajdoe slovo k verhnemy registru

# s = 'hello'
# print('ed' in s) proverka na soderjanie shablona
# s. swapcase() perevodit verhnii registr v nijnii i naoborot
# s = 'hello World'
# print(s.swapcase())

# s.count(str, [start], [end]) podshet shablona v stroke 
# s = 'suppper some'
# print(s.count('s', 0, 5))

# s.lstrip([chars]) - udalenie probelnyh simvolov v nachale stroki
# s = 'hhello'
# print(s.lstrip('h'))

# s.rstrip([chars]) - udalenie probelov

# s.strip([chars]) udal prob v nachale i v konce
# s = 'hellooh '
# print(s.strip())

# s.zfill(width) stroka ne menshe dlinny width v protivnim sluchae zapolnit 0
# s = input('Enter some word ')
# print(s.zfill(15))
 
# task
email = input('enter email ')
password = input('enter password ')
password_confirmation = input('enter password cinfirmation ')
if email.endswith('@gmail.com') or email.endswith('@email.com'):
    if password == password_confirmation:
        print(' vy zaregalis')
    else:
        print('parol ne sovpadaut')
else:
    print('email doljenjfhj')