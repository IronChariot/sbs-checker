# sbs-checker
Sentence by sentence grammar, word and logic checker powered by GPT-3.5.

Even with long contexts (e.g. Claude 2), LLMs can't point out mistakes in large sections of text. Normal word processors can help identify typos and grammar mistakes easily enough, but my most common mistakes are writing one word when I mean another, or forgetting what I'm writing halfway through a sentence and not completing it in a way that makes sense given the beginning of the sentence. Hence, I would benefit from having a decent LLM which can look at my work, sentence by sentence, and identify when I may have made one of these mistakes. Also, a lot of people ignore recommendations made by word processors because they aren't always great, so having something you can quickly paste your work into and it just returns the sentences at fault and what the fault might be, sounds like a better process to have at the end of the writing process than being constantly bombarded with squiggly underlines.

The task here has two parts:
- In the first part, we have to take large-ish chunks of text (maybe split up by carriage returns), and feed them to GPT-3.5, so that it can return a list of the individual sentences.
- Then in the second part, GPT-3.5 is presented with each sentence one at a time without context, and asked to identify the errors mentioned above (along with typos and grammar mistakes, because why not).

The model will be asked to return a standard answer if there were no mistakes, so we can quickly identify when it did find something, and present the user with a list of sentences and associated errors.

An extention of this tool would be for it to take the user through each sentence which had an issue if their own pasted text, and allow keyboard shortcuts to approve or reject a change before moving on to the next issue.
