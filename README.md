
# Synthetic Data Generator 
  
This project is a data analysis and report generation tool that uses synthetic data to simulate real-world scenarios. By leveraging the power of Python, Jinja, and Streamlit, it allows users to conduct statistical tests, calculate key metrics, and create informative HTML reports.  
  
The value of this project lies in its ability to assist data scientists and analysts in their data exploration tasks, offering a streamlined way to generate synthetic data, analyze it, and visualize the results. This can be particularly useful in scenarios where real-world data is not available or limited.  
  
The project is designed with simplicity and flexibility in mind, making it easy to adjust according to specific data analysis needs.  
![image](https://github.com/smadarab/generator/assets/62444992/12c71979-e0ae-4d1c-9044-157350af8e80)

  
## Getting Started  
  
Instructions for setting up your project locally. These could include:  
  
- Prerequisites: What software needs to be installed and what hardware specifications are needed.  
- Installation: Step-by-step guide to getting a development environment running.  
  
## Usage  
  
Explain how to use your project. Provide code examples or screenshots as necessary.  
  
## Evaluation metrics

This repository contains code for evaluating synthetic data using a variety of metrics:  
   
## Metrics  
   
1. **Distribution Consistency (K-S Test)**  
   - **Description**: Compares the distributions of variables in the synthetic and original data.  
   - **Use**: To check if the synthetic data reproduces the distribution of the original data.  
   - **Inference**: A lower K-S statistic and a higher p-value (e.g., > 0.05) indicate that the distributions of the original and synthetic data are not significantly different.  
   - **Ideal Value**: K-S statistic close to 0, p-value > 0.05  
   - **Formula**: `ks_2samp(data1, data2)` from scipy.stats  
   
2. **Statistical Consistency**  
   - **Description**: Ensures key statistical properties (mean, median, mode, variance, etc.) are preserved in the synthetic data.  
   - **Use**: To verify that the synthetic data maintains the same statistical characteristics as the original data.  
   - **Inference**: The closer the values (mean, variance) between the synthetic and original data, the better.  
   - **Ideal Value**: Similar values for the original and synthetic data  
   - **Formula**: `mean(), var()` functions from pandas  
   
3. **Mutual Information**  
   - **Description**: Measures the amount of information that can be obtained about one variable by observing another.  
   - **Use**: To assess how well the relationships between variables are preserved in the synthetic data.  
   - **Inference**: A high mutual information score indicates a strong relationship between variables.  
   - **Ideal Value**: Similar scores for the original and synthetic data  
   - **Formula**: `mutual_info_score(variable1, variable2)` from sklearn.metrics  
   
4. **Discriminative Score**  
   - **Description**: Evaluates the performance of machine learning models trained on the synthetic data and tested on the original data.  
   - **Use**: To measure the utility of synthetic data in machine learning tasks.  
   - **Inference**: A lower discriminative score (e.g., lower mean squared error in regression tasks) indicates that the model performs well on the original data after being trained on the synthetic data.  
   - **Ideal Value**: Low score for regression tasks (e.g., low mean squared error), high score for classification tasks (e.g., high accuracy)  
   - **Formula**: Depends on the machine learning task and model. For linear regression, you can use `mean_squared_error(y_true, y_pred)` from sklearn.metrics  
   
5. **Re-identification Rate**  
   - **Description**: Measures the proportion of records in the synthetic data that can be matched to a record in the original data.  
   - **Use**: To evaluate the privacy of the synthetic data.  
   - **Inference**: A lower re-identification rate indicates better privacy.  
   - **Ideal Value**: 0 (no records in the synthetic data can be matched to the original data)  
   - **Formula**: `len(reidentified_data) / len(synthetic_data)`  
   
Please refer to the code in this repository for a Python implementation of these metrics.
  

  
## Contributing  
  
If you want others to contribute to your project, provide instructions on how they should do so.  
  
## License  
  
MIT License

Copyright (c) LangChain, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.  
  
## Acknowledgments  
  langchain - https://python.langchain.com/v0.1/docs/additional_resources/tutorials/
  
  synthetic data generator - https://python.langchain.com/v0.1/docs/use_cases/data_generation/
