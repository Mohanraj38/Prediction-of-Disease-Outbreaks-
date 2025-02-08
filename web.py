import os
import pickle 
import streamlit as st    
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout="centered",
                   page_icon="bookmark_tabs")
diabetes_model= pickle.load(open(r"Saved models/diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"Saved models/heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"Saved models/parkinsons_model.sav",'rb'))


with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['PROJECT OVERVIEW','DIABETES PREDICTION','HEART DISEASE PREDICTION','PARKINSONS DISEASE PREDICTION'])
if selected == 'PROJECT OVERVIEW':
    st.title('Prediction of Disease Outbreak System')
    st.markdown("""
    ## Project Overview
    
    This project aims to predict the likelihood of disease outbreaks using machine learning models. The system currently supports predictions for the following diseases:
    
    - **Diabetes**: Predicts whether a person is diabetic based on health metrics such as glucose level, blood pressure, BMI, etc.
    - **Heart Disease**: Predicts the likelihood of heart disease based on factors like age, cholesterol levels, blood pressure, etc.
    - **Parkinson's Disease**: Predicts the likelihood of Parkinson's disease based on various health indicators.
    
    ### How It Works
    The system uses pre-trained machine learning models to make predictions. Users can input their health data, and the system will provide a prediction based on the model's analysis.
    
    ### Models Used
    - **Diabetes Prediction Model**: Trained on the Pima Indians Diabetes Dataset.
    - **Heart Disease Prediction Model**: Trained on the Cleveland Heart Disease Dataset.
    - **Parkinson's Disease Prediction Model**: Trained on the Parkinson's Disease Dataset.
    
    ### Future Enhancements
    - **Expand to More Diseases**: Include predictions for other diseases like cancer, Alzheimer's, etc.
    - **Real-time Data Integration**: Integrate real-time health data from wearable devices for more accurate predictions.
    - **User Profiles**: Allow users to create profiles and track their health over time.
    
    ### Contact Information
    For more information, please contact:
    - **Name**: MohanRaj K
    - **Email**: mohanrajk3838@gmail.com
    """)
if selected =='DIABETES PREDICTION' :
    st.title('DIABETES PREDICTION TOOL')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI  value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreeFunction, Age]
        user_input= [float(x) for x in user_input]
        diab_prediction= diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'
    st.success(diab_diagnosis)
    
if selected =='HEART DISEASE PREDICTION':
    st.title('HEART DISEASE PREDICTION TOOL')
    col1,col2,col3 = st.columns(3)
    with col1:
        Age= st.text_input('AGE')
    with col2:
        Sex= st.text_input('SEX')
    with col3:
        Cp= st.text_input('CP')
    with col1:
        Trestbps = st.text_input('TRESTBPS')
    with col2:
        Chol= st.text_input('CHOLESTRAL')
    with col3:
        Fbs = st.text_input('FBS')
    with col1:
        Restecg= st.text_input('RESTECG')
    with col2:
        Thalac= st.text_input('THALAC')
    with col3:
        Exang= st.text_input('EXANG')
    with col1:
        Oldpeak = st.text_input('OLDPEAK')
    with col2:
        Slope= st.text_input('SLOPE')
    with col3:
        Ca = st.text_input('CA')
    with col1:
        Thal= st.text_input('THAL')
            

    heart_diagnosis = ''
    if st.button('HEART DISEASE PREDICTION'):
        if Sex.lower() == 'male':
            Sex = 1
        elif Sex.lower() == 'female':
            Sex = 0
        else:
            st.error("Please enter 'male' or 'female' for SEX.")
            st.stop()
        user_input=[Age, Sex, Cp, Trestbps, Chol,
                        Fbs, Restecg, Thalac, Exang, Oldpeak, Slope, Ca
                        , Thal]
        user_input= [float(x) for x in user_input]
        heart_prediction= heart_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person may have Heart Disease'  
        else:
            heart_diagnosis = 'The person is healthy'

    st.success(heart_diagnosis)

if selected == 'PARKINSONS DISEASE PREDICTION':  
    st.title('PARKINSONS DISEASE PREDICTION TOOL')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Mdvp = st.text_input('MDVP:Fo(Hz)')
    with col2:
        Mdvp2 = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Mdvp3 = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Mdvp4 = st.text_input('MDVP:Jitter(%)')
    with col5:
        Mdvp5 = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        Mdvp6 = st.text_input('MDVP:RAP')
    with col2:
        Mdvp7 = st.text_input('MDVP:PPQ')
    with col3:
        Jitter = st.text_input('Jitter:DDP')
    with col4:
        Mdvp8 = st.text_input('MDVP:Shimmer')
    with col5:
        Mdvp9 = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        shi = st.text_input('Shimmer:APQ3')
    with col2:
        shi1 = st.text_input('Shimmer:APQ5')
    with col3:
        Mdvp1 = st.text_input('MDVP:APQ')
    with col4:
        shi2 = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')            
    with col5:
        spread2 = st.text_input('Spread2')
    with col1:
        d2 = st.text_input('D2')
    with col2:
        ppe = st.text_input('PPE')    

    diagnosis = ''

    if st.button('Parkinsons Test Result'):  
            user_input = [Mdvp, Mdvp2, Mdvp3, Mdvp4, Mdvp5, Mdvp6, Mdvp7, Jitter, 
                          Mdvp8, Mdvp9, shi, shi1, Mdvp1, shi2, nhr, hnr, rpde, 
                          dfa, spread1, spread2, d2, ppe]
            
            user_input = [float(x) for x in user_input]  

            parkinsons_prediction = parkinsons_model.predict([user_input])  

            if parkinsons_prediction[0] == 1:
                diagnosis = 'The person may have Parkinson’s Disease'
            else:
                diagnosis = 'The person is healthy'
       

    st.success(diagnosis)
