import unittest
from Estoque import repor_Estoque

class Test_Reposicao_Estoque(unittest.TestCase):
    def test_repor_Estoque(self):
        lista1 = [("shampoo",7),("condicionador",8),("sabonete",6),("perfume",3)]
        lista2 = [("shampoo",2),("condicionador",1),("sabonete",4),("perfume",3)]
        lista3 = [("shampoo",9),("condicionador",8),("sabonete",6),("perfume",5)]
        self.assertEqual(repor_Estoque(lista1),1)
        self.assertEqual(repor_Estoque(lista2),4)
        self.assertEqual(repor_Estoque(lista3),0)

