def format_chunks(text):
    return text.strip().replace("\n", " ")

def anonymize_text(text):
    return text.replace("John", "[REDACTED]")  # Simulate PHI redaction
