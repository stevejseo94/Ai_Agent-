import os 

def write_file(working_directory: str, file_path: str, content: str) -> str: 
    try: 
        abs_path = os.path.abspath(working_directory) 
        target_file_path = os.path.normpath(os.path.join(abs_path, file_path)) 

        if os.path.commonpath([abs_path, target_file_path]) != abs_path: 
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 
        if os.path.isdir(target_file_path): 
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

        with open(target_file_path, "w") as f: 
            f.write(content) 
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 

    except Exception as e: 
        return f"Error as {e}" 
    

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file within the working directory (overwriting if the file exists)",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write to the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
    