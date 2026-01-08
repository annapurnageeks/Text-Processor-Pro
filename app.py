#!/usr/bin/env python3
"""
Flask Web Application for Integrated Text Processor
Provides a web interface for the AI Humanizer + Grammar Corrector pipeline
"""

from flask import Flask, render_template, request, jsonify
import sys
import os

# Add project directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(parent_dir, 'AI-Humanizer'))
sys.path.insert(0, os.path.join(parent_dir, 'Grammar-Corrector'))

from integrated_processor import IntegratedTextProcessor

app = Flask(__name__)

# Global processor instance
processor = None


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_text():
    """Process text through the integrated pipeline."""
    global processor

    try:
        data = request.get_json()
        text = data.get('text', '')
        mode = data.get('mode', 'academic')
        domain = data.get('domain', 'academic')
        use_ml = data.get('use_ml', False)
        passes = int(data.get('passes', 1))
        skip_grammar = data.get('skip_grammar', False)

        if not text:
            return jsonify({'error': 'No text provided'}), 400

        # Initialize processor with selected options
        processor = IntegratedTextProcessor(
            mode=mode,
            domain=domain,
            use_ml=use_ml,
            humanizer_passes=passes,
            skip_grammar=skip_grammar
        )

        # Process the text (verbose=False for web interface)
        result = processor.process(text, verbose=False)

        # Calculate metrics
        original_words = len(text.split())
        result_words = len(result.split())

        return jsonify({
            'success': True,
            'result': result,
            'metrics': {
                'original_words': original_words,
                'result_words': result_words,
                'original_chars': len(text),
                'result_chars': len(result)
            }
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500


@app.route('/domains', methods=['GET'])
def get_domains():
    """Get available domains."""
    domains = [
        {'id': 'academic', 'name': 'Academic (General)', 'description': 'General academic writing'},
        {'id': 'medical', 'name': 'Medical', 'description': 'Clinical papers, medical research'},
        {'id': 'legal', 'name': 'Legal', 'description': 'Legal briefs, case analysis'},
        {'id': 'scientific', 'name': 'Scientific', 'description': 'Research papers, experiments'},
        {'id': 'technical', 'name': 'Technical', 'description': 'Tech blogs, documentation'},
    ]
    return jsonify({'domains': domains})


@app.route('/modes', methods=['GET'])
def get_modes():
    """Get available humanizer modes."""
    modes = [
        {'id': 'academic', 'name': 'Academic', 'description': 'Optimized for academic writing'},
        {'id': 'professional', 'name': 'Professional', 'description': 'Professional business writing'},
        {'id': 'balanced', 'name': 'Balanced', 'description': 'Balanced approach'},
    ]
    return jsonify({'modes': modes})


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok', 'version': '1.0'})


@app.route('/favicon.ico')
def favicon():
    """Return a simple favicon to prevent 404 errors."""
    return '', 204


if __name__ == '__main__':
    # Create templates and static directories
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)

    # Run the app
    print("\n" + "="*70)
    print("INTEGRATED TEXT PROCESSOR - WEB INTERFACE")
    print("="*70)
    print("\nStarting server at http://localhost:5001")
    print("Press Ctrl+C to stop\n")

    app.run(debug=True, host='0.0.0.0', port=5001)
