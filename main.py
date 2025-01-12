# class creaction
class myclass:

  __privateVar = 27;

  def __privmeth(self):
    print("I'm inside class myclass")

  def hello(self):
    print("private variable value: ",myclass.__privateVar)

foo = myclass()
foo.hello()
foo.__privmeth