def _normalize_mlengine_job_id(job_id):
    match = re.search('\\d|\\{{2}', job_id)
    if match and match.start() == 0:
        job = 'z_{}'.format(job_id)
    else:
        job = job_id
    tracker = 0
    cleansed_job_id = ''
    for m in re.finditer('\\{{2}.+?\\}{2}', job):
        cleansed_job_id += re.sub('[^0-9a-zA-Z]+', '_', job[tracker:m.start()])
        cleansed_job_id += job[m.start():m.end()]
        tracker = m.end()
    cleansed_job_id += re.sub('[^0-9a-zA-Z]+', '_', job[tracker:])
    return cleansed_job_id