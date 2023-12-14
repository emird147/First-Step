# Resume Builder with OpenAI Enhancement

## Introduction
This program is designed to help users create compelling resumes by taking their input and using the OpenAI API to enhance the descriptions of their projects and experiences.

## Features
- **User Input for Resume Data**: Allows users to input their personal information, educational background, work experience, and project details.
- **OpenAI API Integration**: Enhances the descriptions of projects and experiences using advanced language models.
- **PDF Generation**: Converts the final resume into a PDF format for easy sharing and printing.
- **GUI for Easy Interaction**: User-friendly graphical interface to input data and view the generated resume.

## Usage
Detail the steps on how to use the program, including running the script and interacting with the GUI.
1. Install the open ai library by running the following command in your terminal.
      ```
   pip install openai
      ```
2. Install the fpdf library by running the following command in your terminal.
   ```
   pip install fpdf
   ```
4. Open main.py and run the program.
5. A GUI (graphical user interface) will pop up and you can fill out your information in the corresponding entries.
6. Once you've completed the form, press the submit button to download your resume in a PDF form.
7. Check your downloaded resume to make sure all the information is formatted correctly.
8. If it needs any editing, you can just change the information on the GUI and press the submit button again. Otherwise, you can close the GUI window yourself. 

# Example usage steps
python main.py
\```

## Files and Modules
- `main.py`: The main script that launches the program.
- `gui.py`: Contains the graphical user interface logic.
- `utils.py`: Utility functions used across the program.
- `pdf.py`: Module for generating the resume PDF.

