
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
LOCALTESTPATH=$SCRIPTPATH/../tests

docker run --rm -it -v $LOCALTESTPATH/../tests:/work aveit/bamsnap bamsnap \
    --bam /work/data/test_SV1_softclipped_1.bam \
    --title "Clipped read" \
    --pos chr1:37775740 \
    --out /work/test/test_SV1-8.png \
    --bamplot "coverage,read" \
    --margin 100 \
    --no-target-line \
    --show-soft-clipped \
    --read-color-by interchrom \
    --save-image-only