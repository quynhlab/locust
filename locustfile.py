from locust import task, between
from locust.contrib.fasthttp import FastHttpUser

class MyUser(FastHttpUser):
    wait_time = between(2, 5)

    @task
    def index(self):
        response = self.client.get("/")
