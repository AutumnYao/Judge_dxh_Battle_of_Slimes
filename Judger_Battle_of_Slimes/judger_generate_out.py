import subprocess
import os
import sys
IN_SUFFIX='.in'
OUT_SUFFIX='.out'
args_thisdir=os.path.dirname(os.path.abspath(
        sys.executable if getattr(sys, 'frozen', False) else __file__
    ))
thisdir_files=os.listdir(args_thisdir+'\\source\\3_task3')
thisdir_files_cpp=[_ for _ in thisdir_files if _[-4:]=='.cpp']

TASKS = [
    ('1_task1', thisdir_files_cpp),
    ('2_task2', thisdir_files_cpp),
    ('3_task3', thisdir_files_cpp),
]
TASK_NAMES = [n for n, _ in TASKS]


def modify_authentic_output_file(data_out_file):
        with open(data_out_file, 'r') as read_file:
            new_line = []
            lines = read_file.readlines()
            for line in lines:
                #替换Task?.exe中不合理的输出
                new_line += line.replace("pet", "slime")\
                            .replace("starts", "start")\
                            .replace("You sends", "You send")\
                            .replace("Enemy start", "Enemy starts")\
                            .replace("Battle start!", "Battle starts!")\
                            .replace("Enemy WIN! You LOSE!", "You Lose\n")\
                            .replace("You WIN! Enemy LOSE!", "You Win\n")\
                            .replace("Enemy Win You Lose", "You Lose\n")\
                            .replace("You Win Enemy Lose", "You Win\n")\
                            .replace("DRAW!", "Draw\n")
        
        with open(data_out_file, "w") as write_file:
            write_file.writelines(new_line)



for task_name in TASK_NAMES:
    case_choices = sorted(set(
        f.name[:-len(IN_SUFFIX)]
        for f in os.scandir(os.path.join(args_thisdir, 'data', task_name))
        if f.is_file() and f.name.endswith(IN_SUFFIX)
    ))

    args_case=None
    if args_case is None:
        args_case = case_choices.copy()
    else:
        args_case = sorted(set(args_case))
    for case in args_case:

        in_path, std_path = (
        os.path.join(args_thisdir, 'data', task_name, case + suffix)
        for suffix in (IN_SUFFIX, OUT_SUFFIX)
    )
        with open(f'{in_path}','r') as input_address:
            my_input=input_address.read()

        out_path=in_path[ :-3]+'.out'
        res = subprocess.run(
            [f"{args_thisdir}/demo/{task_name}.exe"],
            input=my_input,
            stdout=subprocess.PIPE,
            encoding="utf8",
        )

        with open(f'{out_path}','w') as output_address:
            output_address.write(res.stdout)
        modify_authentic_output_file(f'{out_path}')


