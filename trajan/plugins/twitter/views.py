from trajan.lib import twitter

def twitter_feed(request):
    #twitter_api = twitter.Api()
    #context = {'statuses': twitter_api.GetUserTimeline("derekstegelman")}
    context = {'statuses': Status.objects.all()[:20]}
    return render(request, 'blog/status.html', context)
    
def twitter_sync(request):
    status_sync()
    return redirect("twitter_feed")