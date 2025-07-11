import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File name {filename}: create successfully!")
    except FileExistsError:
        print(f"File name {filename}: already exists!")
        
    except Exception as E:
        print('An error occurd!')
        
def view_all_file():
    files = os.listdir()
    if not files:
        print('No file in this directory!')
    else:
        print('files in directory')
        for file in files :
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!') 
    except FileNotFoundError:
        print('file not found')
        
    except Exception as e:
        print('An error occurd!')
           
def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"content '{filename}' : \n{content}") 
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print('An error occurd!')
        
def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input('Enter content: ')
            f.write(content + "\n")     #\n means new line
            print('content added to {filename} successfully!')
            
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")

    except Exception as e:
        print('An error occurd!')
        
        
def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: create a file')
        print('2: view all files')
        print('3: delete a file')
        print('4: read a file')
        print('5: edit a file')
        print('6: exit a file')
        
        choice = input ('enter your choice(1-6) = ')
        
        if choice == '1':
            filename = input("enter the file-name to create = ")
            create_file(filename)
            
        elif choice == '2':
            view_all_file()
            
        elif choice == '3':
            filename = input("enter the file-name to delete = ")
            delete_file(filename)
            
        elif choice == '4':
            filename = input("enter the file-name to read = ")
            read_file(filename)
            
        elif choice == '5':
            filename = input("enter the file-name to edit = ")
            edit_file(filename)
            
        elif choice == '6':
            print('closing the app ...')    
            break
        
        else:
            print('invalid choice!')
            

if __name__ == "__main__":
    main()
    