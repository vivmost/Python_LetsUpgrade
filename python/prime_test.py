
import unittest
import prime

class primeTest(unittest.TestCase):
    def test1(self):
        temp_n = 2
        result = prime.prime_no(temp_n)
        self.assertEqual(result, prime_no(2))
    def test2(self):
        temp_n = 17
        result = prime.prime_no(temp_n)
        self.assertEqual(result, prime_no(17))
        
if __name__ == '__main__':
        unittest.main()
