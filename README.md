
# Synthetic Data Generator 
  
This project is a data analysis and report generation tool that uses synthetic data to simulate real-world scenarios. By leveraging the power of Python, Jinja, and Streamlit, it allows users to conduct statistical tests, calculate key metrics, and create informative HTML reports.  
  
The value of this project lies in its ability to assist data scientists and analysts in their data exploration tasks, offering a streamlined way to generate synthetic data, analyze it, and visualize the results. This can be particularly useful in scenarios where real-world data is not available or limited.  
  
The project is designed with simplicity and flexibility in mind, making it easy to adjust according to specific data analysis needs.  
![image](https://github.com/smadarab/generator/assets/62444992/12c71979-e0ae-4d1c-9044-157350af8e80)

  
## Getting Started  
  
Instructions for setting up your project locally. These could include:  

## Prerequisites  
  
This project requires the following software:  
  
- Python 3.7+  
- Pip (Python Package Installer)  
  
This project has been tested on the following system:  
  
- OS: Windows 11 
- CPU: Octa cores  
- Memory: 8GB  
  
Your system specifications may need to be higher depending on the size of your datasets.  
  
## Installation  
  
Follow these steps to set up a development environment:  
  
1. Clone the repository to your local machine
2. Navigate to the project directory
3. create a virtual environment for your project -->python3 -m venv env-->source env/bin/activate
4. Install the required packages from requiremnt.txt file -->pip install -r requirements.txt
5. Run  streamlit_synthetic data generator.py Python script

## How to use

[![Video Demo](https://github.com/smadarab/generator/blob/main/652ec20ffbd9a45bcec81932_image1_11zon_e1fb5dcf77.avif)](https://github.com/smadarab/generator/blob/main/syn.mp4)

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

### Why I Chose GPT-4.0  

In developing my project, I explored various language models to determine which would best suit the needs of the project. After careful consideration, I selected OpenAI's GPT-4.0 model. Below, I outline my reasons for this choice, the advantages and disadvantages of GPT-4.0, and its specifications compared to alternative models such as those provided by Hugging Face.  
  
### Reasons for Choosing GPT-4.0  
GPT-4.0 offers several compelling features that align with the project goals:  
- State-of-the-art performance in natural language understanding and generation.  
- Extensive knowledge base and reasoning capabilities.  
- Improved context retention compared to previous versions.  
  
### Advantages of GPT-4.0  
- **Performance:** GPT-4.0 is designed to generate coherent and contextually relevant text, making it highly effective for tasks requiring natural language understanding and generation.  
- **Scalability:** The model's architecture is conducive to a wide range of applications, from chatbots to content creation.  
- **Community and Support:** Being an OpenAI product, it benefits from a robust support network and community-driven resources.  
  
### Disadvantages of GPT-4.0  
- **Resource Intensive:** Due to its size, GPT-4.0 requires significant computational resources, which may be a constraint for individuals or small teams.  
- **Potential for Bias:** As with all language models, there is a risk of generating biased content, a reflection of biases present in the training data.  
  
### Specifications of GPT-4.0  
- **Parameters:** GPT-4.0 hypothetically has 1.76 trillion parameter parameters, allowing for a nuanced understanding of language.  
- **Tokens:** The model is capable of processing up to context windows of 8,192 and 32,768 tokens tokens in a single prompt, providing an extensive context window for text generation. 
- **Training Data:** It has been trained on a vast and diverse dataset to ensure a broad understanding of various topics.  
  
### Comparison to Hugging Face's Language Models  
Hugging Face provides a suite of models with different capabilities. However, GPT-4.0's hypothetical generative prowess and token processing capacity make it superior for tasks that demand long-form content generation and a sophisticated understanding of context. Its architecture is presumed to support more nuanced text generation than models such as BERT or RoBERTa, making it more suitable for high-quality text generation requirements.  
   
  
### Conclusion  
My decision to utilize GPT-4.0 is based on the model's cutting-edge features and its alignment with the project's objectives. While there are limitations, the advantages of GPT-4.0 make it a fitting choice for the project's success.  
  
  
  
  
  
