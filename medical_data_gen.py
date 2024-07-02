from flask import request, Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from flask import Flask, Response, json
#from webargs.flaskp

from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_experimental.tabular_synthetic_data.openai import (
    OPENAI_TEMPLATE,
    create_openai_data_generator,
)
from langchain_experimental.tabular_synthetic_data.prompts import (
    SYNTHETIC_FEW_SHOT_PREFIX,
    SYNTHETIC_FEW_SHOT_SUFFIX,
)
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.pydantic_v1 import BaseModel
import json
import pandas as pd


# app = Flask(__name__)
# api = Api(app)
# CORS(app)

class MedicalBilling(BaseModel):
    patient_id: int
    patient_name: str
    diagnosis_code: str
    procedure_code: str
    total_charge: float
    insurance_claim_amount: float

examples = [
    {
        "example": """Patient ID: 123456, Patient Name: John Doe, Diagnosis Code: 
        J20.9, Procedure Code: 99203, Total Charge: $500, Insurance Claim Amount: $350"""
    },
    {
        "example": """Patient ID: 789012, Patient Name: Johnson Smith, Diagnosis 
        Code: M54.5, Procedure Code: 99213, Total Charge: $150, Insurance Claim Amount: $120"""
    },
    {
        "example": """Patient ID: 345678, Patient Name: Emily Stone, Diagnosis Code: 
        E11.9, Procedure Code: 99214, Total Charge: $300, Insurance Claim Amount: $250"""
    },
]

OPENAI_TEMPLATE = PromptTemplate(input_variables=["example"], template="{example}")

prompt_template = FewShotPromptTemplate(
    prefix=SYNTHETIC_FEW_SHOT_PREFIX,
    examples=examples,
    suffix=SYNTHETIC_FEW_SHOT_SUFFIX,
    input_variables=["subject", "extra"],
    example_prompt=OPENAI_TEMPLATE,
)
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
repo_id = "google/flan-t5-xxl"
repo_id = "huggingfaceh4/zephyr-7b-alpha"
# synthetic_data_generator = create_openai_data_generator(
#     output_schema=MedicalBilling,
#     llm=HuggingFaceEndpoint(
#     repo_id=repo_id,
    
#     #temperature = 0.5,
#     # model_kwargs={
#     # "temperature":0.5},
#     huggingfacehub_api_token="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",timeout=300
# ),
#     prompt=prompt_template,
# )

synthetic_data_generator = create_openai_data_generator(
    output_schema=MedicalBilling,
    llm=AzureChatOpenAI(model="",
            api_key="",
            azure_endpoint="",
            api_version="",
                
                 max_tokens=1500, temperature=0.3
    ),  # You'll need to replace with your actual Language Model instance
    prompt=prompt_template,
)



#@app.route('/create_data', methods=['POST'])
def automation_execution(data):
    
    
    #json_data = request.get_json()
    #cond_num_records  = json_data['Num_Records']
    cond_num_records  = data['Num_Records']
    condition = data["condition"]
    

    synthetic_results = synthetic_data_generator.generate(
    subject="medical_billing",
    extra=f"""Make sure that the data is as close as to the real world data by following scenario following the examples provided.{condition}""",
    runs=cond_num_records,
    )

    output = {"output":[{"patient_id":i.patient_id,"patient_name":i.patient_name," diagnosis_code":i. diagnosis_code, "procedure_code":i.procedure_code, "total_charge":i.total_charge, "insurance_claim_amount":i.insurance_claim_amount} for i in synthetic_results]}
    return output
# if __name__ == '__main__':
#      app.run(host='0.0.0.0',port='2080',debug=True)