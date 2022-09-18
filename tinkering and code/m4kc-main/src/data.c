#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <dirent.h>
#include <limits.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include "data.h"
#include "textures.h"

data_WorldListItem *data_worldList = NULL;
int data_worldListLength = 0;

char directoryName            [PATH_MAX] = { 0 };
char optionsFileName          [PATH_MAX] = { 0 };
char worldsDirectoryName      [PATH_MAX] = { 0 };
char screenshotsDirectoryName [PATH_MAX] = { 0 };

static uint32_t getSurfacePixel   (SDL_Surface *, int, int);
static int      findDirectoryName (char *, const char *);

/* data_init
 * Initializes the data module. Returns zero on success, nonzero on failure.
 */
int data_init (void) {
        int err = 0;

        err = findDirectoryName(directoryName, "/.m4kc");
        if (err) { return err; }
        
        err = findDirectoryName(optionsFileName, "/.m4kc/m4kc.conf");
        if (err) { return err; }
        
        err = findDirectoryName(worldsDirectoryName, "/.m4kc/worlds");
        if (err) { return err; }
        
        err = findDirectoryName (
                screenshotsDirectoryName, "/.m4kc/screenshots");
        if (err) { return err; }
        
        return 0;
}

/* data_directoryExists
 * Test if a directory exists at the specified path. This function does not
 * create or delete anything.
 */
int data_directoryExists (const char *path) {
        struct stat directoryInfo;
        return (stat(path, &directoryInfo) == 0 &&
                S_ISDIR(directoryInfo.st_mode));
        
}

/* data_fileExists
 * Test if a file exists at the specified path.
 */
int data_fileExists (const char *path) {
        return access(path, F_OK) == 0;
}

/* data_ensureDirectoryExists
 * Equivalent to mkdir -p. Creates a directory and all of its parent directories
 * if they don't exist.
 */
int data_ensureDirectoryExists (const char *path) {
        char currentDirectory[PATH_MAX] = "";
        int index = 0;
        
        while (path[index] != 0) {
                while (path[index] != 0) {
                        currentDirectory[index] = path[index];
                        currentDirectory[index + 1] = 0;
                        index ++;
                        char ch = currentDirectory[index - 1];
                        if (ch == '/' || ch == '\\') {
                                break;
                        }
                }

                if (!data_directoryExists(currentDirectory)) {
                        int status;
                        #ifdef _WIN32
                        status = mkdir(currentDirectory);
                        #else
                        status = mkdir(currentDirectory, 0755);
                        #endif
                        if (status != 0) {
                                return 1;
                        }
                }
        }

        return 0;
}

/* data_removeDirectory
 * Equivalent of rm -r. Removes a directory and its contents recursively.
 */
int data_removeDirectory (const char *path) {
        DIR *directory = opendir(path);
        size_t pathLength = strlen(path);

        if (!directory) { return 1; }
        
        struct dirent *directoryEntry;

        int err = 0;
        while (!err) {
                directoryEntry = readdir(directory);
                if (directoryEntry == NULL) {
                        err = 2;
                        break;
                }
        
                if (
                        !strcmp(directoryEntry->d_name, ".") ||
                        !strcmp(directoryEntry->d_name, "..")
                ) {
                        continue;
                }

                size_t newLength =
                        pathLength +
                        strlen(directoryEntry->d_name) + 2;
                        
                char *newPath = malloc(newLength);
                if (newPath == NULL) { return 3; }

                snprintf (
                        newPath, newLength, "%s/%s",
                        path, directoryEntry->d_name);
                
                struct stat fileInfo;
                if (!stat(newPath, &fileInfo)) {
                        if (S_ISDIR(fileInfo.st_mode)) {
                                err = data_removeDirectory(newPath);
                        } else {
                                err = unlink(newPath);
                        }
                }
                free(newPath);
        }
        
        closedir(directory);
        if (rmdir(path)) { return 4; }
        return 0;
}

/* data_getOptionsFileName
 * Returns the file path of the configuration file.
 */
char *data_getOptionsFileName (void) {
        return optionsFileName;
}

/* data_getWorldPath
 * Returns the path to a world, regardless if it exists or not. This function
 * ensures that the worlds directory exists. If it cannot do this, it returns 1.
 */
int data_getWorldPath (char *path, const char *worldName) {
        if (data_ensureDirectoryExists(worldsDirectoryName)) { return 1; }

        snprintf(path, PATH_MAX, "%s/%s", worldsDirectoryName, worldName);
        return 0;
}

/* data_getWorldMetaPath
 * Returns the path to the metadata file of a world, given a world path.
 */
void data_getWorldMetaPath (char *path, const char *worldPath) {
        snprintf(path, PATH_MAX, "%s/metadata", worldPath);
}

/* data_getWorldPlayerPath
 * Returns the path to a player file, given a world path and a player name.
 */
void data_getWorldPlayerPath (
        char *path,
        const char *worldPath,
        const char *name
) {
        snprintf(path, PATH_MAX, "%s/%s.player", worldPath, name);
}

/* data_getScreenshotPath
 * Writes into path the path for a new screenshot. The name will take the form
 * of: snip_YYYY-MM-DD_HH:MM:SS.bmp
 * ... and will be located in the path stored in screenshotsDirectoryName. If
 * the screenshots directory doesn't exist, this function will create it.
 */
int data_getScreenshotPath (char *path) {
        if (data_ensureDirectoryExists(screenshotsDirectoryName)) { return 1; }

        time_t unixTime = time(0);
        struct tm *timeInfo = localtime(&unixTime);
        
        snprintf (
                path, PATH_MAX,
                "%s/snip_%04i-%02i-%02i_%02i-%02i-%02i.bmp",
                screenshotsDirectoryName,
                timeInfo->tm_year + 1900,
                timeInfo->tm_mon  + 1,
                timeInfo->tm_mday,
                timeInfo->tm_hour,
                timeInfo->tm_min,
                timeInfo->tm_sec);
        return 0;
}


/* data_refreshWorldList
 * Regreshes the world list, clearing the previous one. Reads world names and
 * thumbnails from ~/.m4kc/worlds
 */
int data_refreshWorldList (void) {
        // Free previous list
        data_WorldListItem *item = data_worldList;
        while (item != NULL) {
                data_WorldListItem *next = item->next;
                free(item);
                item = next;
        }

        if (data_ensureDirectoryExists(worldsDirectoryName)) { return 1; }
        
        // Iterate through worlds directory
        struct dirent *directoryEntry;
        DIR *directory = opendir(worldsDirectoryName);
        if (!directory) { return 2; }

        data_worldListLength = 0;
        data_WorldListItem *last = NULL;
        while ((directoryEntry = readdir(directory)) != NULL) {
                if (directoryEntry->d_name[0] == '.') { continue; }

                // Allocate new list item
                data_WorldListItem *item = calloc (
                        sizeof(data_WorldListItem), 1);
                if (item == NULL) { return 3; }
                
                strncpy(item->name, directoryEntry->d_name, NAME_MAX);
                if (last == NULL) {
                        data_worldList = item;
                        last = data_worldList;
                } else {
                        last->next = item;
                        last = item;
                }

                // Get thumbnail
                char path[PATH_MAX];
                snprintf (
                        path, PATH_MAX,
                        "%s/%s/thumbnail.bmp",
                        worldsDirectoryName,
                        item->name);

                SDL_Surface *image = SDL_LoadBMP(path);
                int *pixel = item->thumbnail.buffer;
                
                // Do not accept vertical images
                if (image != NULL && image->h <= image->w) {
                        int scale = image->h / 16;
                        for (int y = 0; y < 16; y ++)
                        for (int x = 0; x < 16; x ++) {
                                *pixel = getSurfacePixel (image,
                                        x * scale,
                                        y * scale);
                                pixel ++;
                        }
                } else {
                        for (int y = 0; y < 16; y ++)
                        for (int x = 0; x < 16; x ++) {
                                *pixel = textures [
                                        x +
                                        y * BLOCK_TEXTURE_W +
                                        (BLOCK_GRASS * 3 + 1) *
                                        BLOCK_TEXTURE_W * BLOCK_TEXTURE_H];
                                pixel ++;
                        }
                }

                SDL_FreeSurface(image);

                data_worldListLength ++;
        }
        
        closedir(directory);

        return 0;
}

/* getSurfacePixel
 * Gets a pixel value from an SDL surface at the specified coordinates.
 */
static uint32_t getSurfacePixel (SDL_Surface *surface, int x, int y) {
        return *((uint32_t *) ((uint8_t *) surface->pixels
                + y * surface->pitch
                + x * surface->format->BytesPerPixel));
}

/* findDirectoryName
 * Concatenates the user's home directory with the specified path. subDirectory
 * must begin with a '/'. Uses %APPDATA% instead of home on windows.
 */
static int findDirectoryName (char *path, const char *subDirectory) {
        if (subDirectory[0] != '/') { return 2; }
        
        #ifdef _WIN32
        char *homeDirectory = getenv("APPDATA");
        #else
        char *homeDirectory = getenv("HOME");
        #endif
        if (homeDirectory == NULL) { return 3; }

        snprintf(path, PATH_MAX, "%s%s", homeDirectory, subDirectory);
        
        // Normalize path
        for (char *ch = path; *ch; ch ++) {
                if (*ch == '\\') { *ch = '/'; }
        }
        return 0;
}
