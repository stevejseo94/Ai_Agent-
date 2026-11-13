import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try: 
        target_dir = os.path.normpath(os.path.join(os.path.abspath(working_directory), directory))
        valid_target_dir = os.path.commonpath([os.path.abspath(working_directory), target_dir]) 

        if valid_target_dir != os.path.abspath(working_directory): 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir): 
            return f'Error: "{directory}" is not a directory'


        file_info = []
        for file in os.listdir(target_dir): 
            name = file
            size = os.path.getsize(os.path.join(target_dir, file))
            isdir = os.path.isdir(os.path.join(target_dir, file))
            file_info.append(
                f" - {name}: file_size={size} bytes, is_dir={isdir}"
                )
        return "\n".join(file_info)
        
    except Exception as e: 
        return f"Error: {e}"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

