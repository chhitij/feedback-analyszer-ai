from crewai_tools import tool
import pandas as pd
import os

@tool("CSV Reader Tool")
def csv_reader_tool(file_path: str) -> str:
    """
    Reads a CSV file and returns its contents as a formatted string.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        Formatted string containing CSV data
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            return f"Error: File not found at {file_path}"
        
        # Read CSV
        df = pd.read_csv(file_path)
        
        # Format output
        result = f"CSV File: {file_path}\n"
        result += f"Rows: {len(df)}, Columns: {len(df.columns)}\n"
        result += f"Columns: {', '.join(df.columns.tolist())}\n\n"
        result += "Sample Data (first 5 rows):\n"
        result += df.head().to_string(index=False)
        
        return result
    except Exception as e:
        return f"Error reading CSV: {str(e)}"