import google.generativeai as genai
import pandas as pd

#Read Gemini API key into memory.
with open('gemini-api-key.txt') as f:
    genai_api_key = f.read()

#Configure API and select the Gemini 1.5 Flash language model.
genai.configure(api_key=genai_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def rate_sentiment(text):
    """Rates the positivity of a text on scale of 1-5: 
    5 = Very Positive. 1 = Very Negative.
    """    
    response = model.generate_content(f"Rate the positivity of this student's review of a class on a scale of 1-5, with 1 representing Very Negative and 5 representing Very Positive. Your output should be in the form of a single digit representing your positivity score: {text}") 
    # .text returns just text from Gemini and .strip() removes whitespace.
    return response.text.strip()

# Read student review data into memory.
df = pd.read_csv('student-reviews-dataset.csv')

#Iterate over student reviews with Gemini
df['sentiment_rating'] = df['review'].apply(rate_sentiment)

# Convert sentiment_rating to integer
df['sentiment_rating'] = df['sentiment_rating'].astype(int)

# Use .dtypes to get a summary of data types
result = df.dtypes
print(result)

# Use describe() to get summary statistics of sentiment_rating
summary_statistics = df['sentiment_rating'].describe()
print(summary_statistics)