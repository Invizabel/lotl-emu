# resources for header extraction:
# https://dsibrew.org/wiki/DSi_cartridge_header
# https://gbatemp.net/threads/nds-rom-file-format.202880/

import ctypes

# temp
import time

# get assets
def assets(rom_file):
    # extraction
    title = rom_file[:12].decode()
    game_code = rom_file[12:16].decode()
    maker_code = rom_file[16:18].decode()
    unit_code = rom_file[18:19]
    encryption_seed_select = rom_file[19:20]
    device_capacity = rom_file[20:21]
    reserved = rom_file[21:28]
    game_revision = rom_file[28:30]
    rom_version = rom_file[30:31]

    # parser
    if unit_code == b"\x00":
        unit_code = "NDS"
    if unit_code == b"\x01":
        unit_code = "DSi"
    if unit_code == b"\x02":
        unit_code = "NDS + DSi"
    if unit_code == b"\x03":
        unit_code = "DSi"

    if game_revision == b"\x00\x00":
        game_revision = 0
    else:
        game_revision = game_revision.decode()

    if rom_version == b"\x00":
        rom_version = 0
    else:
        rom_version = rom_version.decode()

    return title, game_code, maker_code, unit_code, encryption_seed_select, device_capacity, game_revision, rom_version

# create window and renderer (credit: https://gist.github.com/NickBeeuwsaert/29780f01debf60dedc8a)
def create_window(width, height, flags):
    window, renderer = ctypes.c_void_p(), ctypes.c_void_p()
    sdl.SDL_CreateWindowAndRenderer(width, height, flags, ctypes.byref(window), ctypes.byref(renderer))
    return window, renderer

# bind to dll and create window
def init():
    sdl = ctypes.CDLL("libSDL2.so")
    sdl_ttf = ctypes.CDLL("libSDL2_ttf.so")
    sdl_ttf.TTF_Init()
    sdl.SDL_Init(0x00000001 | 0x00000010 | 0x00000020 | 0x00000200 | 0x00001000 | 0x00002000 | 0x00004000 | 0x00008000 | 0x00100000)
    return sdl, sdl_ttf

# open rom
def open_rom(rom):
    with open(rom, "rb") as file:
        result = file.read()

    return result

sdl, sdl_ttf = init()
window, renderer = create_window(640,480,2)

# open rom
rom_file = open_rom("test.nds")
title, game_code, maker_code, unit_code, encryption_seed_select, device_capacity, game_revision, rom_version = assets(rom_file)
print("title: " + str(title))
print("game code: " + str(game_code))
print("marker code: " + str(maker_code))
print("unit code: " + str(unit_code))
print("encryption seed select: " + str(encryption_seed_select))
print("device capacity: " + str(device_capacity))
print("game revision: " + str(game_revision))
print("rom version: " + str(rom_version))

# drawing code 
sdl.SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
sdl.SDL_RenderClear(renderer)
sdl.SDL_RenderPresent(renderer)

# temp
time.sleep(1)

sdl.SDL_DestroyRenderer(renderer)
sdl.SDL_DestroyWindow(window)
sdl.SDL_Quit()
