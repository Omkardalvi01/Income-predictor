import pickle
import pandas
import streamlit as st

pickle_in = open('clf.pkl','rb')
clf = pickle.load(pickle_in)

def prediction(age, fnlwgt, education , race,cpt_gain, cpt_loss, work_hours, sex_F, sex_M ):
    prediction = clf.predict( 
        [[age, fnlwgt, education, race, cpt_gain, cpt_loss, work_hours, sex_F, sex_M]]) 
    return prediction

def main():
    st.title('Income predictor')

    age = st.number_input("Age", value=None, min_value=0)
    fnlwgt = st.number_input("fnlwgt",value=None, min_value=0)
    education = st.number_input("Education",value=None, min_value=0)
    cpt_gain = st.number_input("Capital Gain",value=None, min_value=0)
    cpt_loss = st.number_input('Capital Loss',value=None, min_value=0)
    work_hours = st.number_input("Work hours per week",value=None, min_value=0)
    race = st.selectbox('Race', options=['White', 'Black', 'Asian-Pac-Islander','Amer-Indian-Eskimo', 'Other'])
    sex = st.selectbox('Sex', options=['Male', 'Female'])
    result_str =""

    race_in = {"White" : 1, "Black": 2, "Asian-Pac-Islander" : 3, "Amer-Indian-Eskimo" : 4, "Other" : 5}
    sex_in = {"Male" : (0,1) , "Female": (1,0)}


    if age is None or fnlwgt is None or education is None or cpt_gain is None or cpt_loss is None or work_hours is None:
        st.error("Please enter valid numerical values for age, fnlwgt, education, capital gain, capital loss, and work hours.")
        return

    if st.button("Predict"): 
        result = prediction(age,fnlwgt, education,  race_in[race] , cpt_gain, cpt_loss, work_hours, sex_in[sex][0], sex_in[sex][1]) 
        if result == 1:
            result_str = "Yes you make more than 50K"
        else:
            result_str = "No you do not make more than 50K"
    st.success(result_str) 
if __name__ == '__main__':
    main()
