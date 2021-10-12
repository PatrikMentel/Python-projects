class User():
    rank = -8
    progress = 0
    
    def inc_progress(self, rank):
        _ranks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        n = 0
        d = _ranks.index(rank) - _ranks.index(self.rank)
        if rank == self.rank and self.rank != 8: self.progress += 3
        if _ranks.index(rank) == _ranks.index(self.rank)-1: self.progress += 1
        if rank > self.rank: 
            self.progress += 10*d*d
            while self.progress >= 100:
                self.progress -= 100
                n += 1
            if n > len(_ranks) - _ranks.index(self.rank): 
                self.rank = 8
                self.progress = 0
            else: self.rank = _ranks[_ranks.index(self.rank)+n]
            

user = User()
user.inc_progress(8)
print(user.rank)
print(user.progress)