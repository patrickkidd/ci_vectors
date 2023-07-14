import os

import openai
from transformers import pipeline

openai.organization = "org-FrKbOlF1ZnYpO8Phqcidlcdy"
openai.api_key = os.getenv("OPENAI_VECTORS_KEY")
openai.Model.list()

def encode_opinions(opinions):
    encoded_opinions = []
    intensity_scores = []
    sentiment_analyzer = pipeline("sentiment-analysis")
    
    for opinion in opinions:
        response = openai.Completion.create(
            # model="gpt-3.5-turbo",
            engine="text-davinci-003",
            prompt=opinion,
            max_tokens=0,
            logprobs=1,
            echo=True,
            # log_level="silent"
        )
        encoded_opinion = response.choices[0].logprobs.token_ids
        encoded_opinions.append(encoded_opinion)
        
        sentiment = sentiment_analyzer(opinion)[0]
        intensity = sentiment["score"]
        intensity_scores.append(intensity)
    
    return encoded_opinions, intensity_scores

def average_opinions(opinions):
    opinion_vectors, intensity_scores = encode_opinions(opinions)
    weighted_opinions = [
        [intensity * vector for vector in encoded_opinion]
        for intensity, encoded_opinion in zip(intensity_scores, opinion_vectors)
    ]
    average_vector = [
        sum(values) / len(values)
        for values in zip(*weighted_opinions)
    ]
    
    return average_vector


def one():
    # Example usage
    opinions = [
        "I think the movie was fantastic!",
        "In my opinion, the movie was average.",
        "The movie was terrible, I didn't like it at all."
    ]

    average_vector = average_opinions(opinions)
    print(average_vector)

def two():
    def generate_average_opinion(sentiment_score):
        prompt = f"On a scale of 1 to 5, the average sentiment score for the movie is {sentiment_score:.2f}."
        
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
            # log_level="silent"
        )
        
        generated_opinion = response.choices[0].text.strip()
        
        return generated_opinion

    # Example usage
    average_sentiment_score = 3.8

    average_opinion = generate_average_opinion(average_sentiment_score)
    print("The average opinion is:", average_opinion)    

two()
