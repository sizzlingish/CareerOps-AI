import streamlit as st

# -------------------------------------------------
# CareerOps AI
# -------------------------------------------------

st.set_page_config(
    page_title="CareerOps AI",
    page_icon="💼",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("💼 CareerOps AI")
st.subheader("Your AI team for finding jobs, applying, and preparing for interviews.")

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

st.divider()

# -------------------------------------------------
# Run CareerOps
# -------------------------------------------------

if st.button("🚀 Run CareerOps", use_container_width=True):

    if cv_file is None:
        st.warning("Please upload your CV.")

    elif not job_description.strip():
        st.warning("Please provide a job description.")

    else:
        st.success("Inputs received! CareerOps is ready to analyze your application.")

        # Temporary placeholder
        # We will connect this to CrewAI later.
        st.info(
            "🤖 AI agents will appear here once we connect the CrewAI workflow."
        )

        # -------------------------------------------------
        # Results Section
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

        with tab1:
            st.write("Job Analyst results will appear here.")

        with tab2:
            st.write("CV Agent results will appear here.")

        with tab3:
            st.write("Matching Agent results will appear here.")

        with tab4:
            st.write("Application Agent results will appear here.")

        with tab5:
            st.write("Interview Agent results will appear here.")

        with tab6:
            st.write("Reviewer results will appear here.")
