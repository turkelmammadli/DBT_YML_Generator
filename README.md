# DBT YAML Generator

This Python script automates the process of generating YAML documentation files for your DBT (Data Build Tool) models. The only limitation is that, it requires CTE usage, otherwise columns are not generated
Proper documentation is crucial for understanding your data models and facilitating collaboration within your data engineering team. With this script, you can easily create documentation files for each of your DBT models.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python 3.x
- Jinja2 (you can install it using `pip install Jinja2`)

## Usage

1. **Clone the Repository**:

   Clone this repository to your local machine using the following command:
   
   `git clone https://github.com/turkelmammadli/DBT_YML_Generator.git`


2. **Navigate to the Directory**:
   
   Change your working directory to the cloned repository:
    `cd dbt-yaml-generator`


4. **Place Your SQL Files**:

   Place your DBT SQL model files (with a `.sql` extension) in the same directory as the script.

4. **Run the Script**:

   Execute the script by running the following command:

   `python dbt_yaml_generator.py`

   This will process all the SQL files in the current directory and generate YAML documentation files for each model.

6. **Generated YAML Files**:

   The generated YAML documentation files will be saved in the same directory as your SQL files. Each YAML file will have the same name as the corresponding SQL file, but with a `.yml` extension.

7. **Customize Documentation** (Optional):

   You can customize the generated YAML documentation by modifying the Jinja2 template in the `dbt_yaml_generator.py` script. Customize the `description` and other attributes as needed.

### Example

  Suppose you have a DBT model SQL file named `my_model.sql`. After running the script, a YAML documentation file named `my_model.yml` will be generated, containing documentation for the columns in your model.

## Contributing

  Contributions are welcome! If you have any improvements or feature suggestions for this script, please feel free to open an issue or submit a pull request.

## Acknowledgments

  Enjoy automating your DBT model documentation with this script! If you have any questions or encounter issues, please don't hesitate to reach out or open an issue on GitHub.
