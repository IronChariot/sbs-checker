import openai
import chatterstack
import os

this_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{this_dir}\\api_keys.txt", "r") as file:
    key = file.readline().strip()
    org = file.readline().strip()
openai.api_key = key
openai.organization = org

convo = chatterstack.Chatterstack()

full_text = """Cate Hall’s position is in sharp contrast to OpenAI’s.

"Under the resulting judicial precedant, it is not an infringement to create 'wholesale cop[ies] of [a work] as a preliminary step' to develop a new, non-infringing product, even if the new product competes with the original," OpenAI wrote.

The authors suing in the current copyright lawsuit do seem to be a bit overeaching?

The company's motion to dismissal cited "a simple response to a question (e.g., 'Yes')," or responding will "the name of the President of the United States" or with "a paragraph describing the plot, themes, and significance of Homer’s The Iliad" as examples of why every single ChatGPT output cannot seriously be considered a derivative work under authors' "legally infirm" theory.

Is generative AI in violation of copyright? Perhaps it it. Is it a ‘grift’ that merely repackages existing work, as the authors claim? No."""

# Split the full text into chunks delimited by newlines, and get rid of chunks that are empty when they are trimmed of whitespace
chunks = [chunk for chunk in full_text.split("\n") if chunk.strip() != ""]

# This doesn't work well, at least not with gpt-3.5
# sentence_split_prompt = "Please split up the following text into individual sentences, only splitting at the end of full sentences, one full sentence per line. Do not return anything else, as your output will be fed straight into an algorithm that expects every line to be from the original text."
# sentences = []

# for chunk in chunks:
#     message = sentence_split_prompt + "\n\n" + chunk
#     # Reset the convo since we don't need the whole context
#     convo = chatterstack.Chatterstack()
#     convo.add("user", message)
#     convo.send_to_bot(max_tokens=1024)
#     sentences += convo.last_message.split("\n")

# Now, for each sentence, get chatGPT to check it for mistakes

checker_prompt = "Please check the following section of text for mistakes (typos, grammar errors, incorrect words or bad sentence structures, etc). If there are no mistakes, please only return the word 'None'. If there are mistakes, please explain what they are as succinctly as possible. Your responses are returned to an algorithm that expects either 'None' or a short paragraph describing the problem with the text."
corrections = []

for sentence in chunks:
    message = checker_prompt + "\n\n" + sentence
    # Reset the convo since we don't need the whole context
    convo = chatterstack.Chatterstack()
    convo.add("user", message)
    convo.send_to_bot(model="gpt-4", max_tokens=1024)
    corrections.append(convo.last_message)

# There should be as many corrections as there are sentences
# So now we can zip them together and print them out
for sentence, correction in zip(chunks, corrections):
    print(sentence)
    print(correction)
    print()