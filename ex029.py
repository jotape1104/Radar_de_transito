from time import sleep
velo = float(input('Velocidade em que o carro passou: '))
multa = (velo - 80) * 7
print('\033[4;33mPROCESSANDO VELOCIDADE...')
sleep(3)
if velo > 80:
    print('\033[0;31mVOCÊ FOI MULTADO!!!, o limite de velocidade é 80km/h, pague uma multa de R${:.2f}'.format(multa))
else:
    print('\033[0;32mVelocidade dentro do padrão')