from transformers import BertForMaskedLM, BertTokenizerFast
import os

model_path = r"C:\Users\qja19\Desktop\issue_bert\10000i_5000s_large_40ep"
tokenizer = BertTokenizerFast.from_pretrained(model_path)
model = BertForMaskedLM.from_pretrained(os.path.join(model_path, "checkpoint-last"))

REPO_NAME = 'issueBERT-large' # ex) 'my-bert-fine-tuned'
AUTH_TOKEN = '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' # <https://huggingface.co/settings/token>
 
## Upload to Huggingface Hub
model.push_to_hub(
    REPO_NAME, 
    use_temp_dir=True, 
    use_auth_token=AUTH_TOKEN
)
tokenizer.push_to_hub(
    REPO_NAME, 
    use_temp_dir=True, 
    use_auth_token=AUTH_TOKEN
)