# utils/helpers.py
def parse_command(content: str, prefix: str):
    if content.startswith(prefix):
        command_name = content[len(prefix) :].split()[0]
        return command_name
    return None
