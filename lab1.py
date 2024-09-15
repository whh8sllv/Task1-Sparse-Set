import time
import random
import matplotlib.pyplot as plt

class SparseSet():

    def __init__(self, mx_vl, cap):
        self.maxVal = mx_vl
        self.capacity = cap
        self.dense = [-1] * self.capacity
        self.sparse = [-1] * (self.maxVal + 1)
        self.n = 0

    def search(self, x):
        if x > self.maxVal:
            return -1
        elif (self.sparse[x] < self.n) and (self.dense[self.sparse[x]] == x):
            return self.sparse[x]
        else:
            return -1

    def insert(self, x):
        if x > self.maxVal:
            print(f"Error, element {x} can't be greater than maxVal")
            return 0
        elif self.n >= self.capacity:
            print(f"Error, current cardinality of a Set can't exceed or be equal to a capacity")
            return 0
        elif self.search(x) == -1:
            self.dense[self.n] = x
            self.sparse[x] = self.n
            self.n += 1

    def delete(self, x):
        if self.search(x) == -1:
            print(f"Error, element {x} isn't in a Set")
            return 0

        self.tmp = self.dense[(self.n) - 1]
        self.dense[self.sparse[x]] = self.tmp
        self.sparse[self.tmp] = self.sparse[x]
        self.n -= 1
        #print(f'Element {x} was successfully deleted')

    def clear(self):
        self.n = 0

    def union(self, set2):
        new_maxVal = max(self.maxVal, set2.maxVal)
        new_capacity = self.capacity + set2.capacity
        setUnion = SparseSet(new_maxVal, new_capacity)
        for i in range(self.n):
            setUnion.insert(self.dense[i])
        for i in range(set2.n):
            setUnion.insert(set2.dense[i])
        return setUnion

    def intersection(self, set2):
        new_maxVal = max(self.maxVal, set2.maxVal)
        new_capacity = max(self.capacity, set2.capacity)
        setIntersection = SparseSet(new_maxVal, new_capacity)
        for i in range(self.n):
            setIntersection.insert(self.dense[i])
        for i in range(setIntersection.n):
            if set2.search(setIntersection.dense[i]) == -1:
                setIntersection.delete(setIntersection.dense[i])
        return setIntersection

    def difference(self, set2):
        setDifference = SparseSet(self.maxVal, self.capacity)
        for i in range(self.n):
            setDifference.insert(self.dense[i])
        setIntersection = self.intersection(set2)
        for i in range(setDifference.n):
            if setIntersection.search(setDifference.dense[i]) == setIntersection.sparse[setDifference.dense[i]]:
                setDifference.delete(setDifference.dense[i])
        return setDifference

    def symDifference(self, set2):
        setUnion = self.union(set2)
        setIntersection = self.intersection(set2)
        setSymDifference = setUnion.difference(setIntersection)
        return setSymDifference

    def isSubset(self, set2):
        if self.n > set2.n:
            print('Error, Subset cannot have more elements than the Set')
        else:
            for i in range(self.n):
                if set2.search(self.dense[i]) == -1:
                    print('Is Not Subset')
                    return 0
            print('Is Subset')

    def display(self):
        if self.n == 0:
            print('Set is empty')
            return 0
        else:
            for i in range(self.n):
                print(self.dense[i], end=' ')
            print()


def timeTestSearch(n, k):
    time_list = []
    for i in range(1000):
        spSet = SparseSet(n, n)
        elements = [i for i in range(n)]
        random.shuffle(elements)
        for i in range(len(elements)):
            spSet.insert(elements[i])
        start = time.time()
        spSet.search(k)
        end = time.time()
        fin_time = end - start
        time_list.append(fin_time)
    result = sum(time_list)/len(time_list)
    return result

def timeTestUnion(n):
    time_list = []
    for i in range(1000):
        spSetA = SparseSet(n, n)
        elementsA = [i for i in range(n)]
        random.shuffle(elementsA)
        for i in range(len(elementsA)):
            spSetA.insert(elementsA[i])
        spSetB = SparseSet(n, n)
        elementsB = [i for i in range(n)]
        random.shuffle(elementsB)
        for i in range(len(elementsB)):
            spSetB.insert(elementsB[i])
        start = time.time()
        supSetUnion = spSetA.union(spSetB)
        end = time.time()
        fin_time = end - start
        time_list.append(fin_time)
    result = sum(time_list)/len(time_list)
    return result




setA = SparseSet(99, 15)
setB = SparseSet(100, 25)

setA.insert(1)
setA.insert(0)
setA.insert(22)
setA.insert(19)
setA.insert(40)
setA.insert(49)
setA.insert(99)
setA.insert(87)
setA.insert(41)
setA.insert(3)
setA.insert(8)
setA.insert(0)
setB.insert(100)
setB.insert(2)
setB.insert(3)
setB.insert(41)
setB.insert(47)
setB.insert(94)
setB.insert(0)
setB.insert(20)
print('Set A: ')
setA.display()
print('Set B: ')
setB.display()

print('A | B:')
setUnion1 = setA.union(setB)
setUnion1.display()
print('B | A:')
setUnion2 = setB.union(setA)
setUnion2.display()
print('A & B:')
setIntersection1 = setA.intersection(setB)
setIntersection1.display()
print('B & A:')
setIntersection2 = setB.intersection(setA)
setIntersection2.display()
print('A - B:')
setDifference1 = setA.difference(setB)
setDifference1.display()
print('B - A:')
setDifference2 = setB.difference(setA)
setDifference2.display()
print('A ^ B:')
setSymDifference1 = setA.symDifference(setB)
setSymDifference1.display()
print('B ^ A:')
setSymDifference2 = setB.symDifference(setA)
setSymDifference2.display()

set3 = SparseSet(5, 5)
set3.insert(3)
set4 = SparseSet(10, 10)
set4.insert(4)
set3.isSubset(set4)

cardinality = [10, 100, 1000, 10000]

print('***')
print('Search Time Testing')
print('test11: search element that is in a set (set cardinality is 10)')
test11 = timeTestSearch(10,5)
print(f'test11 result: {'{:.20f}'.format(test11)}')
print('test12: search element that is NOT in a set (set cardinality is 10)')
test12 = timeTestSearch(10, 10)
print(f'test12 result: {'{:.20f}'.format(test12)}')
print('test21: search element that is in a set (set cardinality is 100)')
test21 = timeTestSearch(100, 74)
print(f'test21 result: {'{:.20f}'.format(test21)}')
print('test22: search element that is NOT in a set (set cardinality is 100)')
test22 = timeTestSearch(100, 100)
print(f'test22 result: {'{:.20f}'.format(test22)}')
print('test31: search element that is in a set (set cardinality is 1000)')
test31 = timeTestSearch(1000, 541)
print(f'test31 result: {'{:.20f}'.format(test31)}')
print('test32: search element that is NOT in a set (set cardinality is 1000)')
test32 = timeTestSearch(1000, 1000)
print(f'test32 result: {'{:.20f}'.format(test32)}')
print('test41: search element that is in a set (set cardinality is 10000)')
test41 = timeTestSearch(10000, 6542)
print(f'test41 result: {'{:.20f}'.format(test41)}')
print('test42: search element that is NOT in a set (set cardinality is 10000)')
test42 = timeTestSearch(10000, 10000)
print(f'test42 result: {'{:.20f}'.format(test42)}')

all_time1 = [test11, test21, test31, test41]

figure1 = plt.subplots()
plt.plot(all_time1, cardinality, marker='o', linestyle='None', color='r')
plt.yticks(cardinality)
plt.xticks(all_time1)
plt.xlabel('Час виконання операції (секунди)', fontsize=12)
plt.ylabel('Кількість елементів у множині', fontsize=12)
plt.title('Залежність часу виконання операції від кількості елементів (шуканий елемент є в множині)', fontsize=14)
plt.grid(True)
plt.show()

all_time2 = [test12, test22, test32, test42]
figure2 = plt.subplots()
plt.plot(all_time2, cardinality, marker='o', linestyle='None', color='r')
plt.yticks(cardinality)
plt.xticks(all_time2)
plt.xlabel('Час виконання операції (секунди)', fontsize=12)
plt.ylabel('Кількість елементів у множині', fontsize=12)
plt.title('Залежність часу виконання операції від кількості елементів (шуканого елементу немає в множині)', fontsize=14)
plt.grid(True)
plt.show()

print('***')
print('Union Time Testing')
print('Union Test1 - Cardinality is 10')
test1 = timeTestUnion(10)
print(test1)
print('Union Test2 - Cardinality is 100')
test2 = timeTestUnion(100)
print(test2)
print('Union Test3 - Cardinality is 1000')
test3 = timeTestUnion(1000)
print(test3)
print('Union Test4 - Cardinality is 10000')
test4 = timeTestUnion(10000)
print(test4)

all_time3 = [test1, test2, test3, test4]

figure3 = plt.subplots()
plt.plot(all_time3, cardinality, marker='o', linestyle='None', color='r')
plt.yticks(cardinality)
plt.xticks(all_time3)
plt.xlabel("Час виконання операції об'єднання множин (секунди)", fontsize=12)
plt.ylabel('Кількість елементів у множині', fontsize=12)
plt.title('Залежність часу виконання операції від кількості елементів', fontsize=14)
plt.grid(True)
plt.show()