import os
import json


import openai

# Set up OpenAI API credentials
openai.api_key = os.getenv('OPENAI_VECTORS_KEY')

def generate_summary(opinions):
    opinions = opinions[175:]
    prompt = "Opinions:\n" + "\n".join(opinions) + "\n\nSummary:"
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    summary = response.choices[0].text.strip()
    return summary

# Example usage
opinions = [
    "I think the movie was too long and had a weak plot.",
    "In my opinion, the restaurant has great food but poor service.",
    "The new policy is a step in the right direction, but it needs some improvements."
]

REPLIES_FPATH = 'har/musk/1-twitter.com.har.replies.json'
with open(REPLIES_FPATH, 'r') as f:
    opinions = json.load(f)

summary = generate_summary(opinions)
print(summary)
