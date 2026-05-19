import spacy
from PyPDF2 import PdfReader

class ResumeAnalyzer:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def extract_text(self, pdf_path):
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def get_score(self, resume_text, job_description):
        # Mock scoring logic based on token similarity
        resume_doc = self.nlp(resume_text)
        jd_doc = self.nlp(job_description)
        return resume_doc.similarity(jd_doc) * 100
