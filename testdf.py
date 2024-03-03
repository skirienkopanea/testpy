import unittest
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}).to_csv(index=False)
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}).to_csv(index=False)
df3 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 7]}).to_csv(index=False)

# Create a test class that inherits from unittest.TestCase
class TestDataFrame(unittest.TestCase):
    
# Define test methods, each starting with "test_"
    def test_0(self):
        self.assertEqual(df1, df2)  # Assert that 1 + 2 equals 3
        
# Define test methods, each starting with "test_"
    def test_1(self):
        self.assertEqual(df1, df3)  # Assert that 1 + 2 equals 3
    

# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
    