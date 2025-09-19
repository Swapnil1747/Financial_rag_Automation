def split_text(text: str, max_chars: int = 1000, overlap: int = 200) -> list[str]:
    if not text:
        return []

    chunks = []
    start = 0
    text_len = len(text)

    # Safety cap: max 10,000 chunks
    max_chunks = 10000
    count = 0

    while start < text_len and count < max_chunks:
        end = min(text_len, start + max_chars)
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
        if start < 0:
            start = 0
        count += 1

    return chunks
