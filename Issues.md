# Feature Issues
Create one GitHub Issue for each of the following features.

## 1. Finish wall bounces
### Branch: `feature/wall-bounces`
- [ ] Ball bounces off the bottom wall the same way it already bounces off the top wall.
- [ ] Ball bounces off the right wall instead of leaving the screen (this is a placeholder until a second paddle is implemented).
- [ ] Ball's speed stays constant after each bounce. Only the direction changes.
- [ ] Game runs for 30+ seconds without crashing or the ball getting stuck.
- [ ] PR description explains what changed and how it was tested.

## 2. Add paddle movement
### Branch: `feature/paddle-movement`
- [ ] Player can move the paddle up and down with two keys (up/down, a/w, etc.).
- [ ] Chosen keys are documented in the README.
- [ ] Paddle cannot move above the top or below the bottom of the screen.
- [ ] Movement speed feels smooth and consistent.
- [ ] PR description names the keys chosen.

## 3. Add ball–paddle collision
### Branch: feature/paddle-collision
- [ ] Ball bounces off the paddle when it touches it.
- [ ] Ball doesn't get stuck inside the paddle or bounce repeatedly in the same spot.
- [ ] (Optional challenge) Bounce angle changes depending on where the ball hits the paddle (top vs. middle vs. bottom).

## 4. Add scoring and ball reset
### Branch: feature/scoring-reset
- [ ] Game detects when the ball hits the left edge
- [ ] On a miss, the ball resets to the center with a random starting velocity.
- [ ] A score or lives count is tracked and updates on each miss.
- [ ] Game doesn't crash when the score/lives count reaches zero, even if nothing else happens.

## 5. Display score on screen
### Branch: feature/score-display
- [ ] Current score/lives is rendered using `pygame.font`.
- [ ] Text updates immediately when the score changes.
- [ ] Text is readable against the background and doesn't overlap other elements.

## 6. Add game states (splash, playing, game over)
### Branch: feature/game-states
- [ ] Game starts with a splash screen and waits for user input.
- [ ] Pressing a key (like SPACE) takes game from splash to playing mode.
- [ ] A game-over screen appears when the score/lives condition is met.
- [ ] Player can restart from the game-over screen without closing the app.
- [ ] The three states (splash, playing, game over) are clearly separated in code. 

## 7. Add a second player paddle or simple computer opponent
### Branch: feature/second-paddle
- [ ] A second paddle is implemented on the right side of the screen. The right wall bounce is removed.
- [ ] Either a player controls the second paddle or a simple computer algorithm does.
- [ ] Ball bounces off the second paddle the same way it does the first.
- [ ] Player can restart from the game-over screen without closing the app.
- [ ] The score for the second paddle is correctly displayed following the same acceptance criteria as feature 5.

## Create your own features
Suggestions include:
- Sound effects
- Increase speed over time
- Add a pause key