import sys
import shlex
sys.path.append('..')
from src import bamsnap

bamsnap_prog = "src/bamsnap.py"


cmdlist = []
cmdlist.append("""
    -bam ./data/NA12879.bam_chr10_117542947.bam \
    -title "NA12879 (Daughter)" \
    -pos chr10:117542948 \
    -out ./out/NATRIO_chr10_117542948.png \
    -read_group strand
""")
cmdlist.append("""
    -bam ./data/NA12877.bam_chr9_114786932.bam ./data/NA12878.bam_chr9_114786932.bam ./data/NA12879.bam_chr9_114786932.bam \
    -title "NA12877 (Father)" "NA12878 (Mother)" "NA12879 (Daughter)" \
    -pos chr9:114786933 \
    -out ./out/NATRIO_chr9_114786933.png \
    -draw coordinates bamplot base gene \
    -bamplot coverage base read \
    -margin 50 -read_group strand -plot_margin_left 20 -plot_margin_right 20 -border
""")


def test_run():
    
    
    for cmd in cmdlist:
        # for k in range(10):
        #     cmd = cmd.replace('  ',' ')
        # print(cmd)
        cmd = bamsnap_prog + " " + cmd
        sys.argv = shlex.split(cmd)
        # print(cmd)
        # print(shlex.quote(sys.argv))
        bamsnap.cli()


if __name__ == "__main__":
    test_run()
