## Karamuto scripts
Some scripts I have made to visualize the Karamuto model (https://en.wikipedia.org/wiki/Kuramoto_model) used in swarm control. 
The repository requires the numpy, matpotlib and cmath liraries.

## How it works
In the 1D-case, every point is drawn with a radius 10 and an angle phi. The angle phi is updated according to the Karamuto model. For now, the only script that can be run is the "circle.py" script,
which produce an animation of the points moving along the circle. 


## Next steps
For now, I have only implementet a basic karamuto-model in 1D. First I want to improve the initalization of the points, adding random initializatong. Second is a K-matrix that indicates the attraction
between the different poins, which is now assumed to be equal. After a while, I wish to expand it to 2D to illustrate more complicated models (see link above). 
