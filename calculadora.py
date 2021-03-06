import abc
from unittest import TestCase, main

class Calculadora (object):

  def calcular(self, n1, n2, operador):
  operacaoFabrica = OperacaoFabrica()
  operacao = operacaoFabrica.criar(operador)
  if (operacao == None):
    return 0
  else:
    resultado = operacao.executar(n1,n2)
    return resultado

class OperacaoFabrica(object):

  def criar(self, operador):
    if (operador == "soma"):
      return Soma()
    elif (operador == "subtracao"):
      return Subtracao()
    elif (operador == "divisao"):
      return Divisao()
    elif (operador == "multiplicacao"):
      return Multiplicacao()
      
class Operacao(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def executar(self, n1,n2):
    pass
    
class Soma (Operacao):
  def executar (self,n1,n2):
    resultado = n1 + n2
    return resultado
    
class Subtracao (Operacao):
  def executar (self,n1,n2):
    resultado = n1 - n2
    return resultado
    
class Divisao (Operacao):
  def executar (self,n1,n2):
    resultado = n1 / n2
    return resultado

class Multiplicacao (Operacao):
  def executar (self,n1,n2):
    resultado = n1 * n2
    return resultado
    
class Testes (TestCase):

  def test_soma(self):
  calculador = Calculadora()
  result = calculador.calcular(4,2, "soma")
  self.assertEqual(result, 6)
  
  def test_multiplicacao(self):
  calculador = Calculadora()
  result = calculador.calcular(4,2, "multiplicacao")
  self.assertEqual(result, 8)
  
  def test_divisao(self):
  calculador = Calculadora()
  result = calculador.calcular(4,2, "divisao")
  self.assertEqual(result, 2)
  
  def test_subtracao(self):
  calculador = Calculadora()
  result = calculador.calcular(4,2, "subtracao")
  self.assertEqual(result, 2)
  
calculador = Calculadora()
NumeroCalculado = calculador.calcular(4,2 "soma")
print(NumeroCalculado)

if __name__ == '__main__':
  main()
  
