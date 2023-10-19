import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(system_prompt, user_prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content