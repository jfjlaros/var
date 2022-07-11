def lsp(flank: str, indel: str):
    """Find the longest prefix of `flank` that is a subsequence of `indel`.

    :arg flank: Right flanking reference sequence.
    :arg indel: An inserted or deleted sequence.

    :returns: Prefix length.
    """
    i = -1
    for j, c in enumerate(flank):
        if (i := indel.find(c, i + 1)) == -1:
            return j
    return len(indel)


def roll(ref: str, start: int, length: int):
    """Roll a substring to the right.

    :arg ref: Reference sequence.
    :arg start: Start position of the substring.
    :arg length: Length of the substring.

    :returns: End position after rolling (open interval notation).
    """
    for i in range(start, len(ref) - length):
        if ref[i] != ref[i + length]:
            return i + length
    return len(ref)


def sroll(ref: str, length: int):
    """Roll a substring and all of its suffixes to the right.

    :arg ref: Reference sequence.
    :arg length: Length of the substring.

    :returns: End position after rolling (open interval notation).
    """
    i = 0
    for j in range(length, 0, -1):
        i = roll(ref, i, j)
    return i


def extreme(flank: str, indel: str):
    """Find the extreme right position of `indel` applied before `flank`.

    :arg flank: Right flanking reference sequence.
    :arg indel: An inserted or deleted sequence.

    :returns: Extreme right position (open interval notation).
    """
    return sroll(flank, lsp(flank, indel))


ref = 'CATCATATATTTY'
print(ref[:extreme(ref, 'XCXAXTX')])
