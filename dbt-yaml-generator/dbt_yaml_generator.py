#!/usr/bin/env python
"""
This code generates YAML file from all dbt sql model file in the directory.
"""
import os
import re
import jinja2

def get_sql_file_names():
    # Get the current directory
    current_directory = os.getcwd()

    # List all files in the current directory
    all_files = os.listdir(current_directory)

    # Initialize an empty list to store SQL file names without extension
    sql_files_without_extension = []

    # Iterate through all files and filter SQL files
    for file_name in all_files:
        if file_name.endswith(".sql"):
            # Remove the ".sql" extension and add to the list
            sql_file_name = file_name[:-4]
            sql_files_without_extension.append(sql_file_name)

    # Print the list of SQL file names without extension
    return(sql_files_without_extension)

def get_sql_content(file_name):
    # Read the SQL file
    with open(f'{file_name}.sql', 'r') as sql_file:
        sql_content = sql_file.read()

    # Find the last word in sql_content
    last_word_match = re.search(r'\b\w+\b', sql_content[::-1])
    if last_word_match:
        last_word = last_word_match.group(0)[::-1]
    else:
        last_word = ""

    # Use the last word to split sql_content and parse from there
    if last_word:
        sql_content_parts = sql_content.split(last_word, 1)
        if len(sql_content_parts) > 1:
            sql_content_to_parse = sql_content_parts[1]
        else:
            sql_content_to_parse = sql_content
    else:
        sql_content_to_parse = sql_content
    
    return(sql_content_to_parse)

def get_table_columns(sql_content_to_parse):
    pattern = r'(\w+)(?:\s+as\s+(\w+))?(?:,|\s+FROM\b)'
    columns = re.findall(pattern, sql_content_to_parse)
    columns = [(column, alias if alias else column) for column, alias in columns]

    # Create a dictionary to hold column data
    column_data = [{'name': col[1], 'description': ""} for col in columns]

    return column_data

def write_to_yaml_file(file_name, column_data):
    # Render the YAML template using jinja2
    template = jinja2.Template('''\
    version: 2
    
    models:
    - name: {{ file_name }}
        description: "Information on {{ file_name }}"
        columns:
    {% for col in column_data %}
        - name: {{ col['name'] }}
            description: "{{ col['description'] }}"
    {% endfor %}
    ''')
    # Write the rendered YAML content to a file
    with open(f'{file_name}.yml', 'w') as yml_file:
        yml_file.write(template.render(file_name=file_name, column_data=column_data))

    print(f"YAML file named {file_name}.yml generated successfully.")

def main():
    sql_files = get_sql_file_names()
    for file_name in sql_files:
        sql_content = get_sql_content(file_name)
        column_data = get_table_columns(sql_content)
        write_to_yaml_file(file_name, column_data)

if __name__ == '__main__':
    main()