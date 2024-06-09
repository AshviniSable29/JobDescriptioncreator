import streamlit as st

# Define function to generate job description
def generate_job_description(title, key_skills, soft_skills, location, desired_experience, preferred_experience, about_the_team):
    company_name = "Imaginary Inc."
    company_description = "Imaginary Inc. is a forward-thinking company that values innovation, creativity, and diversity. We believe in fostering a positive work environment where every employee can thrive."

    # Construct job description
    job_description = f"""
    **{company_name}** is seeking a **{title}** to join our team.
    
    **About Us:**
    {company_description}
    
    **Location:** {location}
    **Desired Candidate Experience:** {desired_experience} years
    **Preferred Candidate Experience:** {preferred_experience} years
    **Key Skills:** {key_skills}
    **Soft Skills:** {soft_skills}
    
    **About the Team:**
    {about_the_team}
    
    If you're passionate about {key_skills} and {soft_skills}, thrive in a collaborative environment, and are excited about the opportunity to contribute to our team, we want to hear from you!
    """

    return job_description

# Streamlit app UI
st.set_page_config(page_title="Job Description Generator", page_icon=":briefcase:", layout="wide")

st.title("Job Description Generator")

# Create tabs for different sections
tabs = ["Generate Job Description", "About Us"]
selected_tab = st.sidebar.radio("Navigate", tabs)

if selected_tab == "Generate Job Description":
    st.subheader("Fill in Job Details")

    # Input fields for job details
    title = st.text_input("Job Title", help="e.g., Software Engineer, Data Analyst")
    key_skills = st.text_input("Key Skills", help="e.g., Python, Machine Learning, Communication")
    soft_skills = st.text_input("Soft Skills", help="e.g., Teamwork, Problem Solving, Adaptability")
    location = st.text_input("Location", help="e.g., San Francisco, Remote")
    desired_experience = st.slider("Desired Candidate Experience (in years)", min_value=0, max_value=10, value=3)
    preferred_experience = st.slider("Preferred Candidate Experience (in years)", min_value=0, max_value=15, value=5)
    about_the_team = st.text_area("About the Team", help="Provide some information about the team and work culture")

    # Button to trigger job description generation
    if st.button("Generate Job Description"):
        if title and key_skills and location and about_the_team:
            job_description = generate_job_description(title, key_skills, soft_skills, location, desired_experience, preferred_experience, about_the_team)
            st.subheader("Generated Job Description:")
            st.markdown(job_description, unsafe_allow_html=True)
        else:
            st.warning("Please fill in all required fields.")
else:
    st.subheader("About Us")
    st.write("Imaginary Inc. is a forward-thinking company that values innovation, creativity, and diversity. We believe in fostering a positive work environment where every employee can thrive.")

# Additional features
st.sidebar.markdown("---")
st.sidebar.subheader("Additional Features")
if st.sidebar.button("Download as PDF"):
    st.sidebar.success("PDF Downloaded!")
if st.sidebar.button("Share"):
    st.sidebar.success("Shared Successfully!")
if st.sidebar.button("View Source Code"):
    st.sidebar.success("Source Code Viewed!")
