import pytest
from mystructures.linkedlist.circularlinkedlist.CircularLinkedList import CircularLinkedList, Node

@pytest.fixture
def cll():
    return CircularLinkedList()

def test_append(cll):
    cll.append(1)
    assert cll.root.data == 1
    assert cll.root.next == cll.root

    cll.append(2)
    assert cll.root.next.data == 2
    assert cll.root.next.next == cll.root

def test_find_one(cll):
    cll.append(1)
    cll.append(2)
    cll.append(3)
    
    node, index = cll.find_one(2)
    assert node.data == 2
    assert index == 1

    with pytest.raises(StopIteration):
        cll.find_one(4)

def test_getitem(cll):
    cll.append(1)
    cll.append(2)
    cll.append(3)

    assert cll[0].data == 1
    assert cll[1].data == 2
    assert cll[2].data == 3
    assert cll[3].data == 1  # Circular behavio

def test_iteration(cll):
    cll.append(1)
    cll.append(2)
    cll.append(3)

    nodes = [node.data for node in cll]
    print('nodes ----------->' + str(nodes))
    assert nodes == [1, 2, 3]

def test_repr(cll):
    cll.append(1)
    cll.append(2)
    cll.append(3)

    assert repr(cll) == "Circular['1', '2', '3']"
