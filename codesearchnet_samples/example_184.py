def _exit_gracefully(self, signum, frame):
    self.log.info('Exiting gracefully upon receiving signal %s', signum)
    self.terminate()
    self.end()
    self.log.debug('Finished terminating DAG processors.')
    sys.exit(os.EX_OK)