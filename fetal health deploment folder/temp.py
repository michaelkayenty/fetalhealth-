import streamlit as st 
import pickle

# Load the pre-trained model
model = pickle.load(open('C:/Users/Michael Kayentey/OneDrive/Desktop/project 1/gradient_boosting_model.pkl', 'rb'))

def main():
    st.title('Fetal Health Prediction Solution')

    # Input variables 
    baseline_value = st.text_input('Baseline Value')
    accelerations = st.text_input('Accelerations')
    fetal_movement = st.text_input('Fetal Movement')
    uterine_contractions = st.text_input('Uterine Contractions')
    light_decelerations = st.text_input('Light Decelerations')
    severe_decelerations = st.text_input('Severe Decelerations')
    prolongued_decelerations = st.text_input('Prolongued Decelerations')
    abnormal_short_term_variability = st.text_input('Abnormal Short Term Variability')
    mean_value_of_short_term_variability = st.text_input('Mean Value of Short Term Variability')
    percentage_of_time_with_abnormal_long_term_variability = st.text_input('Percentage of Time with Abnormal Long Term Variability')
    mean_value_of_long_term_variability = st.text_input('Mean Value of Long Term Variability')
    histogram_width = st.text_input('Histogram Width')
    histogram_min = st.text_input('Histogram Min')
    histogram_max = st.text_input('Histogram Max')
    histogram_number_of_peaks = st.text_input('Histogram Number of Peaks')
    histogram_number_of_zeroes = st.text_input('Histogram Number of Zeroes')
    histogram_mode = st.text_input('Histogram Mode')
    histogram_mean = st.text_input('Histogram Mean')
    histogram_median = st.text_input('Histogram Median')
    histogram_variance = st.text_input('Histogram Variance')
    histogram_tendency = st.text_input('Histogram Tendency')

    # Prediction code
    if st.button('Predict'):
        prediction = model.predict([[baseline_value, accelerations, fetal_movement, uterine_contractions, 
                                     light_decelerations, severe_decelerations, prolongued_decelerations, 
                                     abnormal_short_term_variability, mean_value_of_short_term_variability, 
                                     percentage_of_time_with_abnormal_long_term_variability, mean_value_of_long_term_variability, 
                                     histogram_width, histogram_min, histogram_max, histogram_number_of_peaks, 
                                     histogram_number_of_zeroes, histogram_mode, histogram_mean, histogram_median, 
                                     histogram_variance, histogram_tendency]])
        output = round(prediction[0])  # Assuming your model outputs class indices
        st.success(f'Your fetal health condition is {output}')

if __name__ == '__main__':
    main()

