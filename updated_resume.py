# Import necessary packages
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
import gradio as gr
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file


model_id = "meta-llama/llama-2-13b-chat"  # Directly specifying the LLAMA2 model

# Set credentials to use the model
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

# Function to polish the resume using the model, making polish_prompt optional
def polish_resume(position_name, resume_content, polish_prompt=""):
    # Check if polish_prompt is provided and adjust the combined_prompt accordingly
    if polish_prompt and polish_prompt.strip():
        prompt_use = f"Given the resume content: '{resume_content}', polish it based on the following instructions: {polish_prompt} for the {position_name} position."
    else:
        prompt_use = f"Suggest improvements for the following resume content: '{resume_content}' to better align with the requirements and expectations of a {position_name} position. Return the polished version, highlighting necessary adjustments for clarity, relevance, and impact in relation to the targeted role."
    
    # Generate a response using the model with parameters
    generated_response = model.generate(prompt_use)
    
    # Extract and return the generated text
    generated_text = generated_response["results"][0]["generated_text"]
    return generated_text

# Create Gradio interface for the resume polish application, marking polish_prompt as optional
resume_polish_application = gr.Interface(
    fn=polish_resume,
    allow_flagging="never", # Deactivate the flag function in gradio as it is not needed.
    inputs=[
        gr.Textbox(label="Position Name", placeholder="Enter the name of the position..."),
        gr.Textbox(label="Resume Content", placeholder="Paste your resume content here...", lines=20),
        gr.Textbox(label="Polish Instruction (Optional)", placeholder="Enter specific instructions or areas for improvement (optional)...", lines=2),
    ],
    outputs=gr.Textbox(label="Polished Content"),
    title="Resume Polish Application",
    description="This application helps you polish your resume. Enter the position your want to apply, your resume content, and specific instructions or areas for improvement (optional), then get a polished version of your content."
)

# Launch the application
resume_polish_application.launch()