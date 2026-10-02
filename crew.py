from crewai import Crew, Process

from agents import (
    manager_agent,
    job_analyst_agent,
    cv_agent,
    matching_agent,
    application_agent,
    interview_agent,
    reviewer_agent
)

from tasks import (
    job_analysis_task,
    cv_analysis_task,
    matching_task,
    application_task,
    interview_task,
    review_task
)


# -------------------------------------------------
# CareerOps Crew
# -------------------------------------------------

careerops_crew = Crew(

    agents=[
        manager_agent,
        job_analyst_agent,
        cv_agent,
        matching_agent,
        application_agent,
        interview_agent,
        reviewer_agent
    ],

    tasks=[
        job_analysis_task,
        cv_analysis_task,
        matching_task,
        application_task,
        interview_task,
        review_task
    ],

    process=Process.sequential,

    verbose=True
)


# -------------------------------------------------
# Run CareerOps
# -------------------------------------------------

def run_careerops(cv_text, job_description):

    result = careerops_crew.kickoff(
        inputs={
            "cv_text": cv_text,
            "job_description": job_description
        }
    )

    return result
