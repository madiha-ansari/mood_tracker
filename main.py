import streamlit as st  # Web Interface
import pandas as pd  # Data Manipulation
import datetime  # Date Handling
import csv  # CSV File Operations
import os  # File Handling

# Mood Log File Name
MOOD_FILE = "mood_log.csv"

# Function to Read Mood Data
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])  # Return Empty DataFrame if File Doesn't Exist
    
    # Read CSV and Ensure Header Exists
    data = pd.read_csv(MOOD_FILE, header=0)

    # If Header is Missing, Return Empty DataFrame
    if "Date" not in data.columns or "Mood" not in data.columns:
        return pd.DataFrame(columns=["Date", "Mood"])
    
    return data

# Function to Save Mood Data
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)
    
    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        # Add Header if File is Empty
        if not file_exists or os.stat(MOOD_FILE).st_size == 0:
            writer.writerow(["Date", "Mood"])

        writer.writerow([date, mood])

# Streamlit App Title
st.title("Mood Tracker")

# Get Today's Date
today = datetime.date.today()

# Mood Selection
st.subheader("How are you feeling today?")
mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

# Log Mood Button
if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

# Load Existing Data
data = load_mood_data()

# Display Mood Trends if Data Exists
if not data.empty:
    st.subheader("Mood Trends Over Time")

    # Convert Date Column to datetime
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')

    # Count Mood Frequencies
    mood_counts = data["Mood"].value_counts()

    # Display Bar Chart
    st.bar_chart(mood_counts)

    # Footer
    
    st.write("Build with ❤️ by [Madiha Ansari](https://github.com/madiha-ansari/mood_tracker)")
