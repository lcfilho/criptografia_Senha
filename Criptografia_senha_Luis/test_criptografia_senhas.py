import unittest
import criptografia_senhas

class Test_criptografia(unittest.TestCase):

    def test_hash_md5(self):
        self.assertEqual(criptografia_senhas.hash_md5('chave'),'c08cbbfd6eefc83ac6d23c4c791277e4')
    def test_hash_md5_1(self):
        self.assertTrue(criptografia_senhas.hash_md5('password'),'5f4dcc3b5aa765d61d8327deb882cf99')        
    def test_hash_sha256(self):
        self.assertEqual(criptografia_senhas.hash_sha256('senha'),'b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c')
    def test_hash_sha256_1(self):
        self.assertEqual(criptografia_senhas.hash_sha256('password'),'5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8')
    

if __name__ == "__main__":
    unittest.main()
