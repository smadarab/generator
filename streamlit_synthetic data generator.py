import streamlit as st
import requests
import pandas as pd
import io
import base64
import json
# Set page title and icon
st.set_page_config(page_title="Synthetic Data Generator", page_icon=":bar_chart:")
import visualisation as vs
import medical_data_gen as dg

# Title with some styling
st.title("Synthetic Data Generator")
st.markdown("---")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = df.rename(columns={i:i.strip().replace(" ", "_") for i in df.columns})
    df=df.iloc[:10]
    input_string =df.to_json(orient="records")
    input_string = input_string.replace("'", '"')
    json_data = json.loads(input_string)
    examples = [{"example":str(i).replace("'","").strip("{}")} for i in json.loads(input_string)]
    # Input box for number of records to generate
    condition = st.text_input("Enter condition to be applied on synthetic data")
    num_records = st.number_input("Number of records to generate:", min_value=1, value=1)

#@st.cache_data
def request_model(data):
    output = dg.automation_execution(data)
    return output
    #return requests.post("http://127.0.0.1:2080/create_data", json=data)

# Submit button
if st.button("Submit"):
    # JSON data

    data = {
        "Num_Records": num_records,
        "examples":examples,
        "condition":condition
    }
    
    # POST request to endpoint
    response = request_model(data)
     
    
    # Check response status
    if response:
        st.success("Data successfully submitted!")
        st.write("Response data:")
        import ast
        import json
        #output = response.json()["output"]
        output = response["output"]
       #output = [json.loads(i) for i in output]
        st.json(output)
        #response_data = response.json() # Display response JSON data
        import ast
        #val = ast.literal_eval(response_data["output"])
        df_out=pd.DataFrame(output) 
        csv = df_out.to_csv(index=False).encode('utf-8')
        records_len = df_out.shape[0]
        visualizations = vs.create_report(df.iloc[:records_len],df_out)
        #vs.create_report(df.iloc[:records_len],df_out)
        st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
       

    else:
        st.error("Failed to submit data. Please try again.")
