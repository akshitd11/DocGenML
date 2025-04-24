def ffmpeg_download_stream(files, title, ext, params={}, output_dir='.', stream=True):
    output = title + '.' + ext
    if not output_dir == '.':
        output = output_dir + '/' + output
    print('Downloading streaming content with FFmpeg, press q to stop recording...')
    if stream:
        ffmpeg_params = [FFMPEG] + ['-y', '-re', '-i']
    else:
        ffmpeg_params = [FFMPEG] + ['-y', '-i']
    ffmpeg_params.append(files)
    if FFMPEG == 'avconv':
        ffmpeg_params += ['-c', 'copy', output]
    else:
        ffmpeg_params += ['-c', 'copy', '-bsf:a', 'aac_adtstoasc']
    if params is not None:
        if len(params) > 0:
            for (k, v) in params:
                ffmpeg_params.append(k)
                ffmpeg_params.append(v)
    ffmpeg_params.append(output)
    print(' '.join(ffmpeg_params))
    try:
        a = subprocess.Popen(ffmpeg_params, stdin=subprocess.PIPE)
        a.communicate()
    except KeyboardInterrupt:
        try:
            a.stdin.write('q'.encode('utf-8'))
        except:
            pass
    return True