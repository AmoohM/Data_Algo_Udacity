import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self._capacity = capacity
        self._cache = collections.OrderedDict()


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        try:
            # try get the requested item and move it to end of dict(recently used)
            self._cache.move_to_end(key)
            return self._cache[key]
        
        except KeyError:
            #non-existent value
            return -1
    
    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        try:
            # Remove existing value at key if present
            self._cache.pop(key)

        except KeyError:
            # check if cache full and remove lRU
            if len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)
        
        #set item
        self._cache[key] = value


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(3))      # return -1