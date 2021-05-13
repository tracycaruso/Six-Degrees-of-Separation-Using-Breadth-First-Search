<img width="1229" alt="Screen Shot 2021-05-13 at 3 28 14 PM" src="https://user-images.githubusercontent.com/6024941/118190104-df573980-b3ff-11eb-8fdc-4d52ccf2b322.png">


This project is the first assignment from [Harvard’s CS50 Introduction to AI class](https://cs50.harvard.edu/ai/2020/projects/0/). 

Most of us have heard of the Six Degrees of Separation. The idea is that individuals are six or fewer social connections away from each other. Often Kevin Bacon is at the root of this explanation. You may have played a fun party game where you connect any actor to Kevin Bacon with six or fewer other actors via the movies in which they have collaborated. In this first challenge from Harvard, they want you to take that game to the next level. The goal is to take any two actors and connect them via the least amount of movies and co-stars possible. 

Here is how Harvard explains it:
“In this problem, we’re interested in finding the shortest path between any two actors by choosing a sequence of movies that connects them. For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.””

Havard provides you with an initial repo. This repo contains three different data sources in CSV form. Actors, movies, and a join table that ties actors to movies. There is also a file called degrees.py which can run from the command line. The file includes a variety of functions that assist you in loading and parsing the CSV files. Upon running the file, it will load all of the csv data into memory and then prompt you to input two actors. Initially, inputting two actors will return an error message. This is a NotImplmentedError that comes from the function named “shortest_path”.  

The goal of the assignment is to complete the implementation of the “shortest_path”. Using a Breadth-First Search algorithm, take in two actors provided via the command line, and connect them via the films they and their co-stars have acted in. The goal is to do this with the least possible connections. Once the path is found, return a list of movies and stars that connect the initial actors.

This repo contains the final implmentation of the "shortest_path" function. To run the file run: <code>python3 degrees.py</code>

Below are some notes from the first unit of the CS50 Intro to AI class. If you want to check out the course on your own, it's completely free and filled with great info. Check out the link here.


# Search Problems

The Anatomy of a Search Problem


Agent : perceives and acts upon its environment, ai game play, determines moves


State: where the agent is in the environment
Initial state: where the agent starts in the problem
Actions: possible movements from one state to another, are functions takes a current state, returns available next state options
Transition Model: the new state that results after preforming an action 
