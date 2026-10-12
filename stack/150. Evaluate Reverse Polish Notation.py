''' https://leetcode.com/problems/evaluate-reverse-polish-notation/ '''
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        expression = {'+','-','*','/'}
        for i in tokens:
            if i not in expression:
                stack.append(i)
            elif i in expression:
                stack_1 = int(stack.pop())
                stack_2 = int(stack.pop())
                if i == '+':
                    stack.append(stack_1 + stack_2)
                elif i == '-':
                    stack.append(stack_2 - stack_1)
                elif i == '*':
                    stack.append(stack_1 * stack_2)
                else:
                    stack.append(int(stack_2 / stack_1))
                
        return int(stack[-1])
