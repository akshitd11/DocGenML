def wanmen_download_by_course(json_api_content, output_dir='.', merge=True, info_only=False, **kwargs):
    for tIndex in range(len(json_api_content[0]['Topics'])):
        for pIndex in range(len(json_api_content[0]['Topics'][tIndex]['Parts'])):
            wanmen_download_by_course_topic_part(json_api_content, tIndex, pIndex, output_dir=output_dir, merge=merge, info_only=info_only, **kwargs)