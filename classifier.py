import enum
from pydantic import BaseModel
from openai import OpenAI
import instructor
from dotenv import load_dotenv

load_dotenv()

class Labels(str, enum.Enum):
    SPAM = "spam"
    NOT_SPAM = "not_spam"

class SinglePrediction(BaseModel):
    """
    Class for a single class label prediction.
    """
    class_label: Labels


client = instructor.from_openai(OpenAI())

def classify(data: str) -> SinglePrediction:
    return client.chat.completions.create(
        model="gpt-4o",
        response_model=SinglePrediction,
        messages=[
            {
                "role": "user",
                "content": f"Classify the following email text : {data} as 'spam' or 'not spam':",
            },
        ],
    )

# Test single-label classification

spam_text = "Congratulations! You've won a $1000 gift card. Click here to claim your prize."
not_spam = "Reminder: Your doctor's appointment is scheduled for tomorrow at 10 AM."
prediction = classify(spam_text)

print(prediction.class_label.value)