import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction='''Your name is Codebot.You are a virtual evaluator for coding questions. Given a programming question, some code written by a student, and the programming language, 
your job is to determine whether the code correctly solves the question. If it's correct, simply reply "CORRECT". If it is incorrect, reply "INCORRECT"
and in the next few lines, explain why the code is incorrect using bullet points without giving away the answer. Keep your explanations short.'''
)

history = []
print("Bot: Hi there! I am coding assistant how can i help u?")
while True:

      user_input = input("User: ")
 
      if user_input.lower() == 'exit':
        break
      chat_session = model.start_chat(
        history=history
        
      )

      response = chat_session.send_message(user_input)

      model_response = response.text
      print(f'Bot: {model_response}')
      print()
      history.append({"role": "user", "parts": [user_input]})
      history.append({"role": "model", "parts": [model_response]})