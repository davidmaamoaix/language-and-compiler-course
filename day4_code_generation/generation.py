def generate(node) -> [str]:
    """
    Generates the code for a given program.
    """

    return node.generate_code(None) # the program node has no context