# python3

class Phonebook:
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(self.bucket_count)]
        self._multiplier = 31
        self._prime = 1000000007

    def _hash_func(self, s):
        """The best hash function from universal family"""
        ans = 0
        for c in reversed(str(s)):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count
    
    def add(self, query):
        string = query.number
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for q in bucket:
            if query.number == q.number:
                q.name = query.name
                return
        self.buckets[hashed] = [query] + bucket

    def delete(self, query):
        string = query.number
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i].number == query.number:
                bucket.pop(i)
                break

    def find(self, query):
        string = query.number
        hashed = self._hash_func(string)
        for q in self.buckets[hashed]:
            if query.number == q.number:
                return q.name
        return "not found"

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    phonebook = Phonebook(9)
    result = []
    for cur_query in queries:
        if cur_query.type == 'add':
            phonebook.add(cur_query)
        elif cur_query.type == 'del':
            phonebook.delete(cur_query)
        else:
            result.append(phonebook.find(cur_query))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))