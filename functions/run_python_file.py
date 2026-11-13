import os 
import subprocess 

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None
                    ) -> str: 
    try: 
        abs_path = os.path.abspath(working_directory) 
        target_file_path = os.path.normpath(os.path.join(abs_path, file_path))

        if os.path.commonpath([abs_path, target_file_path]) != abs_path: 
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path): 
            return f'Error: "{file_path}" does not exist or is not a regular file' 
        if not target_file_path.endswith(".py"): 
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file_path] 
        if args != None: 
            command.extend(args)
        execute = subprocess.run(command, capture_output=True, text=True, timeout=30)

        output: list[str] = []
        if execute.returncode != 0:
            output.append(f"Process exited with code {execute.returncode}")
        if not execute.stdout and not execute.stderr:
            output.append("No output produced")
        if execute.stdout:
            output.append(f"STDOUT:\n{execute.stdout}")
        if execute.stderr:
            output.append(f"STDERR:\n{execute.stderr}")
        return "\n".join(output)
        #if execute.returncode != 0: 
            #return f"Process exited with code x"
        #if execute.stdout == "" and execute.stderr == "": 
            #return f"No output produced"
        #return f"STDOUT: {execute.stdout} STDERR: {execute.stderr}" 

    except Exception as e: 
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}