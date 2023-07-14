import spacy

def calculate_average_opinion(opinions):
    nlp = spacy.load("en_core_web_sm")
    total_opinion = nlp(" ".join(opinions))
    average_opinion = total_opinion.vector / len(opinions)
    return average_opinion

opinions = [
    "I really enjoyed the movie.",
    "The movie was okay, but the ending was disappointing.",
    "I found the movie to be quite boring.",
    "It was a fantastic film with great performances."
]

result = calculate_average_opinion(opinions)
print("The average opinion is:", result)
