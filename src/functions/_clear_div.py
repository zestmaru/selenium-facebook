import re


def clear_div(div: str, tag: str):
    """Clear div from trash and get useful info.

    Args:
        div (str): Div with trash
        tag (str): Tag to sort hardcoded regex for each type

    Returns:
        dict: [tag:"[clear text]"]
    """

    if tag == "text":
        div = re.findall('(?<=start;">)(.*)(?=<)', str(div))
        div = re.sub("(<[^>]*>)", "", str(div))
    if tag == "image":
        div = re.sub("amp;", "", str(div))
        div = re.findall('src\\s*=\\s*"(.+?)"', str(div))
    if tag == "group_name":
        div = re.sub("(<[^>]*>)", "", str(div))

    clean = div
    d = dict([(tag, clean)])
    return d
