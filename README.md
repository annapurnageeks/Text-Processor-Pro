# Integrated Text Processor

A powerful text processing pipeline that combines **AI Humanization** and **Grammar Correction** to transform text into high-quality, human-like, grammatically correct content.

## Overview

This integration combines two projects:
1. **AI-Humanizer**: Transforms AI-generated text to sound more human-like with natural variation
2. **Grammar-Corrector**: Uses transformer models (FLAN-T5) to fix grammar errors

### Processing Pipeline

```
Input Text → AI Humanization → Grammar Correction → Output
```

## Features

- **AI Humanization**: 8-layer transformation including:
  - ML-based paraphrasing
  - Quality enhancement
  - Sentence restructuring
  - Burstiness enhancement
  - Filler removal
  - Rhythm optimization
  - Professional writing patterns

- **Grammar Correction**: Transformer-based grammar correction using FLAN-T5
  - More powerful than rule-based approaches
  - Handles complex grammatical structures
  - Preserves meaning while fixing errors

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download NLTK data (first time only):
```python
python -c "import nltk; nltk.download('punkt')"
```

## Usage

### Command Line Interface

**Basic usage:**
```bash
python integrated_processor.py --text "Your text here"
```

**From file:**
```bash
python integrated_processor.py --file input.txt --output output.txt
```

**With options:**
```bash
python integrated_processor.py \
  --file input.txt \
  --mode academic \
  --domain scientific \
  --passes 2 \
  --output result.txt
```

**Interactive mode:**
```bash
python integrated_processor.py
# Then type/paste your text and press Ctrl+D (Mac/Linux) or Ctrl+Z (Windows)
```

### Command Line Options

- `--text TEXT`: Text to process
- `--file FILE`: Input file path
- `--output FILE`: Output file path (optional)
- `--mode {academic,professional,balanced}`: Humanizer mode (default: academic)
- `--domain {academic,medical,legal,scientific,technical}`: Domain (default: academic)
- `--passes {1,2,3}`: Number of humanization passes (default: 2)
- `--no-ml`: Disable ML-based humanization
- `--quiet`: Minimal output

### Web Interface

Start the Flask web server:
```bash
python app.py
```

Then open your browser to: `http://localhost:5001`

### Python API

```python
from integrated_processor import IntegratedTextProcessor

# Initialize processor
processor = IntegratedTextProcessor(
    mode='academic',
    domain='scientific',
    use_ml=True,
    humanizer_passes=2
)

# Process text
input_text = "Your AI-generated text here..."
result = processor.process(input_text, verbose=True)

print(result)
```

## How It Works

### Step 1: AI Humanization
The text is processed through multiple layers:
1. **ML Paraphrasing** (optional): PEGASUS model for base transformation
2. **Quality Enhancement**: Improves clarity and coherence
3. **Sentence Restructuring**: Varies sentence structures naturally
4. **AI Detection Bypass**: Splits long sentences, simplifies formal language
5. **Burstiness Enhancement**: Dramatically varies sentence lengths
6. **Filler Removal**: Removes unnecessary academic filler
7. **Rhythm Optimization**: Creates natural paragraph flow
8. **Professional Patterns**: Applies domain-specific writing patterns

### Step 2: Grammar Correction
The humanized text is corrected using:
- **FLAN-T5 Transformer Model**: Pre-trained on grammar correction
- **Sentence-level Processing**: Each sentence is corrected individually
- **Context Preservation**: Maintains meaning while fixing grammar

## Examples

### Example 1: Academic Text

**Input:**
```
The implementation of artificial intelligence in contemporary research methodologies
has demonstrated significant potential for enhancing the efficiency of data analysis
processes.
```

**Output (after humanization + grammar correction):**
```
AI implementation in modern research has shown great potential for improving data
analysis efficiency. This technology enhances how researchers approach complex
analytical challenges.
```

### Example 2: Technical Documentation

**Input:**
```
The utilization of machine learning algorithms facilitates unprecedented advancements
in predictive modeling capabilities across numerous scientific domains.
```

**Output:**
```
Machine learning algorithms enable major advances in predictive modeling across many
scientific fields. These tools transform how predictions are made and validated.
```

## Configuration

### Humanizer Modes
- **academic**: Optimized for academic writing
- **professional**: Professional business writing
- **balanced**: Balanced approach

### Domains
- **academic**: General academic writing
- **medical**: Clinical papers, medical research
- **legal**: Legal briefs, case analysis
- **scientific**: Research papers, experiments
- **technical**: Tech blogs, documentation

### Humanization Passes
- **1 pass**: Fast, basic humanization
- **2 passes** (default): Balanced quality and speed
- **3 passes**: Maximum humanization (slower)

## Project Structure

```
Text-Processor-Integration/
├── integrated_processor.py    # Main pipeline implementation
├── app.py                      # Flask web interface
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── templates/                  # Web UI templates (to be created)
    └── index.html
```

## Dependencies

The integration requires both parent projects:
- `../AI-Humanizer/` - AI Humanization project
- `../Grammar-Corrector/` - Grammar Correction project

## Troubleshooting

### Import Errors
Make sure both parent projects are in the correct location:
```
/Users/annapurnageeks/
├── AI-Humanizer/
├── Grammar-Corrector/
└── Text-Processor-Integration/
```

### Model Loading Issues
- Grammar Corrector needs the FLAN-T5 model downloaded (happens automatically on first run)
- Ensure you have enough disk space (~3GB for the model)

### NLTK Data
If you get NLTK errors, download the required data:
```python
import nltk
nltk.download('punkt')
```

## Performance

- **Processing Speed**: Depends on text length and number of passes
  - ~10-30 seconds for short paragraphs (with ML)
  - ~30-60 seconds for longer texts
  - Faster without ML (`--no-ml`)

- **GPU Acceleration**: Grammar correction will use GPU if available (CUDA/MPS)

## License

This integration combines two separate projects. Please refer to the original projects for their respective licenses.

## Credits

- **AI-Humanizer**: Multi-layer humanization system
- **Grammar-Corrector**: Transformer-based grammar correction using FLAN-T5
