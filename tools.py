import io

from pypdf import PdfReader
from crewai.tools import tool


@tool("Read CV PDF")
def read_cv_pdf(pdf_bytes: bytes) -> str:
    """
    Extracts text from an uploaded CV PDF.

    Returns the text from all pages of the PDF.
    """

    try:
        pdf_file = io.BytesIO(pdf_bytes)
        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        if not text.strip():
            return "No readable text was found in the CV."

        return text.strip()

    except Exception as e:
        return f"Error reading CV PDF: {str(e)}"


@tool("Extract Job Description")
def extract_job_description(job_description: str) -> str:
    """
    Cleans and prepares the job description
    before sending it to the AI agents.
    """

    if not job_description.strip():
        return "No job description was provided."

    return job_description.strip()
