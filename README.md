<h1>Film Wharf Server/API</h1>

  This api server data of movies available for free on the web, here reducing the hazzle of surf the net for free movies
  <h3>How to Use</h3>
   <p>NB: this project is opened for contributions and update</p>

   <h3>To run locally</h3>
   Run to clone it om your PC
   
        git clone 'https://github.com/emekadefirst/filmwharf-server-api.git'
    
    
 <p>Change Directory (cd)</p>    

       cd filmwharf-server-api

 <p>Install requirements</p>

       pip install -r requirements.txt

 <p>Run server</p>

       ./manage.py runserver

 <h3>How to consume API endpoints</h3>

    /api (Movie List Endpoint)

      {
        "id": 1,
        "name": "John Wick: Chapter 4",
        "genre": "Action",
        "download_link": "https://123movies.info/movies/john-wick-kapitel-4.html",
        "source": "123movies",
        "release_date": "2023-12-05",
        "thumbnail_url": "https://th.bing.com/th?id=ODL.293687bcfe63039d213b38a1a6b89a89&w=135&h=201&c=10&rs=1&qlt=90&o=6&pid=13.1"
    },
    
   
      
