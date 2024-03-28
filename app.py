import pandas as pd
import streamlit as st

# Function to identify good values
def is_good_value(value, good_values):
    return value in good_values

# Function to process the spreadsheet
def process_spreadsheet(file, value_column, good_values):
    df = pd.read_excel(file)  # Assuming the file is in Excel format, change if different
    df['Good Value'] = df[value_column].apply(lambda x: is_good_value(x, good_values))
    return df

# Main function to run the Streamlit app
def main():
    st.title("Excel Value Checker App")

    uploaded_file = st.file_uploader("Upload a spreadsheet", type=["xlsx", "xls"])
    if uploaded_file is not None:
        # Read the uploaded spreadsheet
        df = pd.read_excel(uploaded_file, nrows=1)  # Read only first row to get column names
        columns = df.columns.tolist()

        # Let user select the column containing the values
        value_column = st.selectbox("Select the column containing the values", options=columns)

        # Allow user to input good values
        good_values_input = st.text_input("Enter the good values separated by commas (e.g., value1,value2,value3)")
        good_values = [value.strip() for value in good_values_input.split(",")]

        if st.button("Process"):
            with st.spinner("Processing..."):
                df_processed = process_spreadsheet(uploaded_file, value_column, good_values)

            st.write("Original Data:")
            st.write(df)

            st.write("Highlighted Data:")
            st.write(df_processed[df_processed['Good Value'] == False])

            # List values not provided in the list of good values
            values_not_provided = df_processed.loc[~df_processed[value_column].isin(good_values), value_column].unique()
            if len(values_not_provided) > 0:
                st.write("Values not provided in the list of good values:")
                st.write(values_not_provided)
            else:
                st.write("All values are good!")

if __name__ == "__main__":
    main()
