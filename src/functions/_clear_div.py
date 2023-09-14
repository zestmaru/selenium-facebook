import re


def clear_div(div: str, tag: str):
    """Clear div from trash and get useful info.

    Args:
        div (str): Div with trash
        tag (str): Tag to sort hardcoded regex for each type

    Returns:
        dict: {'text|group_name': 'str'} 
        or 
        dict: {'image': ['link', 'link', 'link']}
    """

    if tag == "text":
        div = re.findall('(?<=start;">)(.*)(?=<)', str(div))
        div = re.sub("(start;\">)", ">\n", str(div))
        div = re.sub("(<[^>]*>)", "", str(div))
        div = str(div)[2:-2]
    if tag == "image":
        div = re.sub("amp;", "", str(div))
        div = re.findall('src\\s*=\\s*"(.+?)"', str(div))
    if tag == "group_name":
        div = re.sub("(<[^>]*>)", "", str(div))
        div = str(div)[1:-1]

    clean = div
    d = dict([(tag, clean)])
    return d
