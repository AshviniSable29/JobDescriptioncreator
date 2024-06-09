#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import os
from sentence_transformers import SentenceTransformer, util
import uuid

# Load pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize an empty DataFrame to store similarity scores
similarity_scores_df = pd.DataFrame(columns=['Candidate ID', 'Name', 'Job Role', 'Precision', 'Recall', 'Similarity Score'])

def compute_similarity(job_description, resume_text):
    # Convert job description and resume to sentence embeddings
    job_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    # Calculate cosine similarity
    cosine_score = util.pytorch_cos_sim(job_embedding, resume_embedding)

    # Return similarity score
    return cosine_score.item()

def calculate_precision_recall(job_role, resume_text):
    # Load job description based on selected job role
    job_description_file = f'job_descriptions/{job_role}.xlsx'
    job_description_df = pd.read_excel(job_description_file)
    job_description = job_description_df.iloc[0]['Job Description']

    # Compute similarity score between job description and resume
    similarity_score = compute_similarity(job_description, resume_text)

    # Determine if the resume is relevant based on a threshold
    if similarity_score > 0.8:  # Adjust the threshold as needed
        return 1, 1  # Relevant resume found
    else:
        return 0, 1  # Relevant resume not found

def submit_resume(job_role, name, experience, education, projects, skills, soft_skills, additional_info):
    # Generate unique candidate ID
    candidate_id = str(uuid.uuid4())

    # Load job description based on selected job role
    job_description_file = f'job_descriptions/{job_role}.xlsx'
    job_description_df = pd.read_excel(job_description_file)
    job_description = job_description_df.iloc[0]['Job Description']

    # Create a dictionary to store candidate details
    candidate_details = {
        'Name': name,
        'Experience': experience,
        'Education': education,
        'Projects': projects,
        'Skills': skills,
        'Soft Skills': soft_skills,
        'Additional Info': additional_info
    }

    # Convert candidate details to a formatted string
    resume_text = "\n".join([f"{key}: {value}" for key, value in candidate_details.items()])

    # Compute similarity score between job description and resume
    similarity_score = compute_similarity(job_description, resume_text)
    precision, recall = calculate_precision_recall(job_role, resume_text)

    # Append similarity score to DataFrame
    global similarity_scores_df
    similarity_scores_df = similarity_scores_df.append({'Candidate ID': candidate_id, 'Name': name, 'Job Role': job_role, 'Precision': precision, 'Recall': recall, 'Similarity Score': similarity_score}, ignore_index=True)

    # Save similarity scores to Excel file
    similarity_scores_df.to_excel('resume_similarity_scores.xlsx', index=False)

    # Show notification
    return "Resume submitted successfully!"

# List job roles from job_descriptions folder
job_roles = [file.split(".")[0] for file in os.listdir('job_descriptions')]

# Streamlit interface
st.title("Submit Your Resume")
st.write("Fill in your details and submit your resume. You will receive a candidate ID upon submission.")

job_role = st.selectbox("Job Role", job_roles)
st.write("Generated Job Description:")
job_description_file = f'job_descriptions/{job_role}.txt'
with open(job_description_file, 'r') as file:
    job_description = file.read()
st.write(job_description)

name = st.text_input("Name")
experience = st.text_input("Experience")
education = st.text_input("Education")
projects = st.text_input("Projects")
skills = st.text_input("Skills")
soft_skills = st.text_input("Soft Skills")
additional_info = st.text_area("Additional Info")

if st.button("Submit Resume"):
    output = submit_resume(job_role, name, experience, education, projects, skills, soft_skills, additional_info)
    st.write(output)


# In[ ]:




