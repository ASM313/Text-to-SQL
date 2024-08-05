from dotenv import load_dotenv

# Load all the env variables
load_dotenv() 

import streamlit as st
import os, sqlite3
import google.generativeai as genai

## Configure API Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini and provide SQL query as response

def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# Function to retrive rows from database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    
    if sql=='' or sql==None:
        st.subheader("no prompt provided")
    else:
        cur.execute(sql)
        rows = cur.fetchall()
    
    conn.commit()
    conn.close()
    
    for row in rows:
        print(row)
    
    return rows

# Define the prompt

prompt=['''
        You are in expert in converting english questions to SQL query!
        The SQL database has the name STUDENT and has the following columns NAME, CLASS, SECTION and MARKS \n\n For Example, \n Example 1 - How many entries of records are present ?, the SQL command will be something like this SELECT * FROM STUDENT; \n Example 2 - Tell me all students in Gen AI class ?, the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Gen AI";
        also the sql code should not have ``` in beginning or end and sql word in output.
        
       ''' 
]


# question = "print all the rows present in table"

# response = get_gemini_response(question, prompt)
# print(response)

# data = read_sql_query(response, 'student.db')

# for i in data:
#     print(i)


# Streamlit App

st.set_page_config(page_title="Convert ur query to SQL one")
st.header("Ease to Retrieve SQL Data")

question = st.text_input("Input: ", key='input')

submit = st.button("Convert to SQL Query")

# When 'submit' clicked

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    
    data = read_sql_query(response, "student.db")
    st.subheader(f"The response for \n !>>>[ {question} ]<<<! is ")
    for row in data:
        print(row)
        st.header(row)