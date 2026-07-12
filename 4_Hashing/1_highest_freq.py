'''Given an array of size N. Find the highest and lowest frequency element.'''

from collections import Counter
class FrequencyCounter:
    def highest_freq(self, arr):
        freq_map = Counter(arr)
        return freq_map.most_common(1)[0]

    def lowest_freq(self, arr):
        freq_map = Counter(arr)
        return min(freq_map.items(), key=lambda x: x[1])    # comparision based on 2nd element of tuple i.e. count
        
if __name__ == '__main__':
    obj = FrequencyCounter()
    l = [1,2,3,1,2,1,2,2,2,0]
    print(obj.highest_freq(l))
    print(obj.lowest_freq(l))
            