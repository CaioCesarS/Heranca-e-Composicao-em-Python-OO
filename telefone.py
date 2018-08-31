'''
Herança e Composição em Python
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

class Telefone():
  #Contrutor de Atibutos
  def __init__(self, telefone):
    self.__telefone = telefone

  def getTelefone(self):
    return self.__telefone

  def setTelefone(self, telefone):
    self.__telefone = telefone