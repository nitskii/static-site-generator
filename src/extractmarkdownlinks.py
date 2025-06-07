from re import findall

def extract_markdown_links(text):
  regex = r"(?<!!)\[(.*?)\]\((.*?)\)"

  return findall(regex, text)
