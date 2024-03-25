# Excel Value Checker App

This is a simple Streamlit web application for checking values in an Excel spreadsheet. It allows users to upload an Excel file, select the column containing the values, and specify the list of good values. The application then highlights the values in the spreadsheet that are not considered "good".

## Installation

1. Clone this repository: https://github.com/i-am-jar/excel_value_finder
2. Install the required Python packages: pip install pandas streamlit

## Usage

1. Run the Streamlit application: streamlit run app.py
2. Open the provided URL in your web browser.
3. Upload an Excel spreadsheet using the file uploader.
4. Select the column containing the codes from the dropdown menu.
5. Enter the good codes separated by commas into the text input field.
6. Click the "Process" button to highlight the values that are not considered "good".

## Dependencies

- pandas: A powerful data manipulation library.
- streamlit: A library for creating interactive web applications.

## License

This project is licensed under the [MIT License](LICENSE).