#!/usr/bin/env python3
#
# Import libraries
import re  # regular expressions

text = "kAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbTaWEReGHYvkAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbTbCDFuWSXjAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpimvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcptIUYrTGBuAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiAewtloYgcFQaJNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtlXDiQmzjfcpiiERToMKOotloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtltloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtltloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvGmYmvnJIHEmbTkAewtloWAScWQAsNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvdTGXoERBfNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvgTYUmVBNhNhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiGqhRRiUvhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiAewhHVGxmvnJIHEmbTkAewtloYgcFQaJNhHVGxXDiQmzjfcpiAe"

matched_patterns = []  # store matched patterns

# Robust search for patterns because if a match if found, the next search uses previous characters.
for i in range(len(text)):
    # Search for pattern
    match = re.search(r'[A-Z]{3}[a-z][A-Z]{3}', text[i:i + 7])

    # If there is a match append to list of matched patterns
    if match:
        matched_patterns.append(match.group())

# Create a word from small letters found in matched_patterns
small_letters = ''.join(re.findall(r'[a-z]+', ''.join(matched_patterns)))

# Print a created word
print(''.join(small_letters))
