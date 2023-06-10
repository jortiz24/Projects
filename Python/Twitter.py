###I guess this is a twitter simulation???? Such a stupid leetcode problem

class Twitter:

    def __init__(self):

        self.followList = {}
        self.allTweets = {}

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followList:
            self.followList[userId] = []

        self.allTweets[tweetId] = userId 

    def getNewsFeed(self, userId: int) -> List[int]:
        
        feed = []

        tweets = dict(reversed((self.allTweets).items()))

        for x in tweets:
            print(tweets)


            if (tweets[x]) in self.followList[userId] or tweets[x] == userId:
                feed.append(x)

            if len(feed) == 10:
                return feed
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.followList:
            self.followList[followerId] = [followeeId]
        else:
            self.followList[followerId].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.followList:
            if followeeId in self.followList[followerId]:
                (self.followList[followerId]).remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
