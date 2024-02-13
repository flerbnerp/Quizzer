First implementation we will update our qaMathematics.json to use LaTeX notation for the display of math questions

Next we will create a settings widget to house our configuration widgets
    each configuration widget will allow the user to adjust the parameters of the algorithm so they can easily choose which topic to focus more heavily on. Though it's encouraged to ensure you get at least some exposure to multiple fields of study not just a block focused on a single topic.

Next implementation plan is to add a new section to the settings gui:
    This section will allow the user update the qaCategoriesConfig from within the program itself rather than needing to navigate into the program files.

Next implementation is:
    to implement another widget to the settings window that will provide a more user friendly display of the questions in the system
    The user will be able to:
        Add new categories
        Add new question and answer pairs to existing categories
        Edit question and answer pairs that already exist
        See all question and answer pairs along with the meta data.
    The user will not be able to edit their meta data. e.g.
        correct attempts
        total attempts
        question unique id
        etc.