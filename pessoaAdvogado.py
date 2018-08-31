'''
Herança e Composição em Python
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from pessoa import Pessoa

class PessoaAdvogado(Pessoa):#Herança
  #Contrutor de Atibutos
  def __init__(self, oab, nome, idade, cpf, telefone):
    self.__oab = oab
    super().__init__(nome, idade, cpf, telefone)

  #GET
  def getOab(self):
    return self.__oab

  #SET
  def setOab(self, oab):
    self.__oab = oab