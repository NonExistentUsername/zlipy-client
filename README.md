# zlipy CLI Project

## Introduction
`zlipy` is your AI-powered chat assistant designed to simplify deep project investigations and streamline coding tasks. Whether you're a developer debugging code, a researcher exploring
complex systems, or a student learning to program, `zlipy` helps you find solutions quickly. With its ability to understand your queries and provide tailored code snippets, `zlipy` makes
tackling challenging projects easier than ever. For example, you can ask `zlipy` to help debug a specific piece of code or generate a function based on your requirements. Dive in and
discover how `zlipy` can enhance your coding experience today!

## Installation
To get started, you need to install the `zlipy` package. You can do this using pip:

```bash
pip install zlipy
```

After installation, verify that it was successful by checking the version:

```bash
zlipy --version
```

### Prerequisites
Ensure you have Python 3.11 or higher installed, as well as any necessary dependencies that might be required by the package.

## Getting Started

### Step 1: Initialize Configuration
Before using the CLI, you need to initialize the configuration file. This can be done by running the following command:

```bash
zlipy init
```

This command creates a `zlipy.ini` file in the current directory. The configuration file may include various keys that dictate settings for your chat experience, such as API keys, user
preferences, etc. Review and customize this file according to your needs.

### Step 2: Start a Chat
Once the configuration is initialized, you can start a chat by running:

```bash
zlipy chat
```
or
```bash
zlipy
```

This command initiates the chat interface. Users can expect to interact with the chat service directly through the command line. Currently, there are no additional flags or options for
this command, but future updates may introduce more functionality.

## API Key Retrieval

To use the API, you will need an API key. The API key is required to authenticate your requests and ensure secure access to the services provided by our API.

### Steps to Retrieve Your API Key:

1. Visit (https://dev.zlipy.space).
2. Sign up for an account if you don’t have one.
3. Log in and navigate to the API keys section.
4. Generate and retrieve your API key.

### Security Best Practices:

- For best practices, avoid hardcoding your API key in your source code. Instead, consider using environment variables or a secrets management tool to keep your API key
secure.
- Do not share your API key publicly or expose it in client-side code.

## Command options

The chat command supports additional options to tailor the behavior of the application. Two key options are:

-dmf (--disable-markdown-formatting)
- Description: When this flag is set, the application disables the markdown formatting in the console output.
- Usage: Use this option if you prefer plain text output without markdown styles, which can be useful if you encounter formatting issues in certain terminals or if you simply prefer unformatted text.

-dd (--deep-dive)
- Description: This flag enables Deep Dive Mode, an advanced analysis mode that provides more in-depth processing.
- Usage: Enable this option when you need a more thorough investigation or analysis from the chat command. Deep Dive Mode activates additional debugging and analysis routines, which might provide extended information useful for advanced users or developers.
- WARNING: This feature is experimental and may not be fully supported in all scenarios or lead to errors in certain cases. Use with caution.

## Configuration File

The configuration file, `zlipy.ini`, is a key component of the CLI that stores user settings and preferences. This file is created during the initialization process and can be customized.

The ignored_patterns feature allows to provide a customizable list of patterns that define which files or directories should be excluded from processing. These patterns are similar to those used in .gitignore files, supporting wildcards (e.g., "*.log" to ignore all log files) as well as negation rules (using a "!" prefix to specify exceptions).

Example of a configuration file with ignored patterns:

```ini
[settings]
# Your API key for accessing the zlipy API.
api_key = YOUR_API_KEY

# Comma-separated list of patterns to define ignored files and directories.
# Patterns follow .gitignore-like syntax.
ignored_patterns = .git/, node_modules/, *.log, *.tmp, temp/*, !important.log, docs/**, images/*.png, !images/keep.png, temp/**/tempfile.tmp
```

## Nuances of Usage
- **Troubleshooting**: If the chat fails to start, ensure that your configuration file is correctly set up and that you have an active internet connection. Check for error messages that
may indicate what went wrong.
- **Asynchronous Programming**: The CLI uses asynchronous programming with asyncio, which allows for efficient handling of multiple operations. Users unfamiliar with asyncio should be
aware that this may affect how commands are executed.

## Examples and Scenarios
A typical use case for `zlipy` might involve a user initializing their configuration and then engaging in a support chat. For example, after running `zlipy init`, a user might execute
`zlipy chat` to begin a conversation with a support agent.

## Additional Resources
For further assistance, consider the following resources:
- [GitHub Repository](https://github.com/NonExistentUsername/zlipy-client/)
- [Issue Tracker](https://github.com/NonExistentUsername/zlipy-client/issues) for reporting bugs
- Links to relevant community forums or chat groups
