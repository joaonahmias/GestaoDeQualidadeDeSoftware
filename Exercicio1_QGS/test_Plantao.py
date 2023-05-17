from Plantao import*
import unittest

class testeMaiorPlantao(unittest.TestCase):
    #lista1 = [("maria",22), ("joao",32),("lucas,9"),("Lara",33)]
    def teste_plantaoMaisLongo(self):
        lista1 = [("maria",22), ("joao",32),("lucas",33),("Lara",30)]
        lista2 = [("maria",22), ("joao",30),("lucas",9),("Lara",30)]
        lista3 = []
        self.assertEqual(Plantao(lista1),[("lucas",33)])
        self.assertEqual(Plantao(lista2),[("joao",30),("Lara",30)])
        self.assertEqual(Plantao(lista3),[])





