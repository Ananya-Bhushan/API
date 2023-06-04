#  REST API
This project is about building a REST API using Flask,MySQL and MVC (Model-View-Controller) pattern. The API provides movie information based on the provided movie ID.

Tech Stack
1.Flask
2.MySQL
3.Python

controller.py
This file represents the controller layer of MVC pattern.The controller layer is represented by MovieController used for retrieval logic of movie information based on the movie ID. 

model.py
This file represents all the user's data-retrieval related logic.It connects to mysql database retrieves movie information based on movie id.

view.py
This file represents all the records fetched within the model.Raw movie details obtained from the database is transformed into a standardized expected movie response dictionary.

API Definition

GET '/v1/movie/<int:movie_id>'
HOST: <hostname>:<port>
RESPONSE:
{
"id":<movie_id>,
"title":<movie_name>,
"poster_path":<image-url>,
"language":<movie-language>,
"overview":<movie_description>,
"release_date":<date>
}

OUTPUT
When movie_id is valid 

![image](https://github.com/Ananya-Bhushan/API/assets/85629090/23c1f656-34c9-4128-86a8-67bb5153eb3e)

  
When movie_id is invalid
 
![image](https://github.com/Ananya-Bhushan/API/assets/85629090/de9a4838-5906-439b-b348-1935f43a2251)





