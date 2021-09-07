# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 16:11:34 2021

@author: yan_chen
"""
import collections
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        q = collections.deque([(beginWord, 1)])
        visited = {beginWord}
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for j in string.ascii_lowercase:
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in wordSet:
                        q.append((tmp, level+1))
                        visited.add(tmp)
        return 0
