from transformers import AutoModelForCausalLM,AutoTokenizer,BitsAndBytesConfig,HfArgumentParser,TrainingArguments,pipeline, logging, TextStreamer
from peft import LoraConfig, PeftModel, PeftConfig
import os
import torch
from datasets import load_dataset
import platform
import pandas as pd


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


dataset_name = "magnus42/GPTWebScrapingPythonCode"
base_model_name = "codellama/CodeLlama-7b-Python-hf"
validation_set = load_dataset(dataset_name, split="validation")["training_sample"]

base_model = AutoModelForCausalLM.from_pretrained(
    base_model_name,
    low_cpu_mem_usage=True,
    return_dict=True,
    torch_dtype=torch.float16,
    device_map= {"": 0})

tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

validation_loss = validation_loss(base_model, tokenizer, validation_set)

print(validation_loss)