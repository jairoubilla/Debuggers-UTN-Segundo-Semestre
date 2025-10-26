# Clase 9 POO Parte 5
# 12.2 Creamos las clases padres
from abc import ABC, abstractmethod

#ABC significa: Abstract Base Class, convierte una clase en abstracta

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho): ## 13.1 Validaciones en atributos
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto):## 13.1 Validaciones en atributos
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}')

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho): ## 13.1 Validaciones en atributos
            self._ancho = ancho
        else:
            print(f'valor erroneo ancho: {ancho} ')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto): ## 13.1 Validaciones en atributos
            self._alto = alto
        else:
            print(f'valor erroneo alto: {alto} ')

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'FiguraGeometrica Ancho: {self._ancho}, Alto: {self._alto}'

    def _validar_valores(self, valor):# metodo encapsulado
        return True if 0 < valor < 10 else False # # 13.1 Validaciones en atributos

#Clase 10 POO Parte 6 Abstract y Static
# 13.1 Validaciones en atributos
# 13.2 Metodo encapsulado y setter
# 13.3 Explicación de validaciones setter
# 13.4 Clases abstractas: Diagrama de clases UML, teoría y practica
# 13.5 Atributo Read-only y método mro


