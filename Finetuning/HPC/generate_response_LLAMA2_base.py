from transformers import AutoModelForCausalLM,AutoTokenizer
from peft import PeftModel
import os
import torch
from datasets import load_dataset
import json
import pandas as pd


def load_base_model(base_model_name):
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        low_cpu_mem_usage=True,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map= {"": 0})

    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    return base_model, tokenizer

def generate_response(model, tokenizer, prompt):
    runtimeFlag = "cuda:0"
    batch = tokenizer(prompt, return_tensors='pt', return_token_type_ids=False).to(runtimeFlag)
    with torch.cuda.amp.autocast():
        output_tokens = model.generate(**batch, max_new_tokens=2000)
    return tokenizer.decode(output_tokens[0], skip_special_tokens=True)

def get_prompt(dataset, index):
    return dataset[index] + " ### Response: ```"


dataset_name = "magnus42/GPTWebScrapingPythonCode"
base_model_name = "codellama/CodeLlama-7b-Python-hf"
response_directory = f"responses_base"
test_set = load_dataset(dataset_name, split="test")["prompt"]
task_names = load_dataset(dataset_name, split="test")["task"]

model, tokenizer = load_base_model(base_model_name)
for i in range(len(test_set)):
    prompt = get_prompt(test_set, i)
    print(prompt)
    print("-------------------")
    response = generate_response(model, tokenizer, prompt)
    if not os.path.exists(response_directory):
        os.makedirs(response_directory)
    with open(f"{response_directory}/{task_names[i]}.txt", "w") as file:
        file.write(response)