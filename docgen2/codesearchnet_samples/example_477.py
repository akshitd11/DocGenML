def get_mod_time(self, path):
    conn = self.get_conn()
    ftp_mdtm = conn.sendcmd('MDTM ' + path)
    time_val = ftp_mdtm[4:]
    try:
        return datetime.datetime.strptime(time_val, '%Y%m%d%H%M%S.%f')
    except ValueError:
        return datetime.datetime.strptime(time_val, '%Y%m%d%H%M%S')