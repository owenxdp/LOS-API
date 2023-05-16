## Getting Started

```sh
sudo apt-get update
```

Command to install python :

```sh
sudo apt install python3-pip
```


Command to install git to clone this repository :

```sh
sudo apt install git
```

Command to install git to clone this repository you can use your repository git url which you want to host :

```sh
sudo git clone https://github.com/smurfcoders/fastapi-hosting.git
```

Command to change location into the cloned folder you can use your repository name :

```sh
cd fastapi-hosting
```

Command to install all the requirements required for the project to run in our case we have created requirements.txt file you can also create your own requirements :

```sh
pip install -r requirements.txt
```

Command to run the API :

```sh
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```

After running go to AWS instance --> Security tab --> Edit inbound rules --> create rule --> Enable access from anywhere.<br>
Go to the public ip provided by the instance add :8000 in the end as our api is running at that particular port.


