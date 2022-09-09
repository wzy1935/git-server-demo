# Git Server Demo

This is a tiny git server demo written in python. It supports `git clone` and `git pull` with authentication. It is implemented through git dumb http protocol and Basic authentication. For more technical details, please refer to git doc [here](https://www.git-scm.com/docs/http-protocol).



## Instructions

- Clone this project.
- run `pip install flask flask_httpauth` .
- run `python server.py`.

Now you can access to every repository in the `repos` folder. Use the following URL as the remote address: `http://<user_name>:<password>@localhost:8080/<repo_name>.git`

If you need to add more repository for test, please run `git update-server-info` in each repository. For example, let's add this repository itself into `repos`.  

- run `cd repos`
- run `git clone https://github.com/wzy1935/git-server-demo.git`
- run `cd git-server-demo ` 
- run `git update-server-info`

Now you can access to this repo on your own server at `http://user1:123456@localhost:8080/git-server-demo.git`.



## Notice

This repository is only for demonstration of git protocol. The code is unstable and can not be used in any formal project.
