#!/usr/bin/env python3
"""
Test script for the Integrated Text Processor
Demonstrates basic usage with example texts
"""

import sys
import os

# Add project directories to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, os.path.join(parent_dir, 'AI-Humanizer'))
sys.path.insert(0, os.path.join(parent_dir, 'Grammar-Corrector'))

from integrated_processor import IntegratedTextProcessor


def test_basic_processing():
    """Test basic text processing."""
    print("\n" + "="*70)
    print("TEST 1: Basic Processing")
    print("="*70)

    # Sample AI-generated text
    input_text = """
The implementation of artificial intelligence in contemporary research
methodologies has demonstrated significant potential for enhancing the
efficiency of data analysis processes. Furthermore, the utilization of
machine learning algorithms has facilitated unprecedented advancements
in predictive modeling capabilities across numerous scientific domains.
"""

    # Initialize processor
    processor = IntegratedTextProcessor(
        mode='academic',
        domain='scientific',
        use_ml=False,  # Disable ML for faster testing
        humanizer_passes=1
    )

    # Process the text
    print("\nINPUT TEXT:")
    print("-" * 70)
    print(input_text.strip())
    print("-" * 70)

    result = processor.process(input_text, verbose=False)

    print("\nOUTPUT TEXT:")
    print("-" * 70)
    print(result)
    print("-" * 70)

    print("\n✓ Test 1 Complete\n")


def test_multiple_paragraphs():
    """Test processing with multiple paragraphs."""
    print("\n" + "="*70)
    print("TEST 2: Multiple Paragraphs")
    print("="*70)

    input_text = """
The rapid advancement of technology has fundamentally transformed the
landscape of modern communication. Digital platforms have facilitated
unprecedented levels of connectivity and information exchange.

Moreover, the integration of artificial intelligence systems has enabled
sophisticated automation of various processes. This technological evolution
continues to reshape numerous aspects of contemporary society.
"""

    processor = IntegratedTextProcessor(
        mode='professional',
        domain='technical',
        use_ml=False,
        humanizer_passes=1
    )

    print("\nINPUT TEXT:")
    print("-" * 70)
    print(input_text.strip())
    print("-" * 70)

    result = processor.process(input_text, verbose=False)

    print("\nOUTPUT TEXT:")
    print("-" * 70)
    print(result)
    print("-" * 70)

    print("\n✓ Test 2 Complete\n")


def test_short_text():
    """Test processing with short text."""
    print("\n" + "="*70)
    print("TEST 3: Short Text")
    print("="*70)

    input_text = """
Machine learning enables computers to learn from data without explicit
programming. This capability has revolutionized many industries.
"""

    processor = IntegratedTextProcessor(
        mode='balanced',
        domain='academic',
        use_ml=False,
        humanizer_passes=1
    )

    print("\nINPUT TEXT:")
    print("-" * 70)
    print(input_text.strip())
    print("-" * 70)

    result = processor.process(input_text, verbose=False)

    print("\nOUTPUT TEXT:")
    print("-" * 70)
    print(result)
    print("-" * 70)

    print("\n✓ Test 3 Complete\n")


def main():
    """Run all tests."""
    print("\n" + "="*70)
    print("INTEGRATED TEXT PROCESSOR - TEST SUITE")
    print("="*70)
    print("\nRunning tests with ML disabled for faster execution...")
    print("For best results, run with use_ml=True (requires PEGASUS model)\n")

    try:
        # Run tests
        test_basic_processing()
        test_multiple_paragraphs()
        test_short_text()

        print("\n" + "="*70)
        print("ALL TESTS COMPLETED SUCCESSFULLY")
        print("="*70)
        print("\nNext steps:")
        print("1. Try with ML enabled: use_ml=True")
        print("2. Experiment with different modes and domains")
        print("3. Test with your own text using:")
        print("   python integrated_processor.py --text 'Your text here'")
        print("="*70 + "\n")

    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
