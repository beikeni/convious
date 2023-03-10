.. convious documentation master file, created by
   sphinx-quickstart on Thu Feb 9 15:07:30 2023.

Welcome to my Convious Test Task documentation!
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

   **Basic business rules/requirements:**

   - Everyone can add/remove/update restaurants

   - Every user gets X (hardcoded, but "configurable") votes per day. Each vote has a "weight". First user vote on the same restaurant counts as 1, second as 0.5, 3rd and all subsequent votes as 0.25.

   - If a voting result is the same on multiple restaurants, the winner is the one who got more distinct users to vote on it.

   - Every day vote amounts are reset. Unused previous day votes are lost.

   - Show the history of selected restaurants per time period. For example, the front-end should be able to query which restaurant won the vote on a specific day.

   - Do not forget that frontend dev will need a way to show which restaurants users can vote on and which restaurant is a winner

   - Readme on how to use the API, launch the project, etc.

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
- Django Admin: convious.spookykiwi.com/admin // user: admin // pass: c0nvious
