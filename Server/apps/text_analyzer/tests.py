from django.test import TestCase
from apps.text_analyzer.analyzer import Analyzer

# Create your tests here.
class TextAnalyzerTest(TestCase):

    def setUp(self):
        self.analyzer = Analyzer()

    def test_type_of_text_variable(self):
        self.assertIsInstance(self.analyzer.text_to_analyze, str)
    
    def test_getter_setter(self):
        test_text = 'some text'
        self.analyzer.set_text_to_analyze(test_text)
        got_text = self.analyzer.get_text_to_analyze()
        self.assertEqual(test_text, got_text)

    def test_search_terms_exist(self):
        self.analyzer.search_terms

    def test_analyze_text(self):
        test_text_a = 'some'
        test_text_b = 'text'
        test_text = ' '.join([test_text_a, test_text_b])
        self.analyzer.set_text_to_analyze(test_text)
        terms = self.analyzer.analyze_text()
        self.assertIn(test_text_a, test_text)
        self.assertIn(test_text_b, test_text)
        

