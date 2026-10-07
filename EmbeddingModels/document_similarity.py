from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen3-0.6B"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto"
)

# Read the document
with open("output.txt", "r", encoding="utf-8") as f:
    document = f.read()

# Ask your question
question = input("\nAsk a question about the document: ")

# Give both the document and question to Qwen
messages = [
    {
        "role": "user",
        "content": f"""
Here is the document:

{document}

Now answer the following question based only on the document:

{question}
"""
    }
]

# Apply Qwen chat template
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=False
)

# Tokenize
inputs = tokenizer(text, return_tensors="pt")

# Generate
outputs = model.generate(
    **inputs,
    max_new_tokens=150
)

# Extract only the generated answer
answer = tokenizer.decode(
    outputs[0][inputs["input_ids"].shape[1]:],
    skip_special_tokens=True
)

print("\nAnswer:")
print(answer)