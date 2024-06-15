print("olá, Carlos!")
F=float(input('Digite a temperatura em Fahrenheit:'))

tempCelsius = (F-32)*5/9

print('A temperatura em Célsius é:',tempCelsius)

print('Vamos converter segundos em tempo convencional (hh:mm:ss)')
segundos=int(input('Digite a quantidade de segundos: '))

horas=segundos // 3600
segs_restantes = segundos % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

print('Com o valor temos : ',horas,":",minutos,":",segs_restantes_final,".")
