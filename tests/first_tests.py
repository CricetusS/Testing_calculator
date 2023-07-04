import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_calculates_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4
        
    def test_subtraction_calculates_correctly(self):
        assert  self.calc.subtraction(self, 7, 1) == 6
        
    def test_multiplication_calculates_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculates_correctly(self):
        assert  self.calc.division(self,9, 3) == 3
    
    def teardown(self):
        print("Выполнение Teardown")

   