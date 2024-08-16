class TextEditor:

    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def addText(self, text: str) -> None:
        for char in text:
            self.left_stack.append(char)

    def deleteText(self, k: int) -> int:
        count = min(k, len(self.left_stack))
        for _ in range(count):
            self.left_stack.pop()
        return count

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.left_stack))):
            self.right_stack.append(self.left_stack.pop())
        return ''.join(self.left_stack[-10:])
        

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.right_stack))):
            self.left_stack.append(self.right_stack.pop())
        return ''.join(self.left_stack[-10:])
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)