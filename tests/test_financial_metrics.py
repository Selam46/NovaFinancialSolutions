import unittest
from QuantitativeAnalysis.FinancialMetrics import calculate_roi, calculate_ebit  # Adjust imports as needed

class TestFinancialMetrics(unittest.TestCase):
    
    def test_calculate_roi(self):
        """Test the ROI calculation."""
        investment = 1000
        return_value = 1200
        expected_roi = (return_value - investment) / investment
        self.assertAlmostEqual(calculate_roi(investment, return_value), expected_roi, places=2)

    def test_calculate_ebit(self):
        """Test the EBIT calculation."""
        revenue = 5000
        expenses = 2000
        expected_ebit = revenue - expenses
        self.assertEqual(calculate_ebit(revenue, expenses), expected_ebit)

    def test_roi_negative(self):
        """Test ROI calculation with negative return."""
        investment = 1000
        return_value = 800
        expected_roi = (return_value - investment) / investment
        self.assertAlmostEqual(calculate_roi(investment, return_value), expected_roi, places=2)

if __name__ == '__main__':
    unittest.main()