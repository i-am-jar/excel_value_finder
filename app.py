import pandas as pd
import streamlit as st

# Function to identify good codes
def is_good_code(code, good_codes):
    return code in good_codes

# Function to process the spreadsheet
def process_spreadsheet(file, code_column, good_codes):
    df = pd.read_excel(file)  # Assuming the file is in Excel format, change if different
    df['Good Code'] = df[code_column].apply(lambda x: is_good_code(x, good_codes))
    return df

# Main function to run the Streamlit app
def main():
    st.title("Excel Value Checker App")

    uploaded_file = st.file_uploader("Upload a spreadsheet", type=["xlsx", "xls"])
    if uploaded_file is not None:
        # Read the uploaded spreadsheet
        df = pd.read_excel(uploaded_file, nrows=1)  # Read only first row to get column names
        columns = df.columns.tolist()

        # Let user select the column containing the codes
        code_column = st.selectbox("Select the column containing the codes", options=columns)

        # Allow user to input good codes
        good_codes_input = st.text_input("Enter the good codes separated by commas (e.g., code1,code2,code3)")
        good_codes = [code.strip() for code in good_codes_input.split(",")]

        if st.button("Process"):
            st.write("Processing...")

            df_processed = process_spreadsheet(uploaded_file, code_column, good_codes)
            
            st.write("Original Data:")
            st.write(df)

            st.write("Highlighted Data:")
            st.write(df_processed[df_processed['Good Code'] == False])

if __name__ == "__main__":
    main()
