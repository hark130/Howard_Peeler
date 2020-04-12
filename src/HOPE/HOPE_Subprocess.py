import subprocess


def execute_command(cmd_list):
    """
        PURPOSE - Execute a list of commands using subprocess
        PARAMETERS
            cmd_list - A non-empty list of non-empty strings to execute as commands
        RETURNS stdout from execution as a string
        NOTES
            - Raises a RuntimeError if the execution of cmd_list fails
    """
    # INPUT VALIDATION
    if not isinstance(cmd_list, list):
        raise TypeError('The cmd_list parameter must be a list instead of '
                        f'{type(cmd_list)}')
    elif not cmd_list:
        raise ValueError('The cmd_list parameter may not be empty')
    else:
        for entry in cmd_list:
            if not isinstance(entry, str):
                raise TypeError('The cmd_list parameter contains a non-string')
            elif not entry:
                raise ValueError('The cmd_list parameter contains an empty string')

    # LOCAL VARIABLES
    proc_obj = None  # Popen object
    stdout_output = ''  # Store stdout here
    stderr_output = ''  # Store stderr here

    # EXECUTE
    proc_obj = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (stdout_output, stderr_output) = proc_obj.communicate(timeout=15)
    if stderr_output:
        raise RuntimeError(stderr_output.decode())

    # DONE
    return stdout_output.decode()
