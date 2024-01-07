import ctypes

# temp
import time

# create window and renderer (credit: https://gist.github.com/NickBeeuwsaert/29780f01debf60dedc8a)
def display(width, height, flags):
    window, renderer = ctypes.c_void_p(), ctypes.c_void_p()
    sdl.SDL_CreateWindowAndRenderer(width, height, flags, ctypes.byref(window), ctypes.byref(renderer))
    return window, renderer

# bind to dll and create window
sdl = ctypes.CDLL("libSDL2.so")
sdl.SDL_Init(0x00000001 | 0x00000010 | 0x00000020 | 0x00000200 | 0x00001000 | 0x00002000 | 0x00004000 | 0x00008000 | 0x00100000)
window, renderer = display(640,480,2)

# drawing code
sdl.SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
sdl.SDL_RenderClear(renderer)
sdl.SDL_RenderPresent(renderer)
time.sleep(15)
sdl.SDL_DestroyRenderer(renderer)
sdl.SDL_DestroyWindow(window)
sdl.SDL_Quit()
