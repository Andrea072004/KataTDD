import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5, conjunto.promedio())

    def test_conjunto_dosElementos_retornaPromedioElementos( self ):
        conjunto=Conjunto([5,7])
        self.assertEqual(6,conjunto.promedio())

    def test_conjunto_nElementos_retornaPromedioNElementos( self ):
        conjunto=Conjunto([2,4,8,9,10,15])
        self.assertEqual((2+4+8+9+10+15)/6,conjunto.promedio())

## promedio ponderado
    class TestConjuntoPonderado(unittest.TestCase):
        def test_promedio_ponderado_caso1(self):
            datos = [10, 12, 14]
            pesos = [3, 4, 2]
            conjunto_ponderado = ConjuntoPonderado(datos, pesos)
            self.assertAlmostEqual(11.78, conjunto_ponderado.promedio_ponderado(), delta=0.01)

        def test_promedio_ponderado_caso2(self):
            datos = [15, 15, 17]
            pesos = [3, 4, 2]
            conjunto_ponderado = ConjuntoPonderado(datos, pesos)
            self.assertAlmostEqual(15.44, conjunto_ponderado.promedio_ponderado(), delta=0.01)

if __name__ == '__main__':
    unittest.main()
