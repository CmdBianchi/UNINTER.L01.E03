####################################################################################
#--------------- > Execício 03

print('---' * 20)
import random
donor = []
def DonorRecord(nome: str, doacao: float):
    donor.extend(((nome + ' ') * int(doacao // 10)).split())
    return
def PrizeDraw():
    random.shuffle(donor)
    print(f'Lista de doadores embaralhada: {donor}')
    return random.choice(donor)
option = int(input('Cadastrar doador? 0 - Não     1 - Sim : '))
while option == 1:
    _donor = input('Nome do doador: ')
    value = float(input('Valor da doação: '))
    DonorRecord(_donor, value)

    option = int(input('Cadastrar doador? 0 - Não     1 - Sim '))
if len(donor) > 0:
    print('---'*20)
    print(f'Lista de doadores para sorteio: {donor}')
    print(f'O vencedor(a) foi: | > {PrizeDraw()} < | PARABÉNS !!!')
    print('---' * 20)