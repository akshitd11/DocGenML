def _get_conn_params(self):
    conn = self.get_connection(self.snowflake_conn_id)
    account = conn.extra_dejson.get('account', None)
    warehouse = conn.extra_dejson.get('warehouse', None)
    database = conn.extra_dejson.get('database', None)
    region = conn.extra_dejson.get('region', None)
    role = conn.extra_dejson.get('role', None)
    conn_config = {'user': conn.login, 'password': conn.password or '', 'schema': conn.schema or '', 'database': self.database or database or '', 'account': self.account or account or '', 'warehouse': self.warehouse or warehouse or '', 'region': self.region or region or '', 'role': self.role or role or ''}
    '\n        If private_key_file is specified in the extra json, load the contents of the file as a private\n        key and specify that in the connection configuration. The connection password then becomes the\n        passphrase for the private key. If your private key file is not encrypted (not recommended), then\n        leave the password empty.\n        '
    private_key_file = conn.extra_dejson.get('private_key_file', None)
    if private_key_file:
        with open(private_key_file, 'rb') as key:
            passphrase = None
            if conn.password:
                passphrase = conn.password.strip().encode()
            p_key = serialization.load_pem_private_key(key.read(), password=passphrase, backend=default_backend())
        pkb = p_key.private_bytes(encoding=serialization.Encoding.DER, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
        conn_config['private_key'] = pkb
        conn_config.pop('password', None)
    return conn_config