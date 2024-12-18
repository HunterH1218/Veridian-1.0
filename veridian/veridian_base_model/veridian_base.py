import os
import google.generativeai as genai

# Basic Configuration
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join('veridian', 'training_data', 'veridian_base.txt')
with open(file_path, 'r') as file:
  training_data = file.read()

memory = []

generation_config = {
  "temperature": 0.85,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config
)

# Function to generate a response from the model
def generate_response(prompt):
  response = model.generate_content([
    training_data,
    f"{memory}",
    f"input: {prompt}",
    "output: ",
  ])
  memory.append(f"input: {prompt}\n")
  memory.append(f"output: {response.text}\n")
  return response.text
