
General-Purpose AI Agent (Beta)

⚠️ WARNING / DISCLAIMER: This software is in BETA. It is provided for demonstration and educational purposes only. It can read, write, and execute arbitrary code/files on your system. Do not use this agent in production environments or on sensitive/untrusted codebases.

Overview

This project is a general-purpose AI agent capable of reasoning, interacting with the local filesystem, executing Python scripts, and performing mathematical calculations via tool-calling capabilities.

Features

• File Operations: Read file contents, inspect file metadata/info, and write or modify files.
• Python Execution: Safely or dynamically run Python scripts as part of its tool loop.
• Calculator Tool: Dedicated calculator function for evaluating mathematical expressions and numeric data.
• General-Purpose Prompting: Flexible conversational and task-solving agent interface.

Architecture & Tools

The agent interacts with an LLM backend using tool declarations:
1. get_file_content(path) — Reads text or code from a specified file path.
2. get_files_info(path) — Retrieves file size, modification date, and metadata.
3. write_files(path, content) — Writes or overwrites content to a target file.
4. run_python_file(file_path) — Executes a Python file and captures its output.
5. calculator(expression) — Evaluates mathematical expressions.

Project Structure

├── main.py                     # Main agent loop 
├── functions                   # File IO, python runner, and tool definitions 
    ├── get_file_content.py
    ├── get_files_info.py 
    ├── run_python_file.py
    ├── write_files.py        
├── calculator                  # calculator tools 
    ├── main.py 
    ├── pkg 
        ├── calculator.py 
└── README.md                   # Project documentation

Quickstart & Installation

1. Clone the repository:
git clone https://github.com
cd Ai-Agent

2. Configure your API keys:
Set your LLM provider API key in your environment:bash
export API_KEY="your-api-key-here"

3. Run the agent:
uv run main.py "input text or call functions" 


**Safety & Security Notice**

Because this agent can execute Python code and write to your local filesystem, running untrusted prompts or inputs can lead to unintended code execution, data loss, or system compromise. Always run this software inside an isolated container or sandbox (such as Docker or a virtual machine).


**Loop Protection:** Execution halts automatically after `MAX_ITERATIONS` steps.
