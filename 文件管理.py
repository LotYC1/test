import os

def get_file_path():
    target_dir_list = []
    drive_letter = input('请输入盘符(如D)：').strip().upper()
    target_dir_list.append(f'{drive_letter}:\\')
    while True:
        target_dir = input('请依次输入路径(输入*完成输入，输入#退出程序)：')
        target_dir_list.append(target_dir)
        if target_dir.lower() == '*':
            target_dir_list.remove('*')
            break
        elif target_dir.lower() == '#':
            exit()
    return target_dir_list

def cheak_file_path():
    while True:
        target_dir_list = get_file_path()
        file_path = os.path.join(*target_dir_list)
        if os.path.exists(file_path):
            return file_path
        else:
            print(f'\n{file_path}\n')
            print('路径不存在，请重新输入')

def revise_filename():
    while True:    
        file_path = cheak_file_path()
        files_name = os.listdir(file_path)
        try:
            files_name.sort(key=lambda x: int(f'{x[0]}{x[1]}{x[2]}{x[3]}'))
        except ValueError:
            print('文件名格式不正确')
            pass
        counter = 0
        for file_name in files_name:
            counter += 1
            file_number = str(counter).zfill(4)
            old_file_path = os.path.join(file_path, file_name)
            new_file_path = os.path.join(file_path, f'{file_number}_{file_name[5:]}')
            os.rename(old_file_path, new_file_path)
        print('文件名修改完成')
        break

def main():
    print('欢迎使用文件名修改工具！')
    revise_filename()

if __name__ == '__main__':
    main()