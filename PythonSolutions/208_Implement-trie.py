# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:37:46 2021

@author: yan_chen
"""


class TrieNode:

    def __init__(self):

        self.children = collections.defaultdict(TrieNode)
        self.isword = False


class Trie:

    def __init__(self):

        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr = self.root

        for char in word:
            curr = curr.children[char]

        curr.isword = True

    def search(self, word: str) -> bool:

        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.isword

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True
