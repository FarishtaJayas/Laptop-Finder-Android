class Analyzer():

    text_to_analyze = str()
    search_terms = list()

    def get_text_to_analyze(self):
        return self.text_to_analyze
    
    def set_text_to_analyze(self, text):
        self.text_to_analyze = text;
    
    def analyze_text(self):
        self.search_terms = self.text_to_analyze.split()

    