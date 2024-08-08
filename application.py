from flask import Flask, render_template, request
from dotenv import load_dotenv
import os, sqlite3
import google.generativeai as genai

# Load all the env variables
load_dotenv() 

## Configure API Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the prompt

prompt=['''
        You are in expert in converting english questions to SQL query!
        The SQL database has the name STUDENT and has the following columns NAME, CLASS, SECTION and MARKS \n\n For Example, \n Example 1 - How many entries of records are present ?, the SQL command will be something like this SELECT * FROM STUDENT; \n Example 2 - Tell me all students in Gen AI class ?, the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS="Gen AI";
        also the sql code should not have ``` in beginning or end and sql word in output.
        
       ''' 
]
# Function to load Google Gemini and provide SQL query as response

def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# Function to retrive rows from database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    
    conn.commit()
    conn.close()
    
    for row in rows:
        print(row)
    
    return rows

application=Flask(__name__)

@application.route('/')
def index():
    return render_template("index.html")

@application.route('/query', methods=['POST'])
def query():
    if request.method=='POST':
        question=request.form.get('query')
        print(question)
    response = get_gemini_response(question, prompt)
    print(response)
    
    data = read_sql_query(response, "student.db")
    return render_template("index.html", data=data, sql_query=response, question=question)


if __name__=='__main__':
    application.run(debug=True)