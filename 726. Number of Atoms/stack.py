"""
Stack.
Convert input string into a better format. 
For each element, get the count. For each group of elements bounded by () get its count.
If at any point, count is 1 then add that 1.
So Mg(OH)2 becomes ["Mg", 1, "(", "O" , 1, "H", 1, ")", 2]. So for everything, we have a count, except for open brackets.
Now use a stack to push all elements till the top of stack is a closing bracket.
When we encounter a ), pop once and then for keep popping till we hit a (.
For all elements popped, if its an int, multiply its value with current element.
If its an element, simply add to list.
Then append this list in reverse back to the stack.
Once done, we will have a stack with 2*n number of elements where n is the number of elements as they appeared.
This does not mean uniques, if O appeared 3 times, then it will be in 3 separate spots.
Iterate through the stack by jumping 2 at a time. For each pair, update the count.
Sort the keys of the counter and create the result string.

O(nlogn) time for sorting. Creating intermediate input will take n time to go over all elements once. For stack ops we will push and pop an element to the stack at most once each.
O(n) space used by intermediate array and stack.
"""

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        # form a list of the input formula by separating elements and their counts including 1 and include brackets
        form = []
        ## <97 is a uppercase
        element = ""
        count = ""
        for c in formula:
            if c == '(' or c == ')':
                if len(element) > 0:
                    form.append(element)
                if len(count) == 0:
                    count = "1"
                if form and form[-1] != '(':
                    form.append(int(count))
                form.append(c)
                element = ""
                count = ""
            elif c.isnumeric():
                count += c
            elif ord(c) >= 97:
                element += c
            else:
                if len(element) > 0:
                    form.append(element)
                    if len(count) == 0:
                        count = "1"
                    form.append(int(count))
                else:
                    if form and form[-1] == ')':
                        if len(count) == 0:
                            count = "1"
                        form.append(int(count))
                element = c
                count = ""

        if len(element) > 0:
            form.append(element)
        if len(count) == 0:
            count = "1"
        form.append(int(count))

        # use stack to form the final counts by counting from innermost bracket
        stack = []
        for c in form:
            if stack and stack[-1] == ")":
                stack.pop()
                tmp = []
                while stack[-1] != '(':
                    top = stack.pop()
                    if type(top) == int:
                        top *= c
                    tmp.append(top)
                # pop again to remove '(' and add the tmp array in rev
                stack.pop()
                for i in range(len(tmp)-1, -1, -1):
                    stack.append(tmp[i])
            else:
                stack.append(c)
                
        # get counts
        counts = collections.defaultdict(int)
        for i in range(0, len(stack), 2):
            counts[stack[i]] += stack[i+1]
        
        res = ""
        for e in sorted(counts.keys()):
            if counts[e] == 1:
                res += e
            else:
                res += e
                res += str(counts[e])

        return res
