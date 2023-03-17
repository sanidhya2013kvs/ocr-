import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import os
import numpy as np #Image Processing 

#title
st.title("Extract Text from Images")



st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en','hi'])
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    
    w, h = input_image.size
    q=w*h
    t=q/(1024*1024)
    e=t*1.9
    if w<1000 and h<1000 and e<2:
        st.image(input_image) #display image

        with st.spinner("🤖 AI is at Work! "):
        

            result = reader.readtext(np.array(input_image))

            result_text = [] #empty list for results


            for text in result:
                result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
        st.balloons()
    else:
        st.write("please upload max size img 999*999 and size will less than 2 MB")
else:
    st.write("Upload an Image")




    
