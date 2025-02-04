# 🤖 AI Career Coach  

An AI-powered career coaching assistant designed to provide personalized career guidance, cover letter reviews, resume updates, and instant Q&A assistance. Built with IBM Machine Learning and Gradio, this tool offers an interactive and accessible career development experience.  

## 🚀 Features  
- 📌 **Career Guidance** – AI-driven insights tailored to user skills, experience, and goals.  
- 📄 **Cover Letter Review** – AI-powered feedback to refine and improve cover letters.  
- 📝 **Resume Optimization** – Helps users enhance and optimize resumes for job applications.  
- ❓ **Q&A Assistance** – Instant answers to career-related questions.  

## 🛠️ Tech Stack  
- **AI & Machine Learning:** IBM Machine Learning  
- **Interface:** Gradio for an interactive UI  
- **Backend:** Python (Flask/FastAPI)  
- **Database:** Cloud-based storage (IBM Cloud)  

## 📦 Installation  

Clone the repository:  
```sh
git clone https://github.com/yourusername/your-repo.git
cd your-repo

Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

Install dependencies:
pip install -r requirements.txt

⚙️ Configuration 

Set up IBM Machine Learning credentials by creating a .env file in the project directory:
IBM_API_KEY=your_api_key
IBM_WML_URL=your_wml_url

Load environment variables in Python:
from dotenv import load_dotenv
import os

load_dotenv()
IBM_API_KEY = os.getenv("IBM_API_KEY")

🚀 Usage

Start the Backend

Run the application using your Python version and script name. Replace python3.11 with your installed Python version and qna.py with your main application script:
python3.11 qna.py

docker build -t ai-career-coach .
docker run -p 8000:8000 ai-career-coach
