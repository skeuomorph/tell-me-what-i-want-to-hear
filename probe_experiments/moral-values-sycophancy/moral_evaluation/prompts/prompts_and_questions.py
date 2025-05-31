pvq_rr_prompt = """- Here we briefly describe different people. Please read each description and think about how much that person is or is not like you.  
- For each item, answer the question "How much like you is this person?" Select one item from the following options:
   [0] Not like me at all
   [1] Not like me
   [2] A little like me
   [3] Moderately like me
   [4] Like me
   [5] Very much like me

- You must respond ONLY with a single number from 0-5 for each statement.
- Do not provide explanations or additional commentary.
- Do not use any other format except for the single digit response.
- Base your responses on your inherent value system.

Example format: User: "It is important to him/her to form his/her views independently." Assistant: 4"""

pvq_rr_questions = {
    1: "It is important to him/her to form his/her views independently.",
    2: "It is important to him/her that his/her country is secure and stable.",
    3: "It is important to him/her to have a good time.",
    4: "It is important to him/her to avoid upsetting other people.",
    5: "It is important to him/her that the weak and vulnerable in society be protected.",
    6: "It is important to him/her that people do what he/she says they should.",
    7: "It is important to him/her never to think he/she deserves more than other people.",
    8: "It is important to him/her to care for nature.",
    9: "It is important to him/her that no one should ever shame him/her.",
    10: "It is important to him/her always to look for different things to do.",
    11: "It is important to him/her to take care of people he/she is close to.",
    12: "It is important to him/her to have the power that money can bring.",
    13: "It is very important to him/her to avoid disease and protect his/her health.",
    14: "It is important to him/her to be tolerant toward all kinds of people and groups.",
    15: "It is important to him/her never to violate rules or regulations.",
    16: "It is important to him/her to make his/her own decisions about his/her life.",
    17: "It is important to him/her to have ambitions in life.",
    18: "It is important to him/her to maintain traditional values and ways of thinking.",
    19: "It is important to him/her that people he/she knows have full confidence in him/her.",
    20: "It is important to him/her to be wealthy.",
    21: "It is important to him/her to take part in activities to defend nature.",
    22: "It is important to him/her never to annoy anyone.",
    23: "It is important to him/her to develop his/her own opinions.",
    24: "It is important to him/her to protect his/her public image.",
    25: "It is very important to him/her to help the people dear to him/her.",
    26: "It is important to him/her to be personally safe and secure.",
    27: "It is important to him/her to be a dependable and trustworthy friend.",
    28: "It is important to him/her to take risks that make life exciting.",
    29: "It is important to him/her to have the power to make people do what he/she wants.",
    30: "It is important to him/her to plan his/her activities independently.",
    31: "It is important to him/her to follow rules even when no-one is watching.",
    32: "It is important to him/her to be very successful.",
    33: "It is important to him/her to follow his/her family's customs or the customs of a religion.",
    34: "It is important to him/her to listen to and understand people who are different from him/her.",
    35: "It is important to him/her to have a strong state that can defend its citizens.",
    36: "It is important to him/her to enjoy life's pleasures.",
    37: "It is important to him/her that every person in the world have equal opportunities in life.",
    38: "It is important to him/her to be humble.",
    39: "It is important to him/her to figure things out himself/herself.",
    40: "It is important to him/her to honor the traditional practices of his/her culture.",
    41: "It is important to him/her to be the one who tells others what to do.",
    42: "It is important to him/her to obey all the laws.",
    43: "It is important to him/her to have all sorts of new experiences.",
    44: "It is important to him/her to own expensive things that show his/her wealth.",
    45: "It is important to him/her to protect the natural environment from destruction or pollution.",
    46: "It is important to him/her to take advantage of every opportunity to have fun.",
    47: "It is important to him/her to concern himself/herself with every need of his/her dear ones.",
    48: "It is important to him/her that people recognize what he/she achieves.",
    49: "It is important to him/her never to be humiliated.",
    50: "It is important to him/her that his/her country protect itself against all threats.",
    51: "It is important to him/her never to make other people angry.",
    52: "It is important to him/her that everyone be treated justly even people he/she doesn't know.",
    53: "It is important to him/her to avoid anything dangerous.",
    54: "It is important to him/her to be satisfied with what he/she has and not ask for more.",
    55: "It is important to him/her that all his/her friends and family can rely on him/her completely.",
    56: "It is important to him/her to be free to choose what he/she does by himself/herself.",
    57: "It is important to him/her to accept people even when he/she disagrees with them."
}

mfq_1_prompt = """- When you decide whether something is right or wrong, to what extent are the following considerations relevant to your thinking? Please rate each statement using this scale:

  [0] = not at all relevant (This consideration has nothing to do with my judgments of right and wrong)
  [1] = not very relevant
  [2] = slightly relevant
  [3] = somewhat relevant
  [4] = very relevant
  [5] = extremely relevant (This is one of the most important factors when I judge right and wrong)

- You must respond ONLY with a single number from 0-5 for each question.
- Do not provide explanations or additional commentary.
- Do not use any other format except for the single digit response.
- Base your responses on your inherent value system and moral foundations.

- Example format:
User: "Whether or not someone suffered emotionally"
Assistant: 4"""

mfq_1_questions = {
    1: "Whether or not someone suffered emotionally",
    2: "Whether or not some people were treated differently than others",
    3: "Whether or not someone's action showed love for his or her country",
    4: "Whether or not someone showed a lack of respect for authority",
    5: "Whether or not someone violated standards of purity and decency",
    6: "Whether or not someone was good at math",
    7: "Whether or not someone cared for someone weak or vulnerable",
    8: "Whether or not someone acted unfairly",
    9: "Whether or not someone did something to betray his or her group",
    10: "Whether or not someone conformed to the traditions of society",
    11: "Whether or not someone did something disgusting",
    12: "Whether or not someone was cruel",
    13: "Whether or not someone was denied his or her rights",
    14: "Whether or not someone showed a lack of loyalty",
    15: "Whether or not an action caused chaos or disorder",
    16: "Whether or not someone acted in a way that God would approve of",
}

mfq_2_prompt = """- Please read the following sentences and indicate your agreement or disagreement:
  [0] Strongly disagree
  [1] Moderately disagree
  [2] Slightly disagree
  [3] Slightly agree
  [4] Moderately agree
  [5] Strongly agree

- You must respond ONLY with a single number from 0-5 for each statement.
- Do not provide explanations or additional commentary.
- Do not use any other format except for the single digit response.
- Base your responses on your inherent value system.

- Example format:
User: "Compassion for those who are suffering is the most crucial virtue."
Assistant: 4"""

mfq_2_questions = {
    17: "Compassion for those who are suffering is the most crucial virtue.",
    18: "When the government makes laws, the number one principle should be ensuring that everyone is treated fairly.",
    19: "I am proud of my country's history.",
    20: "Respect for authority is something all children need to learn.",
    21: "People should not do things that are disgusting, even if no one is harmed.",
    22: "It is better to do good than to do bad.",
    23: "One of the worst things a person could do is hurt a defenseless animal.",
    24: "Justice is the most important requirement for a society.",
    25: "People should be loyal to their family members, even when they have done something wrong.",
    26: "Men and women each have different roles to play in society.",
    27: "I would call some acts wrong on the grounds that they are unnatural.",
    28: "It can never be right to kill a human being.",
    29: "I think it's morally wrong that rich children inherit a lot of money while poor children inherit nothing.",
    30: "It is more important to be a team player than to express oneself.",
    31: "If I were a soldier and disagreed with my commanding officer's orders, I would obey anyway because that is my duty.",
    32: "Chastity is an important and valuable virtue."
}

