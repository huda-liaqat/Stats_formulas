# Statistics System

A Python-based statistics calculation system that analyzes weight data from CSV files and computes mean, median, and mode.

## Overview

The `StatisticsSystem` class provides a comprehensive solution for loading weight data from CSV files and calculating key statistical measures:
- **Mean**: Arithmetic average of all weights
- **Median**: Middle value when weights are sorted
- **Mode**: Most frequently occurring weight range

## Features

✅ **CSV File Loading**: Automatically reads and parses CSV data  
✅ **Data Validation**: Regex-based file name validation  
✅ **Statistical Calculations**: Accurate mean, median, and mode computation  
✅ **Error Handling**: Graceful handling of missing files and invalid data  
✅ **Sorted Output**: Weights are automatically sorted for median calculation  

## Requirements

- Python 3.6+
- Standard library modules only (csv, collections, re)
- No external dependencies required

## Installation

1. Clone or download the project files
2. Ensure `data.csv` is in the same directory as `Stats.py`
3. No additional packages need to be installed

## Usage

### Basic Usage

```python
from Stats import StatisticsSystem

# Create a system instance with your CSV file
system = StatisticsSystem("data.csv")

# Validate the file name
if system.validate_file_name():
    # Load data from CSV
    system.load_data()
    
    # Calculate statistics
    mean = system.get_mean()
    median = system.get_median()
    mode = system.get_mode()
    
    print(f"Mean -> {mean}")
    print(f"Median -> {median}")
    print(f"Mode -> {mode}")
else:
    print("Invalid File Name")
```

### Running the Script

```bash
python Stats.py
```

Expected output:
```
Mean -> 120.45
Median -> 119.50
Mode -> 122.50
```

## CSV File Format

The CSV file should have the following structure:

```csv
date,cases,country
2021-01-01,100,USA
2021-01-02,150,UK
2021-01-03,120,Canada
...
```

**Required Columns:**
- Column 0: `date` (any date format)
- Column 1: `cases` (numeric weight values)
- Column 2: `country` (location or category)

**Important Notes:**
- First row is treated as header and will be skipped
- Column index 1 (cases) is extracted as weight data
- Weights must be numeric values (int or float)
- File name must match pattern: `^[A-Za-z0-9_]+\.csv$`

## API Reference

### `StatisticsSystem(file_name)`

Constructor that initializes the statistics system.

**Parameters:**
- `file_name` (str): Name of the CSV file to analyze

**Attributes:**
- `file_name`: The CSV file name
- `data`: List containing all CSV rows
- `weights`: Sorted list of numeric weight values

### `load_data()`

Loads and processes CSV data.

**Functionality:**
- Opens the CSV file
- Skips the header row
- Extracts weight values from column 1
- Sorts weights in ascending order
- Handles `FileNotFoundError` gracefully

### `get_mean()`

Calculates the arithmetic mean of all weights.

**Returns:** float - Average weight value rounded to 2 decimal places

**Formula:** Mean = Σ(weights) / count(weights)

### `get_median()`

Calculates the median (middle value) of weights.

**Returns:** float - Median value rounded to 2 decimal places

**Logic:**
- If odd count: Returns middle value
- If even count: Returns average of two middle values
- Requires sorted data (done automatically in `load_data()`)

### `get_mode()`

Calculates the mode by grouping weights into ranges.

**Returns:** float - Mode (midpoint of most frequent range) rounded to 2 decimal places

**Weight Ranges:**
- 75-85, 85-95, 95-105, 105-115
- 115-125, 125-135, 135-145, 145-155
- 155-165, 165-175

**Logic:**
- Groups weights into predefined ranges
- Finds range with highest frequency
- Returns midpoint of the most frequent range

### `validate_file_name()`

Validates the CSV file name using regex pattern.

**Returns:** bool - True if valid, False otherwise

**Pattern:** `^[A-Za-z0-9_]+\.csv$`

**Valid Examples:**
- `data.csv` ✅
- `weight_data_2024.csv` ✅
- `test_123.csv` ✅

**Invalid Examples:**
- `data-file.csv` ❌ (contains hyphen)
- `data.txt` ❌ (wrong extension)
- `my data.csv` ❌ (contains space)

## Error Handling

### FileNotFoundError
If the specified CSV file doesn't exist:
```
File not found
```

### ValueError
If weight values are non-numeric:
```
ValueError: could not convert string to float
```

Ensure column 1 contains only numeric values.

### InvalidFileNameError
If the file name doesn't match the pattern:
```
Invalid File Name
```

## Example Workflow

1. **Prepare CSV File** (data.csv)
   ```csv
   date,weight,category
   2024-01-01,120.5,Group A
   2024-01-02,125.3,Group B
   2024-01-03,120.5,Group A
   ```

2. **Run Script**
   ```bash
   python Stats.py
   ```

3. **View Results**
   ```
   Mean -> 122.10
   Median -> 120.50
   Mode -> 122.50
   ```

## Testing

To test the system with sample data:

```python
# Create a test CSV file
import csv

test_data = [
    ["date", "weight", "location"],
    ["2024-01-01", "120", "USA"],
    ["2024-01-02", "125", "UK"],
    ["2024-01-03", "120", "Canada"],
    ["2024-01-04", "130", "USA"]
]

with open("test_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(test_data)

# Run statistics
system = StatisticsSystem("test_data.csv")
system.load_data()
print(f"Mean: {system.get_mean()}")        # 123.75
print(f"Median: {system.get_median()}")    # 122.5
print(f"Mode: {system.get_mode()}")        # 122.5
```

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "File not found" | CSV file missing | Ensure `data.csv` exists in the same directory |
| ValueError: could not convert | Non-numeric data in column 1 | Check CSV format, ensure column 1 contains only numbers |
| "Invalid File Name" | File name doesn't match pattern | Rename file to match `[A-Za-z0-9_]+.csv` pattern |
| Empty results | No weights loaded | Verify CSV has data rows (not just header) |

## Requirements Met

### Functional Requirements ✅
- [x] System loads CSV data correctly
- [x] System calculates mean accurately
- [x] System calculates median accurately
- [x] System calculates mode using weight ranges

### Non-Functional Requirements ✅
- [x] System validates CSV file names using regex
- [x] Error handling for missing files
- [x] Data type validation for numeric weights

## Future Enhancements

- Database support for larger datasets
- Multiple file batch processing
- Custom weight range definitions
- Standard deviation and variance calculations
- Data visualization (charts/graphs)
- Export results to different formats (JSON, Excel)
- Command-line interface with arguments

## License

Open source - Feel free to use and modify

## Author

Created for SQA Testing Project

## Version

1.0.0 - Initial Release
