import streamlit as st
import pandas as pd
import gspread
import environ

from oauth2client.service_account import ServiceAccountCredentials
from langchain import OpenAI
from langchain.agents import create_pandas_dataframe_agent
from retrying import retry


# OpenAPI Key
env = environ.Env()
environ.Env.read_env()
API_KEY = env("apikey")


# Site Introduction
st.title("Yobi Sales Insight")
st.write("This app allows you to query sales data from a Google Sheets Excel sheet and get insights using natural language queries. It leverages the Google Sheets API, Langchain, and Pandas DataFrame to provide a simple and interactive interface for analyzing sales data.")


# Data Sheet Link
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1viQNYFx4bf7gRAClcrgYRk3nampO7O1usrvmNX95utk/edit#gid=1051128796"
link_text = "Link to the Sales Data"
st.markdown(f"[{link_text}]({spreadsheet_url})")


# Example Queries
query_list = [
    "Tell me details about the 100th sale.",
    "Which country has the most sales count?",
    "What is the average unit price of the sales?",
    "Tell me about some interesting facts about the sales data."
]
st.write("Example Queries:")
st.write("- " + "\n- ".join(query_list))


# Load credentials from the JSON file
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)


# Authorize the client using the credentials
client = gspread.authorize(credentials)


# Access the Google Sheets Excel sheet by its URL
sheet = client.open_by_url(spreadsheet_url).sheet1


# Read data from the sheet
data = sheet.get_all_values()


# Ouery Textbox
query = st.text_area("Insert Query")


# Retry settings
@retry(stop_max_attempt_number=3)
def get_response():

    # Create an OpenAI object.
    llm = OpenAI(openai_api_key=API_KEY)

    # Read the CSV file into a Pandas DataFrame.
    df = pd.DataFrame(data[1:], columns=data[0])

    # Create a Pandas DataFrame agent.
    agent =  create_pandas_dataframe_agent(llm, df, verbose=True)

    # Query the agent.
    return agent.run(query)


# Submit Query
if st.button("Submit Query", type="primary"):
    try:
        # Get the response
        response = get_response()

        # Write the response to the Streamlit app.
        st.write(response)

    except Exception as e:
        # Write the exception to the Streamlit app.
        st.write(f"An error occurred: {e}")
