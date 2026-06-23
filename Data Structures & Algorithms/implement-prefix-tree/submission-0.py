class PrefixTree:

    def __init__(self):
        self.tries = {}
        

    def insert(self, word: str) -> None:
        cur_tries = self.tries
        for c in word:
            if c not in cur_tries:
                cur_tries[c] = {}
            cur_tries = cur_tries[c]
        cur_tries[None] = True

    def search(self, word: str) -> bool:
        cur_tries = self.tries
        for c in word:
            if c not in cur_tries:
                return False
            cur_tries = cur_tries[c]
        return None in cur_tries
        

    def startsWith(self, prefix: str) -> bool:
        cur_tries = self.tries
        for c in prefix:
            if c not in cur_tries:
                return False
            cur_tries = cur_tries[c]
        return True
        
        