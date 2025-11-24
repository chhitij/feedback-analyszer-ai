import pandas as pd
from crewai.tools import tool
import os

@tool("CSV Reader Tool")
def csv_reader_tool(file_path: str) -> str:
    """
    Reads a CSV file and returns its content as a JSON string.
    Useful for reading feedback data.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        JSON string representation of the CSV data
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_json(orient="records")
    except Exception as e:
        return f"Error reading CSV file: {str(e)}"

@tool("CSV Writer Tool")
def csv_writer_tool(file_path: str, data: str) -> str:
    """
    Writes data to a CSV file. Useful for saving generated tickets.
    
    Args:
        file_path: Path where CSV should be saved
        data: JSON string or list of dictionaries to write
        
    Returns:
        Success message with number of records written
    """
    try:
        import json
        if isinstance(data, str):
            data_list = json.loads(data)
        else:
            data_list = data
        
        df = pd.DataFrame(data_list)
        
        # Append if file exists, else create
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False, index=False)
        else:
            df.to_csv(file_path, index=False)
            
        return f"Successfully wrote {len(df)} records to {file_path}"
    except Exception as e:
        return f"Error writing to CSV file: {str(e)}"