from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.utils.enums import ModelTypes, DecodingMethods
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

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

q = "How to be a good data scientist?"
generated_response = model.generate(prompt=q)
print(generated_response['results'][0]['generated_text'])


