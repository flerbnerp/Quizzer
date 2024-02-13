import os
import yaml
# use a dictionary
# Concept/question, subject, related
def scan_directory():
    questions = []
    concepts = []
    for root,dirs, files in os.walk("/home/karibar/Documents/Education"):
        for file in files:
            if file.endswith(".md"):
                with open(os.path.join(root,file), "r", encoding="utf-8") as f:
                    content = f.read()  
                start_delimiter, end_delimiter = "---", "---\n"
                if start_delimiter and end_delimiter:
                    start_index = content.find(start_delimiter) + len(start_delimiter)
                    end_index = content.find(end_delimiter, start_index)
                    if start_index > -1 and end_index > -1:
                        yaml_properties = content[start_index:end_index].strip()
                        try:
                            note_dict = yaml.safe_load(yaml_properties)
                            filename, extension = os.path.splitext(os.path.basename(file))
                            full_filename = f"{filename}.{extension}"
                            note_dict["file_name"] = full_filename
                            if note_dict["type"] == "Concept":
                                concepts.append(note_dict)
                            if note_dict["type"] == "question":
                                questions.append(note_dict)
                        except:
                            pass
    return concepts, questions 
scan_directory()