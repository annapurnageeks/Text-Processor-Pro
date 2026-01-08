#!/usr/bin/env python3
"""
Integrated Text Processing Pipeline
Combines AI Humanizer and Grammar Corrector

Flow: Input Text → Humanize → Grammar Correct → Output
"""

import sys
import os

# Add project directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(parent_dir, 'AI-Humanizer'))
sys.path.insert(0, os.path.join(parent_dir, 'Grammar-Corrector'))

from ultra_humanizer import UltraHumanizer
from correct import GrammarCorrector


class IntegratedTextProcessor:
    """
    Integrated text processing pipeline that combines:
    1. AI Humanization (makes text sound more human-like)
    2. Grammar Correction (fixes grammar errors using transformer model)
    """

    def __init__(self, mode='academic', domain='academic', use_ml=False, humanizer_passes=1, skip_grammar=False):
        """
        Initialize the integrated processor.

        Args:
            mode: Humanizer mode ('professional', 'academic', 'balanced')
            domain: Domain for humanizer ('academic', 'medical', 'legal', 'scientific', 'technical')
            use_ml: Whether to use ML-based humanization (slower but better quality)
            humanizer_passes: Number of humanization passes (1-3, default 1 for speed)
            skip_grammar: Skip grammar correction step (much faster)
        """
        print("="*70)
        print("INITIALIZING INTEGRATED TEXT PROCESSOR")
        print("="*70)

        # Initialize AI Humanizer
        print("\n[1/2] Loading AI Humanizer...")
        self.humanizer = UltraHumanizer(
            mode=mode,
            use_ml=use_ml,
            domain=domain
        )
        print("✓ AI Humanizer loaded")

        # Initialize Grammar Corrector
        self.skip_grammar = skip_grammar
        if not skip_grammar:
            print("\n[2/2] Loading Grammar Corrector (Transformer Model)...")
            self.grammar_corrector = GrammarCorrector()
            print("✓ Grammar Corrector loaded")
        else:
            print("\n[2/2] Grammar Correction disabled (skip_grammar=True)")
            self.grammar_corrector = None

        self.humanizer_passes = humanizer_passes

        print("\n" + "="*70)
        print("INTEGRATED PROCESSOR READY")
        print("="*70)

    def process(self, text, verbose=True):
        """
        Process text through the integrated pipeline.

        Args:
            text: Input text to process
            verbose: Whether to print progress information

        Returns:
            Processed text (humanized + grammar corrected)
        """
        if not text or not text.strip():
            return text

        if verbose:
            print("\n" + "="*70)
            print("PROCESSING TEXT")
            print("="*70)
            print(f"\nOriginal text length: {len(text)} characters")
            print(f"Original word count: {len(text.split())} words")

        # Step 1: Humanize the text
        if verbose:
            print("\n" + "-"*70)
            print("STEP 1: HUMANIZING TEXT")
            print("-"*70)

        humanized_text = self.humanizer.humanize(text, passes=self.humanizer_passes)

        if verbose:
            print(f"\n✓ Humanization complete")
            print(f"Humanized text length: {len(humanized_text)} characters")
            print(f"Humanized word count: {len(humanized_text.split())} words")

        # Step 2: Correct grammar using transformer model (optional)
        if self.skip_grammar or not self.grammar_corrector:
            if verbose:
                print("\n" + "-"*70)
                print("STEP 2: SKIPPING GRAMMAR CORRECTION (disabled)")
                print("-"*70)
            final_text = humanized_text
        else:
            if verbose:
                print("\n" + "-"*70)
                print("STEP 2: CORRECTING GRAMMAR (Transformer Model)")
                print("-"*70)

            # Split into sentences for better grammar correction
            sentences = humanized_text.split('. ')
            corrected_sentences = []

            for i, sentence in enumerate(sentences, 1):
                if not sentence.strip():
                    continue

                # Add period back if it's not the last sentence
                if not sentence.endswith('.') and not sentence.endswith('!') and not sentence.endswith('?'):
                    sentence_to_correct = sentence + '.'
                else:
                    sentence_to_correct = sentence

                if verbose:
                    print(f"  Processing sentence {i}/{len(sentences)}...")

                # Use the transformer-based grammar corrector
                corrected = self.grammar_corrector.correct(sentence_to_correct)
                corrected_sentences.append(corrected)

            final_text = ' '.join(corrected_sentences)

        if verbose:
            if not self.skip_grammar and self.grammar_corrector:
                print(f"\n✓ Grammar correction complete")
            print(f"Final text length: {len(final_text)} characters")
            print(f"Final word count: {len(final_text.split())} words")

            print("\n" + "="*70)
            print("PROCESSING COMPLETE")
            print("="*70)

        return final_text


def main():
    """Main function for CLI usage."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Integrated Text Processor: Humanize + Grammar Correct'
    )
    parser.add_argument(
        '--text',
        type=str,
        help='Text to process'
    )
    parser.add_argument(
        '--file',
        type=str,
        help='File containing text to process'
    )
    parser.add_argument(
        '--output',
        type=str,
        help='Output file (optional, prints to console if not specified)'
    )
    parser.add_argument(
        '--mode',
        type=str,
        default='academic',
        choices=['professional', 'academic', 'balanced'],
        help='Humanizer mode (default: academic)'
    )
    parser.add_argument(
        '--domain',
        type=str,
        default='academic',
        choices=['academic', 'medical', 'legal', 'scientific', 'technical'],
        help='Domain for humanization (default: academic)'
    )
    parser.add_argument(
        '--passes',
        type=int,
        default=2,
        choices=[1, 2, 3],
        help='Number of humanization passes (default: 2)'
    )
    parser.add_argument(
        '--no-ml',
        action='store_true',
        help='Disable ML-based humanization'
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='Minimal output (only show final result)'
    )
    parser.add_argument(
        '--skip-grammar',
        action='store_true',
        help='Skip grammar correction for faster processing'
    )

    args = parser.parse_args()

    # Get input text
    if args.file:
        print(f"Reading from file: {args.file}")
        with open(args.file, 'r', encoding='utf-8') as f:
            input_text = f.read()
    elif args.text:
        input_text = args.text
    else:
        # Interactive mode
        print("\n" + "="*70)
        print("INTEGRATED TEXT PROCESSOR - Interactive Mode")
        print("="*70)
        print("Enter your text (press Ctrl+D or Ctrl+Z when done):\n")
        input_text = sys.stdin.read()

    if not input_text.strip():
        print("Error: No text provided")
        return 1

    # Initialize processor
    processor = IntegratedTextProcessor(
        mode=args.mode,
        domain=args.domain,
        use_ml=not args.no_ml,
        humanizer_passes=args.passes,
        skip_grammar=args.skip_grammar
    )

    # Process the text
    result = processor.process(input_text, verbose=not args.quiet)

    # Output results
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\n✓ Output written to: {args.output}")
    else:
        print("\n" + "="*70)
        print("FINAL RESULT")
        print("="*70)
        print(result)
        print("="*70)

    return 0


if __name__ == '__main__':
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
