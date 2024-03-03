import inspect

def parse_code_og(a,b,c,d,aa,bb,cc,ccc,bbb,bbbb):
   out = ""
   if a:
      out += ('.a')
      if aa:
         out += ('.aa')
      else:
         out += ('.-aa')
      #endif
      out += ('.a')
   elif b:
      out += ('.b')
      if bb:
         out += ('.bb')
      elif bbb:
         out += ('.bbb')
      elif bbbb:
         out += ('.bbbb')
      #endif
      out += ('.b')
   elif c:
      out += ('.c')
      if cc:
         out += ('.cc')
      elif ccc:
         out += ('.ccc')         
      else:
         out += ('.-cc-ccc')
      #endif
      out += ('.c')
   else:
      out += ('.-a-b-c')
      if d:
         out += ('.d')    
      #endif  
      out += ('.-a-b-c')
   #endif
   out += ('.0')
   return out

def test_code_py(a,b,c,d,aa,bb,cc,bbb,ccc,bbbb):
    if 1 == 1: out = ""
    if a: out += ('.a')
    if a and aa: out += ('.aa')
    if a and not (aa): out += ('.-aa')
    if a: out += ('.a')
    if b and not (a): out += ('.b')
    if b and bb and not (a): out += ('.bb')
    if b and bbb and not (a or bb): out += ('.bbb')
    if b and bbbb and not (a or bb or bbb): out += ('.bbbb')
    if b and not (a): out += ('.b')
    if c and not (a or b): out += ('.c')
    if c and cc and not (a or b): out += ('.cc')
    if c and ccc and not (a or b or cc): out += ('.ccc')
    if c and not (a or b or cc or ccc): out += ('.-cc-ccc')
    if c and not (a or b): out += ('.c')
    if not (a or b or c): out += ('.-a-b-c')
    if d and not (a or b or c): out += ('.d')
    if not (a or b or c): out += ('.-a-b-c')
    if 1 == 1: out += ('.0')
    if 1 == 1: return out
    
def generate_binary_matrix(num_digits):
    rows = 2 ** num_digits
    cols = num_digits

    matrix = []
    for i in range(rows):
        binary_str = format(i, '0' + str(num_digits) + 'b')
        row = [int(bit) for bit in binary_str]
        matrix.append(row)

    return matrix

def generate_cases(func_a,func_b,test_name):
    result = f"""import unittest

# Define the function to be tested
{inspect.getsource(func_a)}
{inspect.getsource(func_b)}
# Create a test class that inherits from unittest.TestCase
class Test{test_name.lower().capitalize()}(unittest.TestCase):"""
    signature = inspect.signature(func_a)
    arr_variables = [param.name for param in signature.parameters.values()]
    matrix = generate_binary_matrix(len(arr_variables))
    i = 0
    for row in matrix:
        j=0
        case_variables = []
        for column in row:
            case_variables.append(f'{arr_variables[j]} = {column == 1}')
            j += 1
        
        unit_test_string = f"""
    # Test {i}"
    def test_case_{i}(self):
        self.assertEqual({func_a.__name__}({', '.join(case_variables)}),
                         {func_b.__name__}({', '.join(case_variables)}))
"""
        result += unit_test_string
        i += 1
    result += """
# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
    """
    name = "test_" + test_name + '.py'
    with open(name, 'w') as f:
        f.write(result)

    print(name + " created successfully")
generate_cases(parse_code_og,test_code_py,"elseif")