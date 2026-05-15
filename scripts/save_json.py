import os
import json

def save_viral_segments(segments_data=None, project_folder="tmp"):
    output_txt_file = os.path.join(project_folder, "viral_segments.txt")

    if not os.path.exists(output_txt_file):
        if segments_data is None:
            while True:
                user_input = input("\nPlease enter the JSON in the required format:\n")
                try:
                    segments_data = json.loads(user_input)
                    if "segments" in segments_data and isinstance(segments_data["segments"], list):
                        with open(output_txt_file, 'w', encoding='utf-8') as file:
                            json.dump(segments_data, file, ensure_ascii=False, indent=4)
                        print(f"Viral segments saved to {output_txt_file}")
                        break
                    else:
                        print("Invalid format. Make sure the structure is correct.")
                except json.JSONDecodeError:
                    print("Error decoding JSON. Please check the formatting.")
                print("Please try again.")
        else:
            with open(output_txt_file, 'w', encoding='utf-8') as file:
                json.dump(segments_data, file, ensure_ascii=False, indent=4)
            print(f"Viral segments saved to {output_txt_file}\n")
    else:
        print(f"File {output_txt_file} already exists. No additional input needed.")
