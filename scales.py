###########################################################################
# Sarah's Piano Grade 8 Scales List
# Generates a random scale from the list 'scales'
# Total number of scales: 96, in 6 different keys (16 per key)
# Good luck with your exam!
###########################################################################

import random

scales = [
    # G
    "G maj SM scale 4 oct",
    "G maj CM scale 2 oct",

    "G har min SM scale 4 oct",
    "G har min CM scale 2 oct",

    "G mel min SM scale 4 oct",

    "G SM chromatic scale 4 oct",
    "G CM chromatic scale 2 oct, start an octave apart",

    "G maj SM arpeggio 4 oct + invs",
    "G maj CM arpeggio 2 oct + invs",

    "G min SM arpeggio 4 oct + invs",
    "G min CM arpeggio 2 oct + invs",

    "G Dom 7th 3 oct HS (start from a fifth up)",

    "G maj octaves 2 oct SM",
    "G har min octaves 2 oct SM",
    "G mel min octaves 2 oct SM",

    "Chromatic 3rds from G, H.S. 2 8ves",

    ###############################################

    # A
    "A maj SM scale 4 oct",
    "A maj CM scale 2 oct",

    "A har min SM scale 4 oct",
    "A har min CM scale 2 oct",

    "A mel min SM scale 4 oct",

    "A SM chromatic scale 4 oct",
    "A CM chromatic scale 2 oct, start an octave apart",

    "A maj SM arpeggio 4 oct + invs",
    "A maj CM arpeggio 2 oct + invs",

    "A min SM arpeggio 4 oct + invs",
    "A min CM arpeggio 2 oct + invs",

    "A Dom 7th 3 oct HS (start from a fifth up)",

    "A maj octaves 2 oct SM",
    "A har min octaves 2 oct SM",
    "A mel min octaves 2 oct SM",

    "Chromatic 3rds from A, H.S. 2 8ves",
    ###############################################

    # B
    "B maj SM scale 4 oct",
    "B maj CM scale 2 oct",

    "B har min SM scale 4 oct",
    "B har min CM scale 2 oct",

    "B mel min SM scale 4 oct",

    "B SM chromatic scale 4 oct",
    "B CM chromatic scale 2 oct, start an octave apart",

    "B maj SM arpeggio 4 oct + invs",
    "B maj CM arpeggio 2 oct + invs",

    "B min SM arpeggio 4 oct + invs",
    "B min CM arpeggio 2 oct + invs",

    "B Dom 7th 3 oct HS (start from a fifth up)",

    "B maj octaves 2 oct SM",
    "B har min octaves 2 oct SM",
    "B mel min octaves 2 oct SM",

    "Chromatic 3rds from B, H.S. 2 8ves",

    ##############################################

    # EFLAT
    "EFLAT maj SM scale 4 oct",
    "EFLAT maj CM scale 2 oct",

    "EFLAT har min SM scale 4 oct",
    "EFLAT har min CM scale 2 oct",

    "EFLAT mel min SM scale 4 oct",

    "EFLAT SM chromatic scale 4 oct",
    "EFLAT CM chromatic scale 2 oct, start an octave apart",

    "EFLAT maj SM arpeggio 4 oct + invs",
    "EFLAT maj CM arpeggio 2 oct + invs",

    "EFLAT min SM arpeggio 4 oct + invs",
    "EFLAT min CM arpeggio 2 oct + invs",

    "EFLAT Dom 7th 3 oct HS (start from a fifth up)",

    "EFLAT maj octaves 2 oct SM",
    "EFLAT har min octaves 2 oct SM",
    "EFLAT mel min octaves 2 oct SM",

    "Chromatic 3rds from EFLAT, H.S. 2 8ves",

    ###########################################

    # AFLAT/ GSHARP
    "AFLAT maj SM scale 4 oct",
    "AFLAT maj CM scale 2 oct",

    "AFLAT har min SM scale 4 oct",
    "AFLAT har min CM scale 2 oct",

    "AFLAT mel min SM scale 4 oct",

    "AFLAT SM chromatic scale 4 oct",
    "AFLAT CM chromatic scale 2 oct, start an octave apart",

    "AFLAT maj SM arpeggio 4 oct + invs",
    "AFLAT maj CM arpeggio 2 oct + invs",

    "AFLAT min SM arpeggio 4 oct + invs",
    "AFLAT min CM arpeggio 2 oct + invs",

    "AFLAT Dom 7th 3 oct HS (start from a fifth up)",

    "AFLAT maj octaves 2 oct SM",
    "AFLAT har min octaves 2 oct SM",
    "AFLAT mel min octaves 2 oct SM",

    "Chromatic 3rds from AFLAT, H.S. 2 8ves",
    ###########################################

    # DFLAT/ CSHARP
    "DFLAT maj SM scale 4 oct",
    "DFLAT maj CM scale 2 oct",

    "DFLAT har min SM scale 4 oct",
    "DFLAT har min CM scale 2 oct",

    "DFLAT mel min SM scale 4 oct",

    "DFLAT SM chromatic scale 4 oct",
    "DFLAT CM chromatic scale 2 oct, start an octave apart",

    "DFLAT maj SM arpeggio 4 oct + invs",
    "DFLAT maj CM arpeggio 2 oct + invs",

    "DFLAT min SM arpeggio 4 oct + invs",
    "DFLAT min CM arpeggio 2 oct + invs",

    "DFLAT Dom 7th 3 oct HS (start from a fifth up)",

    "DFLAT maj octaves 2 oct SM",
    "DFLAT har min octaves 2 oct SM",
    "DFLAT mel min octaves 2 oct SM",

    "Chromatic 3rds from DFLAT, H.S. 2 8ves",
    ###########################################
]

print(random.choice(scales))
print('======')
print(len(scales))