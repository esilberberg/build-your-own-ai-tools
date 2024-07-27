import google.generativeai as genai

#Read Gemini API key into memory.
with open('gemini-api-key.txt') as f:
	genai_api_key = f.read()

#Configure API and select the Gemini 1.5 Flash language model.
genai.configure(api_key=genai_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

def create_anagram(name):
    """Create one anagram of the input name"""
    response = model.generate_content(f"Create one anagram with the letters in this person's name: {name}")
    return response

print(create_anagram("albert einstein"))