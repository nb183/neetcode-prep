class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list) # list of (time, tweetId)
        self.follows = defaultdict(set) # set of followeeId
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1   

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        for tweet in self.tweets[userId]:
            heapq.heappush(heap, tweet)
        following = [id for id in self.follows[userId]]

        for uId in following:
            for tweet in self.tweets[uId]:
                heapq.heappush(heap, tweet)
        
        ans = []
        while len(ans) < 10 and heap:
            item = heapq.heappop(heap)
            ans.append(item[1])
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
