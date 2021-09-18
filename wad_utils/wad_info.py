import struct

wad = "/Users/ham/Downloads/doom-wad-shareware-1.9.fixed/doom1.wad"

with open(wad, 'rb') as wad_f:
    magic = wad_f.read(4)
    print(magic)
    num_entries, directory_addr = struct.unpack("<II", wad_f.read(8))
    print(f"directory at: {directory_addr} with {num_entries} entries")

    wad_f.seek(directory_addr)

    for i in range(0, num_entries):
        start_addr, size = struct.unpack("<II", wad_f.read(8))
        lump_name: bytes = wad_f.read(8)
        cur_location = wad_f.tell()
        wad_f.seek(start_addr)
        wad_data = wad_f.read(size)
        wad_f.seek(cur_location)
        print(f"SIZE \t {size} \t Dir entry {i} | {lump_name.decode('utf-8')} - at {start_addr}")
        print(f"STARTS WITH: {wad_data[0:min(len(wad_data)-1, 16)]}")


