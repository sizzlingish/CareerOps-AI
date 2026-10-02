import os
import streamlit as st
from pypdf import PdfReader

from crew import run_careerops


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="CareerOps AI",
    page_icon="💼",
    layout="wide"
)


# -------------------------------------------------
# API Key
# -------------------------------------------------

# Streamlit Cloud Secrets
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]


# -------------------------------------------------
# Helper: Extract CV Text
# -------------------------------------------------

def extract_cv_text(uploaded_file):

    if uploaded_file.type == "application/pdf":

        pdf_reader = PdfReader(uploaded_file)

        text = ""

        for page in pdf_reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    elif uploaded_file.type == "text/plain":

        return uploaded_file.read().decode("utf-8")

    return ""


# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("💼 CareerOps AI")

st.subheader(
    "Your AI team for finding jobs, applying, and preparing for interviews."
)

st.write(
    "Upload your CV and provide a job description. "
    "CareerOps AI will analyze the opportunity, match your qualifications, "
    "create application materials, prepare interview questions, and review the result."
)

st.divider()


# -------------------------------------------------
# Input Section
# -------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.markdown("### 📄 Your CV")

    cv_file = st.file_uploader(
        "Upload your CV",
        type=["pdf", "txt"],
        help="Upload your CV as a PDF or text file."
    )


with col2:

    st.markdown("### 💼 Job Description")

    job_description = st.text_area(
        "Paste the job description",
        height=250,
        placeholder="Paste the complete job description here..."
    )


# -------------------------------------------------
# Run CareerOps
# -------------------------------------------------

if st.button("🚀 Run CareerOps", use_container_width=True):

    if cv_file is None:

        st.warning("Please upload your CV.")
        st.stop()

    if not job_description.strip():

        st.warning("Please provide a job description.")
        st.stop()


    # -------------------------------------------------
    # Extract CV
    # -------------------------------------------------

    with st.spinner("📄 Reading your CV..."):

        cv_text = extract_cv_text(cv_file)


    if not cv_text.strip():

        st.error(
            "Could not extract text from the CV. "
            "Please make sure the PDF contains selectable text."
        )

        st.stop()


    # -------------------------------------------------
    # Run CrewAI
    # -------------------------------------------------

    st.info("🤖 CareerOps AI agents are working...")

    progress = st.progress(0)

    try:

        with st.spinner(
            "🤖 CrewAI is analyzing your application..."
        ):

            results = run_careerops(
                cv_text=cv_text,
                job_description=job_description
            )

        progress.progress(100)

        st.success(
            "✅ CareerOps analysis completed successfully!"
        )

    except Exception as e:

        progress.empty()

        st.error("❌ CareerOps could not complete the analysis.")

        st.exception(e)

        st.stop()


    # -------------------------------------------------
    # Results
    # -------------------------------------------------

    st.divider()

    st.header("📊 CareerOps Results")


    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "🔎 Job Analysis",
            "📄 CV Analysis",
            "🔗 Job Match",
            "✍️ Application",
            "🎤 Interview",
            "🧐 Review"
        ]
    )


    # -------------------------------------------------
    # Job Analysis
    # -------------------------------------------------

    with tab1:

        st.markdown(results["job_analysis"])


    # -------------------------------------------------
    # CV Analysis
    # -------------------------------------------------

    with tab2:

        st.markdown(results["cv_analysis"])


    # -------------------------------------------------
    # Matching
    # -------------------------------------------------

    with tab3:

        st.markdown(results["matching"])


    # -------------------------------------------------
    # Application
    # -------------------------------------------------

    with tab4:

        st.markdown(results["application"])


    # -------------------------------------------------
    # Interview
    # -------------------------------------------------

    with tab5:

        st.markdown(results["interview"])


    # -------------------------------------------------
    # Review
    # -------------------------------------------------

    with tab6:

        st.markdown(results["review"])
