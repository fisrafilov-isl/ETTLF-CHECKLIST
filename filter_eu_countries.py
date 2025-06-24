#!/usr/bin/env python3
"""
EU/Visa-Free Countries Filter for Cyprus

This script filters the countries.txt file to extract only countries whose citizens
can visit Cyprus without visa requirements. This includes EU countries, EEA countries,
and countries with special visa-free agreements with Cyprus.

Usage:
    python filter_eu_countries.py

Input:
    countries.txt - Full list of countries

Output:
    eu_countries.txt - Countries with visa-free access to Cyprus
"""

from pathlib import Path
from typing import List, Set


def get_unlimited_presence_countries_for_cyprus() -> Set[str]:
    """
    Returns a set of countries whose citizens can have unlimited presence in Cyprus.
    
    This includes:
    - EU member states (freedom of movement)
    - EEA countries (Norway, Iceland, Liechtenstein)
    - Switzerland (bilateral agreement for freedom of movement)
    - Microstates with special agreements (Andorra, Monaco, San Marino, Vatican City)
    
    Returns:
        Set of country names that have unlimited presence rights in Cyprus
    """
    
    # EU Member States (27 countries as of 2023)
    eu_countries = {
        "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
        "Denmark", "Estonia", "Finland", "France", "Germany", "Greece",
        "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg",
        "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia",
        "Slovenia", "Spain", "Sweden"
    }
    
    # EEA countries (non-EU)
    eea_countries = {
        "Iceland", "Liechtenstein", "Norway"
    }
    
    # Switzerland (bilateral agreement with EU)
    switzerland = {"Switzerland"}
    
    # Countries with unlimited presence rights (freedom of movement)
    # Note: This list may change based on current agreements
    unlimited_presence_countries = {
        "Andorra", "Monaco", "San Marino", "Vatican City"
        # Note: UK removed - post-Brexit they only have visa-free short stays, not unlimited presence
    }
    
    # Combine all sets
    all_unlimited_presence = eu_countries | eea_countries | switzerland | unlimited_presence_countries
    
    return all_unlimited_presence


def load_countries_from_file(file_path: str) -> List[str]:
    """
    Load country list from text file.
    
    Args:
        file_path: Path to the countries text file
        
    Returns:
        List of country names
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            countries = [line.strip() for line in file if line.strip()]
        return countries
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def filter_unlimited_presence_countries(all_countries: List[str], unlimited_presence_set: Set[str]) -> List[str]:
    """
    Filter countries list to include only those with unlimited presence rights in Cyprus.
    
    Args:
        all_countries: Complete list of countries
        unlimited_presence_set: Set of countries with unlimited presence rights
        
    Returns:
        Filtered list of unlimited presence countries
    """
    filtered_countries = []
    
    for country in all_countries:
        # Check for exact match first
        if country in unlimited_presence_set:
            filtered_countries.append(country)
            continue
            
        # Handle special cases and variations
        country_lower = country.lower()
        
        # Special mappings for countries that might have different names
        name_mappings = {
            "czech republic": "Czech Republic",
            "vatican city": "Vatican City"
            # Note: UK removed from mappings as they no longer have unlimited presence rights
        }
        
        if country_lower in name_mappings:
            mapped_name = name_mappings[country_lower]
            if mapped_name in unlimited_presence_set:
                filtered_countries.append(country)
    
    return filtered_countries


def save_countries_to_file(countries: List[str], output_file: str) -> None:
    """
    Save filtered country list to output file in pipe-separated format with explanations.
    
    Args:
        countries: List of unlimited presence countries
        output_file: Path to output file
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            # Write explanatory header
            file.write("Countries whose citizens can have unlimited presence in Cyprus\n")
            file.write("Last updated: 2024\n")
            file.write("\n")
            file.write("This list includes:\n")
            file.write("- EU Member States (27 countries): Citizens have freedom of movement within EU\n")
            file.write("- EEA Countries (3 countries): Iceland, Liechtenstein, Norway - part of European Economic Area\n")
            file.write("- Switzerland: Has bilateral agreements with EU for freedom of movement\n")
            file.write("- Microstates: Andorra, Monaco, San Marino, Vatican City - special agreements with EU\n")
            file.write("\n")
            file.write("Note: Regulations may change. Always verify current requirements.\n")
            file.write("For E&T/TLF students from these countries: NO additional visa documents required\n")
            file.write("For E&T/TLF students from other countries: Additional visa documents required\n")
            file.write("\n")
            file.write("Format: Country | Country | Country | ...\n")
            file.write("\n")
            
            # Write countries in pipe-separated format
            countries_line = " | ".join(sorted(countries))
            file.write(countries_line)
            file.write("\n")
        
        print(f"Successfully saved {len(countries)} unlimited presence countries to '{output_file}'")
        print("Format: Pipe-separated with explanatory header")
        
    except Exception as e:
        print(f"Error writing to file: {e}")


def main():
    """Main function to filter countries and create EU/visa-free countries list."""
    
    # File paths
    input_file = "countries.txt"
    output_file = "eu_countries.txt"
    
    # Check if input file exists
    if not Path(input_file).exists():
        print(f"Error: '{input_file}' not found in current directory.")
        print("Please ensure countries.txt is available.")
        return
    
    print(f"Loading countries from '{input_file}'...")
    
    # Load all countries
    all_countries = load_countries_from_file(input_file)
    if not all_countries:
        print("No countries loaded or error occurred.")
        return
    
    print(f"Loaded {len(all_countries)} countries")
    
    # Get unlimited presence countries set
    unlimited_presence_set = get_unlimited_presence_countries_for_cyprus()
    print(f"Checking against {len(unlimited_presence_set)} known unlimited presence countries for Cyprus")
    
    # Filter countries
    filtered_countries = filter_unlimited_presence_countries(all_countries, unlimited_presence_set)
    
    if not filtered_countries:
        print("No unlimited presence countries found in the input list.")
        return
    
    # Display results
    print(f"\nFound {len(filtered_countries)} countries with unlimited presence rights in Cyprus:")
    for i, country in enumerate(sorted(filtered_countries), 1):
        print(f"  {i:2d}. {country}")
    
    # Show pipe-separated preview
    print(f"\nPipe-separated format preview:")
    preview_line = " | ".join(sorted(filtered_countries))
    if len(preview_line) > 100:
        print(f"  {preview_line[:100]}...")
    else:
        print(f"  {preview_line}")
    
    # Save to file
    save_countries_to_file(sorted(filtered_countries), output_file)
    
    print(f"\nDone! Unlimited presence countries saved to '{output_file}'")
    print("\nNote: This list includes EU/EEA countries and microstates with unlimited presence rights.")
    print("Regulations may change - please verify current requirements.")


if __name__ == "__main__":
    main() 