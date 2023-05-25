# Yobi Sales Insight

This Streamlit app, "Yobi Sales Insight," allows you to query sales data from a Google Sheets Excel sheet and get insights using natural language queries. It leverages the Google Sheets API, Langchain, and Pandas DataFrame to provide a simple and interactive interface for analyzing sales data.

Live website: https://shihabsarar29-retail-gpt-app-iuhjq9.streamlit.app/ <br>
Sales Data Sheet: https://docs.google.com/spreadsheets/d/1viQNYFx4bf7gRAClcrgYRk3nampO7O1usrvmNX95utk/edit?usp=sharing


## Features

- Displays a link to the Sales Data Google Sheets for reference.
- Provides example queries to get started.
- Allows you to input custom queries using the query textbox.
- Retrieves data from the Google Sheets Excel sheet using the provided credentials.
- Performs natural language queries on the loaded data using the Langchain library.
- Presents the response from the queries in the Streamlit app.

## Setup

To run the app locally, please follow these steps:

1. Install the required dependencies by running the following command:
   pip install -r requirements.txt

2. Replace the `openai_api_key` parameter in the code with your actual OpenAI API key.

3. Replace the `credentials.json` file with your own Google Sheets API credentials file.

4. Run the Streamlit app by executing the following command in the terminal:
   streamlit run app.py

5. Access the app in your browser at the provided local URL (typically http://localhost:8501).


### Happy exploring and analyzing sales data with Yobi Sales Insight!

