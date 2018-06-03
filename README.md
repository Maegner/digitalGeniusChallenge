# Digital Genius Python Challenge

## Dependencies
Dependency |
------------- |
pytest |
flask | 
nltk |
numpy |

## Getting started

## Build the docker image
```sh
$ cd app ;
$ docker build -t chat_bot .
```
## Run the docker image
```sh
$ cd app ;
$ docker run -d -p 5000:5000 chat_bot
```
Now you can access the application via the URL http://localhost:5000

## Usage

All of the following are examples of the body of the following HTTP 1.1 request:

POST http://localhost:5000/help
with the header : Content-type : application/json

### Body Format
```json
{
    "id" : "model_id",
    "request" : "help_request"
}
```

### The available models are:
    * 26444047-56f8-43e5-8e25-b70b8e5367f1
    * f59da1c7-c060-4aec-b3a0-dd7453a4c541


### Response format

The response comes in JSON, with the following format

{
    "response": "response from model"
}

### Example

#### Request
    curl: POST http://localhost:5000/help
    header : Content-type : application/json
    body : 
```json
    {
    "id": "26444047-56f8-43e5-8e25-b70b8e5367f1",
    "request": "Hello my name is Siri, can you help me?"
    }
```
#### Response

```json
    {
    "response": "Thanks for getting in touch Siri! I will try my best to help"
    }
```

## Known Problems

The Model used to find the names in a string of text has some problems with the following request format:
"Hi <NAME> here, can you give me a hand?", sometimes the model will not be able to find the name, for example, if
<NAME> == 'Siri' no name is found but if <NAME> == 'Seydou Abioye' or <NAME> == 'John' it will.

## Pressisting the models

Both models are persisted in a pickle that contains a hash table that maps model_id to the model instance, this pickle is used to simulate an access to a database.

## Author

Francisco Aguiar  : franciscomaguiar@gmail.com
