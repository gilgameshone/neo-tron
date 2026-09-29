TRON FULL-LAYER COMPARISON — Japanese Wikipedia corpus
========================================================================

Layouts compared:
  Layout 1: neo-tron
  Layout 2: tron (original TRON)

Input files:
  neo-tron.dof
  tron.dof
  japanese.json

Corpus: japanese
  Characters : 342,469,956
  Bigrams    : 342,206,919
  Skipgrams  : 341,943,883
  Trigrams   : 341,943,883

Coverage of the Japanese corpus:

  Character coverage : 99.999364%
  Bigram coverage    : 99.998729%
  Skipgram coverage  : 99.998732%
  Trigram coverage   : 99.998099%

The only corpus characters not represented are extremely rare:
  ゑ  ゐ  ゎ  ゕ  ゖ
Together they account for only about 0.000636% of corpus characters.

Parsing note:
  Full-width spaces were treated as empty keys. 

LAYER-ACCESS COST MODEL
------------------------------------------------------------------------
You asked for a layer change to count as one additional key press, while
also treating it as substantially preferable to a finger movement two rows
away from the home row (as in the JIS-kana comparison you described).

The layer split is:

                           neo-tron        TRON
  Base                       70.045%       70.045%
  Red                        13.619%       12.620%
  Blue                       15.054%       16.539%
  Purple                      1.282%        0.796%
  ------------------------------------------------
  Any non-base layer         29.955%       29.955%

Because both layouts place exactly the same total character frequency off
the base layer, a simple one-shot model gives exactly the same layer cost:

  Symbol key press                      1.0000 presses / character
  Extra layer press                     0.2995 presses / character
  Effective KSPC                        1.2995 presses / character

This is the most straightforward interpretation if every non-base symbol
requires one extra layer-access press.

A stricter state-transition interpretation gives:

                           neo-tron        TRON
  Layer-changing bigrams      49.331%       48.969%
  Effective KSPC               1.4933        1.4897

Under that model neo-tron incurs only about +0.0036 presses/character more
than TRON (+0.24% relative).

If returning to base is a release rather than another key press, and only
entering a new non-base layer costs a press:

                           neo-tron        TRON
  Non-base entry events        26.628%       26.266%
  Effective KSPC               1.2663        1.2627


CORE COMPARISON — logical symbol-key movement
------------------------------------------------------------------------
These metrics map each kana to its physical row/column/finger on its layer.
They ignore the physical position of the layer-selector key itself.

Metric                          neo-tron        TRON     Δ neo−TRON   relative
----------------------------------------------------------------------------------
SFB (different physical keys)      6.713%      7.257%      -0.544 pp      -7.5%
DSFB (1-key skip)                  9.692%      9.966%      -0.274 pp      -2.7%
Scissors — all                    3.017%      2.732%      +0.285 pp     +10.4%
Scissors — inward-top             1.310%      1.460%      -0.149 pp     -10.2%
Scissors — outward-top            1.706%      1.273%      +0.434 pp     +34.1%
Pinky–ring bigrams                3.145%      2.958%      +0.187 pp      +6.3%
Lateral stretches (proxy)         5.679%      5.648%      +0.031 pp      +0.6%
Same-position symbol pairs        2.017%      1.996%      +0.021 pp      +1.1%
Same-character repeats            0.792%      0.792%      +0.000 pp      +0.0%

Scissor definition:
  same hand, top-row ↔ bottom-row, using adjacent fingers or fingers one
  apart.

"Inward-top":
  the finger closer to the thumb is on the TOP row.

"Outward-top":
  the reverse orientation.


LAYER-AWARE DIRECT-BIGRAM VIEW
------------------------------------------------------------------------
If a literal layer-change key press occurs between two symbols that are on
different layers, then those two symbol keys are not consecutive physical
keypresses. For that reason it is useful to split SFB/scissor frequency into
same-layer and cross-layer portions.

Metric                          neo-tron        TRON     Δ neo−TRON
------------------------------------------------------------------------
SFB — same layer                  3.317%      3.523%      -0.206 pp
SFB — cross layer                 3.395%      3.734%      -0.339 pp

Scissors — same layer             1.919%      1.713%      +0.206 pp
Scissors — cross layer            1.097%      1.019%      +0.079 pp

Inward-top — same layer           0.966%      0.998%      -0.032 pp
Inward-top — cross layer          0.344%      0.462%      -0.117 pp

Outward-top — same layer          0.953%      0.715%      +0.238 pp
Outward-top — cross layer         0.753%      0.557%      +0.196 pp

Under a strict "layer change = intervening keypress" model, the same-layer
SFB value is the cleaner estimate of direct consecutive symbol-key SFBs:

  neo-tron : 3.317%
  TRON     : 3.523%

That is a 5.8% relative reduction for neo-tron.

Cross-layer pairs still matter as hand movement, but their exact physical
sequence cannot be scored without knowing the layer-selector key position
and finger.


TRIGRAM MOVEMENT COMPARISON
------------------------------------------------------------------------
These use the same hand/finger classifier as the previous base-only report.
They are logical-symbol trigrams. Cross-layer trigrams may contain inserted
layer-change presses in real typing, so they are comparative rather than an
exact physical-keystroke simulation.

Metric                              neo-tron        TRON     Δ neo−TRON
------------------------------------------------------------------------
Inrolls (mixed-hand)                 16.955%     17.434%      -0.478 pp
Outrolls (mixed-hand)                16.766%     16.093%      +0.674 pp
One-hand inrolls                      0.795%      0.821%      -0.026 pp
One-hand outrolls                     0.949%      0.950%      -0.001 pp
Alternates                           30.877%     30.009%      +0.868 pp
Alternates (same finger return)      10.606%     10.369%      +0.237 pp
Redirects                             6.678%      7.157%      -0.480 pp
Mixed-hand SFB trigrams              10.135%     10.379%      -0.245 pp
One-hand SFB trigrams                 6.239%      6.788%      -0.549 pp

Total rolls                          35.466%     35.298%      +0.168 pp
Total alternates                     41.483%     40.378%      +1.105 pp
Total SFB-containing trigrams        16.373%     17.167%      -0.793 pp


HAND LOAD — all mapped characters
------------------------------------------------------------------------
                                  neo-tron        TRON     Δ neo−TRON
------------------------------------------------------------------------
L hand                              47.144%     44.800%      +2.344 pp
R hand                              52.856%     55.200%      -2.344 pp


FINGER LOAD — all mapped characters
------------------------------------------------------------------------
                                  neo-tron        TRON     Δ neo−TRON
------------------------------------------------------------------------
L pinky                              6.838%      6.838%      +0.000 pp
L ring                              10.984%      9.139%      +1.844 pp
L middle                            11.036%     12.625%      -1.589 pp
L index                             18.287%     16.198%      +2.088 pp

R index                             18.762%     21.035%      -2.273 pp
R middle                            13.497%     13.568%      -0.071 pp
R ring                               9.969%      9.969%      +0.000 pp
R pinky                             10.628%     10.628%      +0.000 pp


ROW LOAD — all mapped characters
------------------------------------------------------------------------
                                  neo-tron        TRON     Δ neo−TRON
------------------------------------------------------------------------
Top row                             25.985%     28.329%      -2.344 pp
Home row                            51.887%     51.887%      +0.000 pp
Bottom row                          22.128%     19.784%      +2.344 pp

Both layouts keep 100% of mapped symbol keys within one row of home.


TOP SFB CONTRIBUTIONS
(% of ALL corpus bigrams; pair directions merged)
------------------------------------------------------------------------
neo-tron                           TRON
  えい  0.1901%                     けい  0.3293%
  きい  0.1782%                     のい  0.2901%
  いす  0.1566%                     かに  0.1904%
  ると  0.1536%                     えい  0.1901%
  はで  0.1383%                     きい  0.1782%
  りつ  0.1372%                     きの  0.1584%
  れん  0.1314%                     いす  0.1566%
  とに  0.1244%                     ると  0.1536%
  をい  0.1241%                     はで  0.1383%
  もの  0.1228%                     れん  0.1314%
  う、  0.1159%                     をい  0.1241%
  し。  0.1108%                     う、  0.1159%
  いつ  0.1029%                     のち  0.1108%
  りお  0.1006%                     し。  0.1108%
  たま  0.0965%                     のつ  0.1078%
  はな  0.0936%                     とり  0.1072%
  おい  0.0893%                     いつ  0.1029%
  はの  0.0892%                     たま  0.0965%
  かさ  0.0850%                     ゅに  0.0954%
  りい  0.0843%                     はな  0.0936%


TOP DIRECT SAME-LAYER SFB CONTRIBUTIONS
(% of ALL corpus bigrams; pair directions merged)
------------------------------------------------------------------------
neo-tron                           TRON
  きい  0.1782%                     のい  0.2901%
  いす  0.1566%                     かに  0.1904%
  ると  0.1536%                     きい  0.1782%
  りつ  0.1372%                     きの  0.1584%
  れん  0.1314%                     いす  0.1566%
  とに  0.1244%                     ると  0.1536%
  をい  0.1241%                     れん  0.1314%
  もの  0.1228%                     をい  0.1241%
  う、  0.1159%                     う、  0.1159%
  し。  0.1108%                     し。  0.1108%
  いつ  0.1029%                     のつ  0.1078%
  たま  0.0965%                     とり  0.1072%
  はな  0.0936%                     いつ  0.1029%
  はの  0.0892%                     たま  0.0965%
  かさ  0.0850%                     はな  0.0936%


BIGGEST SFB CHANGES CAUSED BY NEO-TRON
(% of ALL corpus bigrams; negative = removed/reduced)
------------------------------------------------------------------------
Largest reductions:
  いけ   -0.3293 pp
  いの   -0.2901 pp
  かに   -0.1904 pp
  きの   -0.1584 pp
  ちの   -0.1108 pp
  つの   -0.1078 pp
  とり   -0.1072 pp
  にゅ   -0.0954 pp
  すの   -0.0763 pp
  おの   -0.0706 pp

Largest increases:
  つり   +0.1372 pp
  とに   +0.1244 pp
  のも   +0.1228 pp
  おり   +0.1006 pp
  のは   +0.0892 pp
  かさ   +0.0850 pp
  いり   +0.0843 pp
  での   +0.0836 pp
  なの   +0.0643 pp
  ての   +0.0595 pp

The single largest full-layout improvement is removal of the け/い SFB
present in original TRON, worth 0.3293% of all corpus bigrams.


TOP SCISSOR CONTRIBUTIONS
(% of ALL corpus bigrams; pair directions merged)
------------------------------------------------------------------------
neo-tron                           TRON
  この  0.2062%                     ょり  0.1988%
  り、  0.1644%                     はに  0.1640%
  はに  0.1640%                     くっ  0.1199%
  その  0.1217%                     き、  0.1118%
  くっ  0.1199%                     くす  0.1086%
  き、  0.1118%                     るな  0.1061%
  くす  0.1086%                     れ、  0.0746%
  るな  0.1061%                     あ、  0.0745%
  れ、  0.0746%                     こな  0.0695%
  あ、  0.0745%                     あっ  0.0669%
  こな  0.0695%                     るま  0.0583%
  あっ  0.0669%                     く。  0.0565%


WHAT CHANGED FROM THE BASE-ONLY ANALYSIS
------------------------------------------------------------------------
Base-only analysis:
  SFB                  neo 6.609%   TRON 6.905%   neo advantage 4.3%
  DSFB                 neo 9.729%   TRON 9.865%   neo advantage 1.4%
  inward-top scissors  neo 2.008%   TRON 2.088%   neo advantage 3.8%

Full-layer analysis:
  SFB                  neo 6.713%   TRON 7.257%   neo advantage 7.5%
  DSFB                 neo 9.692%   TRON 9.966%   neo advantage 2.7%
  inward-top scissors  neo 1.310%   TRON 1.460%   neo advantage 10.2%

Including the non-base layers therefore strengthens neo-tron's advantage
for SFB, DSFB, and the inward-top scissor direction.

The total-scissor tradeoff remains:
  neo-tron reduces the specifically undesirable inward-top direction,
  but increases outward-top scissors enough that total scissors are higher.


SUMMARY
------------------------------------------------------------------------
• Full-layer coverage is effectively complete: >99.998% for all n-gram
  measures used here.

• neo-tron reduces logical SFB from 7.257% to 6.713%:
  a 7.5% relative reduction.

• Under the stricter layer-aware direct-bigram view, same-layer SFB falls
  from 3.523% to 3.317%:
  a 5.8% relative reduction.

• DSFB falls from 9.966% to 9.692%:
  a 2.7% relative reduction.

• The inward-top scissor direction falls from 1.460% to 1.310%:
  a 10.2% relative reduction.

• Total scissors increase from 2.732% to 3.017% (+10.4%), because
  outward-top scissors rise from 1.273% to 1.706% (+34.1%).

• Total SFB-containing logical trigrams improve from 17.167% to 16.373%.

• Redirects improve from 7.157% to 6.678%.

• Total alternates rise from 40.378% to 41.483%.

• Hand balance improves:
    TRON     44.800% L / 55.200% R
    neo      47.144% L / 52.856% R

• A one-extra-press-per-non-base-symbol model gives the same layer cost
  for both layouts: 1.2995 keypresses per character.

• A strict layer-state transition model slightly favors TRON:
    neo  1.4933 KSPC
    TRON 1.4897 KSPC
  The difference is only 0.0036 presses per character.

• All mapped symbol keys remain within one row of the home row. Under the
  JIS-kana comparison assumption specified for this analysis, that extra
  low-travel layer actuation is treated as substantially preferable to a
  two-row finger reach.

Overall, the full-layer reassessment strengthens the evidence that neo-tron
improves same-finger behavior, the specifically targeted inward-top scissor
direction, hand balance, alternation, and redirects. Its clearest ergonomic
cost is the increase in outward-top scissors, plus a very small increase in
layer-state transition frequency under the strictest layer-toggle model.


METRIC DEFINITIONS / LIMITATIONS
------------------------------------------------------------------------
SFB:
  Adjacent corpus bigram where the two symbol keys use the same finger but
  occupy different physical row/column positions.

DSFB:
  Skipgram A?B where A and B use the same finger on different physical keys.

Scissors:
  Same-hand top↔bottom symbol movement using adjacent fingers or fingers one
  apart.

Lateral stretch proxy:
  Same-row, same-hand bigram separated by >=2 physical columns.

Pinky–ring:
  Same-hand bigram between pinky and ring fingers.

Layer cost:
  Reported separately because an extra key actuation and a long finger
  displacement are not ergonomically interchangeable.

Layer-selector limitation:
  The .dof files specify character positions on base/red/blue/purple layers,
  but do not specify the physical position/finger of the keys used to enter
  those layers. Therefore actual physical-key SFB/roll/redirect metrics that
  include the layer-selector key cannot be calculated exactly.

Trigram limitation:
  Trigram categories classify the symbol sequence, not the fully expanded
  physical keypress sequence with layer-selector presses inserted.

JIS limitation:
  No JIS layout/corpus mapping was supplied here, so the statement about
  two-row JIS reaches is treated as the comparison assumption requested for
  this report rather than a separately measured JIS score.

Fspeed / Score / Bad Redirects / Sft:
  Exact reproduction would require the scoring/category definitions or
  source code of the external analyser.
