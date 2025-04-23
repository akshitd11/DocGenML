def get_streams_by_id(account_number, video_id):
    endpoint = 'https://edge.api.brightcove.com/playback/v1/accounts/{account_number}/videos/{video_id}'.format(account_number=account_number, video_id=video_id)
    fake_header_id = fake_headers
    fake_header_id['Accept'] = 'application/json;pk=BCpkADawqM1cc6wmJQC2tvoXZt4mrB7bFfi6zGt9QnOzprPZcGLE9OMGJwspQwKfuFYuCjAAJ53JdjI8zGFx1ll4rxhYJ255AXH1BQ10rnm34weknpfG-sippyQ'
    html = get_content(endpoint, headers=fake_header_id)
    html_json = json.loads(html)
    link_list = []
    for i in html_json['sources']:
        if 'src' in i:
            if i['src'].startswith('https'):
                link_list.append((str(i['height']), i['src']))
    return link_list