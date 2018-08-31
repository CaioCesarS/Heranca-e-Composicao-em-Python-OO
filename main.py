'''
Herança e Composição em Python
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from pessoaMedico import PessoaMedico
from pessoaAdvogado import PessoaAdvogado

listPessoaMedico = []
listPessoaAdvogado = []

pessoaMedico1 = PessoaMedico(154790, 'Ana Júlia', 26, 78745012306, 999652648)
pessoaMedico2 = PessoaMedico(202010, 'João', 31, 15478965214, 991474560)
listPessoaMedico.append(pessoaMedico1)
listPessoaMedico.append(pessoaMedico2)

pessoaAdvogado1 = PessoaAdvogado(61432144, 'Joaquim', 50, 12345678912, 32415050)
pessoaAdvogado2 = PessoaAdvogado(20017463, 'Francielle', 25, 12345678998, 32428080)
listPessoaAdvogado.append(pessoaAdvogado1)
listPessoaAdvogado.append(pessoaAdvogado2)

print('~'*40)
print('Lista de Advogados:')
for ad in listPessoaAdvogado:
  print('OAB: {} | Nome: {} | Idade: {}'.format(ad.getOab(), ad.getNome(), ad.getIdade()))
  print('CPF: {} | Telefone: {}'.format(ad.getCpf(), ad.getTelefone().getTelefone()), end='\n\n')
print('~'*40)

print('Lista de Médicos:')
for md in listPessoaMedico:
  print('CRM: {} | Nome: {} | Idade: {}'.format(md.getCrm(), md.getNome(), md.getIdade()))
  print('CPF: {} | Telefone: {}'.format(md.getCpf(), md.getTelefone().getTelefone()), end='\n\n')
print('~'*40)