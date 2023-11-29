from transformers import AutoModelForCausalLM,AutoTokenizer
from peft import PeftModel
import os
import torch
from datasets import load_dataset
import json


def load_finetuned_model(base_model_name, model_directory, finetune_name):
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        low_cpu_mem_usage=True,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map= {"": 0})

    print(model_directory + "/" + finetune_name)
    model = PeftModel.from_pretrained(base_model, model_directory + "/" + finetune_name)
    model = model.merge_and_unload()

    # Reload tokenizer
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    return model, tokenizer

def generate_response(model, tokenizer, prompt):
    runtimeFlag = "cuda:0"
    batch = tokenizer(prompt, return_tensors='pt', return_token_type_ids=False).to(runtimeFlag)
    with torch.cuda.amp.autocast():
        output_tokens = model.generate(**batch, max_new_tokens=2000)
    return tokenizer.decode(output_tokens[0], skip_special_tokens=True)

def get_prompt(dataset, index):
    return dataset[index] + " ### Response: ```"


folder_name = "final_model"
dataset_name = "magnus42/GPTWebScrapingPythonCode"
base_model_name = "codellama/CodeLlama-7b-Python-hf"
save_directory = f"trained_models/{folder_name}"
response_directory = f"trained_models/{folder_name}/responses"
test_set = load_dataset(dataset_name, split="test")["prompt"]
task_names = load_dataset(dataset_name, split="test")["task"]

# For each folder in the save directory
for finetune_name in os.listdir(save_directory):
    if "finetuned" not in finetune_name:
        continue
    model, tokenizer = load_finetuned_model(base_model_name, save_directory, finetune_name)
    for i in range(len(test_set)):
        prompt = get_prompt(test_set, i)
        print(prompt)
        print("-------------------")
        response = generate_response(model, tokenizer, prompt)
        # Save the response as a text file in the response directory (create if it doesn't exist)
        if not os.path.exists(response_directory):
            os.makedirs(response_directory)
        with open(f"{response_directory}/{task_names[i]}.txt", "w") as file:
            file.write(response)