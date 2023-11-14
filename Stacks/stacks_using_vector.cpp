#include <iostream>
#include <vector>
#include <string>
class StackUsingVector
{
public:
    std::vector<int> stack;

    void push(int num)
    {
        stack.insert(stack.begin(), num);
    }

    int pop()
    {
        int elem = stack.at(0);
        stack.erase(stack.begin());
        return elem;
    }

    int peek()
    {
        return stack.at(0);
    }

    bool isEmpty()
    {
        if (stack.empty())
        {
            return true;
        }
        return false;
    }

    int getLength()
    {
        return stack.size();
    }

    void printStack()
    {
        for (unsigned int i = 0; i < getLength(); i++)
        {
            std::string separator = i == getLength() - 1 ? "." : "->";
            std::cout << stack.at(i) << separator;
        }
        std::cout << std::endl;
    }
};

int main()
{
    StackUsingVector st = StackUsingVector();
    st.push(5);
    st.push(7);
    st.push(9);
    st.printStack();
    st.pop();
    st.printStack();
    st.push(9);
    std::cout << st.peek() << std::endl;
    std::cout << st.isEmpty() << std::endl;

    return 0;
}