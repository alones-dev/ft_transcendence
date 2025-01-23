# ft_transcendence
ft_transcendence is the latest project from 42School. 
The aim of this project is to take us in a completely different direction from everything we've seen in the curriculum (C and C++ language) by getting us to create a fullstack website.
We used HTML, CSS (Bootstrap) and Javascript for the frontend, and Django (Python) for the backend. The database uses PostgreSQL. These languages were imposed on us to carry out the project.
The project was carried out in groups of 4.
The site implements a Pong game with different features that we could choose according to our desires.

### Here's a list of the features offered by our project:
- A local pong game
- User management including account creation, avatar management, information modification, presence system, friends list...
- Remote connection from API 42
- Remote pong to play online with two browsers
- A matchmaking system with the ability to create private rooms
- Game customization (paddle color, soccer field, etc.)
- Live chat (works with blocked users)
- A tournament system
- AI to challenge players locally
- Game statistics system
- Support for different languages (French, English and Spanish)

## Usage
**1. Clone the repository**
```
git clone https://github.com/alones-dev/ft_transcendence.git
```
**2. Create and fill .env file like .env.template**
```
cd ft_transcendence
mv .env.template .env
```
**3. Run the Docker container**
```
make start
```
**4. Enjoy !**


Run with localhost
```
https://localhost:8443/
```
or with your host ip (fill in .env)
```
https://10.11.12.13:8443/
```





