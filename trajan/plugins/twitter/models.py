from trajan.lib import twitter
class Status(models.Model):
    tweet = models.CharField(max_length=250)
    twitter_id = models.BigIntegerField()
    created_at = models.CharField(max_length=200)
    location = models.ForeignKey(Location)
    
    def __unicode__(self):
        return self.tweet
    
    class Meta:
        ordering = ['-twitter_id']
    

def status_sync():
    from django.contrib.localflavor.us import us_states
    twitter_api = twitter.Api()
    try:
        statuses = twitter_api.GetUserTimeline("derekstegelman")
    except:
        pass
        return HttpResponse("ok", mimetype="text/plain")
    for tweets in statuses:
        try:
            get_status = Status.objects.get(twitter_id=tweets.id)
        except Status.DoesNotExist:
            new_tweet = Status(tweet=tweets.text)
            new_tweet.twitter_id = tweets.id
            new_tweet.created_at = tweets.created_at
            try:
                if tweets.place:
                    if tweets.place["place_type"] == "city":
                        loc = Location.objects.get(city=tweets.place["name"])
                    else:
                        loc = Location.objects.get(pk=1)
                else:
                    loc = Location.objects.get(pk=1)
            except Location.DoesNotExist:
                loc = Location(city=tweets.place["name"])
                import string
                loc.state = string.split(tweets.place["full_name"], ", ")[1]
                loc.country = tweets.place["country"]
                loc.save()

            new_tweet.location = loc
            new_tweet.save()