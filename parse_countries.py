#!/usr/bin/env python3
"""
Country List Parser

This script parses the list_of_countries.html file and extracts all country names
from <span> tags, outputting them to a text file with one country per line.

Usage:
    python parse_countries.py

Output:
    countries.txt - Text file with one country per line
"""

import re
from pathlib import Path
from typing import List


def parse_countries_from_html(html_file_path: str) -> List[str]:
    """
    Parse country names from HTML file containing <span> tags.
    
    Args:
        html_file_path: Path to the HTML file
        
    Returns:
        List of country names
    """
    try:
        # Read the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Find all content within <span> tags using regex
        span_pattern = r'<span[^>]*>(.*?)</span>'
        matches = re.findall(span_pattern, html_content, re.IGNORECASE | re.DOTALL)
        
        # Clean up the extracted text
        countries = []
        for match in matches:
            # Remove any HTML tags that might be nested
            clean_text = re.sub(r'<[^>]+>', '', match)
            # Strip whitespace and decode HTML entities
            clean_text = clean_text.strip()
            
            # Skip empty strings
            if clean_text:
                countries.append(clean_text)
        
        # Remove duplicates while preserving order
        unique_countries = []
        seen = set()
        for country in countries:
            if country not in seen:
                unique_countries.append(country)
                seen.add(country)
        
        return unique_countries
        
    except FileNotFoundError:
        print(f"Error: File '{html_file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def save_countries_to_file(countries: List[str], output_file: str) -> None:
    """
    Save country list to a text file with one country per line.
    
    Args:
        countries: List of country names
        output_file: Path to output text file
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for country in countries:
                file.write(f"{country}\n")
        
        print(f"Successfully saved {len(countries)} countries to '{output_file}'")
        
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    """Main function to parse countries and save to file."""
    # File paths
    html_file = "list_of_countries.html"
    output_file = "countries.txt"
    
    # Check if input file exists
    if not Path(html_file).exists():
        print(f"Error: '{html_file}' not found in current directory.")
        print("Please ensure the HTML file is in the same directory as this script.")
        return
    
    print(f"Parsing countries from '{html_file}'...")
    
    # Parse countries from HTML
    countries = parse_countries_from_html(html_file)
    
    if not countries:
        print("No countries found or error occurred during parsing.")
        return
    
    # Display some statistics
    print(f"Found {len(countries)} unique countries")
    
    # Show first few countries as preview
    if countries:
        print("\nFirst 5 countries found:")
        for i, country in enumerate(countries[:5], 1):
            print(f"  {i}. {country}")
        
        if len(countries) > 5:
            print(f"  ... and {len(countries) - 5} more")
    
    # Save to file
    save_countries_to_file(countries, output_file)
    
    print(f"\nDone! Countries saved to '{output_file}'")


if __name__ == "__main__":
    main() 