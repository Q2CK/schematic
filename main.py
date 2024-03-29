import mcschematic
import os

here = os.path.dirname(os.path.abspath(__file__))


def rearrange(lines: list[str]):
    output: list[str] = []

    for element in lines:

        line = element.strip()
        temp = ""

        line_left = line[0:8]
        line_right = line[8:16]

        for i in range(0, 8):
            temp += line_right[i] + line_left[i]

        output.append(temp[::-1])

    return output


def place_line(schem, line_nr, line, diag_offset, z_offset, repeater):

    for bit, char in enumerate(line):
        if char == "0":
            schem.setBlock((bit + 2 + diag_offset + (2 * line_nr), bit - (2 * line_nr) - diag_offset, 2 + z_offset),
                           "minecraft:white_stained_glass")
        elif char == "1":
            schem.setBlock((bit + 2 + diag_offset + (2 * line_nr), bit - (2 * line_nr) - diag_offset, 2 + z_offset),
                           repeater)


def main():
    schem = mcschematic.MCSchematic()

    bin_raw = open(os.path.join(here, "bin.txt"), "r").readlines()
    bin_rearranged = rearrange(bin_raw)

    for line_nr, line in enumerate(bin_rearranged[0:8]):
        place_line(schem, line_nr, line, 0, 0, "minecraft:repeater[facing=north]")
    for line_nr, line in enumerate(bin_rearranged[8:15]):
        place_line(schem, line_nr, line, 1, 0, "minecraft:repeater[facing=north]")

    for bit, char in enumerate(bin_raw[15][0:8][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 2, 2 * bit, 9), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 2, 2 * bit, 9), "minecraft:repeater[facing=north]")

    for bit, char in enumerate(bin_raw[15][8:16][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 18, 2 * bit - 16, 0), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 18, 2 * bit - 16, 0), "minecraft:repeater[facing=west]")

    for line_nr, line in enumerate(bin_rearranged[16:24]):
        place_line(schem, line_nr, line, 0, 3, "minecraft:repeater[facing=south]")
    for line_nr, line in enumerate(bin_rearranged[24:31]):
        place_line(schem, line_nr, line, 1, 3, "minecraft:repeater[facing=south]")

    for bit, char in enumerate(bin_raw[31][0:8][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 1, 2 * bit + 1, 11), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 1, 2 * bit + 1, 11), "minecraft:repeater[facing=south]")

    for bit, char in enumerate(bin_raw[31][8:16][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 18, 2 * bit - 16, 2), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 18, 2 * bit - 16, 2), "minecraft:repeater[facing=west]")

    for line_nr, line in enumerate(bin_rearranged[32:40]):
        place_line(schem, line_nr, line, 1, 8, "minecraft:repeater[facing=north]")
    for line_nr, line in enumerate(bin_rearranged[40:47]):
        place_line(schem, line_nr, line, 2, 8, "minecraft:repeater[facing=north]")

    for bit, char in enumerate(bin_raw[47][0:8][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 2, 2 * bit + 1, 13), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 2, 2 * bit + 1, 13), "minecraft:repeater[facing=south]")

    for bit, char in enumerate(bin_raw[47][8:16][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 18, 2 * bit - 14, 6), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 18, 2 * bit - 14, 6), "minecraft:repeater[facing=south]")

    for line_nr, line in enumerate(bin_rearranged[48:56]):
        place_line(schem, line_nr, line, 1, 11, "minecraft:repeater[facing=south]")
    for line_nr, line in enumerate(bin_rearranged[56:63]):
        place_line(schem, line_nr, line, 2, 11, "minecraft:repeater[facing=south]")

    for bit, char in enumerate(bin_raw[63][0:8][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 3, 2 * bit + 1, 13), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 3, 2 * bit + 1, 13), "minecraft:repeater[facing=south]")

    for bit, char in enumerate(bin_raw[63][8:16][::-1].strip()):
        if char == "0":
            schem.setBlock((2 * bit + 19, 2 * bit - 15, 14), "minecraft:white_stained_glass")
        else:
            schem.setBlock((2 * bit + 19, 2 * bit - 15, 14), "minecraft:repeater[facing=south]")

    schem.save("C:/Users/Oem/PycharmProjects/schematic", "ms", mcschematic.Version.JE_1_16_5)


if __name__ == "__main__":
    main()
