import models


class Queue(models.Model):
    def __init__(self):
        self.list = []
        # TODO: add job object
        
    def add_job(self, job_obj):
        self.list.append(job_obj)