from locust import HttpUser, constant, task, SequentialTaskSet
import random


class TaskList(SequentialTaskSet):

    @task
    def get_users(self):
        res = self.client.get("api/users?page=2")
        print(res.text)
        print(res.status_code)
        # print(res.headers)

    @task
    def create_user(self):
        res = self.client.post("api/users", data='''{
        "name": "morpheus",
        "job": "leader"
    }''')
        print(res.text)
        print(res.status_code)
        # print(res.headers)

    @task
    def list_request(self):
        res = self.client.get("api/unknown")
        print(res.text)
        print(res.status_code)

    @task
    def get_random_user(self):
        user_id = random.randint(1, 12)
        random_id_url = "api/users/" + str(user_id)
        res = self.client.get(random_id_url)
        print(res.text)
        print(res.status_code)


class MyRequest(HttpUser):

    host = "https://reqres.in/"
    tasks = [TaskList]
    wait_time = constant(1)



