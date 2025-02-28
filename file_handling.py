def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of {file_name}:\n{content}")
            return content
    except FileNotFoundError as er:
        print(f" {file_name} does not exist.")
def modify_file(file_name, new_content):
    try:
        with open(file_name, 'r') as file:
            file.read()
            print(f"Content of {file_name} has been modified.")
    except FileNotFoundError:
        print(f"{file_name} does not exist.")
if __name__ == "__main__":
    file1_content = read_file('file1.txt')
    file2_content=read_file('file2.txt')
    new_content = "This is the new modified content."
    modify_file('file1.txt', new_content)
    modify_file('file2.txt',new_content)
    read_file('file1.txt')
    read_file('file2.txt')

#file1.txt                          #file2.txt
"name" ="Aliya"                  "color"="yellow"
                                 "hobby"="singing"
"branch"="DS"
"college"="BITM"

#OUTPUT
Content of file1.txt:
"name" ="Aliya"
"branch"="DS"
"college"="BITM"
Content of file2.txt:
"color"="yellow"
"hobby"="singing"
Content of file1.txt has been modified.
Content of file2.txt has been modified.
Content of file1.txt:
"name" ="Aliya"
"branch"="DS"
"college"="BITM"
Content of file2.txt:
"color"="yellow"
"hobby"="singing"
