import time

from transformers import XLNetTokenizer, XLNetLMHeadModel
import torch

import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# DEVICE = torch.device("cpu")

tokenizer = XLNetTokenizer.from_pretrained('xlnet-large-cased')
model = XLNetLMHeadModel.from_pretrained('xlnet-large-cased')

model=model.cuda()
# We show how to setup inputs to predict a next token using a bi-directional context.
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is very <mask>", add_special_tokens=False)).unsqueeze(
    0)  # We will predict the masked token
perm_mask = torch.zeros((1, input_ids.shape[1], input_ids.shape[1]), dtype=torch.float)
perm_mask[:, :, -1] = 1.0  # Previous tokens don't see last token
target_mapping = torch.zeros((1, 1, input_ids.shape[1]),
                             dtype=torch.float)  # Shape [1, 1, seq_length] => let's predict one token
target_mapping[0, 0, -1] = 1.0  # Our first (and only) prediction will be the last token of the sequence (the masked token)

input_ids=input_ids.cuda()
perm_mask=perm_mask.cuda()
target_mapping=target_mapping.cuda()
t0 = time.time()
outputs = model(input_ids, perm_mask=perm_mask, target_mapping=target_mapping)
next_token_logits = outputs[0]  # Output has shape [target_mapping.size(0), target_mapping.size(1), config.vocab_size]
print(f'next_token_logits:{next_token_logits}, takes{time.time() - t0}')
# The same way can the XLNetLMHeadModel be used to be trained by standard auto-regressive language modeling.
input_ids = torch.tensor(tokenizer.encode("Hello, my dog is very <mask>", add_special_tokens=False)).unsqueeze(
    0)  # We will predict the masked token
labels = torch.tensor(tokenizer.encode("cute", add_special_tokens=False)).unsqueeze(0)
assert labels.shape[0] == 1, 'only one word will be predicted'
perm_mask = torch.zeros((1, input_ids.shape[1], input_ids.shape[1]), dtype=torch.float)
perm_mask[:, :, -1] = 1.0  # Previous tokens don't see last token as is done in standard auto-regressive lm training
target_mapping = torch.zeros((1, 1, input_ids.shape[1]),
                             dtype=torch.float)  # Shape [1, 1, seq_length] => let's predict one token
target_mapping[
    0, 0, -1] = 1.0  # Our first (and only) prediction will be the last token of the sequence (the masked token)
input_ids=input_ids.cuda()
perm_mask=perm_mask.cuda()
target_mapping=target_mapping.cuda()
labels=labels.cuda()

t1 = time.time()
for i in range(200):
    outputs = model(input_ids, perm_mask=perm_mask, target_mapping=target_mapping, labels=labels)
    # loss, next_token_logits = outputs[:2]  # Output has shape [target_mapping.size(0), target_mapping.size(1), config.vocab_size]

print(f'outputs:{outputs}, takes{(time.time() - t1) / 200}')