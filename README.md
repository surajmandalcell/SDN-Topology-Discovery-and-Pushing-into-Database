### Topology Discovery and Monitoring

Todo:

- [X] : Make presentation for the project
- [X] : Make sure topology is runnable
- [X] : Make sure controller is runnable
- [X] : Make sure data can be logged
- [X] : Make sure data can be sent to database
- [ ] : ~~Make sure data can be visualized~~
- [X] : Finish the project

---

#### Steps to run the project:

python binary which the controller and topology uses will be printed at start of the controller, usually it is `/usr/bin/python3`.

Install dependencies:

```
/usr/bin/python3 -m pip install requirements.txt
```

Run the controller(if it stops, run it again asap after running topology):

```
ryu-manager controller.py
```

To run ring topology:

```
sudo ring.py
```

To run star topology:

```
sudo star.py
```

#### Project Members:

- Suraj Mandal
- Lakhwinder Singh
- Priyanka
- Saurav Singh
