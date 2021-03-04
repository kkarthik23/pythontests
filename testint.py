import unittest
import my_calc


class TestIntMethods(unittest.TestCase):
   """
   Test ADD
   """
   def test_add(self):
      self.assertTrue(my_calc.add(6,5),11)
   """
   Test Subtract
   """
   def test_sub(self):
      self.assertEqual(my_calc.sub(6,5),1)
   """
   Test Multiply
   """
   def test_multiply(self):
      self.assertEqual(my_calc.multiply(5,5),25)
   """
   Test Divide
   """
   def test_divide(self):
       self.assertEqual(my_calc.divide(8,4),2)
   """
   Test Exponent
   """
   def test_exponent(self):
        self.assertEqual(my_calc.exponent(4,4),256)

   """
   Test Square Root
   """
   def test_squareroot(self):
          self.assertEqual(my_calc.squareroot(4),2)
if __name__ == '__main__':
    unittest.main()




   
   
