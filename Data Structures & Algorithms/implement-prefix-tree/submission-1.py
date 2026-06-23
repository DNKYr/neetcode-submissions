class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEndWord = False
        

    def insert(self, word: str) -> None:
        cur_tries = self
        for c in word:
            if c not in cur_tries.children:
                cur_tries.children[c] = PrefixTree()
            cur_tries = cur_tries.children[c]
        cur_tries.isEndWord = True

    def search(self, word: str) -> bool:
        cur_tries = self
        for c in word:
            if c not in cur_tries.children:
                return False
            cur_tries = cur_tries.children[c]
        return cur_tries.isEndWord
        

    def startsWith(self, prefix: str) -> bool:
        cur_tries = self
        for c in prefix:
            if c not in cur_tries.children:
                return False
            cur_tries = cur_tries.children[c]
        return True
        
        