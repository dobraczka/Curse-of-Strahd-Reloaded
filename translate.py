from pathlib import Path

if __name__ == "__main__":
    fp = Path("./Act I - Into the Mists/Arc B - Welcome to Barovia.md")
    with open(fp) as infile:
        inside_div_block = False
        current_div_block = []
        for line in infile:
            if "<div" in line:
                inside_div_block = True
            if inside_div_block:
                if line.startswith("<div class"):
                    current_div_block.append("> [!quote]\n")
                elif "</div>" in line:
                    inside_div_block = False
                    print("> ".join(current_div_block))
                    break
                else:
                    current_div_block.append(line.replace("<p>", "").replace("</p>", ""))
