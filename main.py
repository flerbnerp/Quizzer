from initialize import initialize_education_directory
from initializeFilePath import construct_filepaths_directory
from gui import guiMain
import signal



def handle_interrupt(signum, frame):
    print("Exiting...")
    guiMain.stop_question_loop()
    exit(0)

def main():
    # Initialize directories and config files
    initialize_education_directory()
    construct_filepaths_directory()
    # Set up interrupt handling
    signal.signal(signal.SIGINT, handle_interrupt)
    guiMain.start_gui()

if __name__ == "__main__":
    main()
    
#Github instructions
# Run this first if you have made changes to the software on another system. Best to
# run this before you start working on the software on your system.
# git fetch origin
# git pull origin main

# Run these commands to push your changes to the repository
# git status
# git add .
# git commit -m "message"
# git push origin main