class Homework:
    def __init__(self, description="", completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        completed_str = ""
        if self.completed == True:
            completed_str = " DONE!"
        return self.description + completed_str
    
class HomeworkList:
    def __init__(self, name):
        self.name = name
        self.__homeworklist = []

    def addHomework(self, homework):
        self.__homeworklist.append(homework)

    def getHomework(self, number):
        index = number - 1
        homework = self.__homeworklist[index]
        return homework
    
    def removeHomework(self, homework):
        self.__homeworklist.remove(homework)

    def getCount(self):
        return len(self.__homeworklist)
    
    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        if self.__index >= len(self.__homeworklist)-1:
            raise StopIteration()
        self.__index += 1
        homework = self.__homeworklist[self.__index]
        return homework
    
    def __str__(self):
        homeworklist_str = ""
        for homework in self.__homeworklist:
            homeworklist_str += str(homework) + " | "
            homeworklist_str = homeworklist_str[:-3]
            return homeworklist_str