<h1 align="center">Telegram bot template</h1>

## 🐍 This template is used to create telegram bots using AIOgram 

📚 Structure
```
├── Dockerfile
├── bot.py
├── docker-compose.yml
├── requirements.txt
└── tgbot
    ├── config.py
    ├── filters
    ├── handlers
    ├── keyboards
    ├── middlewares
    ├── misc
    ├── models
    └── services
```
- The `tgbot` package is the root package for the bot, and it contains sub-packages for filters, handlers, and middlewares.

- The `filters` package contains classes that define custom filters for the bot's message handlers.

- The `handlers` package contains classes that define the bot's message handlers, which specify the actions to take in response to incoming messages.

- The `middlewares` package contains classes that define custom middlewares for the bot's dispatcher, which can be used to perform additional processing on incoming messages.

### `bot.py`
The bot.py script is the entry point for the template Telegram bot. It performs the following steps to start and run the bot:

1. Set up logging: The z
`logging` module is imported and configured to log messages to the console.
2. Load the configuration: The `load_config()` function from the `tgbot.config` module is called to read the configuration from the environment.
3. Set up the storage: Depending on the `use_redis` flag in the configuration, either a `MemoryStorage` or a `RedisStorage2` instance is created to store the bot's state.
4. Create the bot and the dispatcher: A `Bot` instance is created using the bot token from the configuration, and a `Dispatcher` instance is created using the `Bot` instance and the `storage`.
5. Register middlewares, filters, and handlers: The `register_all_middlewares()`, `register_all_filters()`, and `register_all_handlers()` functions are called to register all the middlewares, filters, and handlers that are used by the bot.
6. Start the polling loop: The `start_polling()` method of the Dispatcher instance is called to start the main event loop for the bot. This method listens for incoming messages and routes them to the appropriate handler.

### `tg_bot/config`
- The `config.py` script defines a data structure for storing configuration options for the bot, such as the Telegram bot token, database credentials, and other parameters.
- The `config.py` script also includes a `load_config` function for loading the configuration from a file using the environs library.
- The `config.py` file defines a Config class, which is used to store configuration settings for the bot.
- The `Config` class has three nested classes, `TgBot`, `DbConfig`, and `Miscellaneous`, which are used to store configuration settings for the Telegram bot, the database, and miscellaneous settings, respectively.
- The `load_config` function is used to load the configuration settings from an environment file and create a `Config` object.

### `tg_bot/handlers/echo.py`
The `echo.py` file defines a `register_echo` function, which is used to register an event handler for the `/echo` command. This event handler is responsible for repeating the text of the message back to the user. The `register_echo` function takes a `Dispatcher` object as its parameter, and it uses this object to register the `/echo` command handler.

### `docker-compose.yml`
- The `docker-compose.yml` file defines the services that are used by the application, as well as the networks and volumes that are needed by the application. The file begins by specifying the version of the Docker Compose file format that is being used.

- The `services` section of the file defines the containers that should be run as part of the application. In this example, there is only one service, called `bot`, which is based on the `tg_bot-image` Docker image. The container_name specifies the name that should be used for the container, and the build section specifies the location of the Dockerfile that should be used to build the image.

- The `working_dir` specifies the working directory that should be used by the container, and the volumes section specifies the files and directories that should be mounted into the container. In this case, the entire project directory is mounted into the container, which allows the application to access the files on the host machine.

- The `command `specifies the command that should be run when the container is started, and the restart setting specifies that the container should be automatically restarted if it exits.

- The `env_file` setting specifies the location of the `.env` file, which contains the configuration settings for the application.

- The `networks` section defines the networks that the container should be connected to. In this example, there is only one network, called `bot`, which is based on the bridge driver. This network allows the containers in the application to communicate with each other.

### `Dockerfile`
The Dockerfile defines the instructions for building the Docker image that is used by the bot service. The file begins by specifying the base image that should be used for the image, which in this case is python:3.9-buster. The ENV instruction sets the value of the BOT_NAME environment variable, which is used by the WORKDIR instruction to specify the working directory for the container.

The COPY instructions are used to copy the requirements.txt file and the entire project directory into the image. The RUN instruction is used to install the Python dependencies from the requirements.txt file. This allows the application to run in the container with all the necessary dependencies.
