from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")