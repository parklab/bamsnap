
## download docker image
# docker pull danielmsk/bamsnap

SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
LOCALTESTPATH=$SCRIPTPATH/../tests

docker run --rm -it -v $LOCALTESTPATH/../tests:/work danielmsk/bamsnap bamsnap -bam /work/data/test_SV1_softclipped_1.bam \
    -title "Clipped read" \
    -pos chr1:37775740 \
    -out /work/test/test_SV1-7.png \
    -bamplot coverage read \
    -margin 100 \
    -no_target_line \
    -show_soft_clipped \
    -read_color_by interchrom \
    -save_image_only

