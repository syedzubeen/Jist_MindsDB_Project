from flask import Flask, request, render_template
from flask_session import Session  # Flask-Session for session management

import fitz  # PyMuPDF for PDFs
import os, requests, asyncio, re
from docx import Document  # python-docx for DOCs

app = Flask(__name__)

# Configure the Flask-Session extension
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Variable to hold the content of uploaded files
file_content = ""
file_uploaded = False


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    
    global file_content, file_uploaded
    
    username, password = read_env_vars()

    if username is None or password is None:
        return "Credentials not found."

    if request.method == 'POST':
        if 'uploadfile' in request.form:  # Check if the "Upload File" button was clicked
            uploaded_file = request.files['file']

            if uploaded_file:
                # Check the file extension
                if uploaded_file.filename.endswith('.pdf'):
                    # For PDF files
                    pdf_text = read_pdf(uploaded_file)
                    file_content = pdf_text
                elif uploaded_file.filename.endswith('.docx'):
                    # For DOC files
                    docx_text = read_docx(uploaded_file)
                    file_content = docx_text
                else:
                    return "Unsupported file format. Please upload a PDF or DOCX file."
                
                # Mark that a file has been uploaded
                file_uploaded = True
       
        # Check if the "Summarize" button was clicked
        elif 'summarizebutton' in request.form:
            if not file_uploaded:
                return "Please upload a file before summarizing."
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            summarizer_response = None

            summarizer_response = loop.run_until_complete(summarizer(username, password, file_content))
            
            loop.close()

            # Clear the file upload flag to allow re-uploading
            file_uploaded = False

            return render_template('index.html', content=file_content, summarizer_response=summarizer_response)
    
    return render_template('index.html', content=file_content, summarizer_response=None)
    

def read_pdf(uploaded_file):
    text = ""
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype='pdf')
    for page in pdf_document:
        text += page.get_text()
    return text

def read_docx(uploaded_file):
    text = ""
    doc = Document(uploaded_file)
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

def read_env_vars():
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    env_file_path = os.path.join(current_file_directory, 'env_vars.txt')

    username = None
    password = None

    with open(env_file_path) as file:
        for line in file:
            key, value = line.strip().split('=')
            if key == 'USERNAME':
                username = value
            elif key == 'PASSWORD':
                password = value

    return username, password

async def summarizer(username, password, paper):
    session = requests.Session()
    session.post('https://cloud.mindsdb.com/cloud/login', json={
        'email': username,
        'password': password
    })

    
    input_string = paper
    cleaned_string = re.sub(r'[^a-zA-Z .]', '', input_string)
    print(cleaned_string)

    custom_query = "SELECT answer FROM project_summary_gen.summaries WHERE question = 'You are a scientist and a researcher who understands scientific research papers and provide concise summaries of each paper. You aim is to generate a summary of the paper in 5-10 lines, capturing the key findings and contributions, followed by 5 key points from the paper presented in a bullet format. You should be able to handle research papers from various domains and adapt to the specific terminology and structure of the paper and should also prioritize the most relevant information and avoid excessive repetition in the summaries. The contents of the paper are long and I will send you the its contents in chunks and here is the first one: " + cleaned_string + "';"
    resp = session.post('https://cloud.mindsdb.com/api/sql/query', json={'query': custom_query})
    
    json_response = resp.json()
    print("json response is:\n")
    #print (json_response)
    # Assuming there's only one element in the inner list
    summarised = json_response['data'][0][0]  
    #print("summarised response is:\n")
    #print (json_response)
    # Remove special characters from start and end
    summarised = summarised.strip('[\n]').strip()
    #print("stripped response is:\n")
    #print (json_response)
    #Debug and print value
    print(summarised)

    if resp.status_code == 200:
        return summarised
    else:
        return 'Error fetching your summary'


if __name__ == '__main__':
    app.run(debug=True)
