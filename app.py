import streamlit as st
import cv2
import numpy as np
import skimage.io as io
import pandas as pd
from skimage import img_as_float
from skimage import filters

favicon = 'favicon.png'

# main page
st.set_page_config(page_title='Gaussian APP', page_icon = favicon, layout = 'wide', initial_sidebar_state = 'auto')
st.title('Applying Gaussain Fillterz !')
st.sidebar.title('My Sidebar')



# add dropdown to select pages on left
app_mode = st.sidebar.selectbox('Navigate',
                                  ['About', 'Apply Filter'])

# About page
if app_mode == 'About':
    st.markdown('Lets USE THE FILLTERZ !')

    st.markdown('''
                ## About -> \n
                We LOOVEEE to apply filterz \n
                SO LETS DO THAT! \n
                Enjoy!
                ''') 

# Run image
if app_mode == 'Apply Filter':
    
    st.sidebar.markdown('---') # adds a devider (a line)
    
    # choosing a k value (either with +- or with a slider)
    sigma_value = st.sidebar.number_input('Insert Sigma value=:', value=1, min_value = 1, max_value = 20) # asks for input from the user
    st.sidebar.markdown('---') # adds a devider (a line)
    
    # attempts_value_slider = st.sidebar.slider('Number of attempts', value = 7, min_value = 1, max_value = 10) # slider example
    # st.sidebar.markdown('---') # adds a devider (a line)
    
    # read an image from the user
    img_file_buffer = st.sidebar.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

    # assign the uplodaed image from the buffer, by reading it in
    if img_file_buffer is not None:
        image = io.imread(img_file_buffer)
        # display on the sidebar the uploaded image
        st.sidebar.text('Original Image')
        st.sidebar.image(image)
        
        smooth = filters.gaussian(img_as_float(image), sigma=sigma_value)

        # Display the result on the right (main frame)
        st.subheader('Output Image')
        st.image(smooth, use_column_width=True)
        
    else: # if no image was uploaded, then segment the demo image
        st.markdown('noob')

