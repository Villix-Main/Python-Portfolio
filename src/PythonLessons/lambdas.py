from functools import reduce

addFunc = lambda x, y: x + y
print(addFunc(5, 5))


strLenStripped = lambda str: len(str.strip())
print(strLenStripped("                    DM"))


def send_to_database(data, endFunc):
    print(f"Sending {data} to database...")
    print("Sent data to database")

    endFunc('passed')

name = ''
send_to_database("some stuff", lambda result: print(f"the result is {result}"))


points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# points2D_sorted = sorted(points2D, key=lambda x: x[1])
points2D_sorted = sorted(points2D, key=lambda x: sum(x))
print(points2D)
print(points2D_sorted)

nums = [1, 2, 3, 4, 5]
nums2 = map(lambda x: x*3, nums)
print(list(nums2))

moreNums = [x*4 for x in nums]
print(moreNums)


# moreNums = filter(lambda x: x%2==0, nums)
moreNums = [x for x in nums if x%2==0]
print(moreNums)

nums = [2, 2, 3, 3]
product_a = reduce(lambda x,y: x*y, nums)
print(product_a)
