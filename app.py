import pandas as pd
import streamlit as st

#Function that identifies "good" codes
def is_good_code(code):
    good_codes = ['THE VALUE YOU WANT TO LOOK FOR HERE'] #Add "good codes" here
    return code in good_codes

#Function to process spreadsheet
def process_spreadsheet(file):
    df = pd.read_excel(file) #Change this function depending on spreadsheet format
    df['Good Code'] = df['PUT NAME OF COLUMN HERE'].apply(is_good_code)
    return df

#Streamlit app
def main():
    st.title("Find the good codes!!!!!!")

    uploaded_file = st.file_uploader("Upload a spreadsheet", type=["xlsx", "xls"])
    if uploaded_file is not None:
        st.write("Processing...")

        df = process_spreadsheet(uploaded_file)

        st.write("Original Data:")
        st.write(df)

        st.write("Highlighted Data:")
        st.write(df[df['Good Code'] == False])

if __name__ == "__main__":
     main()

