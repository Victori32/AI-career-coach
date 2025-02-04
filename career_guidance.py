# Import necessary packages
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
import gradio as gr
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

# Model and project settings
model_id = "meta-llama/llama-2-13b-chat"  # Directly specifying the LLAMA2 model

# Set credentials
my_credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
}

watsonx_API = os.getenv("WATSONX_API_KEY")
project_id = os.getenv("PROJECT_ID")

generate_params = {
    GenParams.MAX_NEW_TOKENS: 250
}

model = Model(
    model_id = 'meta-llama/llama-2-13b-chat', # you can also specify like: ModelTypes.LLAMA_2_70B_CHAT
    params = generate_params,
    credentials={
        "apikey": watsonx_API,
        "url": "https://us-south.ml.cloud.ibm.com"
    },
    project_id= project_id
    )

# Function to generate career advice
def generate_career_advice(position_applied, job_description, resume_content):
    # The prompt for the model
    prompt = f"Considering the job description: {job_description}, and the resume provided: {resume_content}, identify areas for enhancement in the resume. Offer specific suggestions on how to improve these aspects to better match the job requirements and increase the likelihood of being selected for the position of {position_applied}."
    
    # Generate response
    generated_response = model.generate(prompt, gen_parms)
    
    # Extract and format the generated text
    advice = generated_response["results"][0]["generated_text"]
    return advice

# Create Gradio interface for the career advice application
career_advice_app = gr.Interface(
    fn=generate_career_advice,
    allow_flagging="never", # Deactivate the flag function in gradio as it is not needed.
    inputs=[
        gr.Textbox(label="Position Applied For", placeholder="Enter the position you are applying for..."),
        gr.Textbox(label="Job Description Information", placeholder="Paste the job description here...", lines=10),
        gr.Textbox(label="Your Resume Content", placeholder="Paste your resume content here...", lines=10),
    ],
    outputs=gr.Textbox(label="Advice"),
    title="Career Advisor",
    description="Enter the position you're applying for, paste the job description, and your resume content to get advice on what to improve for getting this job."
)

# Launch the application
career_advice_app.launch()