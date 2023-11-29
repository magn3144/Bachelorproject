import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
from datasets import load_dataset


def get_response(system_prompt, user_prompt, model):
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content

def get_prompt(dataset, index):
    return dataset[index] + " ### Response: ```"


folder_name = "final_model"
dataset_name = "magnus42/GPTWebScrapingPythonCode"
base_model_name = "codellama/CodeLlama-7b-Python-hf"
save_directory = f"trained_models/{folder_name}"
test_set = load_dataset(dataset_name, split="test")["prompt"]
response_dict = {}

        prompt = get_prompt(test_set, i)
        print(prompt)
        print("-------------------")
        response = generate_response(prompt)
        response_dict.setdefault(finetune_name, []).append(response)

# Save the respose_dict as a json file using json.dump
with open(f"trained_models/{folder_name}/generated_responses.json", "w") as file:
    json.dump(response_dict, file)