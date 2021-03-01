import sys
import shlex

sys.path.append('..')
bamsnap_prog = "src/bamsnap.py"
from src import bamsnap

# import bamsnap
# bamsnap_prog = "bamsnap"


cmdlist = []


cmdlist.append("""
    -bam ./data/test_SV1_softclipped_1.bam \
    -title "Clipped read" \
    -pos chr1:37775740 chr1:37775780 chr1:37775783 chr1:37775785 chr1:37775789 \
    -out ./out/test_SV1-7_proc1 \
    -bamplot coverage read \
    -margin 100 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -zipout \
    -save_image_only
""")

cmdlist.append("""
    -bam ./data/test_SV1_softclipped_1.bam \
    -title "Clipped read" \
    -pos chr1:37775740 chr1:37775780 chr1:37775783 chr1:37775785 chr1:37775789 \
    -out ./out/test_SV1-7_proc2 \
    -bamplot coverage read \
    -margin 100 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -zipout \
    -process 2 \
    -save_image_only
""")

def getopt(target_option):
    flag = False
    value = ""
    for opt1 in sys.argv:
        if flag:
            if opt1[0] == '-':
                break
            else:
                value += ' ' + opt1

        if opt1 == target_option:
            flag = True
    return value.strip()


def test_run():
    for cmd in cmdlist:
        # cmd = cmdlist[-1]
        cmd = bamsnap_prog + " " + cmd.strip()
        sys.argv = shlex.split(cmd)
        print(' '.join(sys.argv))
        # print(cmd)
        bamsnap.cli()

        out = getopt('-out')
        assert bamsnap.util.is_exist(out + '.zip') == True



if __name__ == "__main__":
    test_run()
