# Senior Backend Developer Challenge

### Take-Home Assignment

## Description

With this exercise, we will evaluate your ability to develop a simple backend application that meets the requirements for an imaginary product we want to build.

Completing this should take you anywhere from a couple of hours to up to a day depending on your level of expertise, available time to focus, and level of detail you consider sufficient.

That said, if it is taking you more than a day, you are probably spending more effort than necessary in some details.
We expect that you submit your final work within one week of receiving the assignment, but please let us know if this is too short notice for you.

Please feel free to reach out and ask questions if you need any clarification.

## Details

### The Application

We are developing a simpler version of our core application. This application handles the information of our patients and the studies they have made.

## Requirements

As we said before, it can take you a couple of hours or a day.

-   Python 3.8
-   PEP-8 Coding Style
-   Good use of git (commits, pull requests, branches)
-   Use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages

1. Implement the CRUD for Patients (Needs testing)
2. Implement the CRUD for Studies (Needs testing)
3. Implement the listing view of Patients that displays their Studies (Needs testing)
4. Fix Github Actions workflow for pipeline to work.
7. Refactor the code
8. Ensure that all tests are passing.

## How to deliver

1. Clone this repo and share the link with us at the time to deliver (DO NOT FORK)
2. Add the next users to your private repo:
   1. @IvanDiazNoriega, @daniel2101, @mauarcet, @antoniotorres
3. Please document the repo and your code (using [docstring](https://www.python.org/dev/peps/pep-0257/)
5. On the README, write a summary of what else you could/would like to have done if you had more time.

---

### Setup

```
make build
make up
```

### Execute the tests

```
make test
```

### Create new migrations

```
make migrations
```

### Run migrations into db

```
make migrate
```

### Create new super-user.

```
make su
```

### Format the code

```
make format
```

## TODOs
