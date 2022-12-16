# Computational Research Workflows Homework
## Doctoral Programme in Science and Engineering (DSSE)

## Practicalities

By email to [jack.hale@uni.lu](mailto:jack.hale@uni.lu), Subject: Computational
Research Workflows Homework.

Please ask questions on the [Etherpad](https://pad.carpentries.org/cwul2022).

*Deadline: Monday 19th December 2022 1800*

You must have attended the course and complete the homework to receive the ECTS
credits.

The email should contain a link to a GitHub repository with:

* a modified version of this file `README.md` file containing the specific
  commands that you used to complete the exercises. You do not have to include
  everything, just the key commands. I have left placeholders where these commands
  should go:

    ```
    # Add your commands here
    ```
* A `wallet.py` file that passes the unit tests.
* A `Dockerfile`.
* A working GitHub Actions file `.github/workflows/test.yml` that runs the unit
  tests inside the built image.

## High level overview

At the end of this homework, you will have a computational workflow consisting
of:

1. A git repository hosted at https://github.com.

1. A `Dockerfile` describing an environment containing `python` and the Python module
   `pytest`.

2. A Docker image built from the `Dockerfile` and uploaded to the Dockerhub.

3. A simple Python program describing a simple Wallet class and a set of unit tests.

4. A continuous integration setup using GitHub Actions.

For reference, you can use my notes that I used during the course
[here](https://github.com/jhale/computational-workflows/blob/master/README_instructor.md)
and the references listed at the bottom of the [main course
page](https://jhale.github.io/computational-workflows/).

## Setting up a git version control repository

1. Go to [GitHub](https://github.com). Click on the plus icon in the top right
   hand corner of the screen. Then click on New Repository.

2. Create a *public* repository called e.g.
   `jhale/computational-workflows-homework`.

3. Clone your repository. In a terminal run, e.g.:

     git clone git@github.com:jhale/computational-workflows-homework.git

   substituting with the correct location of your repository.

4. Copy this `README.md` text file to your new repository. `git add`, `git
   commit` and `git push` it to your repository.

## Dockerfile

1. Create a file `Dockerfile` in the repository containing the following text.

```
FROM ubuntu:21.04

RUN apt-get -y update && \
    apt-get install -y python3-minimal python3-ipython python3-pytest python3-numpy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```

2. `git add` and `git push` the file `Dockerfile` to the repository.

```
$ git add Dockerfile

$ git commit -m "init"

$ git push
```

## Build and push Docker image

1. `docker build`, `docker login` and `docker push` the image described by the
   `Dockerfile` to the Dockerhub. Tag your Docker image
   `<yourdockerhubusername>/computational-workflows`.

```
$ docker build .

$ docker login

$ docker tag 3010a4c7ce13 wang422003/computational-workflows

$ docker image push wang422003/computational-workflows
```

## Run a container, and share in files from the host.

1. `docker run` the image. Use the `-v` flag to share the root of the git
   repository to `/root/shared` inside the container. Use the `-ti` flag to get
   an interactive prompt inside the running container.

```
$ docker run -ti -v "$(pwd):/shared" wang422003/computational-workflows
```

## Setup a simple Python test suite

1. In a terminal running on the host (outside the container), copy across the
   files ``wallet.py`` and
   ``test_wallet.py`` to the root of your homework
   repository.  ``git add``, ``git commit`` and ``git push`` them.

```
$ cp ~/Documents/computational-workflows-homework-master/*.py ~/Documents/computational-workflows-homework/

$ git add --all

$ git commit -m "add .py files"

$ git push
```

2. Start a Docker container using your image and share your repository into a
   directory `/root/shared` into the container.

```
$ docker run -ti -v "$(pwd):/shared" wang422003/computational-workflows
```

3. Run the tests inside the container by going to `/root/shared` and running the
   command `py.test-3`. The tests should fail.

3. In a terminal on the host modify ``wallet.py`` until the tests in
   ``test_wallet.py`` all pass.

4. ``git add``, ``git commit`` and ``git push`` the working ``wallet.py`` file.

## GitHub Actions for Continuous Integration

1. Using the example in the class notes make a `.github/workflows/test.yml`
   file that checks out your repository and runs the unit tests inside the
   Docker image that you pushed to the DockerHub.

3. Push the `.github/workflows/test.yml` file to GitHub. Check that you get the
   green tick showing that your tests pass.
