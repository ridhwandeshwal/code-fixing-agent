def wrap(text, cols):
    lines = []
    while len(text) > cols:
        end = text[:cols + 1].rfind(' ')
        if end == -1:
            end = cols
        line, text = text[:end], text[end:].lstrip()
        lines.append(line)
    lines.append(text)
    return lines