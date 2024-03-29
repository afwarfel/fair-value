# Fair Value Repository

This repository contains supporting code for data analysis on the [Fair Value newsletter](https://www.alexwarfel.com/). It is maintained by Alex Warfel, who can be reached at alexwarfel@gmail.com.

## Python Version

This repository uses Python 3.9.10. Ensure your Python version is correct by typing `python --version` in your terminal. If you don't have the correct version, you can download it from the [Python official website](https://www.python.org/downloads/).

## Setting Up the Project

### Cloning the Repository

To work with this project on your local machine, you'll need to clone the repository. Here are the steps:

1. **Install Git**: Git is a version control system that lets you manage and keep track of your source code history. If you don't have Git installed on your machine, you can download it from the [Git official website](https://git-scm.com/downloads).

2. **Open Terminal**: Open a terminal window. On Windows, you can use Command Prompt or PowerShell. On MacOS/Linux, you can use Terminal.

3. **Navigate to the Desired Directory**: Use the `cd` command to navigate to the directory where you want to clone the repository. For example, if you want to clone the repository to a directory named "projects", you would use the following command:

   ```bash
   cd path/to/projects
   ```

4. **Clone the Repository**: Now, you can clone the repository by running the following command:

   ```bash
   git clone https://github.com/username/repository.git
   ```

   Replace "username" with the username of the repository owner and "repository" with the name of the repository. This command creates a new directory in your current directory where the repository files are cloned.

5. **Navigate to the Repository Directory**: Use the `cd` command to navigate to the newly created repository directory:

   ```bash
   cd repository
   ```

   Replace "repository" with the name of the repository.

Now, you have a local copy of the project that you can open with your favorite IDE or text editor.

This project requires a Python virtual environment for managing dependencies. Here are the steps to set it up:

1. **Create a Virtual Environment**: A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages. To create a virtual environment, open your terminal and navigate to the project directory. Then, run the following command:

   ```bash
   python -m venv env
   ```

   This command creates a virtual environment named `env` in your project directory.

2. **Activate the Virtual Environment**: Before you can start installing or using packages in the virtual environment, you’ll need to activate it. Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running `python` will get you that particular version and installation of Python. Here's how to activate the virtual environment:

   On Windows:

   ```bash
   env\Scripts\activate
   ```

   On MacOS/Linux:

   ```bash
   source env/bin/activate
   ```

   After running this command, you should see `(env)` next to your terminal prompt, indicating that you are now working inside the `env` virtual environment.

3. **Check if pip is Installed**: `pip` is a package manager for Python and is used to install and manage software packages. To check if `pip` is installed, run the following command:

   ```bash
   pip --version
   ```

   If `pip` is installed, this command will display the version of `pip` installed. If `pip` is not installed, you will need to [install pip](https://pip.pypa.io/en/stable/installation/) before proceeding.

4. **Install Required Packages**: Once `pip` is installed and you have your virtual environment activated, you can install the required packages. The `requirements.txt` file contains a list of items to be installed using `pip install`. Run the following command to install these packages:

   ```bash
   pip install -r requirements.txt
   ```

5. **Verify Installation**: After installation, you can confirm that the correct packages were installed with `pip freeze`. This command will print the packages installed in the current environment in the console. These should match the packages listed in the `requirements.txt` file.

   ```bash
   pip freeze
   ```

## Repository Structure

The repository is structured in the following way:

- Notebooks: Contain the analysis.
- Utils directory: Contains functions that support the notebooks.

Please note that pathing is relatively complicated in this repository. The notebooks utilize these functions that need to have pathways from the perspective of the notebooks. Some try/except blocks have been added to help with this. Please read up and understand how pathing works deeply when running into issues.

## Contributing

If you notice an error, please submit a pull request to correct it. If there are best practices that you notice I am not following, please reach out and let me know.

## Newsletter

The goal of this repository is to share my code with more people in order to find errors, correct analysis, and share strategies for extracting data with others. If this type of analysis is interesting to you, please consider subscribing to the [Fair Value newsletter](https://www.alexwarfel.com/).

## API Keys

This project requires API keys from the following services:

- [FRED](https://fred.stlouisfed.org/docs/api/api_key.html)
- [AlphaVantage](https://www.alphavantage.co/)

To add these API keys to the project:

1. Obtain the API keys from the above services. They are free to use.

2. Open the `.env.example` file in the project root directory.

3. Replace the placeholder values with your actual API keys.

4. Save the file, and then rename it from `.env.example` to `.env`.

The `.env` file is used to store environment variables, which include API keys. It can be accessed throughout your project. This file is listed in the `.gitignore` file, which means it will not be tracked by Git. This helps to keep your API keys secure.
