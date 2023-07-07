# LOCAL VERSION
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
cache_dir= "C:\\Users\\Surabhi\\OneDrive\\Desktop\\projectcode\\virtual-companion\\backend\\hf_cache"

tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum", cache_dir=cache_dir)
model = AutoModelForSeq2SeqLM.from_pretrained("philschmid/bart-large-cnn-samsum", cache_dir=cache_dir)

def summarise_text(text):
    input_ids = tokenizer.encode(text, truncation=True, return_tensors="pt")
    summary_ids = model.generate(input_ids, num_beams=4, max_length=100, early_stopping=True)
    summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
    return summary
