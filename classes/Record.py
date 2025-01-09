#Record
#this class is 'abstract' and should not be instantiated explicitly, rather only it's subclasses
#this class represents a record to be inserted in the NexLynk DMS database
class Record:
    def __init__(self, id):
        self.id = id
        self.version = 0
#end of class definition