#include <limits.h>
#include "gameloop.h"
#include "textures.h"
#include "utility.h"
#include "options.h"
#include "blocks.h"
#include "menus.h"
#include "data.h"
#include "gui.h"

/* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * WARNING!!!                                                                *
 *                                                                           *
 * This file is where all the decompiled nonsense is. Things are so heavily  *
 * nested and spaghetti-like that its the only place with an indent size of  *
 * two spaces (predominantly).                                               *
 *                                                                           *
 * Looking at this code for extended periods of time can cause adverse       *
 * psychological effects.                                                    *
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * */

World world = { 0 };
Player *player = &world.player;

static Coords playerOffsetPos = { 0.0, 0.0, 0.0 };

int gameState = STATE_TITLE;
int gamePopup;

static int guiOn;
static int debugOn;

static SDL_Rect backgroundRect;
static char *errorMessage = NULL;
static long l;

static void gameLoop_gameplay        (SDL_Renderer *, Inputs *);
static void gameLoop_drawPopup       (SDL_Renderer *, Inputs *);
static void gameLoop_processMovement (Inputs *, int);

static uint32_t
        fps_lastmil = 0,
        fps_count   = 0,
        fps_now     = 0;

/* gameLoop_resetGame
 * Resets elements of the game such as time and the player position. This will
 * also reset the world.
 */
void gameLoop_resetGame () {
        l = SDL_GetTicks();

        gamePopup = 0;
        
        guiOn   = 1;
        debugOn = 0;

        backgroundRect.x = 0;
        backgroundRect.y = 0;
        backgroundRect.w = BUFFER_W;
        backgroundRect.h = BUFFER_H;
        
        chatAdd("Game started");
}

/* gameLoop
 * Does all the raycasting stuff, moves the player around, etc.
 * If by chance the game ends, it returns false - which should
 * terminate the main while loop and end the program.
 */
int gameLoop (
        Inputs *inputs,
        SDL_Renderer *renderer
) {
        // If there is an error, show it and stop
        if (errorMessage) {
                if (state_err(renderer, inputs, errorMessage)) {
                        errorMessage = NULL;
                        // TODO: add capability to recover from error:
                        return 0;
                } else {
                        return 1;
                }
        }

        switch (gameState) {
        case STATE_TITLE:
                // A main menu
                if (state_title(renderer, inputs, &gameState)) return 0;
                break;

        case STATE_SELECT_WORLD:
                // World creation menu
                state_selectWorld(renderer, inputs, &gameState, &world);
                break;

        case STATE_NEW_WORLD:
                // World creation menu
                state_newWorld(renderer, inputs, &gameState, &world);
                break;

        case STATE_LOADING:
                // Generate a world and present a loading screen
                if (state_loading(renderer, &world, world.seed, player->pos)) {
                        gameLoop_resetGame();
                        gameState = 5;
                };
                break;

        case STATE_GAMEPLAY:
                // The actual gameplay
                gameLoop_gameplay(renderer, inputs);
                break;

        case STATE_OPTIONS:
                state_options(renderer, inputs, &gameState);
                break;

        default:
                state_egg(renderer, inputs, &gameState);
                break;
        }

        if (gameState != STATE_GAMEPLAY || gamePopup != POPUP_HUD) {
                inputs->mouse.left  = 0;
                inputs->mouse.right = 0;
        }

        return 1;
}

/* gameLoop_gameplay
 * Runs game logic and rendering. This is where most of the obfuscated code is.
 */
static void gameLoop_gameplay (SDL_Renderer *renderer, Inputs *inputs) {
  static double
        f21,
        f22,
        f23,
        f24,
        f25,
        f26,
        f27,
        f28,
        f29,
        f30,
        f31,
        f32,
        f33,
        f34,
        f35,
        f36;

  static int
        blockSelected = 0,
        selectedPass;
  
  static IntCoords blockSelect       = { 0 };
  static IntCoords blockSelectOffset = { 0 };
  static IntCoords coordPass         = { 0 };
  static IntCoords blockRayPosition  = { 0 };
  
  static Chunk *chunk;
  
  /* Look to see if there are chunks that need to be
  loaded in*/
  
  // static int chunkLoadNum = 0;
  // if(chunkLoadNum < CHUNKARR_SIZE) {
    // static IntCoords chunkLoadCoords = { 0 };
    // chunkLoadCoords.x =
      // ((chunkLoadNum % CHUNKARR_DIAM) -
      // CHUNKARR_RAD) * 64 + player.pos.x;
    // chunkLoadCoords.y =
      // (((chunkLoadNum / CHUNKARR_DIAM) % CHUNKARR_DIAM) -
      // CHUNKARR_RAD) * 64 + player.pos.y;
    // chunkLoadCoords.z =
      // ((chunkLoadNum / (CHUNKARR_DIAM * CHUNKARR_DIAM)) -
      // CHUNKARR_RAD) * 64 + player.pos.z;
    // chunkLoadNum++;
    // 
    // genChunk (
      // &world, world.seed,
      // chunkLoadCoords.x,
      // chunkLoadCoords.y,
      // chunkLoadCoords.z, world->type, 0,
      // player.pos
    // );
  // } else {
    // chunkLoadNum = 0;
  // }

  ;int headInWater = World_getBlock (&world,
    player->pos.x,
    player->pos.y,
    player->pos.z) == BLOCK_WATER;

  int feetInWater = World_getBlock (&world,
    player->pos.x,
    player->pos.y + 1,
    player->pos.z) == BLOCK_WATER;

  int effectDrawDistance = options.drawDistance;
  // Restrict view distance while in water
  if (headInWater) { effectDrawDistance = 10; }

  // Update directional vectors
  player->vectorH.x = sin(player->hRot);
  player->vectorH.y = cos(player->hRot);
  player->vectorV.x = sin(player->vRot);
  player->vectorV.y = cos(player->vRot);

  // Update offset player position
  playerOffsetPos.x = player->pos.x + PLAYER_POSITION_OFFSET;
  playerOffsetPos.y = player->pos.y + PLAYER_POSITION_OFFSET;
  playerOffsetPos.z = player->pos.z + PLAYER_POSITION_OFFSET;
  
  // Skybox, basically
  double timeCoef;
  switch (world.dayNightMode) {
    case 0:
      timeCoef  = (double)(world.time % 102944) / 16384;
      timeCoef  = sin(timeCoef);
      timeCoef /= sqrt(timeCoef * timeCoef + (1.0 / 128.0));
      timeCoef  = (timeCoef + 1) / 2;
      break;
    case 1:
      timeCoef = 1;
      break;
    case 2:
      timeCoef = 0;
      break;
  }

  // Change ambient color depending on if we are in the water or the air
  if (headInWater) {
    SDL_SetRenderDrawColor (
      renderer,
      48  * timeCoef,
      96  * timeCoef,
      200 * timeCoef,
      255
    );
  } else {
    SDL_SetRenderDrawColor (
      renderer,
      153 * timeCoef,
      204 * timeCoef,
      255 * timeCoef,
      255
    );
  }
  
  SDL_RenderClear(renderer);
  
  if (inputs->keyboard.esc) {
    gamePopup = gamePopup ? 0 : 1;
    inputs->keyboard.esc = 0;
  }
  
  fps_count++;
  if (fps_lastmil < SDL_GetTicks() - 1000) {
    fps_lastmil = SDL_GetTicks();
    fps_now     = fps_count;
    fps_count   = 0;
  }
  
  /* Things that should run at a constant speed, regardless
  of CPU power. If the rendering takes a long time, this
  will fire more times to compensate. */
  while (SDL_GetTicks() - l > 10L) {
    world.time++;
    l += 10L;
    gameLoop_processMovement(inputs, feetInWater);
  }
  
  if (gamePopup == POPUP_HUD) {
    if (blockSelected) {
      InvSlot *activeSlot = &player->inventory.hotbar [
        player->inventory.hotbarSelect
      ];

      // Breaking blocks
      if (inputs->mouse.left > 0) {
        Block blockid = World_getBlock (
          &world,
          blockSelect.x,
          blockSelect.y,
          blockSelect.z
        );

        // Can't break other players
        if (blockid != BLOCK_PLAYER_BODY && blockid != BLOCK_PLAYER_HEAD) {
          InvSlot pickedUp = {
            .blockid    = blockid,
            .amount     = 1,
            .durability = 1
          };

          Inventory_transferIn(&player->inventory, &pickedUp);
          
          World_setBlock (
            &world,
            blockSelect.x,
            blockSelect.y,
            blockSelect.z, 0, 1
          );
        }
      }
      
      blockSelectOffset.x += blockSelect.x;
      blockSelectOffset.y += blockSelect.y;
      blockSelectOffset.z += blockSelect.z;

      // Placing blocks
      if (inputs->mouse.right > 0) {
        if (
          // Player cannot be obstructing the block
          (
            fabs(player->pos.x - 0.5 - blockSelectOffset.x) >= 0.8  ||
            fabs(player->pos.y       - blockSelectOffset.y) >= 1.45 ||
            fabs(player->pos.z - 0.5 - blockSelectOffset.z) >= 0.8
          ) &&
          // Player must have enough of that block
          activeSlot->amount > 0
        ) {
          int blockSet = World_setBlock (
            &world,
            blockSelectOffset.x,
            blockSelectOffset.y,
            blockSelectOffset.z,
            activeSlot->blockid, 1
          );

          if (blockSet) {
            activeSlot->amount --;
            if (activeSlot->amount == 0) activeSlot->blockid = 0;
          }
        }
      }
    }

    inputs->mouse.left  = 0;
    inputs->mouse.right = 0;

    // Toggle GUI
    if (inputs->keyboard.f1) {
      inputs->keyboard.f1 = 0;
      guiOn ^= 1;
    }

    // Toggle debug mode
    if (inputs->keyboard.f3) {
      inputs->keyboard.f3 = 0;
      debugOn = !debugOn;
    }

    // Toggle advanced debug menu
    #ifndef small
    if (inputs->keyboard.f4) {
      inputs->keyboard.f4 = 0;
      gamePopup = (gamePopup == POPUP_ADVANCED_DEBUG) ? 0 : 4;
    }
    #endif

    // Enter chat
    if (inputs->keyboard.t) {
      // reset text input
      inputs->keyboard.t = 0;
      inputs->keyTyped   = 0;
      gamePopup = POPUP_CHAT;
    }

    // Enter inventory
    if (inputs->keyboard.e) {
      inputs->keyboard.e = 0;
      gamePopup = POPUP_INVENTORY;
    }

    // Swap hotbar selection with offhand
    if (inputs->keyboard.f) {
      inputs->keyboard.f = 0;
      InvSlot_swap (
        &player->inventory.hotbar[player->inventory.hotbarSelect],
        &player->inventory.offhand
      );
    }
    
    // Select hotbar slots with scroll wheel
    if (inputs->mouse.wheel != 0) {
            player->inventory.hotbarSelect -= inputs->mouse.wheel;
            player->inventory.hotbarSelect = nmod (
                    player->inventory.hotbarSelect, 9);
            inputs->mouse.wheel = 0;
    }

    // Select hotbar slots with number keys
    if (inputs->keyboard.num1) { player->inventory.hotbarSelect = 0; }
    if (inputs->keyboard.num2) { player->inventory.hotbarSelect = 1; }
    if (inputs->keyboard.num3) { player->inventory.hotbarSelect = 2; }
    if (inputs->keyboard.num4) { player->inventory.hotbarSelect = 3; }
    if (inputs->keyboard.num5) { player->inventory.hotbarSelect = 4; }
    if (inputs->keyboard.num6) { player->inventory.hotbarSelect = 5; }
    if (inputs->keyboard.num7) { player->inventory.hotbarSelect = 6; }
    if (inputs->keyboard.num8) { player->inventory.hotbarSelect = 7; }
    if (inputs->keyboard.num9) { player->inventory.hotbarSelect = 8; }
  }
  
  /* Cast rays. selectedPass passes wether or not a block is
  selected to the blockSelected variable */

  // Decrease fov when in water
  double effectFov = options.fov;
  if (headInWater) { effectFov += 20; }
  
  selectedPass = 0;
  for (int pixelX = 0; pixelX < BUFFER_W; pixelX++) {
    double rayOffsetX = (pixelX - BUFFER_HALF_W) / effectFov;
    for (int pixelY = 0; pixelY < BUFFER_H; pixelY++) {
      int finalPixelColor = 0;
      int pixelMist = 255;
      int pixelShade;
      
      double rayOffsetY = (pixelY - BUFFER_HALF_H) / effectFov;

      // Ray offset Z?
      f21 = 1.0;
      
      f22 = f21        * player->vectorV.y + rayOffsetY * player->vectorV.x;
      f23 = rayOffsetY * player->vectorV.y - f21        * player->vectorV.x;
      f24 = rayOffsetX * player->vectorH.y + f22        * player->vectorH.x;
      f25 = f22        * player->vectorH.y - rayOffsetX * player->vectorH.x;

      double rayDistanceLimit = effectDrawDistance;
      
      f26 = 5.0;
      for (int blockFace = 0; blockFace < 3; blockFace++) {
        f27 = f24;
        if (blockFace == 1) f27 = f23;
        if (blockFace == 2) f27 = f25;
        f28 = 1.0 / ((f27 < 0.0) ? (-1 * f27) : f27);
        f29 = f24 * f28;
        f30 = f23 * f28;
        f31 = f25 * f28;
        f32 = playerOffsetPos.x - (int)playerOffsetPos.x;
        if (blockFace == 1) f32 = playerOffsetPos.y - (int)playerOffsetPos.y;
        if (blockFace == 2) f32 = playerOffsetPos.z - (int)playerOffsetPos.z;
        if (f27 > 0.0)      f32 = 1.0 - f32; 
        f33 = f28 * f32;
        f34 = playerOffsetPos.x + f29 * f32;
        f35 = playerOffsetPos.y + f30 * f32;
        f36 = playerOffsetPos.z + f31 * f32;
        if (f27 < 0.0) {
          if (blockFace == 0) f34--; 
          if (blockFace == 1) f35--; 
          if (blockFace == 2) f36--; 
        }
        
        /* Whatever's in this loop needs to run *extremely*
        fast */
        while (f33 < rayDistanceLimit) {
          blockRayPosition.x = (int)f34 - PLAYER_POSITION_OFFSET;
          blockRayPosition.y = (int)f35 - PLAYER_POSITION_OFFSET;
          blockRayPosition.z = (int)f36 - PLAYER_POSITION_OFFSET;
          
          /* Imitate getBlock so we don't have to launch
          into a function then another function a zillion
          times per second. This MUST BE STATIC because
          this information needs to carry over between
          iterations of gameLoop. */
          // TODO: make this an inline function
          static IntCoords lookup_ago = {
            100000000,
            100000000,
            100000000
          }, lookup_now;
          
          lookup_now.x = blockRayPosition.x >> 6;
          lookup_now.y = blockRayPosition.y >> 6;
          lookup_now.z = blockRayPosition.z >> 6;

          if (
            lookup_now.x != lookup_ago.x ||
            lookup_now.y != lookup_ago.y ||
            lookup_now.z != lookup_ago.z
          ) {
            lookup_ago = lookup_now;

            // hash coordinates
            lookup_now.x &= 0x3FF;
            lookup_now.y &= 0x3FF;
            lookup_now.z &= 0x3FF;
            
            lookup_now.y <<= 10;
            lookup_now.z <<= 20;
            
            uint32_t lookup_hash = lookup_now.x | lookup_now.y | lookup_now.z;
            lookup_hash++;
            
            int lookup_first  = 0,
                lookup_last   = CHUNKARR_SIZE - 1,
                lookup_middle = (CHUNKARR_SIZE - 1) / 2;

            // Perform binary search
            while (lookup_first <= lookup_last) {
              if (world.chunk[lookup_middle].coordHash > lookup_hash) {
                lookup_first = lookup_middle + 1;
                
              } else if (world.chunk[lookup_middle].coordHash == lookup_hash) {
                chunk = &world.chunk[lookup_middle];
                goto foundChunk;
                
              } else {
                lookup_last = lookup_middle - 1;
              }
              
              lookup_middle = (lookup_first + lookup_last) / 2;
            }
            chunk = NULL;
          }
          
          Block intersectedBlock;
          foundChunk: if (chunk) {
            intersectedBlock = chunk->blocks [
               nmod(blockRayPosition.x, 64)        +
              (nmod(blockRayPosition.y, 64) << 6 ) +
              (nmod(blockRayPosition.z, 64) << 12)
            ];
          } else {
            intersectedBlock = 0;
            goto chunkNull;
          }
          
          if (
            intersectedBlock != BLOCK_AIR &&
            !(headInWater && intersectedBlock == BLOCK_WATER)
          ) {
            // Determine what texel the ray hit
            int textureX = (int)((f34 + f36) * 16.0) & 0xF;
            int textureY = ((int)(f35 * 16.0) & 0xF) + 16;
            if (blockFace == 1) {
              textureX = (int)(f34 * 16.0) & 0xF;
              textureY = (int)(f36 * 16.0) & 0xF;
              if (f30 < 0.0)
                textureY += 32; 
            }
            
            // Block outline color
            int pixelColor = 0xFFFFFF;
            if (
              (
                !blockSelected                      ||
                blockRayPosition.x != blockSelect.x ||
                blockRayPosition.y != blockSelect.y ||
                blockRayPosition.z != blockSelect.z
              ) || (
                   textureX > 0  
                && textureY % 16 > 0
                && textureX < 15
                && textureY % 16 < 15
              ) || !guiOn || gamePopup
            ) {
              if (intersectedBlock >= NUMBER_OF_BLOCKS) {
                pixelColor = 0xFF0000;
              } else {
                pixelColor = textures [
                  textureX + (textureY * 16) + intersectedBlock * 256 * 3];
              }
            }
            
            /* See if the block is selected. There must be a
            better way to do this check... */
            if (
              f33 < f26 && (
                (
                   ! options.trapMouse
                  && pixelX == inputs->mouse.x / BUFFER_SCALE
                  && pixelY == inputs->mouse.y / BUFFER_SCALE
                ) || (
                     options.trapMouse
                  && pixelX == BUFFER_HALF_W
                  && pixelY == BUFFER_HALF_H
                )
              )
            ) {
              selectedPass = 1;
              coordPass = blockRayPosition;

              blockSelectOffset = (const IntCoords) { 0 };
              switch (blockFace) {
                case 0: blockSelectOffset.x = 1 - 2 * (f27 > 0.0); break;
                case 1: blockSelectOffset.y = 1 - 2 * (f27 > 0.0); break;
                case 2: blockSelectOffset.z = 1 - 2 * (f27 > 0.0); break;
              }
              
              f26 = f33;
            }
            
            if (pixelColor > 0) {
              finalPixelColor = pixelColor;
              pixelMist = 255 - (int)(
                f33 / (double)effectDrawDistance * 255.0F);
              pixelShade = 255 - (blockFace + 2) % 3 * 50;
              rayDistanceLimit = f33;
            } 
          }
          chunkNull:
          f34 += f29;
          f35 += f30;
          f36 += f31;
          f33 += f28;
        } // This concludes our warpspeed rampage
      }
      
      // Draw inverted color crosshair
      if (options.trapMouse && (
        (pixelX == BUFFER_HALF_W
          && abs(BUFFER_HALF_H - pixelY) < 4) ||
        (pixelY == BUFFER_HALF_H
          && abs(BUFFER_HALF_W - pixelX) < 4)
      )) {
        finalPixelColor = 0x1000000 - finalPixelColor;
      }
      
      if (finalPixelColor > 0) {
        SDL_SetRenderDrawColor(
          renderer,
          ((finalPixelColor >> 16 & 0xFF) * pixelShade) >> 8,
          ((finalPixelColor >> 8  & 0xFF) * pixelShade) >> 8,
          ((finalPixelColor       & 0xFF) * pixelShade) >> 8,
          options.fogType ? sqrt(pixelMist) * 16 : pixelMist
        );
        
        SDL_RenderDrawPoint(renderer, pixelX, pixelY);
      }
    }
  }

  // Make camera blue if in water
  if (headInWater) {
    SDL_SetRenderDrawColor(renderer, 16, 32, 255, 128);
    SDL_RenderFillRect(renderer, &backgroundRect);
  }
  
  // Pass info about selected block on
  blockSelected = selectedPass;
  blockSelect   = coordPass;
  
  inputs->mouse.x /= BUFFER_SCALE;
  inputs->mouse.y /= BUFFER_SCALE;

  // Draw current popup
  gameLoop_drawPopup(renderer, inputs);
  
  // If we need to take a screenshot, do so
  if (inputs->keyboard.f2) {
    inputs->keyboard.f2 = 0;
    char path [PATH_MAX];
    int err = data_getScreenshotPath(path);
    gameLoop_screenshot(renderer, err ? NULL : path);
  }
}

void gameLoop_drawPopup (SDL_Renderer *renderer, Inputs *inputs) {
        // In-game menus
        if (gamePopup != 0) {
                SDL_SetRelativeMouseMode(0);
        }

        switch (gamePopup) {
        case POPUP_HUD:
                // HUD
                if (options.trapMouse) SDL_SetRelativeMouseMode(1);
                if (guiOn) popup_hud (
                renderer, inputs, &world,
                &debugOn, &fps_now, player
                );
                break;

        case POPUP_PAUSE:
                // Pause menu
                tblack(renderer);
                SDL_RenderFillRect(renderer, &backgroundRect);
                popup_pause(renderer, inputs, &gamePopup, &gameState, &world);
                break;

        case POPUP_OPTIONS:
                // Options
                tblack(renderer);
                SDL_RenderFillRect(renderer, &backgroundRect);
                popup_options (renderer, inputs, &gamePopup);
                break;

        case POPUP_INVENTORY:
                // Inventory
                popup_inventory(renderer, inputs, player, &gamePopup);
                break;

        #ifndef small
        case POPUP_ADVANCED_DEBUG:
                // Advanced debug menu
                tblack(renderer);
                SDL_RenderFillRect(renderer, &backgroundRect);
                popup_debugTools(renderer, inputs, &gamePopup);
                break;

        case POPUP_CHUNK_PEEK:
                // Chunk peek
                tblack(renderer);
                SDL_RenderFillRect(renderer, &backgroundRect);
                popup_chunkPeek(renderer, inputs, &world, &gamePopup, player);
                break;

        case POPUP_ROLL_CALL:
                // Chunk info viewer
                tblack(renderer);
                SDL_RenderFillRect(renderer, &backgroundRect);
                popup_rollCall(renderer, inputs, &world, &gamePopup);
                break;

        case POPUP_OVERVIEW:
                // View all chunks
                tblack(renderer);
                SDL_RenderFillRect(renderer, &backgroundRect);
                popup_overview(renderer, inputs, &world, &gamePopup);
                break;
        #endif

        case POPUP_CHAT:
                // Chat
                popup_chat(renderer, inputs, world.time);
                break;
        }
}

static void gameLoop_processMovement (Inputs *inputs, int inWater) {
        // Run at half speed if in water
        static int flipFlop = 0;
        flipFlop = !flipFlop;
        int doPhysics = !inWater || flipFlop;

        // Only process movement controls if there are no active popup
        if (gamePopup == 0) {
                // Looking around
                if (options.trapMouse) {
                        player->hRot += (double)inputs->mouse.x / 64;
                        player->vRot -= (double)inputs->mouse.y / 64;
                } else {
                        double cameraMoveX =
                                (inputs->mouse.x - BUFFER_W * 2) /
                                (double)BUFFER_W * 2.0;
                        double cameraMoveY =
                                (inputs->mouse.y - BUFFER_H * 2) /
                                (double)BUFFER_H * 2.0;

                        double cameraMoveDistance = sqrt (
                        cameraMoveX * cameraMoveX +
                        cameraMoveY * cameraMoveY) - 1.2;

                        if (cameraMoveDistance < 0.0) {
                                cameraMoveDistance = 0.0;
                        }
                        if (cameraMoveDistance > 0.0) {
                                player->hRot += cameraMoveX *
                                        cameraMoveDistance / 400.0;
                                player->vRot -= cameraMoveY *
                                        cameraMoveDistance / 400.0;
                        }
                }

                // Restrict camera vertical position
                if (player->vRot < -1.57) player->vRot = -1.57;
                if (player->vRot >  1.57) player->vRot =  1.57;

                double speed = 0.02;

                if (doPhysics) {
                        player->FBVelocity =
                                (inputs->keyboard.w - inputs->keyboard.s) *
                                speed;
                        player->LRVelocity =
                                (inputs->keyboard.d - inputs->keyboard.a) *
                                speed;
                }
        }
        
        static Coords playerMovement  = { 0.0, 0.0, 0.0 };

        // Moving around
        if (doPhysics) {
                playerMovement.x *= 0.5;
                playerMovement.y *= 0.99;
                playerMovement.z *= 0.5;

                playerMovement.x +=
                        player->vectorH.x * player->FBVelocity +
                        player->vectorH.y * player->LRVelocity;
                playerMovement.z +=
                        player->vectorH.y * player->FBVelocity -
                        player->vectorH.x * player->LRVelocity;
                playerMovement.y += 0.003;
        }


        // Detect collisions and jump
        for (int axis = 0; axis < 3; axis++) {
                if (!doPhysics) { break; }

                Coords playerPosTry = {
                        player->pos.x + playerMovement.x * (double)((axis + 2) % 3 / 2),
                        player->pos.y + playerMovement.y * (double)((axis + 1) % 3 / 2),
                        player->pos.z + playerMovement.z * (double)((axis + 3) % 3 / 2),
                };

                playerPosTry.x += PLAYER_POSITION_OFFSET;
                playerPosTry.y += PLAYER_POSITION_OFFSET;
                playerPosTry.z += PLAYER_POSITION_OFFSET;
                
                for (int step = 0; step < 12; step++) {
                        int blockX = playerPosTry.x +
                                ((step >> 0) & 1) * 0.6 - 0.3;
                        int blockY = playerPosTry.y +
                                ((step >> 2) - 1) * 0.8 + 0.65;
                        int blockZ = playerPosTry.z +
                                ((step >> 1) & 1) * 0.6 - 0.3;

                        // Very ad-hoc. TODO: look into a deeper fix than this.
                        // blockX -= (blockX < 0);
                        // blockY -= (blockY < 0);
                        // blockZ -= (blockZ < 0);
                        // ---

                        Block block = World_getBlock (&world,
                                blockX - PLAYER_POSITION_OFFSET,
                                blockY - PLAYER_POSITION_OFFSET,
                                blockZ - PLAYER_POSITION_OFFSET);

                        int shouldCollide = 1;
                        // Blocks that have collision disabled
                        shouldCollide &= block != BLOCK_AIR;
                        shouldCollide &= block != BLOCK_WATER;
                        shouldCollide &= block != BLOCK_TALL_GRASS;
                        // Uncomment this line to be able to enter chunks that
                        // don't exist in memory
                        // shouldCollide &= block != BLOCK_NIL;
                        
                        if (shouldCollide) {
                                if (axis != 1) { goto stopCheck; }
                                
                                if (
                                        inputs->keyboard.space > 0 &&
                                        (playerMovement.y > 0.0)   &&
                                        !gamePopup
                                ) {
                                        inputs->keyboard.space = 0;
                                        playerMovement.y = -0.1;
                                        goto stopCheck;
                                }
                                playerMovement.y = 0.0;
                                goto stopCheck;
                        }
                }

                playerPosTry.x -= PLAYER_POSITION_OFFSET;
                playerPosTry.y -= PLAYER_POSITION_OFFSET;
                playerPosTry.z -= PLAYER_POSITION_OFFSET;

                player->pos.x = playerPosTry.x;
                player->pos.y = playerPosTry.y;
                player->pos.z = playerPosTry.z;

                stopCheck:;
        }

        // Swim in water
        if (inWater && doPhysics) {
                if (
                        inputs->keyboard.space > 0 &&
                        (playerMovement.y > -0.05)   &&
                        !gamePopup
                ) {
                        inputs->keyboard.space = 0;
                        playerMovement.y = -0.1;
                }
        }
}

int gameLoop_screenshot (SDL_Renderer *renderer, const char *path) {
        SDL_Surface *grab = SDL_CreateRGBSurfaceWithFormat (
                0, BUFFER_W * BUFFER_SCALE, BUFFER_H * BUFFER_SCALE,
                32, SDL_PIXELFORMAT_ARGB8888
        );

        SDL_RenderReadPixels (
                renderer, NULL, SDL_PIXELFORMAT_ARGB8888,
                grab->pixels, grab->pitch
        );

        if (path == NULL) {
                chatAdd("Couldn't save screenshot");
                return 1;
        }
        
        int saved = SDL_SaveBMP(grab, path);
        SDL_FreeSurface(grab);

        if (saved == 0) {
                chatAdd("Saved screenshot");
                return 0;
        } else {
                chatAdd("Couldn't save screenshot");
                return 1;
        }
}

void gameLoop_error (char *message) {
        errorMessage = message;
}
