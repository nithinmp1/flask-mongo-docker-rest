# flask-mongo-docker-rest
Flask CRUD operation API where mongo db used as the database and dockerized application 


docker build -t pythonflask_web .

docker pull mongo

docker-compose up -d

docker exec -it my_mongo_db mongosh
show dbs
use users

db.accounts.insertOne({
    "username": "example_user",
    "email": "user@example.com",
    "age": 30
})

db.accounts.insertMany([
    {
        "username": "user1",
        "email": "user1@example.com",
        "age": 25
    },
    {
        "username": "user2",
        "email": "user2@example.com",
        "age": 30
    },
    {
        "username": "user3",
        "email": "user3@example.com",
        "age": 35
    }
])

db.accounts.find()


