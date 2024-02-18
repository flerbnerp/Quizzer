# Planned changes:
## Core Functionality
### Stats module
- This module will be a menu option that shows the user a variety of states
- Number of questions that are loaded in quizzer
- Number of questions by subject type
- Total number of questions they've answered
- Total correct attempts
- Total incorrect attempts
- Longest Revision Streak
- Average time per quiz (every quiz will append a time_taken float value to a list data_type stores inside stats.json), calling the option to list stats will get the average value of this key: value pair.
### move storage of questions to a seperate questions.json, seperate from the primary config.json
Initialize function then update config.json with data from the questions.json, if the config.json gets corrupted at any point, the scores are backed up in a separate .json file
### Backup storage module
- In case data might get overwritten, a regular backup should be made. A function that can be called from within the program should help make this easy for the user to backup their files
- A second function can be called that pulls the files from backups/ and overwrites the files in the main directory.
### add in config options
- First option to tell quizzer how many questions should be in each exam:
### add in config option: questions by subject
- Only effects the question type
- This option will allow the user to specify whether they want more or less questions from certain fields of study
## Check function to see which concepts have questions and which don't
- Function should also grab how many questions each concept has:
## To Do
- develop a framework for question generation based on note type
- 
## Feature Creep
