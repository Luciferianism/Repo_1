import os
import sys
# Modify
class concept(object):
  i = 1234
  def __init__(self, var_a, var_b, var_c):
    self.var_a = var_a
    self.var_b = var_b
    self.var_c = var_c
    
    def function_second(self, number):
      pass
    
    def function_third(self, i):
      operation = i + 24
    return operation
  
  class concept_second(concept):
    def __init__(self, var_a,var_b,var_c,var_d):
      super().__init__(var_a,var_b,var_c)
      self.var_d = var_d
      pass
    
