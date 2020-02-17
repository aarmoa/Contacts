#!/bin/python3

import os
import sys

class ContactsList:

    def __init__(self):
        self.contactList = []

    def addContact(self, aContact):
        self.contactList.append(aContact)

    def matchesNumberForPrefix(self, aContactPrefix):
        return len([aContact for aContact in self.contactList if aContact.startswith(aContactPrefix)])

class TrieNode:

    def __init__(self):
         self.children = {}
         self.counter = 0

    def childOrNewFor(self, aCharacter):
        child = self.children.get(aCharacter)
        if not child:
            child = TrieNode()
            self.children[aCharacter] = child

        return child

    def childFor(self, aCharacter):
        return self.children.get(aCharacter)

    def firstLevelChildren(self):
        return list(self.children.values())

    def numberOfChildren(self):
        return self.counter


class TrieTree:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, aString):
        current = self.root

        for aCharacter in aString:
            current = current.childOrNewFor(aCharacter)
            current.counter += 1

    def numberOfPossibilitiesFor(self, aPrefixString):
        current = self.root
        for aCharacter in aPrefixString:
            current = current.childFor(aCharacter)
            if not current:
                return 0

        return current.numberOfChildren()

def processQuery(aQueryComponents, aContactsList, aResultsCollection):
    if aQueryComponents[0] == 'add':
        aContactsList.addWord(aQueryComponents[1])
    if aQueryComponents[0] == 'find':
        aResultsCollection.append(aContactsList.numberOfPossibilitiesFor(aQueryComponents[1]))

#
# Complete the contacts function below.
#
def contacts(queries):
    #
    # Write your code here.
    #
    contactsList = TrieTree()
    results = []

    for queryComponents in queries:
        processQuery(queryComponents, contactsList, results)

    return results

def contactsOld(queries):
    #
    # Write your code here.
    #
    contactsList = ContactsList()
    results = []

    for queryComponents in queries:
        processQuery(queryComponents, contactsList, results)

    return results

"""if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
"""