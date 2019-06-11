# python3
"""
Coursera Specialization: Data Structure and Algorithm
Course: Data Structure

week 4-2 Hash chain

In this task your goal is to implement a hash table with lists chaining. You are already given the
number of buckets 𝑚 and the hash function. It is a polynomial hash function
ℎ(𝑆) =⎝|𝑆∑︁|−1𝑖=0𝑆[𝑖]𝑥𝑖 mod 𝑝⎞⎠ mod 𝑚 ,
where 𝑆[𝑖] is the ASCII code of the 𝑖-th symbol of 𝑆, 𝑝 = 1 000 000 007 and 𝑥 = 263. Your program
should support the following kinds of queries:
∙ add string — insert string into the table. If there is already such string in the hash table, then
just ignore the query.
∙ del string — remove string from the table. If there is no such string in the hash table, then
just ignore the query.
∙ find string — output “yes" or “no" (without quotes) depending on whether the table contains
string or not.
∙ check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of
the list. If 𝑖-th list is empty, output a blank line.
When inserting a new string into a hash chain, you must insert it in the beginning of the chain.

"""

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
            #.check = int(query[1])
        else:
            self.s = query[1]
            #self.find = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        #self.elems = []
        #self.hashTable = [[]] * bucket_count
        self.hashTable = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query_org(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            try:
                self.write_chain(cur for cur in reversed(self.hashTable[query.ind]) if self._hash_func(cur) == query.ind)
            except:
                self.write_chain([])
        else:
            hashedVal = self._hash_func(query.s)

            if query.type == 'add':
                if hashedVal in self.hashTable:
                    if query.s not in self.hashTable[hashedVal]:
                        self.hashTable[hashedVal].append(query.s)
                else:
                    self.hashTable[hashedVal] = [query.s]

            try:
                ind = self.hashTable[hashedVal].index(query.s)
            except:
                ind = -1

            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'del':
                if ind != -1:
                    self.hashTable[hashedVal].pop(ind)
        #print(self.hashTable)


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()