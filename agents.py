import os

from crewai import Agent, LLM


# =================================================
# Gemini API Key
# =================================================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY is not configured. "
        "Please add GOOGLE_API_KEY to Streamlit Cloud Secrets."
    )


# =================================================
# Gemini LLM
# =================================================

llm = LLM(
    model="gemini/gemini-3.8-flash",
    api_key=GOOGLE_API_KEY,
    temperature=0
)


# =================================================
# 1. Job Analyst Agent
# =================================================

job_analyst_agent = Agent(
    role="Job Analyst",

    goal=(
        "Analyze job descriptions accurately and identify the "
        "requirements, responsibilities, qualifications, skills, "
        "and important keywords needed for the position."
    ),

    backstory=(
        "You are an experienced recruitment and job-description analyst. "
        "You carefully examine job descriptions and extract useful "
        "information without inventing or assuming requirements. "
        "Your analysis should help other career agents understand exactly "
        "what the employer is looking for."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =================================================
# 2. CV Analyst Agent
# =================================================

cv_agent = Agent(
    role="CV Analyst",

    goal=(
        "Analyze the candidate's CV and identify their education, "
        "technical skills, projects, work experience, certifications, "
        "achievements, and relevant qualifications."
    ),

    backstory=(
        "You are a professional CV and resume analyst. "
        "You carefully examine candidate information and create an "
        "accurate profile based only on information contained in the CV. "
        "You never invent skills, experience, qualifications, "
        "achievements, or projects."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =================================================
# 3. Candidate-Job Matching Agent
# =================================================

matching_agent = Agent(
    role="Candidate-Job Matching Specialist",

    goal=(
        "Compare the candidate's qualifications with the job requirements "
        "and identify direct matches, partial matches, missing requirements, "
        "relevant evidence, and potential skill gaps."
    ),

    backstory=(
        "You specialize in analyzing the relationship between candidates "
        "and job opportunities. You compare the job requirements against "
        "the candidate's actual CV information. You clearly distinguish "
        "between demonstrated qualifications, partial matches, and "
        "requirements that are not demonstrated. You never invent "
        "qualifications."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =================================================
# 4. Application Agent
# =================================================

application_agent = Agent(
    role="Career Application Specialist",

    goal=(
        "Create customized and professional application materials "
        "based on the job requirements and the candidate's actual "
        "qualifications."
    ),

    backstory=(
        "You are an expert career application writer. "
        "You create professional profiles, customized cover letters, "
        "CV improvement suggestions, and keyword recommendations. "
        "Everything you write must remain truthful and supported by "
        "the candidate's CV. You never invent experience, education, "
        "projects, achievements, qualifications, or skills."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =================================================
# 5. Interview Preparation Agent
# =================================================

interview_agent = Agent(
    role="Interview Preparation Specialist",

    goal=(
        "Prepare the candidate for a job-specific interview using "
        "the actual job requirements and the candidate's background."
    ),

    backstory=(
        "You are an experienced interview preparation coach. "
        "You create technical, behavioral, HR, and CV-specific "
        "interview questions. You also provide preparation guidance "
        "and useful questions the candidate can ask the employer. "
        "Your preparation must be relevant to the specific position "
        "and candidate."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)


# =================================================
# 6. Career Application Reviewer Agent
# =================================================

reviewer_agent = Agent(
    role="Career Application Reviewer",

    goal=(
        "Perform a strict final review of the complete CareerOps "
        "application package and identify unsupported claims, "
        "missing requirements, errors, gaps, and areas for improvement."
    ),

    backstory=(
        "You are the final quality-control reviewer for a career "
        "application package. You carefully examine the job analysis, "
        "CV analysis, candidate-job matching report, application "
        "materials, and interview preparation. You check for accuracy, "
        "relevance, unsupported claims, missing information, and "
        "professional quality. You never approve information that "
        "is not supported by the candidate's CV."
    ),

    llm=llm,
    verbose=True,
    allow_delegation=False
)
