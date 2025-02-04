# 🤖 AI Career Coach

An AI-powered career coaching assistant designed to provide personalized career guidance, cover letter reviews, resume updates, and instant Q&A assistance. Built with IBM Machine Learning and Gradio, this tool offers an interactive and accessible career development experience.

## 🚀 Features
	•	📌 Career Guidance – AI-driven insights tailored to user skills, experience, and goals.
	•	📄 Cover Letter Review – AI-powered feedback to refine and improve cover letters.
	•	📝 Updated Resume – Helps users enhance and optimize resumes for job applications.
	•	❓ Q&A Assistance – Instant answers to career-related questions.

## 🛠️ Tech Stack
	•	AI & Machine Learning: IBM Machine Learning
	•	Interface: Gradio for an interactive UI
	•	Backend: Python (Flask/FastAPI)
	•	Database: Cloud-based storage (IBM Cloud)

## 📦 Installation  
Clone the repository:  
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo

### Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate

### Install dependencies
pip install -r requirements.txt

## ⚙️ Configuration
Set up IBM Machine Learning credentials by creating a .env file:
IBM_API_KEY=your_api_key
IBM_WML_URL=your_wml_url

Load environment variables in Python:
from dotenv import load_dotenv
import os

load_dotenv()
IBM_API_KEY = os.getenv("IBM_API_KEY")

## 🚀 Usage
Start the Backend:
python app.py ( replace with the version of Python: eg. Python 3.11 and the name of the app eg. qna.py)

