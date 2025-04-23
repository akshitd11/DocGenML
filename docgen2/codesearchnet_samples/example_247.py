def dispose_orm():
    log.debug('Disposing DB connection pool (PID %s)', os.getpid())
    global engine
    global Session
    if Session:
        Session.remove()
        Session = None
    if engine:
        engine.dispose()
        engine = None