#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Required Libraries
import pandas as pd
import numpy as np

# Load the dataset
recommendations_df = pd.read_csv('Curriculum_Improvement_Recommendations.csv')

# Fill missing values
recommendations_df.fillna('Unknown', inplace=True)

# Feature Engineering: Create a column for "Skill Gaps Match" (i.e., areas where both employers and graduates identify gaps)
recommendations_df['Skill Gap Match'] = recommendations_df.apply(lambda row: row['Skill Gaps Identified_x'] == row['Skill Gaps Identified_y'], axis=1)

# Filter the rows where both employers and graduates identified skill gaps
gaps_df = recommendations_df[recommendations_df['Skill Gap Match'] == False]

# Grouping data by the program to summarize the identified skill gaps
curriculum_suggestions = gaps_df.groupby('Program Title')['Skill Gaps Identified_x'].apply(lambda x: ', '.join(set(x))).reset_index()

# Display the resulting dataset
print(curriculum_suggestions)


# In[2]:


# Simple Rule-Based Recommendation Function
def recommend_curriculum(program_title):
    recommendation = curriculum_suggestions[curriculum_suggestions['Program Title'] == program_title]
    if not recommendation.empty:
        return f"For {program_title}, the identified gaps are: {recommendation['Skill Gaps Identified_x'].values[0]}"
    else:
        return f"No significant gaps identified for {program_title}"

# Example usage
print(recommend_curriculum('Electrical Engineering'))


# In[3]:


#pip install streamlit


# In[4]:


import streamlit as st
import pandas as pd

# Load the dataset
recommendations_df = pd.read_csv('Curriculum_Improvement_Recommendations.csv')

# Fill missing values
recommendations_df.fillna('Unknown', inplace=True)

# Feature Engineering
recommendations_df['Skill Gap Match'] = recommendations_df.apply(lambda row: row['Skill Gaps Identified_x'] == row['Skill Gaps Identified_y'], axis=1)

# Filter the rows where both employers and graduates identified skill gaps
gaps_df = recommendations_df[recommendations_df['Skill Gap Match'] == False]

# Grouping data by the program to summarize the identified skill gaps
curriculum_suggestions = gaps_df.groupby('Program Title')['Skill Gaps Identified_x'].apply(lambda x: ', '.join(set(x))).reset_index()

# Streamlit UI
st.title('Curriculum Recommendation Dashboard')

# Dropdown to select the program
program_title = st.selectbox('Select a Program', curriculum_suggestions['Program Title'].unique())

# Function to recommend curriculum improvements
def recommend_curriculum(program_title):
    recommendation = curriculum_suggestions[curriculum_suggestions['Program Title'] == program_title]
    if not recommendation.empty:
        return f"For {program_title}, the identified gaps are: {recommendation['Skill Gaps Identified_x'].values[0]}"
    else:
        return f"No significant gaps identified for {program_title}"

# Display recommendation based on selected program
st.write(recommend_curriculum(program_title))

# Display raw data option
if st.checkbox('Show Raw Data'):
    st.write(recommendations_df)


# In[5]:streamlit run curriculum_dashboard.py





# In[ ]:import streamlit as st
import pandas as pd

# Load the dataset
recommendations_df = pd.read_csv('Curriculum_Improvement_Recommendations.csv')

# Fill missing values
recommendations_df.fillna('Unknown', inplace=True)

# Feature Engineering
recommendations_df['Skill Gap Match'] = recommendations_df.apply(lambda row: row['Skill Gaps Identified_x'] == row['Skill Gaps Identified_y'], axis=1)

# Filter the rows where both employers and graduates identified skill gaps
gaps_df = recommendations_df[recommendations_df['Skill Gap Match'] == False]

# Grouping data by the program to summarize the identified skill gaps
curriculum_suggestions = gaps_df.groupby('Program Title')['Skill Gaps Identified_x'].apply(lambda x: ', '.join(set(x))).reset_index()

# Streamlit UI
st.title('Curriculum Recommendation Dashboard')

# Dropdown to select the program
program_title = st.selectbox('Select a Program', curriculum_suggestions['Program Title'].unique())

# Function to recommend curriculum improvements
def recommend_curriculum(program_title):
    recommendation = curriculum_suggestions[curriculum_suggestions['Program Title'] == program_title]
    if not recommendation.empty:
        return f"For {program_title}, the identified gaps are: {recommendation['Skill Gaps Identified_x'].values[0]}"
    else:
        return f"No significant gaps identified for {program_title}"

# Display recommendation based on selected program
st.write(recommend_curriculum(program_title))

# Display raw data option
if st.checkbox('Show Raw Data'):
    st.write(recommendations_df)






# %%
