def wait_until_finished(self):
    for (file_path, processor) in self._processors.items():
        while not processor.done:
            time.sleep(0.1)