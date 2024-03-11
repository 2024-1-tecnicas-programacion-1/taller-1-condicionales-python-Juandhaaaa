import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.division import evaluar

class TestDivision(unittest.TestCase):
    def testDivisionExacta1(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 2\n" \
                         "Residuo: 4"
        valor_actual = evaluar(14, 5)
        self.assertEqual(valor_esperado, valor_actual)
        
    def testDivisionExacta2(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 3\n" \
                         "Residuo: 0"
        valor_actual = evaluar(15, 0)
        self.assertEqual(valor_esperado, valor_actual)

    def testDivisionExacta3(self):
        valor_esperado = "La división es exacta. \n" \
                         "Cociente: 3\n" \
                         "Residuo: 1"
        valor_actual = evaluar(10, 3)
        self.assertEqual(valor_esperado, valor_actual)
    
    # Puedes agregar más casos de prueba aquí

if __name__ == '__main__':
    unittest.main()
