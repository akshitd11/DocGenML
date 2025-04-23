def run_cli(self, pig, verbose=True):
    with TemporaryDirectory(prefix='airflow_pigop_') as tmp_dir:
        with NamedTemporaryFile(dir=tmp_dir) as f:
            f.write(pig.encode('utf-8'))
            f.flush()
            fname = f.name
            pig_bin = 'pig'
            cmd_extra = []
            pig_cmd = [pig_bin, '-f', fname] + cmd_extra
            if self.pig_properties:
                pig_properties_list = self.pig_properties.split()
                pig_cmd.extend(pig_properties_list)
            if verbose:
                self.log.info('%s', ' '.join(pig_cmd))
            sp = subprocess.Popen(pig_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=tmp_dir, close_fds=True)
            self.sp = sp
            stdout = ''
            for line in iter(sp.stdout.readline, b''):
                stdout += line.decode('utf-8')
                if verbose:
                    self.log.info(line.strip())
            sp.wait()
            if sp.returncode:
                raise AirflowException(stdout)
            return stdout