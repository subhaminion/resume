from collections import namedtuple
from datetime import datetime


basicInfo = {
    "name": "\t\tSubham Bhattacharjee",
    "email": "\tsubham.bhattacharjee1@gmail.com",
    "phone": "\t+91-9046789016",
    "github": "\thttps://github.com/subhaminion",
    "linkedin": "\thttps://www.linkedin.com/in/subhaminion/",
    "twitter": "\thttps://twitter.com/subhaminion/"
}


def initInitials():
    for key, info in basicInfo.items():
        print(key.capitalize() + ": ", info)


class JobExp(object):

    def __repr__(self):
        return "{0} - {1}, {2}, {3}, {4}\n{5}\n{6}".format(
            self.started.strftime("%B %Y"),
            self.left if isinstance(self.left, str) else self.left.strftime("%B %Y"),
            self.company,
            self.location,
            self.title,
            "\n".join(self.description),
            "=" * 20
        )


# Experience
class AppKnox(JobExp):
    company = "AppKnox"
    location = "Bangalore, India"
    title = "Software Engineer"
    started = datetime(2017, 11, 1)
    left = "Current"
    description = [
        """
        - Maintaining the Backend part of the Scanners
        - Added major and minor features
        - Improved the existing API Scanner by adding SqlMap as a API Scanner
        - Restructured the existing Team Structure, Included Django Guardian for Object level permission
        - Restructured backend CRM for enterprise deployment
        - Integrated Zapier webhooks for automations works
        - Created Slack notifications for user and user scan flow
        """
    ]


class Freelancer(JobExp):
    company = "Freelance Web Developer"
    location = "Bangalore, India"
    title = "Freelance Web Developer"
    started = datetime(2017, 5, 1)
    left = "Current"
    description = [
        """
        - Enhancement of products based on client need by performing business process gap analysis
        - Data Enrichment(by attribute development and extraction) and Cleansing(Quality Check)
        - Integration of products using SOAP, REST, JSON (Healthcare, E-commerce, Telecom Customer Verification, etc)
        - Data Integration (ETL lifecycle) and building reports for various Geographic, Demographic, Census and Behavioral data
        - Requirement Analysis for various clients and showcasing various aspects of Data Quality Suite
        - Development of application in Python for verifying Contact Data using Google APIs
        - Data formatting and cleansing using various Python libraries
        """
    ]


class Rplanx(JobExp):
    company = "Rplanx Technology Pvt. Ltd"
    location = "Kolkata, India"
    title = "Web Application Developer"
    started = datetime(2016, 12, 1)
    left = datetime(2017, 5, 1)
    description = [
        """
        Working closely with client and coordinating with project manager to deliver product within stipulated time.
        Understanding clients requirement and implementing them with creativity.
        Collaborating with designer to bring out the best outcome.
        Worked on several projects from Front End development to Backend.
        As a startup I've also provided some of the major decisions in the project management.
        """
    ]

class DreamzTech(JobExp):
    company = "DreamzTech Solutions Pvt. Ltd"
    location = "Kolkata, India"
    title = "Web Application Developer"
    started = datetime(2016, 8, 1)
    left = datetime(2016, 11, 1)
    description = [
        """
        - Develop and Design a website from scratch
        - Collaborating with Team Leaders to bring out perfect outcome
        """
    ]

class Education(object):

    def __repr__(self):
        return "{0} - {1}, {2}, {3}, {4}\n{5}\n{6}".format(
            self.started.strftime("%B %Y"),
            self.left if isinstance(self.left, str) else self.left.strftime("%B %Y"),
            self.name,
            self.location,
            self.course,
            "\n".join(self.description),
            "=" * 20
        )

# Education
class Master(Education):
    name = "St. Xavier's College"
    location = "Kolkata, India"
    course = "Masters in Computer Science"
    started = datetime(2016, 8, 1)
    left = datetime(2016, 9, 1)
    description = [
        """
        Dropped Out
        """,
    ]

class Bsc(Education):
    name = "Malda College"
    location = "Malda, India"
    course = "Applied Computer Science BSc"
    started = datetime(2013, 8, 1)
    left = datetime(2016, 5, 1)
    description = [
        """
        I studied Computer Science at the Malda College, Malda,
        where I got hands on experience and exposure to the industry in areas
        such as C programming, C++ programming,Core Java, SQL, Algorithms, Data Structures,
        Database Design, Computer Networks, Operating Systems.
        """,
    ]


Project = namedtuple("Project", "name description")


if __name__ == "__main__":
    experience = [AppKnox(), Freelancer(), Rplanx(), DreamzTech()]
    initInitials()

    print("Experience:")
    for exp in experience:
        print(exp)

    print("Education:")
    eduction = [Master(), Bsc()]
    for edu in eduction:
        print(edu)

    print("Projects & Interests:")
    projects = [
        Project("Multi User MarkDown Editor", "Multi User Real Time Markdown Editor where several user can collaborate on a single editor with unique URL"),
        Project("InstaLoad", "Downloads High Quality Instagram Images")
    ]
    for pro in projects:
        print(pro)

    print("Languages: Python, JavaScript , PHP")
    print("Technologies: Git, AWS, Heroku, Redis, Django, Flask, PostgresSQL")
    print("Familiar With: Web Services(REST API), HTML, CSS, Responsive Web Design, Cross Browser Compatibility, JQuery, AJAX, Memcached, Celery, Selenium, NumPy, NodeJs, ExpressJs, AngularJs")
    print("Summary: Constant learner. Excited to work on open-source.")