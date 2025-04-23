def ds_format(ds, input_format, output_format):
    return datetime.strptime(ds, input_format).strftime(output_format)