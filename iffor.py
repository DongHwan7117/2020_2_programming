class Pizza_store():
    def __init__(self,a):

        self.__store_name = a
        self.__pizza_list=['슈퍼슈프림','콤비네이션','불고기']


    def confirm(self, a):
        for i in range(len(self.__pizza_list)):
            if self.__pizza_list[i]==a:
                print('Yes')
                return 0

        print('No')


            
myshape= Pizza_store("pizza school")
myshape.confirm('슈퍼슈프f림')