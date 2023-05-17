import unittest
from Prontuario import paciente_mais_visitas
from Prontuario import pacientes_premiados
class Test_Prontuario(unittest.TestCase):
    def test_paciente_mais_visitas(self):
        lista = [(1, 'Carla','5/2/22', 1), (2, 'Danilo', '5/2/22', 1), (3, 'Danilo', '5/2/22',2), (4,'Carla', '5/2/22', 2), (5, 'Carla', '4/9/21', 1)]
        medico = 1
        r_esperado = ["Carla"]
        self.assertEqual(paciente_mais_visitas(lista,medico), r_esperado)
        medico2 = 2
        r_esperado2 = ["Danilo","Carla"]
        self.assertEqual(paciente_mais_visitas(lista,medico2), r_esperado2)
        medico3 = 0
        r_esperado3 = "Paciente não encontrado"
        self.assertEqual(paciente_mais_visitas(lista,medico3), r_esperado3)
    

    def test_pacientes_premiados(self):
        lista1 = [('1/22', 1, 1), ('1/22', 2, 4),('2/22', 1, 2), ('3/22', 1, 3), ('4/22', 1, 7), ('5/22', 1, 4),('6/22', 1, 8), ('7/22', 1, 10)]
        r_esperado1 = [1]
        lista2 = [('1/22', 2, 1), ('1/22', 2, 4),('2/22', 2, 2), ('3/22', 1, 3), ('4/22', 1, 7), ('5/22', 1, 4)]
        r_esperado2 = [2,1]
        self.assertEqual(pacientes_premiados(lista1),r_esperado1)
        self.assertEqual(pacientes_premiados(lista2),r_esperado2)

        




