#!/usr/bin/env python3
"""
check_word_count.py
Checks that each provided .docx file meets the minimum word count.
Usage: python check_word_count.py file1.docx file2.docx ...
"""

import sys
from docx import Document

MIN_WORDS = 500
failed = False

if len(sys.argv) < 2:
    print("Usage: python check_word_count.py <file1.docx> [file2.docx ...]")
    sys.exit(0)

for path in sys.argv[1:]:
    path = path.strip()
    if not path:
        continue
    if not path.lower().endswith('.docx'):
        print(f"  Skipping non-.docx file: {path}")
        continue
    try:
        doc = Document(path)
        full_text = ' '.join(
            para.text for para in doc.paragraphs if para.text.strip()
        )
        word_count = len(full_text.split())
        if word_count < MIN_WORDS:
            print(f"FAIL: '{path}' has only {word_count} words (minimum: {MIN_WORDS})")
            failed = True
        else:
            print(f"PASS: '{path}' has {word_count} words")
    except Exception as e:
        print(f"ERROR: Could not read '{path}': {e}")
        failed = True

if failed:
    print("\nOne or more documents did not meet the minimum word count of 500.")
    sys.exit(1)
else:
    print("\nAll documents meet the minimum word count requirement!")
    sys.exit(0)
