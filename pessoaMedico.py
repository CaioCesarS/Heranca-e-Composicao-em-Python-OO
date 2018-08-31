'''
Herança e Composição em Python
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from pessoa import Pessoa

class PessoaMedico(Pessoa):#Herança
  #Contrutor de Atibutos
  def __init__(self, crm, nome, idade, cpf, telefone):
    self.__crm = crm
    super().__init__(nome, idade, cpf, telefone)

  #GET
  def getCrm(self):
    return self.__crm

  #SET
  def setCrm(self, crm):
    self.__crm = crm  