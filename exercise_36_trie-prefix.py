class Trie:
    """Prefix trie for insertion and word/prefix lookup."""
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for character in word:
            node = node.setdefault(character, {})
        node[None] = True

    def contains(self, word):
        node = self.root
        for character in word:
            if character not in node:
                return False
            node = node[character]
        return None in node

    def starts_with(self, prefix):
        node = self.root
        for character in prefix:
            if character not in node:
                return False
            node = node[character]
        return True
