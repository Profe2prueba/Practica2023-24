class misTests:
    def ejemplo(self):
        print ("running ejemplo")
        assert (self.sumValues(5,3)==8)

    def sumValues(self,a, b):
        return a + b


obj=misTests()
obj.ejemplo()

