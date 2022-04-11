
# 클래스 선언
class Queue:

    # 초기 설정, 스택으로 사용할 리스트 선언
    def __init__(self):
        self.queue = []

    # In 함수 / insert 함수 List의 Insert 함수 이용
    def insert(self, data):
        self.queue.insert(0, data)

    # Out 함수 / Remove 함수, List의 pop함수 이용
    def remove(self):
        if len(self.queue) <= 0 :
            return ("No Data in Stack")
        else :
            return self.queue.pop()



ExStack = Queue()
ExStack.insert("A")
ExStack.insert("B")
ExStack.insert("C")
ExStack.insert("D")

ExStack.remove()
ExStack.remove()
print(ExStack.queue)