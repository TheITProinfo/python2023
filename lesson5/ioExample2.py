# coding=utf-8
f_name="test.txt"
with open(f_name,'r') as f:
    lines=f.readlines()
    # print(lines)
    copy_f_name="test2.txt"
    with open(copy_f_name,'w') as copy_f:
        copy_f.writelines(lines)
        print("file {0} is copyed to {1} successfully".format(f_name,copy_f_name))