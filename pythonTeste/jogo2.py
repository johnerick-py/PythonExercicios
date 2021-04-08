
km_total = float(input('distancia total:'))
km = int(input('Digite quantos km:'))
preco_petroleo = float(input('Digite o preço do petroleo:'))

print('Voce ira percorrrer {}km o seu carro faz {} km/l o preço do alcool esta {} e voce ira gastar R$ {:.2f}'.format(km_total, km, preco_petroleo, km_total/km*preco_petroleo))