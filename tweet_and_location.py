# import
venue_path=open('/home/vivek/Desktop/Thesis/Four_Square/california_venues_venue.txt','r')
arr=[]
for line in venue_path:
    arr.append(line.lower())
sorted(arr)
print arr
file_path=open('/home/vivek/Desktop/Thesis/Four_Square/all_tweets_cali','r')
file_write=open('/home/vivek/Desktop/Thesis/Four_Square/tweet_venue_cali','w')
for file_line in file_path:
    tweet_words=file_line.lower().split(" ")
    for tweet_word in tweet_words:
        if tweet_word in arr:
            print file_line
            file_write.write(file_line+":"+tweet_word)
file_write.close()