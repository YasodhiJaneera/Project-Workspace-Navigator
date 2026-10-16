from pathlib import Path
import os
PROJECT_ROOT = Path.cwd().resolve()
  

def main():
    message_list=[]

project_path=input("Enter the project path").strip()
project_path=project_path if project_path !="" else"./"
os.environ["PROJECT_ROOT"]=str(project_path)
PROJECT_ROOT=Path(project_path).resolve()

print(PROJECT_ROOT)



#while True:
#
#         print("Starting...")


if __name__ == "__main__":
    main()