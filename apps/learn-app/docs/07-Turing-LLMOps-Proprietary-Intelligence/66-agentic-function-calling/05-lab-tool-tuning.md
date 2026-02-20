---
sidebar_position: 5
title: "Lab - Tool Tuning"
chapter: 66
lesson: 5
duration_minutes: 60

# HIDDEN SKILLS METADATA
skills:
  - name: "Executing Agentic Fine-Tuning Jobs"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can configure and run a fine-tuning job for tool-calling with appropriate hyperparameters and monitor progress"

  - name: "Configuring Tool-Calling Training Parameters"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can select appropriate learning rate, batch size, and epochs for tool-calling fine-tuning based on dataset size"

  - name: "Validating Training Progress"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can interpret training metrics and identify when training is converging vs diverging"

learning_objectives:
  - objective: "Configure and execute a fine-tuning job for tool-calling on Task API dataset"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Successfully complete training run with monitored checkpoints"

  - objective: "Select appropriate hyperparameters for agentic fine-tuning"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Justify learning rate, batch size, and epoch choices based on dataset characteristics"

  - objective: "Interpret training metrics to validate convergence"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Identify loss curve patterns indicating successful training vs problems"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (fine-tuning job, hyperparameters, loss curves, checkpoints, validation split, inference testing) within B1-B2 limit"

differentiation:
  extension_for_advanced: "Compare training results across different base models (Llama 3 8B vs Mistral 7B) and analyze quality/cost tradeoffs"
  remedial_for_struggling: "Use a smaller subset (100 examples) for faster iteration before scaling to full dataset"
---

# Lab - Tool Tuning

You've built a 500+ example dataset for Task API tool-calling. Now you'll train a model to use it. This hands-on lab walks through the complete fine-tuning workflow—from configuration to validation to your first tool-calling inference.

By the end, you'll have a working agentic model ready for evaluation in the next lesson.

## Lab Overview

| Phase | Duration | Outcome |
|-------|----------|---------|
| 1. Environment Setup | 10 min | Training environment ready |
| 2. Data Preparation | 10 min | Dataset uploaded and validated |
| 3. Training Configuration | 15 min | Hyperparameters selected |
| 4. Training Execution | 20 min | Model training (may run in background) |
| 5. Validation Testing | 5 min | Quick inference check |

## Phase 1: Environment Setup

### Option A: OpenAI Fine-Tuning API

The fastest path for production-grade tool-calling models:

```python
import openai
from openai import OpenAI

client = OpenAI()

# Verify API access
models = client.models.list()
print(f"Available base models for fine-tuning:")
for model in models.data:
    if "gpt-3.5" in model.id or "gpt-4" in model.id:
        print(f"  - {model.id}")
```

**Output:**
```
Available base models for fine-tuning:
  - gpt-3.5-turbo-0125
  - gpt-4o-mini-2024-07-18
```

### Option B: Local Training with Unsloth

For full control and no API costs:

```bash
# Create environment
python -m venv ch66-training
source ch66-training/bin/activate

# Install Unsloth (optimized for consumer GPUs)
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install transformers datasets trl

# Verify GPU
python -c "import torch; print(f'GPU: {torch.cuda.get_device_name(0)}')"
```

**Output:**
```
GPU: NVIDIA GeForce RTX 4090
```

For this lab, we'll show both paths. Choose based on your resources.

## Phase 2: Data Preparation

### Split Dataset

Training needs validation data to monitor for overfitting:

```python
import json
import random

def split_dataset(input_file: str, train_ratio: float = 0.9):
    """Split dataset into training and validation sets."""
    with open(input_file) as f:
        examples = [json.loads(line) for line in f]

    random.shuffle(examples)

    split_idx = int(len(examples) * train_ratio)
    train_data = examples[:split_idx]
    val_data = examples[split_idx:]

    # Save splits
    with open("train.jsonl", "w") as f:
        for ex in train_data:
            f.write(json.dumps(ex) + "\n")

    with open("val.jsonl", "w") as f:
        for ex in val_data:
            f.write(json.dumps(ex) + "\n")

    print(f"Training examples: {len(train_data)}")
    print(f"Validation examples: {len(val_data)}")

split_dataset("task_api_tool_calling.jsonl")
```

**Output:**
```
Training examples: 470
Validation examples: 53
```

### Upload to OpenAI (Option A)

```python
# Upload training file
train_file = client.files.create(
    file=open("train.jsonl", "rb"),
    purpose="fine-tune"
)
print(f"Training file ID: {train_file.id}")

# Upload validation file
val_file = client.files.create(
    file=open("val.jsonl", "rb"),
    purpose="fine-tune"
)
print(f"Validation file ID: {val_file.id}")
```

**Output:**
```
Training file ID: file-abc123
Validation file ID: file-def456
```

### Prepare for Local Training (Option B)

```python
from datasets import load_dataset

# Load and format dataset
def format_for_unsloth(example):
    """Convert to Unsloth chat format."""
    # Unsloth expects specific format
    messages = example["messages"]
    formatted = []

    for msg in messages:
        role = msg["role"]
        if role == "assistant" and "tool_calls" in msg:
            # Format tool calls as special content
            content = f"<tool_call>{json.dumps(msg['tool_calls'])}</tool_call>"
        else:
            content = msg.get("content", "")

        formatted.append({"role": role, "content": content})

    return {"conversations": formatted}

# Load dataset
dataset = load_dataset("json", data_files={
    "train": "train.jsonl",
    "validation": "val.jsonl"
})

dataset = dataset.map(format_for_unsloth)
```

## Phase 3: Training Configuration

### Hyperparameter Selection

For agentic fine-tuning, these parameters matter most:

| Parameter | Recommended | Why |
|-----------|-------------|-----|
| **Learning Rate** | 1e-5 to 3e-5 | Lower than standard SFT—structured output needs precision |
| **Batch Size** | 4-8 | Smaller batches for tool-calling format consistency |
| **Epochs** | 3-5 | More epochs for format learning |
| **Warmup Ratio** | 0.1 | Gradual ramp-up prevents early divergence |

### OpenAI Configuration (Option A)

```python
# Create fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file=train_file.id,
    validation_file=val_file.id,
    model="gpt-4o-mini-2024-07-18",
    hyperparameters={
        "n_epochs": 3,
        "batch_size": 4,
        "learning_rate_multiplier": 1.0  # OpenAI uses multiplier, not absolute
    },
    suffix="task-api-tools"
)

print(f"Fine-tuning job created: {job.id}")
print(f"Status: {job.status}")
```

**Output:**
```
Fine-tuning job created: ftjob-abc123
Status: queued
```

### Unsloth Configuration (Option B)

```python
from unsloth import FastLanguageModel
from trl import SFTTrainer
from transformers import TrainingArguments

# Load base model with 4-bit quantization
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/llama-3-8b-Instruct-bnb-4bit",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)

# Add LoRA adapters for efficient training
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing=True,
)

# Training configuration
training_args = TrainingArguments(
    output_dir="./task-api-tools",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=2,  # Effective batch size: 8
    learning_rate=2e-5,
    warmup_ratio=0.1,
    logging_steps=10,
    save_steps=100,
    eval_strategy="steps",
    eval_steps=50,
    fp16=True,
)
```

## Phase 4: Training Execution

### Monitor OpenAI Job (Option A)

```python
import time

def monitor_job(job_id: str, check_interval: int = 30):
    """Monitor fine-tuning job until completion."""
    while True:
        job = client.fine_tuning.jobs.retrieve(job_id)

        print(f"Status: {job.status}")

        if job.status == "succeeded":
            print(f"Training complete!")
            print(f"Fine-tuned model: {job.fine_tuned_model}")
            return job.fine_tuned_model

        elif job.status == "failed":
            print(f"Training failed: {job.error}")
            return None

        elif job.status in ["queued", "running"]:
            # Show training metrics if available
            events = client.fine_tuning.jobs.list_events(job_id, limit=5)
            for event in events.data:
                print(f"  {event.message}")

        time.sleep(check_interval)

# Monitor training
model_name = monitor_job(job.id)
```

**Output (during training):**
```
Status: running
  Step 100: training loss=0.45
  Step 200: training loss=0.28
  Step 300: training loss=0.15
Status: running
  Step 400: training loss=0.09
  Step 470: training loss=0.06
Status: succeeded
Training complete!
Fine-tuned model: ft:gpt-4o-mini-2024-07-18:org::abc123
```

### Run Local Training (Option B)

```python
# Create trainer
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    args=training_args,
    dataset_text_field="conversations",
    max_seq_length=2048,
)

# Start training
print("Starting training...")
trainer.train()

# Save model
model.save_pretrained("task-api-tools-final")
tokenizer.save_pretrained("task-api-tools-final")
print("Model saved to task-api-tools-final/")
```

**Output:**
```
Starting training...
{'loss': 0.8234, 'learning_rate': 4e-06, 'epoch': 0.21}
{'loss': 0.4521, 'learning_rate': 1.2e-05, 'epoch': 0.43}
{'loss': 0.2156, 'learning_rate': 1.8e-05, 'epoch': 0.64}
{'eval_loss': 0.1823, 'epoch': 0.64}
...
{'loss': 0.0523, 'learning_rate': 6e-06, 'epoch': 2.98}
Training complete in 18:34
Model saved to task-api-tools-final/
```

### Understanding Training Metrics

Watch for these patterns:

| Metric Pattern | Interpretation | Action |
|----------------|----------------|--------|
| Loss decreasing smoothly | Good training | Continue |
| Loss plateaus early | Learning rate too low | Increase LR |
| Loss spikes up | Learning rate too high | Decrease LR |
| Val loss increasing while train decreases | Overfitting | Stop early, reduce epochs |
| Loss very low (&lt;0.01) | Possible overfitting | Check generalization |

## Phase 5: Validation Testing

### Quick Inference Test

Before formal evaluation, verify the model works:

```python
# Test with OpenAI fine-tuned model
def test_tool_calling(model_name: str, user_message: str):
    """Test tool-calling capability."""
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": user_message}
        ],
        tools=TASK_API_TOOLS,
        tool_choice="auto"
    )

    msg = response.choices[0].message

    if msg.tool_calls:
        print(f"Tool called: {msg.tool_calls[0].function.name}")
        print(f"Arguments: {msg.tool_calls[0].function.arguments}")
    else:
        print(f"Response: {msg.content}")

# Test examples
test_cases = [
    "Create a task to review the quarterly report",
    "What tasks do I have due this week?",
    "Mark the budget task as complete",
]

for test in test_cases:
    print(f"\nUser: {test}")
    test_tool_calling(model_name, test)
```

**Output:**
```
User: Create a task to review the quarterly report
Tool called: create_task
Arguments: {"title": "Review the quarterly report"}

User: What tasks do I have due this week?
Tool called: list_tasks
Arguments: {"due_before": "2024-01-21"}

User: Mark the budget task as complete
Tool called: complete_task
Arguments: {"task_id": "budget_task"}
```

The model is calling the right tools. Formal accuracy measurement comes in Lesson 7.

## Common Training Issues

### Issue: Training Loss Doesn't Decrease

**Cause**: Learning rate too low or data format issues

**Solution**:
```python
# Increase learning rate
hyperparameters={
    "learning_rate_multiplier": 2.0  # Double the default
}

# Or check data format
# Ensure all examples have valid tool_calls structure
```

### Issue: Model Outputs Natural Language Instead of Tool Calls

**Cause**: Training examples have mixed outputs (some with tools, some without)

**Solution**:
```python
# Separate datasets for tool-calling vs conversation
# Or add explicit instruction in system prompt:
"When a task operation is requested, you MUST call the appropriate tool.
Do NOT describe what you would do - actually call the tool."
```

### Issue: JSON Parsing Errors in Output

**Cause**: Model not learning exact JSON format

**Solution**:
```python
# Lower temperature at inference
response = client.chat.completions.create(
    model=model_name,
    temperature=0.0,  # Deterministic for structured output
    ...
)

# Or add more training epochs focused on format
```

## Checkpoint Your Progress

Save your training artifacts:

```bash
# Create checkpoint directory
mkdir -p checkpoints/ch66-lab

# Copy important files
cp train.jsonl val.jsonl checkpoints/ch66-lab/
cp -r task-api-tools-final/ checkpoints/ch66-lab/  # If local training

# Record model name
echo "ft:gpt-4o-mini-2024-07-18:org::abc123" > checkpoints/ch66-lab/model_name.txt
```

## Reflect on Your Skill

Update your `agentic-tuning` skill:

1. **Add training configuration template**: Hyperparameters for tool-calling
2. **Add metric interpretation guide**: What loss patterns mean
3. **Add troubleshooting section**: Common issues and solutions

## Try With AI

### Prompt 1: Interpret Training Logs

```
Here are my training metrics:

Step 100: loss=0.85, lr=5e-6
Step 200: loss=0.52, lr=1e-5
Step 300: loss=0.38, lr=1.5e-5
Step 400: loss=0.35, lr=2e-5
Step 500: loss=0.34, lr=1.5e-5
Step 600: loss=0.33, lr=1e-5

Help me interpret this:
1. Is training progressing well?
2. Should I continue or stop?
3. What would you change for the next run?
```

**What you're learning**: Metric interpretation—understanding when training is working vs when to intervene.

### Prompt 2: Debug Training Failure

```
My fine-tuned model is calling tools, but the arguments are wrong.
For "Create a task to buy groceries tomorrow", it outputs:

{"name": "create_task", "arguments": {"title": "buy groceries"}}

It's missing the due_date. What might cause this? How do I fix it?
Consider:
- Training data issues
- Hyperparameter problems
- Inference configuration
```

**What you're learning**: Debugging structured output—tracing issues to root causes in training or inference.

### Prompt 3: Optimize Training Cost

```
My training job on OpenAI costs ~$20 for 500 examples over 3 epochs.
I want to reduce cost while maintaining quality. Help me analyze:

1. Can I use fewer examples? What's the minimum for tool-calling?
2. Can I use fewer epochs? How do I know if 2 is enough?
3. Should I use gpt-3.5-turbo instead of gpt-4o-mini?

What experiments would you run to find the cost-quality sweet spot?
```

**What you're learning**: Cost optimization—making pragmatic tradeoffs for production systems.

### Safety Note

Training on real user data requires privacy considerations. For this lab, you used synthetic data. In production, ensure training data is anonymized, user-consented, and doesn't contain sensitive information. Fine-tuned models can memorize training examples.
