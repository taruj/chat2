import streamlit as st
import pandas as pd
import numpy as np 

try:
    from ctransformers import AutoModelForCausalLM
    print("ctransformers is installed correctly.")
except ImportError:
    print("ctransformers is not installed correctly.")

import os
print(os.path.exists('/Users/taruj/Documents/chat2/src/llm/llama-2-7b-chat.Q8_0.gguf'))



llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7b-Chat-GGUF", 
                                           model_file='/Users/taruj/Documents/chat2/src/llm/llama-2-7b-chat.Q8_0.gguf', 
                                           model_type="llama", 
                                           gpu_layers=0)

# llm2 = 


input_ = None
while input_ != 'end':
    input_ = input("Enter your question: ")
    print(llm(input_))
    


# Title of the app
st.title("Streamlit Demo App")

# Adding a slider
slider_val = st.slider("Select a value", 0, 100, 50)
st.write("Selected value:", slider_val)

# Adding a text input
text_val = st.text_input("Enter some text")
st.write("Entered text:", text_val)

# Generate a random DataFrame and display it
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)
st.write("Randomly generated DataFrame:")
st.dataframe(data)

# Plotting data
st.line_chart(data)

# Interactive checkbox to show/hide data
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)


# looking for the list of employees of "Mismo Systems LLP", New Delhi, India.
#  Here are some of the best ways to find employee directory:
# 1. Check the company's website: Many companies, including Mismo Systems LLP, have an employee directory section on their website. You can check the website and look for the employee directory link.
# 2. Contact HR department: You can reach out to the HR department of Mismo Systems LLP and ask for the employee directory. They may provide you with a list of employees or direct you to the appropriate person who can help you.
# 3. Use LinkedIn: LinkedIn is a professional networking site where many companies, including Mismo Systems LLP, have a presence. You can search for employees of Mismo Systems LLP on LinkedIn and see their profiles.
# 4. Check with the state government: If you are looking for employees of a specific office or location of Mismo Systems LLP, you can check with the state government's labor department or business registration office. They may have a list of employees for that location.
# 5. Use people search websites: There are several people search websites available online that can help you find employee directory of Mismo Systems LLP. Some popular options include LinkedIn, ZoomInfo, and Data.com.