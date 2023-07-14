# ci_vectors :: Collective Intelligence Vectors

This is an experiment in deriving collective opinions from a list of diverse
opinions on a topic. The motivation is a key theoretical principle in the
quantitative field of Collective Intelligence, that the average of a set of
diverse viewpoints on a single topic is often more accurate to reality than a
single expert. A goal here is to take a list of english-language opinions, in
this case from a single Twitter thread, and produce some aggregated summary of
the opinions from it.

See "Theoretical Background" for more.

I don't have any experience in Language Models or machine learning, and am not
that great with data science in general. I do have a doctorate in Psychology and
advanced training in Bowen Theory, which guides some of the novel propositions
to augment findings from the field of Collective Behavior.

## Experiment 1: Twitter thread replies

A script was written to scrape twitter thread replies from a safari dev tools
network tab HAR (JSON) export of all requests. Reply text are written to a json
file. This is the raw inputs for this project. A little over 200 replies can be
produced after manually scrolling to the bottom of a twitter thread to load them
all asynchronously. Twitter appears to cap the results provided in the web
interface.

The idea is that the thread's original tweet is the "topic." All replies in that
thread are assumed to be "votes" on that topic. A goal is to start with tweets
from public figures that generate many thousands of polarized replies for every
tweet, like @jordanbpeterson or @elonmusk.

_Opinion Summary_

`test_summary.py` uses the ChatGPT API to produce an
english-language summary of all of the opinions. This requires the number of
opinions to be capped at about 175.

ChatGPT thread: https://chat.openai.com/share/78b0cde6-6374-4ef3-bb52-20f860ee8e0f

_Factor Analysis_

`test_factors.py` uses `sklearn` and `nltk` to generate a
factor analysis of terms. This script has not been tested yet. The idea here is
that instead of a single "average" of the opinons, that opions might cluster
together with different weights. That information might be useful for a person
to aggregate the factors subjectively in their head to draw a single conclusion.

ChatGPT Thread: https://chat.openai.com/share/7e9ba27d-6138-4d11-a6ee-100e2c10d3a3

_Other Ideas_: 

Here are some other attempts at getting starting points from ChatGPT:

- Emotion Vectors 1: https://chat.openai.com/share/99691cdb-9d83-4a8b-b2d5-7910a6d70f42
- Emotion Vectors 2: https://chat.openai.com/share/009f720d-2da4-4fe2-90fc-cea21cb9986d
- Straight CI: https://chat.openai.com/share/f7564a4f-e287-4518-80e2-372bd0910fdc


## Theoretical Background

A current goal of Twitter is to become the "least untrue" source of information
available. The key assumption is that if individuals are allowed to express
their opinions as freely as possible on a given topic, then it will be the best
for society's ability to make sense of that topic. It turns out that there is a
technical argument for this assumption in Collective Intelligence, which
suggests that biological systems have evolved instinctual mechanisms for making
group decisions that are far superior to a decision that any one individual
could make. These intelligience mechanisms work through local interactions
between relatively uninformed individuals that aggregate into a single and far
more sophisticated decision making system.

This principle applies to baboons making pathfinding decisions, bees making
decisions on where to move a nest, schools of fish avoiding a predator in a
manner that minimizes individual losses, and others. In the case of humans, this
pertains to the automatic verbal and non-verbal cues that occur when multiple
stakeholders engage with each other on problem. This instinctual dialog, or
*dialogos* in Latin, can hypothetically occur in debates, arguments, even wars.

A new hypothetical idea is that automatic emotional responses in humans during
dialog represent "votes" on the problem. The votes are automatically tallied
through the actual behavioral outcome of the dialog. All of this is so automatic
that we are not used to observing it while it happens.

For example, consider that persons A, B, and C are trying to figure out where
hold an office Christmas party. The dialog might look like this:

- Person A: "Let's have it at the roller rink!"
- Person B: "That place is too small."
- Person A: "But they have the best activity that everyone can do."
- Person C: "But their food is terrible."
- Person B: "How about just having it at the office?"
- Person C: "I guess that could work!" (with great positivity)
- Person A: "Hmmm, Let me think about it."
- Person B: "It would be free, and everyone knows how to get there."
- Person C: "Yeah, com on Person A, let's do it there."
- Person A: "Well, I'm not totally on board but it's two against one."
- Person B: "OK, sorry but I think it makes the most sense."
- The Christmas Party ended up at the office.

In this sequence each interaction is a vote that biases the final decision in a
particular direction. For example, "Let's have it at the roller rink!" is a
clear vote for the roller rink. "That place is too small" is clear vote against
the first vote. There are more votes that push the group's bias toward or away
the roller rink. Then a new vote for the office comes, a few more votes for and
against the office, and one with great positivity that carries a bit more weight
than the others.

Finally, the actual behavioral outcome is to have the party at the office. The
actual behavioral outcome is important because it may not always be the outcome
that was explicitly agreed upon. The main idea of CI is that the mechanism for
collective intelligence has *evolved*, which means it is instinctual/automatic,
which means that it may not be the same as what people say they will do. People
do not always do what they say they will do and *instinctual* behavior can only
be inferred through actual behavior.

Similarly, the decision was not unanimous. This is important. Agreement is not
required, and it is epected that there will be some votes that are not in line
with an explicit group decision or actual behavioral outcome. This is because
the CI process is not about *fairness*, it is about getting as close to reality
as possible. The key CI principle is that each individual provides a vote or
votes that merely biases the decions in one direction or another. The "votes"
are then tallied and then the group decision is enforced through actual
behavior.

Anecdotal evidence for this process existing at all is that each step in a
dialog series has an impact on each individual's model of the problem. People
are heavily influenced by the process of deliberation in a group. Exactly *how*
this occurs is unknown and likely very complex.

However, evidence *that* it occurs can be obtained in a single experiement. Ask
each person in an experimental group for their opinion on a topic separately
prior to being told they will participate in a group deliberation on that topic.
Then hold the group deliberation, recording each statement a person makes to the
others about the topic. The prediction is that at least some of the people will
demonstrate that their opinions have changed while the deliberation is occuring,
either verbally or non-verbally. This only occurs after seeing or hearing the
responses from others.

Most people do not really own their opinons, as demonstrated in this kind of
experiment, and more formally in this experiment where the evolution of
individual opinions through group context was demonstrated:
https://www.youtube.com/watch?v=O_m8IZzl48E&feature=youtu.be. Confederates could
flip an individual opinion on a topic merely by flipping their own. The
proposition here is that individual's opinions on a problem exist and operate
primarily in conjunction with the group of affiliated stakeholders on that
problem, and that the end result is something like an average of the individual
opinions.

A hypothesis is that this applies even when groups are highly polarized on a
topic. In fact, the proposition is that the poles *function* to balance each
other out in this instinctual CI process. In other words, in an argument the
"truth is somehwere in the middle." Providing a method for producing an opinion
"somewhere in the middle" from a list of diverse opinions would benefit
collective decision making, especially on difficult topics.