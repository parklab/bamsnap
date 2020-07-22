import sys
import shlex
sys.path.append('..')
from src import bamsnap

bamsnap_prog = "src/bamsnap.py"

# -ref /Users/pcaso/db/DATA/PUB/reference/GRCh38d1/GRCh38_full_analysis_set_plus_decoy_hla.fa \
# -ref /home/mk446/park/SOFTWARE/REFERENCE/GRCh38d1/GRCh38_full_analysis_set_plus_decoy_hla.fa
# -bam /home/mk446/bio/DATA/AshkenazimTrio/hg38/HG002.x60/HG002.GRCh38.60x.1_addrg_bqsr.bam \
# /home/mk446/bio/DATA/AshkenazimTrio/hg38/HG003.x60/HG003.GRCh38.60x.1_addrg_bqsr.bam \
# /home/mk446/bio/DATA/AshkenazimTrio/hg38/HG004.x60/HG004.GRCh38.60x.1_addrg_bqsr.bam \
cmdlist = []
cmdlist.append("""
    -bam ./data/NA12877.bam ./data/NA12878.bam ./data/NA12879.bam \
    -title "NA12877 (Father)" "NA12878 (Mother)" "NA12879 (Daughter)" \
    -vcf ./data/NATRIO_test_30.vcf \
    -out ./out/NATRIO_test_30 \
    -ref /Users/pcaso/db/DATA/PUB/reference/GRCh38d1/GRCh38_full_analysis_set_plus_decoy_hla.fa \
    -save_image_only \
    -process 5
""")
cmdlist.append("""
    -bam ./data/NA12879.bam \
    -title "NA12879 (Daughter)" \
    -pos chr10:117542948 \
    -out ./out/NATRIO_chr10_117542948_1.png
""")
cmdlist.append("""
    -bam ./data/NA12879.bam \
    -title "NA12879 (Daughter)" \
    -pos chr10:117542948 \
    -margin 500 \
    -out ./out/NATRIO_chr10_117542948_2.png
""")
cmdlist.append("""
    -bam ./data/NA12879.bam \
    -title "NA12879 (Daughter)" \
    -pos chr10:117542948 \
    -out ./out/NATRIO_chr10_117542948.png \
    -read_group strand
""")
cmdlist.append("""
    -bam ./data/NA12877.bam ./data/NA12878.bam ./data/NA12879.bam \
    -title "NA12877 (Father)" "NA12878 (Mother)" "NA12879 (Daughter)" \
    -pos chr9:114786933 \
    -out ./out/NATRIO_chr9_114786933.png \
    -draw coordinates bamplot base gene \
    -bamplot coverage base read \
    -margin 50 -read_group strand -plot_margin_left 20 -plot_margin_right 20 -border
""")
cmdlist.append("""
    -bam ./data/NA12879.bam \
    -title "NA12879 (Daughter)" \
    -draw bamplot \
    -bamplot coverage base \
    -pos chr10:117542948 \
    -separator_height 0 \
    -margin 500 \
    -no_title \
    -width 700 \
    -plot_margin_top 0 \
    -plot_margin_bottom 0 \
    -out ./out/NATRIO_chr10_117542948_baseplot_ex1.png
""") # base plot example 1
cmdlist.append("""
    -bam ./data/NA12879.bam \
    -title "NA12879 (Daughter)" \
    -draw bamplot \
    -bamplot coverage base \
    -pos chr10:117542948 \
    -separator_height 0 \
    -margin 50 \
    -no_title \
    -width 700 \
    -plot_margin_top 0 \
    -plot_margin_bottom 0 \
    -out ./out/NATRIO_chr10_117542948_baseplot_ex2.png
""") # base plot example 2
cmdlist.append("""
    -bam ./data/NA12879.bam \
    -title "NA12879 (Daughter)" \
    -draw bamplot \
    -bamplot coverage base \
    -pos chr10:117542948 \
    -separator_height 0 \
    -margin 10 \
    -no_title \
    -width 700 \
    -plot_margin_top 0 \
    -plot_margin_bottom 0 \
    -out ./out/NATRIO_chr10_117542948_baseplot_ex3.png
""") # base plot example 3

cmdlist.append("""
    -bam ./data/NA12879.bam \
    -pos chr10:117542948 \
    -no_title \
    -draw coordinates \
    -out ./out/NATRIO_chr10_117542948_coordinates3.png \
    -no_target_line \
    -coordinates_axisloc middle
""") # coordinates track example 3


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
