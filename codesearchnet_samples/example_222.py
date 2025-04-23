def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    (output, stderr) = [stream.decode(sys.getdefaultencoding(), 'ignore') for stream in process.communicate()]
    if process.returncode != 0:
        raise AirflowConfigException('Cannot execute {}. Error code is: {}. Output: {}, Stderr: {}'.format(command, process.returncode, output, stderr))
    return output