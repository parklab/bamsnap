import sys
import shlex

# sys.path.append('..')
# from src import bamsnap
# bamsnap_prog = "src/bamsnap.py"

import bamsnap
bamsnap_prog = "bamsnap"


# -ref /Users/pcaso/db/DATA/PUB/reference/GRCh38d1/GRCh38_full_analysis_set_plus_decoy_hla.fa \
# -ref /home/mk446/park/SOFTWARE/REFERENCE/GRCh38d1/GRCh38_full_analysis_set_plus_decoy_hla.fa
# -bam /home/mk446/bio/DATA/AshkenazimTrio/hg38/HG002.x60/HG002.GRCh38.60x.1_addrg_bqsr.bam \
# /home/mk446/bio/DATA/AshkenazimTrio/hg38/HG003.x60/HG003.GRCh38.60x.1_addrg_bqsr.bam \
# /home/mk446/bio/DATA/AshkenazimTrio/hg38/HG004.x60/HG004.GRCh38.60x.1_addrg_bqsr.bam \
cmdlist = []
cmdlist.append("""
    -bam ./data/test_SV1_softclipped_1.bam \
    -title "Clipped read" \
    -pos chr1:37775740 \
    -out ./out/test_SV1-7.png \
    -bamplot coverage read \
    -margin 100 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_softclipped_2.bam \
    -title "Clipped read" \
    -pos chr1:37775690 \
    -out ./out/test_SV1-8.png \
    -bamplot coverage read \
    -margin 100 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_softclipped.bam \
    -title "Clipped read" \
    -pos chr1:37775720 \
    -out ./out/test_SV1-5.png \
    -bamplot coverage read \
    -margin 100 \
    -no_target_line \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_softclipped.bam \
    -title "Clipped read" \
    -pos chr1:37775720 \
    -out ./out/test_SV1-6.png \
    -bamplot coverage read \
    -margin 100 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1.bam \
    -title "SVA example (chr1:37,776,131)" \
    -pos chr1:37776200 \
    -out ./out/test_SV1-1.png \
    -bamplot coverage read \
    -margin 50 \
    -no_target_line \
    -grid 1 \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1.bam \
    -title "SVA example (chr1:37,776,131)" \
    -pos chr1:37776131 \
    -out ./out/test_SV1-2.png \
    -bamplot coverage read \
    -margin 500 \
    -no_target_line \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_softclipped_3.bam \
    -title "SVA example (chr1:37775710)" \
    -pos chr1:37774190 \
    -out ./out/test_SV1-8.png \
    -bamplot coverage read \
    -margin 70 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_hardclipped_1.bam \
    -title "SVA example (chr1:37775710)" \
    -pos chr1:37774930 \
    -out ./out/test_SV1-9.png \
    -bamplot coverage read \
    -margin 30 \
    -no_target_line \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_chr1_37775710.bam \
    -title "SVA example (chr1:37775710)" \
    -pos chr1:37775710 \
    -out ./out/test_SV1-3.png \
    -bamplot coverage read \
    -margin 1000 \
    -no_target_line \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_chr1_37775710.bam \
    -title "SVA example (chr1:37775710)" \
    -pos chr1:37775710 \
    -out ./out/test_SV1-3_1.png \
    -bamplot coverage read \
    -margin 1000 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/test_SV1_chr1_37775710.bam \
    -title "SVA example (chr1:37775710)" \
    -pos chr1:37775710 \
    -out ./out/test_SV1-4.png \
    -bamplot coverage read \
    -margin 1000 \
    -no_target_line \
    -read_color_by strand \
    -save_image_only
""")
cmdlist.append("""
    -bam ./data/NA12877.bam ./data/NA12878.bam ./data/NA12879.bam \
    -title "NA12877 (Father)" "NA12878 (Mother)" "NA12879 (Daughter)" \
    -vcf ./data/NATRIO_test_3.vcf \
    -out ./out/NATRIO_test_3 \
    -save_image_only
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

cmdlist.append("""
    -bam ./data/test_INVERSION_4_180098865_hg19.bam\
    -pos 4:180098865 \
    -margin 300 \
    -title inversion \
    -bamplot coverage read \
    -out ./out/test_INV_1.png \
    -refversion hg19 \
    -read_color_by interchrom \
    -show_soft_clipped \
    -save_image_only
""")  # inversion example 1

cmdlist.append("""
    -bam ./data/test_DEL_4_180097876_180097877.bam \
    -pos 4:180097878-180098507 \
    -margin 1000 \
    -title deletion \
    -out ./out/test_DEL_1.png \
    -refversion hg19 \
    -show_soft_clipped \
    -read_color_by interchrom \
    -save_image_only
""")  # coordinates track example 3


cmdlist.append("""
    -bam ./data/test_noMDtag_1_102345_103355.bam \
    -pos 1:102545 \
    -margin 1000 \
    -title noMDtag \
    -out ./out/test_noMDtag_1.png \
    -refversion hg19 \
    -show_soft_clipped \
    -save_image_only
""")  # coordinates track example 3

def test_run():
    for cmd in cmdlist:
        # cmd = cmdlist[-1]
        cmd = bamsnap_prog + " " + cmd.strip()
        sys.argv = shlex.split(cmd)
        print(' '.join(sys.argv))
        # print(cmd)
        # print(shlex.quote(sys.argv))
        bamsnap.cli()
        # break


if __name__ == "__main__":
    test_run()
