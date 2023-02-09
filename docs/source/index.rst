.. mozio documentation master file, created by
   sphinx-quickstart on Wed Dec 14 15:07:30 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Alessandro Baccini's Convious Test Task documentation!
=================================

Contents
""""""""

.. toctree::
   :maxdepth: 2

   install_locally
   API

Repo
""""
https://github.com/beikeni/convious

Brief
"""""

**Prompt:**

Implement voting REST API for choosing where to go to lunch. Imagine
that this API will be consumed by a front-end developer to create UI
on top of it. Approach this task as you would approach a real
assignment when you are at work.

Basic business rules/requirements:
1. Everyone can add/remove/update restaurants

2. Every user gets X (hardcoded, but "configurable") votes per
day. Each vote has a "weight". First user vote on the same
restaurant counts as 1, second as 0.5, 3rd and all subsequent
votes as 0.25.

2.1. If a voting result is the same on multiple restaurants, the
winner is the one who got more distinct users to vote on it.

3. Every day vote amounts are reset. Unused previous day votes are
lost.

4. Show the history of selected restaurants per time period. For
example, the front-end should be able to query which restaurant
won the vote on a specific day.

5. Do not forget that frontend dev will need a way to show which
restaurants users can vote on and which restaurant is a winner

6. Readme on how to use the API, launch the project, etc.

**Technologies:**

Select what best suits you. Since we use Python with Django, it is
preferred. However, feel free to choose other languages/frameworks.

**Bonus points (not mandatory):**
- Wrapping the app in Docker
- Deploying the API somewhere (for example, Heroku)

Notes
"""""

- This project is deployed at https://convious.spookykiwi.com/api/v1/ via **AWS Route53** and a 1gb Ubuntu instance from Vultr.
- The deployment is managed via a GitHub Actions pipeline that **tests, builds and deploys** the application each time changes are pushed to the main branch.
- The build stage is performed with **Docker** and the application is served with **Nginx**.
- The datatabase is a **PostgreSQL** instance running in a Docker container.
- The content comes pre-loaded with 10 users, 10 restaurants and 5 votes for each user for every day from the 1st Jan 2023 up to the 8th Feb.

 server due to the fact that the application is running on a ``t2.micro`` EC2 instance. On my laptop the response time is consistently in the 0.3 ~ 0.4 seconds range.