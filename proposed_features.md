# Planned changes:
## Core Functionality
### Picture and GUI module
- CLI is useful, but doesn't allow for display of images for problems. If this is to be used for science and mathematics, support for latex and picture display needs to be added in:
- I would say this is front end
#### Modify quiz function (simple client-server architecture)
- If we modify the generate quiz function to return only a single random question
- Then
- The client app will only need to do two things 
- Make a server call for the question:
- Make a server call to update the score and stats for that particular user:
- Within a simplified architecture in place, we could develop a quick client app for ios, android, MacOS, Windows, and Linux platforms.
### Stats module
- This module will be a menu option that shows the user a variety of states (added menu option)
- Number of questions that are loaded in quizzer
- Number of questions by subject type
- Total number of questions they've answered
- Total correct attempts
- Total incorrect attempts
- Longest Revision Streak
- Average time per quiz (every quiz will append a time_taken float value to a list data_type stores inside stats.json), calling the option to list stats will get the average value of this key: value pair.
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
