#Class with kwargs
class Info:
    def show(self, **data):
        for k, v in data.items():
            print(k, "=", v)

obj = Info()
obj.show(name="Venkat", age=22)
