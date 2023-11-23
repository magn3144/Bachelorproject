# Save a txt file to trained_models folder, to show that this script has started
print("1: This script has started")

from transformers import AutoModelForCausalLM,AutoTokenizer,BitsAndBytesConfig,TrainingArguments
from peft import LoraConfig, PeftModel
import torch
from datasets import load_dataset
from trl import SFTTrainer
import wandb
import os

hf_token = "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"
wandb_key = "7ea086a098e40728fdf48b616051776a17daf566"

#monitering login
wandb.login(key=wandb_key)

print("2: Modules imported")


def reload_model(model_name, dataset, r, epochs, lr):
    # Load base model(code-llama-7b) and tokenizer
    bnb_config = BitsAndBytesConfig(
        load_in_4bit= True,
        bnb_4bit_quant_type= "nf4",
        bnb_4bit_compute_dtype= torch.bfloat16,
        bnb_4bit_use_double_quant= False,
    )
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,
        device_map={"": 0}
    )
    model.config.use_cache = False # silence the warnings. Please re-enable for inference!
    model.config.pretraining_tp = 1
    print("2b: model loaded")
    # Load LLaMA tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.add_eos_token = True
    tokenizer.add_bos_token, tokenizer.add_eos_token
    print("2c: tokenizer loaded")

    peft_config = LoraConfig(
        lora_alpha = 8,
        lora_dropout = 0.1,
        r = r,
        bias = "none",
        task_type = "CAUSAL_LM",
        layers_to_transform = [i for i in range(10, 32)]
    )

    training_arguments = TrainingArguments(
        output_dir= "./results",
        num_train_epochs= epochs, # 1
        per_device_train_batch_size= 2,
        gradient_accumulation_steps= 2,
        optim = "paged_adamw_8bit",
        save_steps= 100,
        logging_steps= 10, # 10,
        learning_rate= lr,
        weight_decay= 0.001,
        fp16= False,
        bf16= False,
        max_grad_norm= 0.3,
        max_steps= -1,
        warmup_ratio= 0.2, # 0.3
        group_by_length= True,
        lr_scheduler_type= "linear", # "constant"
        report_to="wandb",
        run_name=f"finetuned_lr{lr}_e{epochs}"
    )

    # Setting sft parameters
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=peft_config,
        max_seq_length= None,
        dataset_text_field="training_sample",
        tokenizer=tokenizer,
        args=training_arguments,
        packing= False,
    )

    print("3: Model and dataset loaded and hyper-parameters set")
    print(f"Hyperparameters: r = {r}, epochs = {epochs}")
    print("Ready to train")

    return trainer, model

def save_model(trainer, model, save_directory, finetune_name):
    # Save the fine-tuned model in directory
    trainer.model.save_pretrained(save_directory + "/" + finetune_name)
    wandb.finish()
    model.config.use_cache = True
    model.eval()
    print("5: Model has been saved to file")

def load_finetuned_model(base_model_name, model_directory, finetune_name):
    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        low_cpu_mem_usage=True,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map= {"": 0})

    model = PeftModel.from_pretrained(base_model, model_directory + "/" + finetune_name)
    model = model.merge_and_unload()

    # Reload tokenizer
    tokenizer = AutoTokenizer.from_pretrained(base_model_name, trust_remote_code=True)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    return model, tokenizer

def upload_to_huggingface(model, tokenizer, finetuned_model_name):
    # Upload model to huggingface
    model.push_to_hub(finetuned_model_name, use_auth_token=hf_token)
    tokenizer.push_to_hub(finetuned_model_name, use_auth_token=hf_token)


model_name = "codellama/CodeLlama-7b-Python-hf" # "meta-llama/Llama-2-7b-hf"
dataset_name = "magnus42/GPTWebScrapingPythonCode"
finetuned_model_name = "magnus42/llama2-python-web-scraping"
save_directory = "/work3/s204164/LLAMA2_Finetuning/trained_models/epochs_test"
dataset = load_dataset(dataset_name, split="train[0:860]") #860
print("2a: dataset loaded")

lr = 0.001
epoch_values = [epoch for epoch in range(1, 15)]
r = 16
print("epoch values:", epoch_values)

for epochs in epoch_values:
    finetune_name = f"finetuned_epochs{epochs}"
    # Check if model has already been trained
    if os.path.exists(save_directory + "/" + finetune_name):
        print(f"Model '{finetune_name}' has already been trained")
        continue

    print(f"finetune_name: {finetune_name}")
    trainer, model = reload_model(model_name, dataset, r, epochs, lr)
    trainer.train()
    save_model(trainer, model, save_directory, finetune_name)
    # upload_to_huggingface(model_name, save_directory, finetune_name)
    print(f"4: Model '{finetune_name}' has been trained and saved to file")
    # Clear the memory footprint
    del model, trainer
    torch.cuda.empty_cache()


print("This script has finished")