class Candidate:
    def __init__(self, name, skills):
        self.name = name
        self.skills = set(skills)

class Job:
    def __init__(self, title, req_skills):
        self.title = title
        self.req_skills = set(req_skills)

c = Candidate("Irfan", ["Python", "SQL"])
job = Job("Developer", ["Python", "SQL"])

scores = {"Irfan": 85}

if job.req_skills.issubset(c.skills) and scores["Irfan"] >= 70:
    print("Selected")
else:
    print("Rejected")