def truncate_content(content: str, max_length: int) -> str:
    """
    Truncate content to a specified max length.
    """
    return content[:max_length] if len(content) > max_length else content
