# Spam Classifier

This project implements a spam classifier using OpenAI's GPT-4 model. The classifier categorizes email text as either 'spam' or 'not spam' based on the content of the email. The implementation leverages Pydantic for data validation and the `instructor` library for seamless integration with the OpenAI API.

## Features

- Classifies email text into 'spam' or 'not spam'
- Utilizes OpenAI's GPT-4 model for text classification
- Uses Pydantic for data validation
- Leverages the `instructor` library for simplified API interactions

## Prerequisites

- Python 3.7+
- OpenAI API Key
- `.env` file with your OpenAI API Key

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jaxayprajapati/Spam-Classifier-LLM-Instructor.git
    cd spam-classifier
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file with your OpenAI API Key:
    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. **Import necessary modules:** Import required libraries including `enum`, `pydantic`, `openai`, `instructor`, and `dotenv`.

2. **Define Labels Enum and SinglePrediction Model:** Use Pydantic to create a model for the classification labels.

3. **Initialize the OpenAI client:** Use the `instructor` library to initialize the OpenAI client.

4. **Define the classify function:** Create a function that sends the email text to the GPT-4 model and receives the classification.

5. **Test the classifier with sample email texts:** Use sample texts to test and validate the classifier's performance.

## Libraries Used

### Pydantic
Pydantic is used for data validation, providing type checking, validation, and autocomplete features which help catch errors before they happen. Pydantic models are defined using standard Python type hints, making them easy to integrate with existing Python codebases.

### Instructor
The `instructor` library simplifies interactions with the OpenAI API by adding a `response_model` parameter, allowing you to map LLM outputs directly to Pydantic models. This enhances data validation and serialization, making it easier to work with structured outputs from language models.
## Example

To classify an email text, use the `classify` function with the email content as input. This will return a prediction indicating whether the email is 'spam' or 'not spam'.
