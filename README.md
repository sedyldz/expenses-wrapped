# Expenses Wrapped

## Overview

`expenses-wrapped` is a Python script designed to automate the categorization of monthly expenses from Excel files. It processes transaction records, including company names, dates, and amounts, and categorizes each expense based on predefined keywords. The script handles Turkish-specific case conversions for accurate categorization and includes visualization through pie charts to represent the distribution of expenses across different categories. This tool is particularly useful for individuals looking to gain insights into their spending patterns and manage their finances more effectively.

<img width="848" alt="Screenshot 2024-02-05 at 17 54 03" src="https://github.com/sedyldz/expenses-wrapped/assets/41821819/8c155b75-1367-4434-94bb-0f3095b94a25">

## Features

- **Turkish Case Conversion**: Custom function to accurately match Turkish characters during the categorization process.
- **Automated Categorization**: Expenses are automatically categorized based on a pre-defined list of Turkish keywords.
- **Visualization**: Generates pie charts to visually display the distribution of spending across categories.
- **Excel and CSV Support**: Processes Excel files and outputs categorized expenses into CSV files for easy analysis.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system along with the following Python libraries:
- pandas
- matplotlib
- openpyxl

You can install these libraries using pip:

```bash
pip install pandas matplotlib openpyxl
```

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/expenses-wrapped.git
cd expenses-wrapped
```

### Usage
Place your monthly expense Excel files in the expenses folder. Ensure each file follows the format provided by your bank, with columns for company names, dates, and amounts.
Run the script:
```bash
python expenses_wrapped.py
```

Check the output folders for categorized expense reports and pie charts.

## Next Steps

I will continue categorizing more expenses with ChatGPT to reduce the amount of expenses categorized under 'Other'.


