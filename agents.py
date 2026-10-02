from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os


# -------------------------------------------------
# Gemini LLM
# -------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


# -------------------------------------------------
# 1. Manager Agent
# -------------------------------------------------

manager_agent = Agent(
    role="Career Operations Manager",
    goal="Coordinate the career application workflow and ensure every agent completes its task.",
    backstory=(
        "You are an experienced career operations manager. "
        "You coordinate specialized AI agents to help candidates "
        "find opportunities, create applications, and prepare for interviews."
    ),
    llm=llm,
    verbose=True
)


# -------------------------------------------------
# 2. Job Analyst Agent
# -------------------------------------------------

job_analyst_agent = Agent(
    role="Job Analyst",
    goal="Analyze the job description and identify the requirements of the position.",
    backstory=(
        "You are a professional recruitment analyst. "
        "You carefully examine job descriptions and extract "
        "qualifications, skills, responsibilities, and important keywords."
    ),
    llm=llm,
    verbose=True
)


# -------------------------------------------------
# 3. CV Agent
# -------------------------------------------------

cv_agent = Agent(
    role="CV Analyst",
    goal="Analyze the candidate's CV and identify relevant qualifications and experience.",
    backstory=(
        "You are a professional CV analyst. "
        "You identify the candidate's education, skills, projects, "
        "experience, achievements, and other relevant qualifications."
    ),
    llm=llm,
    verbose=True
)


# -------------------------------------------------
# 4. Matching Agent
# -------------------------------------------------

matching_agent = Agent(
    role="Candidate-Job Matching Specialist",
    goal="Compare the candidate's qualifications with the job requirements.",
    backstory=(
        "You specialize in matching candidates to job opportunities. "
        "You identify direct matches, partial matches, missing requirements, "
        "and areas that should be emphasized in the application."
    ),
    llm=llm,
    verbose=True
)


# -------------------------------------------------
# 5. Application Agent
# -------------------------------------------------

application_agent = Agent(
    role="Application Specialist",
    goal="Create customized and truthful application materials for the job.",
    backstory=(
        "You are an expert career application writer. "
        "You create professional profiles, cover letters, "
        "and application responses based only on the candidate's actual experience."
    ),
    llm=llm,
    verbose=True
)


# -------------------------------------------------
# 6. Interview Agent
# -------------------------------------------------

interview_agent = Agent(
    role="Interview Preparation Specialist",
    goal="Prepare the candidate for a job-specific interview.",
    backstory=(
        "You are an experienced interview coach. "
        "You create technical, behavioral, and role-specific questions "
        "based on the actual job requirements and the candidate's background."
    ),
    llm=llm,
    verbose=True
)


# -------------------------------------------------
# 7. Reviewer Agent
# -------------------------------------------------

reviewer_agent = Agent(
    role="Career Application Reviewer",
    goal="Review the complete application and identify errors, gaps, and improvements.",
    backstory=(
        "You are a strict final reviewer. "
        "You check applications for accuracy, relevance, unsupported claims, "
        "missing requirements, and professional quality."
    ),
    llm=llm,
    verbose=True
)
