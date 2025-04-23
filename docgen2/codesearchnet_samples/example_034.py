def download(self, **kwargs):
    if 'json_output' in kwargs and kwargs['json_output']:
        json_output.output(self)
    elif 'info_only' in kwargs and kwargs['info_only']:
        if 'stream_id' in kwargs and kwargs['stream_id']:
            stream_id = kwargs['stream_id']
            if 'index' not in kwargs:
                self.p(stream_id)
            else:
                self.p_i(stream_id)
        elif 'index' not in kwargs:
            self.p([])
        else:
            stream_id = self.streams_sorted[0]['id'] if 'id' in self.streams_sorted[0] else self.streams_sorted[0]['itag']
            self.p_i(stream_id)
    else:
        if 'stream_id' in kwargs and kwargs['stream_id']:
            stream_id = kwargs['stream_id']
        else:
            stream_id = self.streams_sorted[0]['id'] if 'id' in self.streams_sorted[0] else self.streams_sorted[0]['itag']
        if 'index' not in kwargs:
            self.p(stream_id)
        else:
            self.p_i(stream_id)
        if stream_id in self.streams:
            urls = self.streams[stream_id]['src']
            ext = self.streams[stream_id]['container']
            total_size = self.streams[stream_id]['size']
        else:
            urls = self.dash_streams[stream_id]['src']
            ext = self.dash_streams[stream_id]['container']
            total_size = self.dash_streams[stream_id]['size']
        if not urls:
            log.wtf('[Failed] Cannot extract video source.')
        download_url_ffmpeg(urls[0], self.title, 'mp4', output_dir=kwargs['output_dir'], merge=kwargs['merge'], stream=False)
        if not kwargs['caption']:
            print('Skipping captions.')
            return
        for lang in self.caption_tracks:
            filename = '%s.%s.srt' % (get_filename(self.title), lang)
            print('Saving %s ... ' % filename, end='', flush=True)
            srt = self.caption_tracks[lang]
            with open(os.path.join(kwargs['output_dir'], filename), 'w', encoding='utf-8') as x:
                x.write(srt)
            print('Done.')