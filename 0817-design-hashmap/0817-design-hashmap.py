class MyHashMap:

    def __init__(self):
        self.mp = [None] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.mp[key] = value
        print(key, self.mp[key])
        

    def get(self, key: int) -> int:
        return -1 if self.mp[key] == None else self.mp[key]
        

    def remove(self, key: int) -> None:
        self.mp[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)