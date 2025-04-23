def reserve_free_tcp_port(self):
    self.reserved_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.reserved_tcp_socket.bind(('127.0.0.1', 0))
    self.sql_proxy_tcp_port = self.reserved_tcp_socket.getsockname()[1]