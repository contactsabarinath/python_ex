#import os
#os.chdir('C:\Python34\Sab\MapReduce')
#print(os.getcwd())

from mrjob.job import MRJob

class MRRatingCounter(MRJob):
    def mapper(self,key,line):
        (userid,movieid,rating,timestamp) = line.split('\t')
        yield rating,1
        
    def reducer(self,rating,occurence):
        yield rating,sum(occurence)
        

if __name__ == '__main__' :
    MRRatingCounter.run()
