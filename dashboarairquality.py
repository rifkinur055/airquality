import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
all_data = pd.read_csv('all_data.csv')
def main():
    # Add a title to the app
    districts = all_data['station'].unique()
    selected_district = st.sidebar.selectbox('Select a district', districts)
    selected_data = all_data[all_data['station'] == selected_district]
    avg_pm25 = selected_data['PM2.5'].mean()
    avg_pm10 = selected_data['PM10'].mean()
    avg_so2 = selected_data['SO2'].mean()
    avg_no2 = selected_data['NO2'].mean()
    st.write(f'### Average PM2.5, PM10, SO2, and NO2 for {selected_district}')
    avg_pm_dict = {'PM2.5': [avg_pm25], 'PM10': [avg_pm10], 'SO2': [avg_so2], 'NO2': [avg_no2]}
    avg_df = pd.DataFrame.from_dict(avg_pm_dict, orient='index', columns=['Average'])
    st.bar_chart(avg_df)
    

if __name__ == '__main__':
    st.title('Air Quality Analysis')
    st.write('Select a district from the sidebar to see its average pollution value.')
    main()
