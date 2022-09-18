#pragma once

#include <SDL2/SDL.h>
#include "terrain.h"
#include "main.h"
#include "player.h"

#define PLAYER_POSITION_OFFSET 128
 
int  gameLoop            (Inputs *inputs, SDL_Renderer *renderer);
void gameLoop_resetGame  ();
void gameLoop_error      (char *);
int  gameLoop_screenshot (SDL_Renderer *, const char *);
