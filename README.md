# Chess Engines

This is a **Dockerized App** built with [**Django**](https://www.djangoproject.com/), a **_python_** web-framework. It is a _microservice_ that is used in [**playchess**](https://github.com/swarup-ranjan-mondal/playchess) app.

It is backend service which returns a good move from a chess engine based on the board position. Currently, it has only two chess engines, **_Stockfish_** and **_Komodo_**.

## Build

To build the image of this microservice app, run the following command:

```sh
$ docker build --platform linux/amd64 -t chess-engines .
```

## Usage

The **_Docker image_** of the app is available on [**Docker Hub**](https://hub.docker.com/) and can be seen from [**here**](https://hub.docker.com/r/swarupranjanmondal/chess-engines).

###### Note: To run a _Docker container_ from the app image, make sure [Docker](https://www.docker.com/) is installed. If it's not then download and install it from [here](https://docs.docker.com/get-docker/).

### Run

To start a container of the app on port `8080`, run the following command:

```sh
$ docker run -d -p 8080:8000 swarupranjanmondal/chess-engines
```

Now, open the browser and navigate to [`http://localhost:8080/`](http://localhost:8080/).

### Execute

On the browser, you would see a **Django REST framework** page. Now, select `Media type` as `application/json`. In the `Content` box paste the **JSON** given below and click `POST`.

```json
{
  "fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
  "engine_name": "stockfish"
}
```

Accordingly, based on the [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) (which represents board position of a chess game), you will get a **JSON** response from the engine whose name you've given in `engine_name` (here **_Stockfish_**). That response will look similar to the **JSON** response given below.

```json
{
  "success": true,
  "engine_move": {
    "e2e4": "e4"
  }
}
```
