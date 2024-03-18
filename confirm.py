import subprocess


def confirm(command, shell=False):
    print(command + ' \033[1;34m[\033[1;35m<Enter>\033[1;34m to continue, \033[1;35m<CTRL-BREAK>\033[1;34m to exit]\033[0;0m')
    try:
        raw_input()
    except NameError:
        input()
    output = subprocess.check_output(command.split(), stderr=subprocess.STDOUT, shell=shell)
    if output.replace('\n', '').strip() == "":
        print('\033[1;32mOK\033[0;0m')
    else:
        print(output)
    if not output.endswith('\n'):
        print('')