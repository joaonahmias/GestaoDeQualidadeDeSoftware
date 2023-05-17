import unittest
from Venda import Percentual_Venda_Produto
from Venda import Total_Vendas
from Venda import Percentual_Crescimento

class Test_Venda(unittest.TestCase):
    
    def test_Percentual_Venda_Produto(self):
        lista1 = [(1,1,2),(1,2,4),(1,3,1),(2,2,2),(2,4,0)]
        lista_esperada = [(1,0.2222),(2,0.6667),(3,0.1111),(4,0.0)]
        self.assertEqual(Percentual_Venda_Produto(lista1),lista_esperada)

    def test_Total_Vendas(self):
        lista1= [(1,300.50),(2,450.50),(3,200),(4,20.99)]
        resultado_esperado = 971.99
        lista2 = []
        self.assertEqual(Total_Vendas(lista1), resultado_esperado)
        self.assertEqual(Total_Vendas(lista2),0)

    def test_Percentual_Crescimento(self):
        lista=[('01/22', 400.50),('2/22', 1000.00), ('3/22', 10.50), ('4/22', 100.30)]
        parametro1 = "3/22"
        r_esperado1 = -98.95
        parametro2 = "01/22"
        r_esperado2 = 0
        self.assertEqual(Percentual_Crescimento(lista, parametro1),r_esperado1)
        self.assertEqual(Percentual_Crescimento(lista, parametro2),r_esperado2)




                 