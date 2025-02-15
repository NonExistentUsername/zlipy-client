# zlipy CLI Project

## Introduction
Developers often find themselves trapped in a cycle of researching code, rewriting sections, fixing bugs, and checking for best practices. These tasks, while essential to keeping a product running smoothly, can be time-consuming. Frequent code reviews, constant documentation checks, and ongoing maintenance efforts demand a lot of attention, leaving less room for creativity or strategic thinking.

When so much energy is spent on small technical details, it becomes difficult for developers to get distracted and focus on the main vision of the project: delivering valuable features that meet real business needs. This imbalance slows down progress on the very elements that make a product unique. Imagine if some of these routine coding operations could be automated, allowing developers to focus on innovation and the true goals of the project.

Zlipy is an AI-powered automation assistant designed to simplify routine coding tasks so developers can focus on what really matters - building an outstanding product. By taking care of repetitive work like creating template code, answering technical requests, and helping to configure features, Zlipy frees teams from the time-consuming routine of daily maintenance. Instead of fixing bugs and rewriting code, developers can focus on the bigger picture: building the user experience, improving the core functionality of the product, and creating real business value. With Zlipy taking care of the nuts and bolts, you can devote more energy to innovation and strategic growth.

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


## Examples

Q: `Provide list of api endpoints`

A:
```markdown
Here is the list of API endpoints defined in the project:

### User API Endpoints
- **POST /api/user** - Register a new user
- **POST /api/user/login** -
Log in a user
- **POST /api/user/logout** - Log out a user (requires authentication)
- **POST /api/user/verify-email** - Verify user email
- **POST /api/user/refresh-token** -
Refresh user authentication token
- **POST /api/user/forgot-password** - Initiate a password reset (requires authentication)
- **POST /api/user/send-verification-code** - Send a
verification code to the user

### Edit User Endpoints
- **POST /api/user/change-password** - Change user password (requires authentication)
- **PUT /api/user** - Edit user
details (requires authentication, allows image upload)
- **GET /api/user** - Get user details (requires authentication)
- **DELETE /api/user** - Delete user account (requires
authentication)

These endpoints are part of the user management functionality in the API. If you need additional details or endpoints related to other functionalities, please let me know!
```

Q: `Can you provide list of environment variables that need to be set?`

A:
```markdown
The following environment variables need to be set for the project to function properly:

1. **DB_URI**: The database connection string.
2. **PORT**: The
port on which the application will run (defaults to 3000 if not set).
3. **JWT_SECRET_KEY**: The secret key used for signing JWT tokens.
4. **REFRESH_TOKEN_SECRET_KEY**: The secret
key used for signing refresh tokens.
5. **AWS_ACCESS_KEY_ID**: Your AWS Access Key ID for accessing AWS services.
6. **AWS_SECRET_ACCESS_KEY**: Your AWS Secret Access Key for
accessing AWS services.
7. **AWS_REGION**: The AWS region where your resources are located.
8. **BUCKET_NAME**: The name of the S3 bucket used for file storage.

Make sure to setthese environment variables in your local environment or in your deployment configuration to ensure the application runs smoothly.
```

Q: `I'm going to run this project locally, but I need a database for it and also write the env variables to the .env file. Can you provide a compose.yml file that starts the database and provide a finished .env file that I can use to run this project with all the variables I need?`
A:
```markdown
Here is the `docker-compose.yml` file and the `.env` file you can use to run the project
locally:

**docker-compose.yml**:
version: '3.8'

services:
  mongodb:
    image: mongo:latest
    container_name: mongodb

ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:

**.env**:
# Server
Configuration
PORT=3000

# Database Configuration
DB_URI=mongodb://mongodb:27017/your_database_name

# JWT
Configuration
JWT_SECRET_KEY=your_jwt_secret_key
REFRESH_TOKEN_SECRET_KEY=your_refresh_token_secret_key

# AWS Configuration (if applicable)
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_REGION=your_aws_region
BUCKET_NAME=your
_bucket_name

**Instructions**:
1. Place the `docker-compose.yml` file in the root directory of your project.
2. Replace
`your_database_name`, `your_jwt_secret_key`, `your_refresh_token_secret_key`, `your_aws_access_key_id`, `your_aws_secret_access_key`,
`your_aws_region`, and `your_bucket_name` with your actual values.
3. Create a `.env` file in the root directory of your project with the provided
content.
4. Run `docker-compose up` in your terminal to start the MongoDB service.

This setup will allow you to run the project locally with the
necessary database and environment variables. If you have any further questions or need additional assistance, feel free to ask!
```


## Nuances of Usage
- **Troubleshooting**: If the chat fails to start, ensure that your configuration file is correctly set up and that you have an active internet connection. Check for error messages that may indicate what went wrong.

## Additional Resources
For further assistance, consider the following resources:
- [GitHub Repository](https://github.com/NonExistentUsername/zlipy-client/)
- [Issue Tracker](https://github.com/NonExistentUsername/zlipy-client/issues) for reporting bugs
- Links to relevant community forums or chat groups
