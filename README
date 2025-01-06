# Data Extraction Tool

This repository contains a Python script to extract structured data from unstructured text files and save it in CSV format. The tool is designed to process input logs and extract key fields like type, category, URL, hostname, and additional information.

## Features

- Extracts data fields using regular expressions
- Supports type, category, URL, hostname, and additional information fields
- Saves output in a structured CSV format

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-extraction-tool.git
   cd data-extraction-tool
   ```

2. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your input file (e.g., `result.txt`) in the repository folder.

2. Run the script:
   ```bash
   python data_extraction.py
   ```

3. Enter the input file path when prompted.

4. The output will be saved as `result.csv` in the same folder.

## File Structure

```
|-- data-extraction-tool/
    |-- data_extraction.py  # Main script
    |-- requirements.txt    # Dependency list (if any)
    |-- README.md           # Documentation (this file)
    |-- result.csv          # Generated CSV output (example output file)
    |-- input.txt           # Example input file (optional)
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Example Input
```
[azure-domain-tenant] [http] [info] https://login.microsoftonline.com:443/example/v2.0/.well-known/openid-configuration ["example-id"]
```

### Example Output
| type                  | category | url                                                         | hostname                  | additional_info |
|-----------------------|----------|-------------------------------------------------------------|---------------------------|-----------------|
| azure-domain-tenant  | info     | https://login.microsoftonline.com:443/example/v2.0/.well... | login.microsoftonline.com | example-id      |
