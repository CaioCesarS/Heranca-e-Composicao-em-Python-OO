'''
Herança e Composição em Python
'''
__author__ = 'Caio César'
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Development'

from telefone import Telefone

class Pessoa():
  #Contrutor de Atibutos
  def __init__(self, nome, idade, cpf, telefone):
    self.__nome = nome
    self.__idade = idade
    self.__cpf = cpf
    self.__telefone = Telefone(telefone)#Composição

  #GET
  def getNome(self):
    return self.__nome

  def getIdade(self):
    return self.__idade

  def getCpf(self):
    return self.__cpf

  def getTelefone(self):
    return self.__telefone

  #SET
  def setNome(self, nome):
    self.__nome = nome

  def setIdade(self, idade):
    self.__idade = idade

  def setCpf(self, cpf):
    self.__cpf = cpf

  def setTelefone(self, telefone):
    self.__telefone = Telefone().setTelefone(telefone)