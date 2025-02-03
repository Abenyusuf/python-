from Deque import Deque


def main():
    deque = Deque()

    # Testing push_front and push_back
    deque.push_front(21)
    deque.push_back(32)
    deque.push_front(43)
    deque.push_back(54)

    print("Deque after push operations:", end=" ")
    while not deque.is_empty():
        print(deque.pop_front(), end=" ")
    print()

    # Testing pop_front and pop_back
    deque.push_front(31)
    deque.push_back(42)
    deque.push_front(53)
    deque.push_back(64)

    print("Deque after pop operations:", end=" ")
    while not deque.is_empty():
        print(deque.pop_front(), end=" ")
    print()


if __name__ == "__main__":
    main()
