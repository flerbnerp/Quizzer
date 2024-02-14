# Planned changes:
## add in config options
First option to tell quizzer, how many of each type of question to present in each quiz

## Scoring methodology
- get filename.md
- add scoring metrics
- add above to json file for permanent storage (JSON exists now)
- Scan will check whether filename.md in config.json (Just in case) 
- already exists in the scoreboard.json. If not, add in new json object to represent the file:
- every question object will contain the yaml properties, subject, related, question_text, answer_text, 
#### Scores should never be overwritten, but json objects should update based on when files in obsidian change
- This can be accomplished by updated the values with dict[k] = "value"

## Update quiz function to take advantage of scoring metrics
### this will require quizzer to pull questions from the .json file instead of from a prescanned list.
### Updates quiz function will have an algorithm to determine how to populate the quiz based on current scoring metrics:

## add in config option: questions by subject
### Only effects the question type