from transformers import AutoModelForCausalLM,AutoTokenizer,BitsAndBytesConfig,HfArgumentParser,TrainingArguments,pipeline, logging, TextStreamer
from peft import LoraConfig, PeftModel, PeftConfig
import os
import torch
from datasets import load_dataset
import platform
import pandas as pd


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

def validation_loss(model, tokenizer, validation_set):
    # Tokenize the validation set
    validation_set = tokenizer(validation_set, padding=True, truncation=True, return_tensors="pt").to("cuda:0")
    # Calculate the validation loss for each validation datapoint and return the mean
    validation_loss_sum = 0
    for i in range(len(validation_set["input_ids"])):
        input_ids = validation_set["input_ids"][i].unsqueeze(0)
        attention_mask = validation_set["attention_mask"][i].unsqueeze(0)
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=input_ids)
        loss = outputs.loss
        validation_loss_sum += loss.item()
    validation_loss = validation_loss_sum / len(validation_set["input_ids"])

    return validation_loss


folder_name = "seed_test"
dataset_name = "magnus42/GPTWebScrapingPythonCode"
base_model_name = "codellama/CodeLlama-7b-Python-hf"
save_directory = f"trained_models/{folder_name}"
validation_set = load_dataset(dataset_name, split="validation")["training_sample"]
validation_loss_dict = {}

# For each folder in the save directory
for finetune_name in os.listdir(save_directory):
    if ("finetuned" not in finetune_name):
        continue
    model, tokenizer = load_finetuned_model(base_model_name, save_directory, finetune_name)
    validation_loss_dict[finetune_name] = validation_loss(model, tokenizer, validation_set)

# Save validation loss as a CSV file with column names "model", "validation_loss"
validation_loss_df = pd.DataFrame(validation_loss_dict.items(), columns=["model", "validation_loss"])
validation_loss_df.to_csv(f"validation_loss_{folder_name}.csv", index=False)