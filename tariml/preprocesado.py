"""
Resumen modulo bla bla bla para evitar error pylint
"""
from typing import Union
VarNum = Union[int, float, complex]
def suma(number_a: VarNum, number_b: VarNum) -> VarNum:
    """Descripcion 1
    :param number_a: Primer numero
    :type number_a: int, float, complex
    :param number_b: Segundo numero
    :type number_b: int, float, complex
    :return: Resultado de la suma
    :rtype: int, float, complex
    >>> from tariml.preprocesado import resta
    >>> suma(5,5)
    10
    """
    return number_a+number_b
def resta(number_a: VarNum, number_b: VarNum) -> VarNum:
    """Funcion 2 que resta dos numeros

    :param number_a: Primer numero
    :type number_a: int, float, complex
    :param number_b: Segundo numero
    :type number_b: int, float, complex

    :return: Resultado de la resta
    :rtype: int, float, complex

    >>> from tariml.preprocesado import resta
    >>> resta(5,5)
    0
    """
    return number_a-number_b
