import base64


def analysis_base64(content):
    data = base64.b64decode(content)
    return data


def write_file(new_file_path, content):
    fo = open(new_file_path, "w+")
    fo.write(content)
    fo.close()
    return 'ok'
