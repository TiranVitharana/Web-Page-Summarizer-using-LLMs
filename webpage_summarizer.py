import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

# Load environment variables in a file called .env
load_dotenv(override=True)
api_key = os.getenv('GOOGLE_API_KEY')

# Check whether your API calls are working
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)

# Test API connection
response = gemini.chat.completions.create(
    model="gemini-2.5-flash-preview-05-20", 
    messages=[{"role":"user", "content": "what is the most beatiful word in the world?"}]
)
print(response.choices[0].message.content)

# We will create a class to represent a Webpage

# Some websites need you to use proper headers when fetching them:
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Website:
    def __init__(self, url):
        """
        Create this Website object from the given url using the BeautifulSoup library
        """
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

# Let's try one out. Change the website and add print statements to follow along.
cnn = Website("https://cnn.com")
print(cnn.title)
print(cnn.text)

# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."
system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown."

# A function that writes a User Prompt that asks for summaries of websites:
def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

# See how this function creates exactly the format above
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

# And now: call the OpenAI API. We implement a function for summarizing the webpage.
def summarize(url):
    website = Website(url)
    response = gemini.chat.completions.create(
        model = "gemini-2.5-flash-preview-05-20",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

# call the function with a website and see the wonder!
summary = summarize("https://cnn.com")
print(summary)

# A function to display this nicely in the Jupyter output, using markdown
def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))

# Example usage
if __name__ == "__main__":
    display_summary("https://cnn.com")