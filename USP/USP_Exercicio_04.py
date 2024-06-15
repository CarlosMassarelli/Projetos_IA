"""
Exercício USP Cursera
Conversão de segundos em dias, horas, minutos e segundos
"""

print('Olá, vamos converter segundos em dias, horas, minutos e segundos!')

seg=int(input('Por favor, entre com o número de segundos que deseja converter:'))

#calculando os valores
dia=seg // 86400
segs_rest = seg % 86400
horas=segs_rest // 3600
segs_rest = segs_rest % 3600
min = segs_rest // 60
segs_rest_final = segs_rest % 60

print(dia,'dias,',horas,'horas,', min,'minutos e', segs_rest_final,'segundos.')

