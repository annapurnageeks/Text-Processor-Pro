# Quick Start Guide

Get started with the Integrated Text Processor in 5 minutes!

## Installation

1. **Navigate to the project directory:**
```bash
cd Text-Processor-Integration
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Download NLTK data (first time only):**
```bash
python -c "import nltk; nltk.download('punkt')"
```

## Usage Examples

### 1. Command Line - Quick Test

Process a simple text:
```bash
python integrated_processor.py --text "The implementation of artificial intelligence has demonstrated significant potential for enhancing data analysis processes."
```

### 2. Command Line - From File

Create a file `input.txt` with your text, then:
```bash
python integrated_processor.py --file input.txt --output result.txt
```

### 3. Interactive Mode

Start interactive mode:
```bash
python integrated_processor.py
```
Then paste your text and press `Ctrl+D` (Mac/Linux) or `Ctrl+Z` (Windows).

### 4. Run Test Suite

Test the integration with example texts:
```bash
python test_integration.py
```

### 5. Web Interface

Start the web server:
```bash
python app.py
```
Then open your browser to: `http://localhost:5001`

## Common Options

### Fast Processing (No ML)
```bash
python integrated_processor.py \
  --text "Your text here" \
  --no-ml \
  --passes 1
```

### Maximum Quality (With ML)
```bash
python integrated_processor.py \
  --text "Your text here" \
  --passes 3
```

### Different Domains
```bash
# Medical
python integrated_processor.py --text "Your text" --domain medical

# Legal
python integrated_processor.py --text "Your text" --domain legal

# Scientific
python integrated_processor.py --text "Your text" --domain scientific
```

## Python API

```python
from integrated_processor import IntegratedTextProcessor

# Initialize
processor = IntegratedTextProcessor(
    mode='academic',
    domain='scientific',
    use_ml=True,
    humanizer_passes=2
)

# Process text
text = "Your AI-generated text here..."
result = processor.process(text)
print(result)
```

## What Happens During Processing?

1. **Humanization** (AI-Humanizer):
   - Makes text sound more natural and human-like
   - Varies sentence structure and length
   - Removes unnecessary filler words
   - Optimizes rhythm and flow

2. **Grammar Correction** (Grammar-Corrector):
   - Fixes grammar errors using transformer models
   - Corrects subject-verb agreement
   - Fixes punctuation and capitalization
   - Preserves meaning while improving clarity

## Expected Processing Time

- **Short text (1-2 paragraphs)**: 10-30 seconds
- **Medium text (3-5 paragraphs)**: 30-60 seconds
- **Long text (6+ paragraphs)**: 1-2 minutes

*Note: Processing is faster with `--no-ml` flag*

## Troubleshooting

### "Module not found" error
Make sure you're in the correct directory and both parent projects exist:
```bash
cd ~/Text-Processor-Integration
ls ../AI-Humanizer
ls ../Grammar-Corrector
```

### Slow processing
Use `--no-ml` flag for faster processing:
```bash
python integrated_processor.py --text "Your text" --no-ml
```

### NLTK errors
Download required data:
```bash
python -c "import nltk; nltk.download('punkt')"
```

## Next Steps

1. Try the web interface: `python app.py`
2. Run the test suite: `python test_integration.py`
3. Experiment with different modes and domains
4. Process your own documents

For full documentation, see `README.md`
