import os 
from config import MAX_CHARS 

def get_file_content(working_directory: str, file_path: str) -> str: 
    try: 
        target_file_path = os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))
        valid_file_path = os.path.commonpath([os.path.abspath(working_directory), target_file_path])
    

        if valid_file_path != os.path.abspath(working_directory): 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path): 
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file_path, "r") as f: 
            content = f.read(MAX_CHARS) 
            if f.read(1): 
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]' 
        return content 

    except Exception as e: 
        return f"Error: {e}"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}