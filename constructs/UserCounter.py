from mrjob.job import MRJob

class UserCounter(MRJob):
    def mapper(self,key,line):
        (userid,movie,rating,timestamp) = line.split('\t')
        yield userid,1
    def reducer(self,userid,occurence):
        yield userid,sum(occurence)

if __name__ == '__main__':
    UserCounter.run()