import re

def clear_div(div: str, tag: str) -> dict:
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
    elif tag == "image":
        div = re.sub("amp;", "", str(div))
        div = re.findall('src\\s*=\\s*"(.+?)"', str(div))
        div = re.findall(r"https://[^\s\"'>]+", str(div))
        div = list(set(div))
    elif tag == "group_name":
        div = re.sub("(<[^>]*>)", "", str(div))
        div = str(div)[1:-1]

    d = dict([(tag, div)])
    return d
