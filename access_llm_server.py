from google.genai import Client

# Initialize the client with your API key
client = Client(api_key="AIzaSyCuZG5ERSlWF0VRa3uXlIGsgj2bkfQkWPI")

# Choose a Gemini model
# e.g., 'gemini-2.5-flash' or 'gemini-2.0-flash'
model_name = "gemini-2.5-flash"

# Prompt you want to generate text for
prompt = "Explain in simple words how AI works."

# Generate content
response = client.models.generate_content(
    model=model_name,
    contents=prompt
)

print("=== Gemini AI Response ===")
print(response.text)