import google.generativeai as genai

#Read Gemini API key into memory.
with open('gemini-api-key.txt') as f:
	genai_api_key = f.read()

#Read student review into memory.
with open('student-review-1.txt') as f:
    student_review = f.read()

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

print(rate_sentiment(student_review))