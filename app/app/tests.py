"""Testing the calc module"""
# noqa
from django.test import SimpleTestCase
from app import calc 



class CalulatorTest(SimpleTestCase):
    
    """Tests calc module output"""
    
    def test_calc_add(self):
        val=calc.add(10,12)
        
        self.assertEqual(val,22)
        
    
    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res=calc.subtract(20,30)
        
        self.assertEqual(res,-10)
            