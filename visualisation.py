import pandas as pd  
import numpy as np  
from scipy import stats  
from sklearn.metrics import mutual_info_score  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error  
import pandas as pd  
import numpy as np  
from scipy import stats  
from sklearn.metrics import mutual_info_score  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error  
import datetime  
from bs4 import BeautifulSoup   


def create_report(original_data,synthetic_data):  
    results = {}  
    
    # Distribution Consistency (K-S Test)  
    for column in ['total_charge', 'insurance_claim_amount']:  
        results[column + '_ks_statistic'], results[column + '_ks_pvalue'] = stats.ks_2samp(  
            original_data[column], synthetic_data[column])  
    
    # Statistical Consistency  
    for column in ['total_charge', 'insurance_claim_amount']:  
        results[column + '_original_mean'] = original_data[column].mean()  
        results[column + '_synthetic_mean'] = synthetic_data[column].mean()  
        results[column + '_original_variance'] = original_data[column].var()  
        results[column + '_synthetic_variance'] = synthetic_data[column].var()  
    
    # Mutual Information  
    for column1 in ['total_charge', 'insurance_claim_amount']:  
        for column2 in ['total_charge', 'insurance_claim_amount']:  
            if column1 != column2:  
                results[column1 + '_and_' + column2 + '_mutual_information'] = mutual_info_score(  
                    original_data[column1], synthetic_data[column2])  
    
    # Discriminative Score (hypothetical example using a linear regression model)  
    X_train, X_test, y_train, y_test = train_test_split(original_data[['total_charge']], original_data['insurance_claim_amount'], test_size=0.2, random_state=42)  
    model = LinearRegression().fit(X_train, y_train)  
    predictions = model.predict(X_test)  
    results['discriminative_score'] = mean_squared_error(y_test, predictions)  
    
    # Privacy Evaluation (simple example: re-identification based on 'total_charge' and 'insurance_claim_amount')  
    reidentified_data = synthetic_data[synthetic_data['total_charge'].isin(original_data['total_charge']) & synthetic_data['insurance_claim_amount'].isin(original_data['insurance_claim_amount'])]  
    results['reidentification_rate'] = len(reidentified_data) / len(synthetic_data)  
    
    # Convert results to a DataFrame  
    results_df = pd.DataFrame([results])  # Wrapping results in a list to create a single-row DataFrame  
    
    # Save as HTML with a timestamp  
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    # Check if the metrics meet the ideal criteria  
    # results_df['ks_test_passed'] = np.where((results_df['ks_statistic'] < 0.05) & (results_df['ks_pvalue'] > 0.05), 'Yes', 'No')  
    # results_df['stat_consistency_passed'] = np.where(abs(results_df['original_mean'] - results_df['synthetic_mean']) < 0.01, 'Yes', 'No')  # Adjust the 0.01 threshold as necessary  
    # results_df['mutual_info_passed'] = np.where(abs(results_df['original_mutual_info'] - results_df['synthetic_mutual_info']) < 0.01, 'Yes', 'No')  # Adjust the 0.01 threshold as necessary  
    # results_df['discriminative_score_passed'] = np.where(results_df['discriminative_score'] < 0.05, 'Yes', 'No')  # Adjust the 0.05 threshold as necessary  
    # results_df['reidentification_rate_passed'] = np.where(results_df['reidentification_rate'] == 0, 'Yes', 'No')  
    # def color_red(val):  
    #     color = 'red' if val == 'No' else 'black'  
    #     return 'color: %s' % color  
  
    # styled_results_df = results_df.style.applymap(color_red)  
    # Open the HTML file and append the new table  
    with open('evaluation_results.html', 'a+') as f:  
        f.write(f'<h2>{timestamp}</h2>')  # Write the timestamp as a new HTML header  
        f.write(results_df.to_html())  # Append the new table  
        # f.seek(0)  # Go to the beginning of the file  
        # soup = BeautifulSoup(f, 'html.parser')  
    
        # # Create a new table with the results and add a timestamp as the table name  
        # new_table = pd.DataFrame.to_html(results_df)  
        # new_table_soup = BeautifulSoup(new_table, 'html.parser')  
        # new_table_soup.table['id'] = timestamp  # Add the timestamp as the table name  
    
        # # Append the new table to the existing HTML  
        # soup.append(new_table_soup)  
    
        # # Write everything back to the file  
        # f.seek(0)  
        # f.write(str(soup))  
        # f.truncate() 
# output = [
#   {
#     " diagnosis_code": "I10",
#     "insurance_claim_amount": 300,
#     "patient_id": 456789,
#     "patient_name": "Alice Brown",
#     "procedure_code": "99204",
#     "total_charge": 450
#   },
#   {
#     " diagnosis_code": "J45.909",
#     "insurance_claim_amount": 160,
#     "patient_id": 123456,
#     "patient_name": "Michael Johnson",
#     "procedure_code": "99203",
#     "total_charge": 200
#   }
# ]
# df_out=pd.DataFrame(output) 
# csv = df_out.to_csv(index=False).encode('utf-8')
# records_len = df_out.shape[0]
# # metrics = vs.compare_statistics(df_out,df.iloc[:records_len])
# # visualizations = vs.visualize_comparison(df_out,df.iloc[:records_len])
# df = pd.read_csv(r"C:\Users\E009819\Documents\synthetic data\medical_dataset.csv")
# df = df.rename(columns={i:i.strip().replace(" ", "_") for i in df.columns})
# #df=df.iloc[:10]   
# records_len = df_out.shape[0]
# create_report(df.iloc[:records_len],df_out)