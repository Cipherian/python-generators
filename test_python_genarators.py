import pytest

import time

from main import LinkedList, Node, count_calls, time_it, sum_node_values2


@pytest.fixture
def linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    return ll


def test_linked_list_append(linked_list):
    linked_list.append(10)
    assert str(linked_list) == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> "


def test_len_linked_list(linked_list):
    assert len(linked_list) == 9


def test_len_empty_linked_list():
    linked_list = LinkedList()
    assert len(linked_list) == 0

def test_linked_list_equality(linked_list):
    linked_list2 = LinkedList()
    linked_list2.append(1)
    linked_list2.append(2)
    linked_list2.append(3)
    linked_list2.append(4)
    linked_list2.append(5)
    linked_list2.append(6)
    linked_list2.append(7)
    linked_list2.append(8)
    linked_list2.append(9)
    assert linked_list == linked_list2

def test_linked_list_equality_2():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    assert linked_list1 == linked_list2



def test_sum_node_values2_no_calls(linked_list):
    assert sum_node_values2.count == 0

def test_sum_node_values2_one_calls(linked_list):
    sum_node_values2(linked_list)
    assert sum_node_values2.count == 1

def test_sum_node_values2_multiple_calls(linked_list):
    sum_node_values2(linked_list)
    sum_node_values2(linked_list)
    sum_node_values2(linked_list)
    assert sum_node_values2.count == 4



def test_sum_node_values(linked_list):
    assert sum_node_values2(linked_list) == 45


def test_sum_node_values2(linked_list):
    linked_list.append(10)
    assert sum_node_values2(linked_list) == 55

def test_sum_node_values3():
    ll = LinkedList()
    assert sum_node_values2(ll) == 0


def test_sum_node_values2_with_empty_list():
    ll = LinkedList()
    assert sum_node_values2(ll) == 0


def test_sum_node_values2_with_single_node():
    ll = LinkedList()
    ll.append(10)
    assert sum_node_values2(ll) == 10


def test_time_it(linked_list, capsys):
    @time_it
    def test_func(ll):
        time.sleep(1)
        return sum_node_values2(ll)

    test_func(linked_list)
    captured = capsys.readouterr()
    assert "test_func took" in captured.out

