def parse_query_param(url, param):
    try:
        return parse.parse_qs(parse.urlparse(url).query)[param][0]
    except:
        return None