def levenshtein(source, target):
    if len(source) < len(target):
        return levenshtein(target, source)

    if len(target) == 0:
        return len(source)

    previous_row = range(len(target) + 1)
    for i, c1 in enumerate(source):
        current_row = [i + 1]
        for j, c2 in enumerate(target):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]