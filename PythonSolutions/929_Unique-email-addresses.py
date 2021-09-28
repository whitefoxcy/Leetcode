# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:20:28 2021

@author: yan_chen
"""


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            emails_set.add(local+'@'+domain)

        return len(emails_set)
