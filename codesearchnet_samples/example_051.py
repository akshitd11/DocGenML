def wanmen_download_by_course_topic_part(json_api_content, tIndex, pIndex, output_dir='.', merge=True, info_only=False, **kwargs):
    html = json_api_content
    title = _wanmen_get_title_by_json_topic_part(html, tIndex, pIndex)
    bokeccID = _wanmen_get_boke_id_by_json_topic_part(html, tIndex, pIndex)
    bokecc_download_by_id(vid=bokeccID, title=title, output_dir=output_dir, merge=merge, info_only=info_only, **kwargs)