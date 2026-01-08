# Performance Optimization Guide

## Speed vs Quality Tradeoff

The integrated text processor offers several options to balance processing speed with output quality.

## Performance Settings

### 🚀 FASTEST (Recommended for Most Users)
**Estimated Time:** 5-15 seconds for typical paragraphs

```bash
python integrated_processor.py \
  --text "Your text" \
  --passes 1 \
  --skip-grammar
```

**Web UI Settings:**
- Humanization Passes: 1 Pass (Fast - Recommended)
- Enable ML Humanization: ✗ Unchecked
- Skip Grammar Correction: ✓ Checked

**When to use:**
- Quick drafts
- Testing
- Long documents
- When speed is priority

---

### ⚡ FAST & ACCURATE
**Estimated Time:** 10-30 seconds for typical paragraphs

```bash
python integrated_processor.py \
  --text "Your text" \
  --passes 1
```

**Web UI Settings:**
- Humanization Passes: 1 Pass
- Enable ML Humanization: ✗ Unchecked
- Skip Grammar Correction: ✗ Unchecked

**When to use:**
- Most use cases
- Good balance of speed and quality
- **DEFAULT SETTING**

---

### 🎯 BALANCED
**Estimated Time:** 20-60 seconds for typical paragraphs

```bash
python integrated_processor.py \
  --text "Your text" \
  --passes 2
```

**Web UI Settings:**
- Humanization Passes: 2 Passes
- Enable ML Humanization: ✗ Unchecked
- Skip Grammar Correction: ✗ Unchecked

**When to use:**
- Important documents
- Better humanization quality
- When you have time

---

### 🏆 MAXIMUM QUALITY
**Estimated Time:** 60-180 seconds for typical paragraphs

```bash
python integrated_processor.py \
  --text "Your text" \
  --passes 3
```

**Web UI Settings:**
- Humanization Passes: 3 Passes
- Enable ML Humanization: ✓ Checked
- Skip Grammar Correction: ✗ Unchecked

**When to use:**
- Critical documents
- Academic papers
- Professional publications
- When quality is paramount

---

## Performance Comparison

| Setting | Speed | Quality | Word Retention | Use Case |
|---------|-------|---------|----------------|----------|
| Fastest | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | 95% | Quick drafts |
| Fast & Accurate | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 90% | **Most use cases** |
| Balanced | ⚡⚡⚡ | ⭐⭐⭐⭐ | 85% | Important docs |
| Maximum | ⚡⚡ | ⭐⭐⭐⭐⭐ | 80% | Critical docs |

## What Each Option Does

### Humanization Passes (1-3)
- **1 Pass:** Single transformation through all 8 layers
  - Fastest
  - Good quality
  - **Recommended for most users**

- **2 Passes:** Text processed twice
  - Slower (2x time)
  - Better humanization
  - More variation in sentence structure

- **3 Passes:** Maximum transformation
  - Slowest (3x time)
  - Best humanization
  - Maximum variation

### ML Humanization
When **ENABLED** (use_ml=True):
- Uses PEGASUS transformer model for paraphrasing
- Much slower (adds 20-60 seconds)
- Better quality paraphrasing
- Requires model download (~2GB first time)

When **DISABLED** (use_ml=False):
- Uses rule-based transformation only
- Much faster
- Still produces good quality
- **Recommended for most users**

### Grammar Correction
When **ENABLED** (default):
- Uses FLAN-T5 transformer model
- Fixes grammar errors
- Adds 5-20 seconds processing time
- **Recommended for final output**

When **DISABLED** (--skip-grammar):
- Skips grammar correction
- Much faster
- Uses only basic grammar fixes from humanizer
- Good for drafts

## Word Reduction

The system may reduce word count due to:

1. **Filler Removal:** Removes unnecessary academic filler
   - "notably", "significantly", "it is worth noting that"
   - "in this context", "fundamentally"
   - Makes text more concise and readable

2. **Sentence Combining:** Merges short sentences
   - Reduces repetition
   - Improves flow

3. **Clarity Enhancement:** Simplifies complex phrases
   - "utilization of" → "using"
   - "implementation of" → "implementing"

**Typical Word Reduction:**
- 1 Pass: 5-10% reduction
- 2 Passes: 10-15% reduction
- 3 Passes: 15-20% reduction

**To Minimize Word Reduction:**
- Use 1 pass only
- Disable ML humanization
- The text will be more concise but retain meaning

## Processing Time Examples

### Short Text (1-2 paragraphs, ~100 words)
- Fastest: 5-10 seconds
- Fast & Accurate: 10-20 seconds
- Balanced: 20-40 seconds
- Maximum: 60-90 seconds

### Medium Text (3-5 paragraphs, ~300 words)
- Fastest: 10-20 seconds
- Fast & Accurate: 20-40 seconds
- Balanced: 40-80 seconds
- Maximum: 120-180 seconds

### Long Text (10+ paragraphs, ~1000 words)
- Fastest: 30-60 seconds
- Fast & Accurate: 60-120 seconds
- Balanced: 120-240 seconds
- Maximum: 300-600 seconds

## Optimization Tips

### 1. Process in Batches
For long documents, split into smaller sections:
```bash
# Process each section separately
python integrated_processor.py --file section1.txt --output out1.txt
python integrated_processor.py --file section2.txt --output out2.txt
# Then combine outputs
```

### 2. Use Fastest Settings for Drafts
First pass with fast settings, then refine:
```bash
# Draft (fast)
python integrated_processor.py --text "..." --passes 1 --skip-grammar

# Final version (slower, better quality)
python integrated_processor.py --text "..." --passes 2
```

### 3. GPU Acceleration
Grammar correction automatically uses GPU if available:
- CUDA (NVIDIA): Significantly faster
- MPS (Apple Silicon): Moderately faster
- CPU: Standard speed

Check your device:
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"MPS available: {torch.backends.mps.is_available()}")
```

### 4. Disable What You Don't Need
```bash
# No ML, no grammar (fastest)
python integrated_processor.py --text "..." --skip-grammar

# No ML, with grammar (fast & accurate)
python integrated_processor.py --text "..."  # Default is no ML

# With ML, no grammar
python integrated_processor.py --text "..." --skip-grammar --no-ml=false
```

## Recommended Settings by Use Case

### Academic Writing
```bash
python integrated_processor.py \
  --file paper.txt \
  --mode academic \
  --domain scientific \
  --passes 2
```
**Time:** 20-60 seconds per 300 words

### Business Documents
```bash
python integrated_processor.py \
  --file report.txt \
  --mode professional \
  --domain technical \
  --passes 1
```
**Time:** 10-30 seconds per 300 words

### Quick Blog Posts
```bash
python integrated_processor.py \
  --file blog.txt \
  --mode balanced \
  --passes 1 \
  --skip-grammar
```
**Time:** 5-15 seconds per 300 words

### Legal Documents
```bash
python integrated_processor.py \
  --file legal.txt \
  --mode professional \
  --domain legal \
  --passes 2
```
**Time:** 20-60 seconds per 300 words

## Troubleshooting Slow Performance

### Issue: Processing takes too long

**Solution 1:** Use faster settings
```bash
python integrated_processor.py --text "..." --passes 1 --skip-grammar
```

**Solution 2:** Disable ML humanization (already default)
```bash
# ML is disabled by default, but you can explicitly disable:
python integrated_processor.py --text "..." --no-ml
```

**Solution 3:** Process smaller chunks
Split your text into smaller sections and process separately.

### Issue: Grammar correction is slow

**Solution:** Skip grammar correction for drafts
```bash
python integrated_processor.py --text "..." --skip-grammar
```

### Issue: Out of memory errors

**Solution:** Process in smaller batches or reduce passes
```bash
python integrated_processor.py --text "..." --passes 1
```

## Summary

**For 95% of users, we recommend:**
```bash
python integrated_processor.py --text "Your text" --passes 1
```

Or in the web UI:
- Humanization Passes: **1 Pass (Fast - Recommended)**
- Enable ML Humanization: **Unchecked**
- Skip Grammar Correction: **Unchecked**

This provides excellent results in 10-30 seconds for most texts!
