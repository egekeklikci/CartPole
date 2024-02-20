# CartPole
 A reinforcement learning program which uses q learning to solve cart-pole problem.
# Cart Pole Problem
 This environment corresponds to the version of the cart-pole problem described by Barto, Sutton, and Anderson in “Neuronlike Adaptive Elements That Can Solve Difficult Learning Control Problem”. A pole is attached by an un-actuated joint to a cart, which moves along a frictionless track. The pendulum is placed upright on the cart and the goal is to balance the pole by applying forces in the left and right direction on the cart.
 <p align="center">
    <img src="https://gymnasium.farama.org/_images/cart_pole.gif" width="300" height="150" class="center"/>
 </p>

The aim of this program is to create a machine learning model which aims to hold the pole as long as possible using q learning. 
To tackle this problem [Cart Pole](https://gymnasium.farama.org/environments/classic_control/cart_pole/) enviroment of [Gymnasium](https://gymnasium.farama.org) by Farama Foundation is used.

# Machine Learning Model
Q table consist of 420 rows, each corresponds to carts current poleAngle starting at -2.0 and ending at 2.19. For example rows start as -2.0, -1.99, -1.98 and ends as 2.18, 2.19, 2.19.
Each row consist of 3 1 dimension arrays which has a dimension of 1x8. This 3 arrays corresponds if the x position of the cart is near the upper or lower limit defined before. For this example x limits are -1.5 and 1.5. Inside these
3 arrays there are 8 floats as mentioned before. These floats correspond to the value of this state according to the angular velocity of the pole. In total there are 10,800 parameters. 

# Lessons Learned 
Although the cart velocity is also given by the environment, it is not used. To further improve the model cart velocity also can be used.

# How To Use
After downloading gymnasium and pygame just run the program. Keep in mind that the learning take place on every run. This means that the success of the model can be changed in every run. 

When the program starts, in learning it will print the episode and epsilon values every 100,000 iterations. After the learning it will print a message that will inform you that learning has been finished. After the completion, q table will be printed.

At last a window of pygame will pull up and cart pole model will run with graphical interface 10 times. After these trials, times of the last seen 10 iterations and the average time will be printed.

Example video of an agent controled by our machine learning model in the environment can be found below:



https://github.com/egekeklikci/CartPole/assets/102902284/a53de6cb-d0cd-4a7d-933a-f17734b01751

