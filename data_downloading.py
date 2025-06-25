from datasets import load_dataset
import json

# Step 1: Load a small subset of the dataset (1% or first 1000 examples)
print("📥 Loading CodeParrot Clean dataset...")
dataset = load_dataset("codeparrot/codeparrot-clean", split="train[:1000]")

# Step 2: Save to a local JSONL file
output_path = "codeparrot_clean_subset.jsonl"

print(f"💾 Saving {len(dataset)} samples to {output_path}...")
with open(output_path, "w", encoding="utf-8") as f:
    for item in dataset:
        json.dump({"code": item["content"]}, f)
        f.write("\n")

# Step 3: Preview a few samples
print("\n🧪 Sample code from dataset:\n")
for i in range(3):
    print(f"Example {i+1}:\n{dataset[i]['content']}\n{'-'*50}")
