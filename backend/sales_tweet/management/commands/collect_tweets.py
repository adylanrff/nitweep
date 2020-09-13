from django.core.management.base import BaseCommand
from django.utils import timezone
from common.twitter import TwitterClient

class Command(BaseCommand):
    help = 'Collect sales tweets in Indonesia'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, help='Number of tweets that will be collected')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        client = TwitterClient()
        tweets = client.api.search(q="nitip jualan", result_type="recent", count=count)
        for tweet in tweets:
            print(tweet.__dict__.keys())
            print(tweet.user)
            print(tweet.text)
        