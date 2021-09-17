
set(CMAKE_VERBOSE_MAKEFILE 1)

add_compile_options(-g -Wall)
add_compile_definitions(NORMALUNIX)
include_directories(/usr/X11/include)
link_directories(/usr/X11R6/lib)



add_executable(doom interfaces/i_main.c)

target_sources(doom PUBLIC
        doom/doomdef.c
        doom/doomstat.c
        strings/dstrings.c
        interfaces/i_system.c
        interfaces/i_sound.c
        interfaces/i_video.c
        interfaces/i_net.c
        rendering/tables.c
        final/f_finale.c
        final/f_wipe.c
        doom/d_main.c
        doom/d_net.c
        doom/d_items.c
        doom/g_game.c
        menu/m_menu.c
        menu/m_misc.c
        misc/m_argv.c
        misc/m_bbox.c
        misc/m_fixed.c
        misc/m_swap.c
        misc/m_cheat.c
        misc/m_random.c
        automap/am_map.c
        play/p_ceilng.c
        play/p_doors.c
        play/p_enemy.c
        play/p_floor.c
        play/p_inter.c
        play/p_lights.c
        play/p_map.c
        play/p_maputl.c
        play/p_plats.c
        play/p_pspr.c
        play/p_setup.c
        play/p_sight.c
        play/p_spec.c
        play/p_switch.c
        play/p_mobj.c
        play/p_telept.c
        play/p_tick.c
        play/p_saveg.c
        play/p_user.c
        rendering/r_bsp.c
        rendering/r_data.c
        rendering/r_draw.c
        rendering/r_main.c
        rendering/r_plane.c
        rendering/r_segs.c
        rendering/r_sky.c
        rendering/r_things.c
        wad/w_wad.c
        win/wi_stuff.c
        rendering/v_video.c
        status/st_lib.c
        status/st_stuff.c
        hud/hu_stuff.c
        hud/hu_lib.c
        sound/s_sound.c
        memory/z_zone.c
        doom/info.c
        sound/sounds.c)


add_subdirectory(strings)
add_subdirectory(automap)

target_link_libraries(doom Xext X11 m)
