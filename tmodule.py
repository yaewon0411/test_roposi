import turtle as t

t.shape('turtle')

size = int(input('집의 크기는 얼마로 할까요? '))

for i in range(4):
    t.forward(size)
    t.right(90)

t.left(60)

for i in range(2):
    t.forward(size)
    t.right(120)

t.color('white')
t.goto(200,0)
t.color('black')


t.right(180)

for i in range(4):
    t.forward(size*2)
    t.right(90)

t.left(60)

for i in range(2):
    t.forward(size*2)
    t.right(120)
