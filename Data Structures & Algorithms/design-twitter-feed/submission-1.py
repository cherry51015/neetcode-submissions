class Twitter:

    def __init__(self):
        self.time=0
        self.tweets=defaultdict(list)
        self.following=defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if self.tweets[user]:
                idx=len(self.tweets[user])-1
                time,tweet=self.tweets[user][idx]
                heapq.heappush(heap,(-time,tweet,user,idx))
        while heap and len(res)<10:
            ntime,tweet,u,idx=heapq.heappop(heap)
            res.append(tweet)
            if idx>0:
                idx-=1
                time,tweet=self.tweets[u][idx]
                heapq.heappush(heap,(-time,tweet,u,idx))
        return res




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId!=followerId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
