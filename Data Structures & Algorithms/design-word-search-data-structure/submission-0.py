# Bruteforce -> We can just put the words in a set and for searching word check if the word is in set. For each character of the word including".", we iterate it through every word in set. TC ->  N * M, N is no of words, M is max length of word, SC -> O(N * M)

# Optimize -> We build a trie. For adding, it will be just the common adding functionality of a basic trie. However,  for searching we need to handle the cases of ".". For characters not ".", we just check in the trie and return if it is there or not. For cases of ".", for current node, we need to recurisvely check if any of its children form the remaing part of the word. This will still be optimal (O(N)) as we are doing it max twice that is 26 * 26
# TC -> O(N), SC -> O(N + T), T -> total trie words

class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            cur = node

            for i in range(idx, len(word)):
                c = word[i]
                if c != ".":
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                else:
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True
                    return False
            return cur.end

        return dfs(self.root, 0)


        
