
#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;

class LRUCache {
private:
    int capacity;

    // Front = most recently used
    // Back  = least recently used
    list<pair<int, int>> cache;

    // Key -> iterator pointing to its list node
    unordered_map<int, list<pair<int, int>>::iterator> mp;

public:
    LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        auto it = mp.find(key);

        // Key does not exist
        if (it == mp.end()) {
            return -1;
        }

        // Move accessed item to the front
        cache.splice(cache.begin(), cache, it->second);

        return it->second->second;
    }

    void put(int key, int value) {
        if (capacity <= 0) return;

        auto it = mp.find(key);

        // Key already exists: update its value
        if (it != mp.end()) {
            it->second->second = value;
            cache.splice(cache.begin(), cache, it->second);
            return;
        }

        // Cache is full: remove least recently used item
        if (cache.size() == capacity) {
            int lruKey = cache.back().first;
            mp.erase(lruKey);
            cache.pop_back();
        }

        // Insert new item as most recently used
        cache.push_front({key, value});
        mp[key] = cache.begin();
    }
};

int main() {
    LRUCache cache(2);

    cache.put(1, 10);
    cache.put(2, 20);

    cout << cache.get(1) << '\n';  // 10

    cache.put(3, 30);              // Evicts key 2

    cout << cache.get(2) << '\n';  // -1
    cout << cache.get(3) << '\n';  // 30

    return 0;
}
