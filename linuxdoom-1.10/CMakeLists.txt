
set(CMAKE_VERBOSE_MAKEFILE 1)

add_compile_options(-g -Wall)
add_compile_definitions(NORMALUNIX)
include_directories(/usr/X11/include)
link_directories(/usr/X11R6/lib)

add_executable(doomexe interfaces/i_main.c)

add_subdirectory(automap)
add_subdirectory(doom)
add_subdirectory(final)
add_subdirectory(hud)
add_subdirectory(interfaces)
add_subdirectory(memory)
add_subdirectory(menu)
add_subdirectory(misc)
add_subdirectory(play)
add_subdirectory(rendering)
add_subdirectory(sound)
add_subdirectory(status)
add_subdirectory(strings)
add_subdirectory(wad)
add_subdirectory(win)

target_link_libraries(doomexe Xext X11 m)
