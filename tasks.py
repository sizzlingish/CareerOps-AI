from crewai import Task

from agents import (
    manager_agent,
    job_analyst_agent,
    cv_agent,
    matching_agent,
    application_agent,
    interview_agent,
    reviewer_agent
)


# -------------------------------------------------
# 1. Job Analysis Task
# -------------------------------------------------

job_analysis_task = Task(
    description="""
    Analyze the provided job description.

    Extract:
    1. Job title
    2. Required qualifications
    3. Technical skills
    4. Soft skills
    5. Responsibilities
    6. Preferred qualifications
    7. Important keywords

    Do not invent information.
    Only use information provided in the job description.

    Job Description:
    {job_description}
    """,

    expected_output="""
    A structured analysis containing:
    - Job title
    - Required qualifications
    - Technical skills
    - Soft skills
    - Responsibilities
    - Preferred qualifications
    - Important keywords
    """,

    agent=job_analyst_agent
)


# -------------------------------------------------
# 2. CV Analysis Task
# -------------------------------------------------

cv_analysis_task = Task(
    description="""
    Analyze the candidate's CV.

    Identify:
    1. Education
    2. Technical skills
    3. Projects
    4. Work experience
    5. Certifications
    6. Achievements
    7. Relevant experience

    Do not invent qualifications or experience.

    Candidate CV:
    {cv_text}
    """,

    expected_output="""
    A structured candidate profile containing:
    - Education
    - Technical skills
    - Projects
    - Experience
    - Certifications
    - Achievements
    - Relevant qualifications
    """,

    agent=cv_agent
)


# -------------------------------------------------
# 3. Matching Task
# -------------------------------------------------

matching_task = Task(
    description="""
    Compare the job requirements with the candidate's qualifications.

    Identify:
    1. Direct matches
    2. Partial matches
    3. Requirements not demonstrated
    4. Relevant evidence from the CV
    5. Skills and keywords that should be emphasized
    6. Potential gaps

    Never invent qualifications.

    JOB ANALYSIS:
    {job_analysis}

    CV ANALYSIS:
    {cv_analysis}
    """,

    expected_output="""
    A clear candidate-job matching report containing:
    - Direct matches
    - Partial matches
    - Missing or unsupported requirements
    - Evidence from the CV
    - Important keywords
    - Areas for improvement
    """,

    agent=matching_agent
)


# -------------------------------------------------
# 4. Application Task
# -------------------------------------------------

application_task = Task(
    description="""
    Create customized application materials using the job analysis,
    CV analysis, and matching report.

    Prepare:

    1. Professional profile
    2. Customized cover letter
    3. Key CV improvement suggestions
    4. Important keywords to emphasize

    All content must be truthful.

    Never invent:
    - Experience
    - Projects
    - Qualifications
    - Achievements
    - Skills

    JOB ANALYSIS:
    {job_analysis}

    CV ANALYSIS:
    {cv_analysis}

    MATCHING REPORT:
    {matching_report}
    """,

    expected_output="""
    Customized application materials containing:
    - Professional profile
    - Cover letter
    - CV improvement suggestions
    - Important keywords
    """,

    agent=application_agent
)


# -------------------------------------------------
# 5. Interview Preparation Task
# -------------------------------------------------

interview_task = Task(
    description="""
    Prepare the candidate for an interview for this position.

    Generate:

    1. Technical interview questions
    2. Behavioral questions
    3. HR questions
    4. Questions based specifically on the candidate's CV
    5. Questions the candidate can ask the employer
    6. Preparation guidance for each important topic

    Base the questions on the actual job requirements
    and candidate information.

    JOB ANALYSIS:
    {job_analysis}

    CV ANALYSIS:
    {cv_analysis}

    MATCHING REPORT:
    {matching_report}
    """,

    expected_output="""
    A job-specific interview preparation guide containing:
    - Technical questions
    - Behavioral questions
    - HR questions
    - CV-based questions
    - Questions to ask the interviewer
    - Preparation guidance
    """,

    agent=interview_agent
)


# -------------------------------------------------
# 6. Review Task
# -------------------------------------------------

review_task = Task(
    description="""
    Review the complete CareerOps output.

    Check for:

    1. Accuracy
    2. Evidence from the CV
    3. Job relevance
    4. Missing requirements
    5. Unsupported claims
    6. Professional language
    7. Important omissions
    8. Interview preparation gaps

    Clearly separate:
    - APPROVED ITEMS
    - ITEMS TO FIX
    - MISSING INFORMATION
    - FINAL RECOMMENDATIONS

    Never approve information that is unsupported by the CV.

    JOB ANALYSIS:
    {job_analysis}

    CV ANALYSIS:
    {cv_analysis}

    MATCHING REPORT:
    {matching_report}

    APPLICATION:
    {application}

    INTERVIEW PREPARATION:
    {interview_preparation}
    """,

    expected_output="""
    A final review containing:
    - Approved items
    - Items to fix
    - Missing information
    - Final recommendations
    """,

    agent=reviewer_agent
)
