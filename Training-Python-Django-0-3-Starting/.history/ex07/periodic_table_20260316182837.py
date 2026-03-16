#!/usr/bin/env python3
import sys

def parse_periodic_table(filename):
    """Parse the periodic_table.txt file and return a dictionary of elements."""
    elements = {}
    
    try:
        with open(filename, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                
                # Parse line format: Name = position:X, number:X, small: X, molar:X, electron:X X X
                parts = line.strip().split(' = ')
                name = parts[0]
                
                attributes = {}
                for attr in parts[1].split(', '):
                    key, value = attr.split(':')
                    attributes[key.strip()] = value.strip()
                
                elements[name] = {
                    'position': int(attributes['position']),
                    'number': int(attributes['number']),
                    'symbol': attributes['small'],
                    'molar': float(attributes['molar']),
                    'electron': attributes['electron']
                }
        
        return elements
    except FileNotFoundError:
        print(f"Error: File {filename} not found", file=sys.stderr)
        sys.exit(1)


def organize_elements(elements):
    """Organize elements into a periodic table structure."""
    # Initialize 7 rows (0-6) with 18 columns each
    table = [[None for _ in range(18)] for _ in range(7)]
    
    # Regular elements (excluding lanthanides and actinides initially)
    for name, data in elements.items():
        number = data['number']
        position = data['position']
        row = get_element_row(number)
        
        if 57 <= number <= 71 or 89 <= number <= 103:
            continue  # Handle separately
        
        if row < 7:
            table[row][position] = name
    
    return table


def get_element_row(number):
    """Determine the row number for an element based on its atomic number."""
    if number <= 2:
        return 0
    elif number <= 10:
        return 1
    elif number <= 18:
        return 2
    elif number <= 36:
        return 3
    elif number <= 54:
        return 4
    elif 57 <= number <= 71 or number <= 86:
        return 5
    elif 89 <= number <= 103 or number <= 118:
        return 6
    else:
        return 6


def create_element_cell(name, data):
    """Create an HTML cell for an element."""
    cell = f'            <td style="border: 2px solid black; padding: 10px; width: 80px; height: 100px; text-align: center; vertical-align: top; background-color: #e8f4f8;">\n'
    cell += f'                <h4 style="margin: 5px 0; font-size: 14px;">{name}</h4>\n'
    cell += '                <ul style="list-style-position: inside; margin: 5px 0; padding: 0; font-size: 10px;">\n'
    cell += f'                    <li>No. {data["number"]}</li>\n'
    cell += f'                    <li>{data["symbol"]}</li>\n'
    cell += f'                    <li>{data["molar"]}</li>\n'
    cell += f'                    <li>{data["electron"]} electrons</li>\n'
    cell += '                </ul>\n'
    cell += '            </td>\n'
    return cell


def create_html(elements, output_filename):
    """Create an HTML file representing the periodic table."""
    # Build lookup dictionary for element names by number
    element_by_number = {data['number']: name for name, data in elements.items()}
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Periodic Table of Elements</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        table {
            border-collapse: collapse;
            margin: 20px 0;
            background-color: white;
        }
        td {
            border: 1px solid #333;
            padding: 10px;
        }
        .empty {
            background-color: #f0f0f0;
        }
        h1 {
            text-align: center;
        }
        h2 {
            margin-top: 30px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Periodic Table of Elements</h1>
    
"""
    
    # Build table structure
    table = [[None for _ in range(18)] for _ in range(7)]
    
    # Place all regular elements
    for name, data in elements.items():
        number = data['number']
        position = data['position']
        
        if 57 <= number <= 71 or 89 <= number <= 103:
            continue  # Handle separately below
        
        row = get_element_row(number)
        if row < 7 and position < 18:
            table[row][position] = name
    
    # Generate main table
    html_content += "    <table>\n"
    
    for row_idx in range(7):
        html_content += "        <tr>\n"
        for col_idx in range(18):
            element_name = table[row_idx][col_idx]
            if element_name is None:
                html_content += '            <td class="empty" style="width: 80px; height: 100px; background-color: #f0f0f0;"></td>\n'
            else:
                data = elements[element_name]
                html_content += create_element_cell(element_name, data)
        html_content += "        </tr>\n"
    
    html_content += "    </table>\n"
    
    # Handle Lanthanides
    lanth_elements = sorted(
        [(n, elements[en]) for n, en in element_by_number.items() if 57 <= n <= 71],
        key=lambda x: x[0]
    )
    
    if lanth_elements:
        html_content += "\n    <h2>Lanthanides Series</h2>\n"
        html_content += "    <table>\n"
        html_content += "        <tr>\n"
        for number, data in lanth_elements:
            element_name = element_by_number[number]
            html_content += f'            <td style="border: 2px solid purple; padding: 10px; width: 80px; height: 100px; text-align: center; vertical-align: top; background-color: #f0e6ff;">\n'
            html_content += f'                <h4 style="margin: 5px 0; font-size: 14px;">{element_name}</h4>\n'
            html_content += '                <ul style="list-style-position: inside; margin: 5px 0; padding: 0; font-size: 10px;">\n'
            html_content += f'                    <li>No. {data["number"]}</li>\n'
            html_content += f'                    <li>{data["symbol"]}</li>\n'
            html_content += f'                    <li>{data["molar"]}</li>\n'
            html_content += '                </ul>\n'
            html_content += '            </td>\n'
        html_content += "        </tr>\n"
        html_content += "    </table>\n"
    
    # Handle Actinides
    actin_elements = sorted(
        [(n, elements[en]) for n, en in element_by_number.items() if 89 <= n <= 103],
        key=lambda x: x[0]
    )
    
    if actin_elements:
        html_content += "\n    <h2>Actinides Series</h2>\n"
        html_content += "    <table>\n"
        html_content += "        <tr>\n"
        for number, data in actin_elements:
            element_name = element_by_number[number]
            html_content += f'            <td style="border: 2px solid red; padding: 10px; width: 80px; height: 100px; text-align: center; vertical-align: top; background-color: #ffe6f0;">\n'
            html_content += f'                <h4 style="margin: 5px 0; font-size: 14px;">{element_name}</h4>\n'
            html_content += '                <ul style="list-style-position: inside; margin: 5px 0; padding: 0; font-size: 10px;">\n'
            html_content += f'                    <li>No. {data["number"]}</li>\n'
            html_content += f'                    <li>{data["symbol"]}</li>\n'
            html_content += f'                    <li>{data["molar"]}</li>\n'
            html_content += '                </ul>\n'
            html_content += '            </td>\n'
        html_content += "        </tr>\n"
        html_content += "    </table>\n"
    
    html_content += """
</body>
</html>
"""
    
    try:
        with open(output_filename, 'w') as f:
            f.write(html_content)
        print(f"Successfully created {output_filename}")
    except IOError as e:
        print(f"Error writing to file {output_filename}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to create the periodic table HTML."""
    input_file = "periodic_table.txt"
    output_file = "periodic_table.html"
    
    # Parse the periodic table data
    elements = parse_periodic_table(input_file)
    
    # Create the HTML file
    create_html(elements, output_file)


if __name__ == "__main__":
    main()
