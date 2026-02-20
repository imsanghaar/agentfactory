---
sidebar_position: 7
title: "Troubleshooting and Monitoring"
chapter: 64
lesson: 7
duration_minutes: 40

# HIDDEN SKILLS METADATA
skills:
  - name: "Interpreting Training Loss Curves"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can diagnose underfitting, overfitting, and convergence from a training loss curve"

  - name: "Diagnosing Common Training Failures"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify cause and fix for OOM errors, NaN loss, and training stalls"

  - name: "Managing GPU Memory During Training"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can monitor memory usage and implement techniques to reduce peak memory"

  - name: "Implementing Checkpoint-Based Recovery"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can configure checkpoint saving and resume training from a saved state"

learning_objectives:
  - objective: "Interpret training loss curves to diagnose underfitting, overfitting, and convergence"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Given a loss curve, student correctly identifies the issue and proposes appropriate fix"

  - objective: "Diagnose and fix common training failures (OOM, NaN loss, stalls)"
    proficiency_level: "B2"
    bloom_level: "Analyze"
    assessment_method: "Student correctly identifies cause and solution for provided error scenarios"

  - objective: "Monitor and manage GPU memory during training"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student implements memory monitoring and applies at least one memory reduction technique"

  - objective: "Configure checkpoint saving and resume training from saved state"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student successfully resumes a training run from checkpoint"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (loss curves, overfitting, underfitting, OOM handling, gradient checkpointing, checkpoint saving, resume training) within B2 limit (7-10 concepts)"

differentiation:
  extension_for_advanced: "Implement custom callbacks for early stopping and learning rate scheduling based on validation loss"
  remedial_for_struggling: "Focus on the diagnostic flowchart; understand the symptoms before diving into causes"
---

# Troubleshooting and Monitoring

Training failures are inevitable. The question isn't whether you'll encounter problems, but how quickly you can diagnose and fix them. A developer who understands loss curves and error patterns can fix issues in minutes. A developer who doesn't might waste hours or abandon the training run entirely.

This lesson gives you the diagnostic frameworks to troubleshoot any training issue. You'll learn to read loss curves like a doctor reads vital signs, identify problems from error messages, and implement recovery strategies.

## The Diagnostic Mindset

When training fails, resist the urge to immediately change parameters and try again. That's trial-and-error, and it wastes GPU time. Instead, follow this diagnostic process:

```
1. OBSERVE: What exactly is the symptom?
   - Error message? Loss behavior? Memory usage?

2. HYPOTHESIZE: What could cause this?
   - Use the diagnostic tables below

3. TEST: Make ONE change and observe
   - Don't change multiple things at once

4. DOCUMENT: Record what you learned
   - Update your skill with the pattern
```

## Reading Loss Curves

The training loss curve is your primary diagnostic tool. It tells you whether the model is learning, how fast, and when to stop.

### Healthy Training

```
Loss
 ^
 |    \.
 |     \.
 |      \..
 |        '...
 |            '''...._____
 +----------------------------> Steps
```

A healthy loss curve:
- Starts high (model is random)
- Decreases rapidly at first (learning easy patterns)
- Decreases slowly later (learning nuances)
- Flattens toward the end (convergence)

### Underfitting: Model Not Learning

```
Loss
 ^
 |  ___________________________
 |
 |
 |
 |
 +----------------------------> Steps
```

**Symptoms**:
- Loss stays flat or decreases very slowly
- Loss remains high after many epochs
- Model outputs generic/wrong responses

**Causes and Fixes**:

| Cause | How to Identify | Fix |
|-------|-----------------|-----|
| Learning rate too low | Loss decreases very slowly | Increase LR to 5e-4 or 1e-3 |
| Bad data format | Loss never decreases | Check dataset structure |
| Wrong prompt template | High loss throughout | Verify EOS tokens present |
| Model frozen incorrectly | No trainable params | Check LoRA configuration |

### Overfitting: Learning Too Specifically

```
Loss
 ^     Training \.
 |               \..
 |  Validation     \. ....____   (diverging)
 |                   \_/
 |                     Training continues down
 +----------------------------> Steps
```

**Symptoms**:
- Training loss keeps decreasing
- Validation loss increases after initial decrease
- Model repeats training examples verbatim
- Poor performance on new inputs

**Causes and Fixes**:

| Cause | How to Identify | Fix |
|-------|-----------------|-----|
| Too many epochs | Val loss increases after epoch 2-3 | Stop earlier |
| Dataset too small | Train/val diverge quickly | Get more data or use data augmentation |
| Learning rate too high | Rapid train loss, unstable val | Reduce LR to 1e-4 |
| No regularization | Smooth overfit curve | Add weight_decay=0.05 |

### Loss Explosion: Model Destabilized

```
Loss
 ^                    /
 |                   /
 |           \.    /   (NaN)
 |            \. /
 |             X
 +----------------------------> Steps
```

**Symptoms**:
- Loss suddenly increases dramatically
- Loss becomes NaN or inf
- Training crashes with numerical errors

**Causes and Fixes**:

| Cause | How to Identify | Fix |
|-------|-----------------|-----|
| Learning rate too high | Sudden spike | Reduce LR to 1e-4 |
| Bad data (very long sequences) | Happens at specific step | Check that example |
| No warmup | Explodes in first steps | Add warmup_ratio=0.1 |
| Mixed precision issues | Random NaN | Try fp32 (slower but stable) |

## Common Error Messages

### CUDA Out of Memory (OOM)

```
RuntimeError: CUDA out of memory. Tried to allocate X MiB
(GPU 0; 15.90 GiB total capacity; Y GiB already allocated)
```

**Immediate fixes** (in order of preference):

```python
# 1. Reduce batch size
per_device_train_batch_size = 2  # Down from 4

# 2. Increase gradient accumulation to compensate
gradient_accumulation_steps = 8  # Keep effective batch same

# 3. Enable gradient checkpointing (trades compute for memory)
model.gradient_checkpointing_enable()

# 4. Reduce sequence length
max_seq_length = 1024  # Down from 2048
```

**Memory monitoring** to prevent OOM:

```python
import torch

def print_memory_stats():
    allocated = torch.cuda.memory_allocated() / 1024**3
    reserved = torch.cuda.memory_reserved() / 1024**3
    max_allocated = torch.cuda.max_memory_allocated() / 1024**3
    print(f"Allocated: {allocated:.2f} GB")
    print(f"Reserved: {reserved:.2f} GB")
    print(f"Peak: {max_allocated:.2f} GB")

# Call before and during training
print_memory_stats()
```

**Output:**
```
Allocated: 8.42 GB
Reserved: 9.50 GB
Peak: 13.21 GB
```

### NaN or Inf Loss

```
Loss is NaN or Inf at step X
```

**Causes and fixes**:

```python
# 1. Lower learning rate
learning_rate = 1e-4  # Down from 2e-4

# 2. Add warmup
warmup_ratio = 0.1  # 10% of steps

# 3. Check for bad examples
# Look at the step number where NaN occurred
# That batch contains problematic data

# 4. Disable mixed precision (last resort)
fp16 = False  # Slower but more numerically stable
```

**Finding bad data**:

```python
# If NaN occurs at step N, find that batch
step_size = per_device_train_batch_size * gradient_accumulation_steps
start_idx = step_size * N
end_idx = start_idx + step_size
print(f"Check examples {start_idx} to {end_idx}")

# Examine those examples
for i in range(start_idx, min(end_idx, len(dataset))):
    print(f"Example {i}: length = {len(dataset[i]['text'])}")
```

### Training Stalls

**Symptoms**:
- Progress bar stops moving
- No new log entries
- GPU utilization drops to 0%

**Common causes**:

| Cause | How to Identify | Fix |
|-------|-----------------|-----|
| Colab disconnected | Browser shows disconnection | Reconnect, resume from checkpoint |
| Deadlock in data loading | GPU 0%, CPU high | Restart runtime |
| Very long sequence | Stalls on specific batch | Reduce max_seq_length |

## Memory Management

T4 has 16GB VRAM. Here's how it's typically used:

```
Memory Breakdown (T4, Llama-3-8B-4bit):

Model weights (4-bit):    ~4.5 GB
Optimizer states:         ~1.5 GB
Gradients:               ~1.0 GB
Activations:             ~2-8 GB (depends on batch/sequence)
----------------------------------
Total:                   ~9-15 GB
```

### Techniques to Reduce Memory

**1. Gradient Checkpointing**

Trades compute for memory by recomputing activations during backward pass.

```python
# Reduces memory by ~30-40%, increases time by ~20%
model.gradient_checkpointing_enable()
```

**2. Smaller Batches with Gradient Accumulation**

Same effective batch size, lower peak memory.

```python
# Instead of: batch=8, accumulation=2 (needs 8 examples in memory)
# Use: batch=2, accumulation=8 (only needs 2 examples in memory)
per_device_train_batch_size = 2
gradient_accumulation_steps = 8
```

**3. Shorter Sequences**

Memory scales with sequence length squared for attention.

```python
# 2048 tokens uses ~4x memory of 1024 tokens
max_seq_length = 1024  # If your data allows
```

**4. Clear Cache Between Operations**

```python
import torch
import gc

# After loading model, before training
gc.collect()
torch.cuda.empty_cache()

# Monitor
print(f"Free memory: {torch.cuda.memory_reserved() - torch.cuda.memory_allocated()}")
```

## Checkpoint Strategy

Colab sessions disconnect. Servers crash. Power fails. Without checkpoints, you lose everything.

### Configuring Checkpoints

```python
training_args = TrainingArguments(
    output_dir="./task-api-checkpoints",

    # Save after each epoch
    save_strategy="epoch",

    # Or save every N steps
    # save_strategy="steps",
    # save_steps=50,

    # Keep only last N checkpoints (save disk space)
    save_total_limit=3,

    # Also save optimizer state for resume
    save_safetensors=True,
)
```

### Checkpoint Directory Structure

```
./task-api-checkpoints/
  checkpoint-32/
    adapter_config.json
    adapter_model.safetensors
    optimizer.pt
    scheduler.pt
    trainer_state.json
  checkpoint-64/
    ...
  checkpoint-96/
    ...
```

### Resuming from Checkpoint

```python
from transformers import Trainer

# Load trainer with same config
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    args=training_args,
)

# Resume from last checkpoint
trainer.train(resume_from_checkpoint=True)

# Or resume from specific checkpoint
trainer.train(resume_from_checkpoint="./task-api-checkpoints/checkpoint-64")
```

**Output:**
```
Resuming training from checkpoint ./task-api-checkpoints/checkpoint-64
Starting from step 64/96
```

### Colab-Safe Training Pattern

```python
# Colab-safe training with Google Drive backup
from google.colab import drive
drive.mount('/content/drive')

# Save checkpoints to Drive
training_args = TrainingArguments(
    output_dir="/content/drive/MyDrive/task-api-checkpoints",
    save_strategy="steps",
    save_steps=20,  # More frequent for Colab
    save_total_limit=5,
)

# Training loop with exception handling
try:
    trainer.train()
except Exception as e:
    print(f"Training interrupted: {e}")
    print("Checkpoints saved to Google Drive")
    print("Reconnect and run trainer.train(resume_from_checkpoint=True)")
```

## Monitoring Dashboard

For longer training runs, set up proper monitoring:

```python
# Option 1: Weights & Biases (recommended for serious work)
training_args = TrainingArguments(
    report_to="wandb",  # Enable W&B logging
    run_name="task-api-v1",
)

# Option 2: TensorBoard (local alternative)
training_args = TrainingArguments(
    report_to="tensorboard",
    logging_dir="./logs",
)

# Launch TensorBoard
%load_ext tensorboard
%tensorboard --logdir ./logs
```

### Key Metrics to Monitor

| Metric | What It Tells You | Target |
|--------|-------------------|--------|
| `train/loss` | Model learning progress | Decreasing |
| `train/learning_rate` | LR schedule is working | Warmup then stable/decay |
| `train/epoch` | Training progress | 1-3 for small datasets |
| `eval/loss` | Generalization | Close to train_loss |
| GPU memory | Whether you'll OOM | &lt; 15GB on T4 |

## Diagnostic Flowchart

```
Training Issue?
      |
      v
+------------------+
| Check Loss Curve |
+------------------+
      |
      +---> Flat/High -------> Underfitting
      |                        - Increase LR
      |                        - Check data format
      |
      +---> Exploding/NaN ---> Instability
      |                        - Decrease LR
      |                        - Add warmup
      |
      +---> Decreasing ------> Check Validation
             then flat         |
                               +---> Val also flat --> Converged (good!)
                               |
                               +---> Val increasing -> Overfitting
                                                       - Fewer epochs
                                                       - More data
```

```
OOM Error?
    |
    v
+------------------------------------+
| 1. Reduce batch size               |
| 2. Enable gradient checkpointing   |
| 3. Reduce sequence length          |
| 4. Check for memory leaks          |
+------------------------------------+
```

## Try With AI

### Prompt 1: Diagnose a Loss Curve

```
Here's my training log:

Step 10: loss=2.45, lr=6.67e-05
Step 20: loss=2.38, lr=0.000133
Step 30: loss=2.31, lr=0.0002
Step 40: loss=2.28, lr=0.0002
Step 50: loss=2.26, lr=0.000175
Step 60: loss=2.24, lr=0.00015
Step 70: loss=2.23, lr=0.000125
Step 80: loss=2.22, lr=0.0001
Step 90: loss=2.21, lr=7.5e-05

Dataset: 500 examples
Configuration: epochs=3, lr=2e-4, batch=4, accumulation=4

Analyze this training run:
1. Is the model converging properly?
2. What does the slow loss decrease suggest?
3. What would you change for the next run?
```

**What you're learning**: Loss curve interpretation. You're developing the skill to extract actionable insights from training metrics.

### Prompt 2: Debug an OOM Error

```
I'm getting this error on Colab T4:

RuntimeError: CUDA out of memory. Tried to allocate 512.00 MiB
(GPU 0; 15.90 GiB total; 14.32 GiB allocated; 237.56 MiB free;
14.89 GiB reserved in total by PyTorch)

My current configuration:
- Model: Llama-3-8B-4bit
- Batch size: 4
- Sequence length: 2048
- Gradient accumulation: 4
- Gradient checkpointing: disabled

Walk me through a systematic debugging process.
What should I try first, second, third?
How much memory would each change save?
```

**What you're learning**: Systematic debugging. You're developing the skill to approach memory problems methodically rather than randomly changing parameters.

### Prompt 3: Design a Monitoring Strategy

```
I'm training a production model that will run for 8 hours overnight.
I can't watch it the whole time, but I need to know if something goes wrong.

Requirements:
1. Detect if training stalls
2. Catch if loss explodes
3. Save progress regularly
4. Alert me if there's a problem

What monitoring and checkpoint strategy would you recommend?
Include specific TrainingArguments configuration.
```

**What you're learning**: Production monitoring design. You're developing the skill to build robust training pipelines that handle failures gracefully.

**Safety Note**: When training on shared resources (like Colab), be mindful of GPU time limits. Save checkpoints frequently, and don't leave training running unattended without proper recovery mechanisms. A crashed training run without checkpoints wastes both your time and shared compute resources.
