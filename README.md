# GAME_Alien_Invasion
Developed with pygame

__*Main project from Chapter 12 of "Python Crash Course", but with major modifications*__

* __alien_invasion.py__ is the driver file.
* User controls a ship (left and right key) to shoot down (spacebar) all aliens droppin down from the sky. User loses one life if the ship is shot by alien's missle or touched by the alien.
* Game over when user loses all his/her lives.
* User starts with 4 bullets (maximum 4 bullets allowed on screen) with single projectile for each shot. 
  * As game progresses, user can get rewards from shooting down aliens (rewards dropping randomly among the aliens).
  * Four types of rewards: 
    * increase bullet (more bullet available on screen)
    * multiple projectile (multiple bullets can be released at one shoot)
    * unlimited bullet
    * life boost (add one life)
    * shield (allows user to sustain one hit from alien's missle or touched once by alien)
  * Rewards dropping rate differs from level to level.
* Aliens start with 2 rows.
  * As game progresses, more rows of alien fleet would appear.
  * Alien moving speed also increases as level progresses.
  * Starting from level 2, alien starts to fire missles down at user's ship. Firing happens each time one alien hits the edge of the screen, and the firing is random. The number of missles fired per level is equivalent to the level number minus one.
* Scoring system
  * Hit alien = 50 pts
  * Successfully avoid one alien missle = 5 pts
  * High score is displayed on the screen and also saved in a separate file called "high_score.txt".
* User can press 'Q' at any time during the game to quit.
