class MinStack:

    def __init__(self):
        # 初始化一个列表作为栈。
        # 栈里存放的是元组：(当前值, 到当前为止的最小值)
        self.stack = []

    def push(self, val: int) -> None:
        # 如果栈是空的，那当前值就是目前的最小值
        if not self.stack:
            self.stack.append((val, val))
        else:
            # 如果栈里有东西，就看看新来的 val 和之前的最小值谁更小
            current_min = self.stack[-1][1]
            new_min = min(val, current_min)
            # 把值和新的最小值一起打包入栈
            self.stack.append((val, new_min))

    def pop(self) -> None:
        # 正常弹出栈顶元素即可
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        # 栈顶元素的第 0 个位置，就是真实的值
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        # 栈顶元素的第 1 个位置，就是记录的最小值
        if self.stack:
            return self.stack[-1][1]

