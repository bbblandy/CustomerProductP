from customerList import *

def testConstructor():
    cList = Customer()
    print(f"Testing constructor.  Expect empty list. {cList}")
    print(f"Expect count property to be 0. {cList.count}")
    print(f"Expect len function to be 0. {len(cList)}")


def testAppend():
    cList = Customer()
    c1 = Customer('1', "Bob", "James")
    c2 = Customer('2', "John", "Johnson")
    cList.append(c1)
    cList.append(c2)
    print(f"Testing append.  Expect list with 2 customers. {cList}")
    print(f"Expect count property to be 2. {cList.count}")
    print(f"Expect len function to be 2. {len(cList)}")


def createList():
    cList = Customer()
    c1 = Customer('1', "Bob", "James")
    c2 = Customer('2', "John", "Johnson")
    c3 = Customer("3", "Jane", "Joe")
    cList.append(c1)
    cList.append(c2)
    cList.append(c3)
    return cList


def testPop():
    cList = createList()
    print(f"Testing pop.  Before pop expect list with 3 customers. {cList}")
    print(f"Expect count property to be 3. {cList.count}")
    print(f"Expect len function to be 3. {len(cList)}")
    c3 = cList.pop()
    print(f"After pop with no parameter.  Expect first 2 customers. {cList}")
    print(f"Expect popped customer to be Jane. {c3}")
    print(f"Expect count property to be 2. {cList.count}")
    print(f"Expect len function to be 2. {len(cList)}")
    c1 = cList.pop(0)
    print(f"After pop with 0 parameter.  Expect just John. {cList}")
    print(f"Expect popped customer to be John. {c1}")
    print(f"Expect count property to be 1. {cList.count}")
    print(f"Expect len function to be 1. {len(cList)}")


def testFind():
    cList = createList()
    print(f"Testing find.  Current list with 3 customers. {cList}")
    index = cList.find("2")
    print(f"Called find with 2 as parameter.  Expect index to be 1. {index}")
    c2 = Customer('2', "John", "Johnson")
    # this will return -1 if __eq__ is not defined on the product class
    index = cList.find(c2)
    print(f"Called find with customer object 2 as parameter.  Expect index to be 1. {index}")
    index = cList.find("4")
    print(f"Called find with 4 as parameter.  Expect index to be -1. {index}")
    c4 = Customer("4", "Joan", "James")
    index = cList.find(c4)
    print(f"Called find with customer object 4 as parameter.  Expect index to be -1. {index}")


def testRemove():
    cList = createList()
    c2 = Customer('2', "John", "Johnson")
    print(f"Testing find.  Current list with 3 customers. {cList}")
    cList.remove(c2)
    print(f"Called remove with Customer object p102 as parameter.  Expect list to now have 2 customers. {cList}")
    c4 = Customer("4", "Joan", "James")
    try:
        cList.remove(c4)
        print(f"Called remove with Customer object 4 as parameter.  An exception should have been thrown but was not.")
    except ValueError:
        print(f"Called remove with customer object 4 as parameter.  An exception was expected and was thrown")
        print(f"Expect list to still have 2 customers. {cList}")


def testClear():
    cList = createList()
    print(f"Testing clear.  Current list with 3 customers. {cList}")
    cList.clear()
    print(f"After the call to clear.  Expect list to be empty. {cList}")


def testGetItem():
    cList = createList()
    print(f"Testing list access by index.  Current list with 3 customers. {cList}")
    c = cList[1]
    print(f"Element at index 1.  Expect 2. {c}")
    c = cList["3"]
    print(f"Element with key of 3.  Expect 3. {c}")
    try:
        c = cList[2.5]
    except TypeError:
        print(f"Used [] with float as index.  An exception was expected and was thrown")


def testSetItem():
    cList = createList()
    print(f"Testing changing a list element by index.  Current list with 3 customers. {cList}")
    c4 = Customer("4", "Joan", "James")
    cList[2] = c4
    print(f"Set element at index 2 to 4.  4 should be at the end of the list. {cList}")
    try:
        cList["4"] = c4
    except TypeError:
        print(f"Used [] with string as index.  An exception was expected and was thrown")
    try:
        cList[1] = "cat"
    except TypeError:
        print(f"Used [] with string element rather than a product.  An exception was expected and was thrown")


def testIn():
    cList = createList()
    print(f"Testing in.  Current list with 3 customers. {cList}")
    c2 = Customer('2', "John", "Johnson")
    c4 = Customer("4", "Joan", "James")
    print(f"Is 2 in the list?  Expect true  {c2 in cList}")
    print(f"Is 4 in the list?  Expect false  {c4 in cList}")


def testForLoop():
    cList = createList()
    print(f"Testing for loop.  Current list with 3 customers. {cList}")
    print(f"Iterating through the list with for in.  Expect 3 individual customers")
    for c in cList:
        print(c)


def testAdd():
    cList = createList()
    cList2 = createList()
    cListCombined = cList + cList2
    print(f"Testing adding 2 customer lists.  Expect list with 6 customers. {cListCombined}")