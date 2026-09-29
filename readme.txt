Neo-tron was created with the following in mind:

 - One key per kana [not qwerty romaji]
 - All keys 1U from home if possible.  [not JIS kana]
 - Index, middle, and ring fingers should if possible hold most of the load. Pinky should limit its load to homerow. [not NICOLA]
 - Home thumb via one shot layer switch is very ergonomic. [not chorded as original TRON]
 - Turbid sounds should be placed logically, at the same position as the main kana key.  [not as per NICOLA]
 - SFBs should be reduced if possible. [けい、のい from original TRON eliminated]
 - Bad scissors should be reduced (bad scissor is index top row and middle bottom row).
 - Extreme stretching should be reduced.
 - Trigrams should be easy to press via roll or alternation.
 - Redirects should be reduced. 

TODO - Move ぁ to あ's location for logical positioning. 


JAPANESE KEYBOARD LAYOUT ANALYSIS
CORRECTED JIS TRADITIONAL FINGERING — FSPEED & LAYER-ACCESS METRICS REMOVED
==================================================================================================

Layouts: neo-tron, original TRON, NICOLA, JIS kana, Naginata
Corpus: llm-jp-wikipedia (uploaded japanese-wiki.json)
Corpus size: 1,970,361,017 characters


COVERAGE
--------------------------------------------------------------------------------------------------
All five layouts cover the same corpus inventory. The only omissions are the extremely rare
ゑ ゐ ゎ ゕ ゖ.

FULL COMPARISON - FIVE LAYOUTS
--------------------------------------------------------------------------------------------------
Metric                                      neo-tron          TRON        NICOLA           JIS      Naginata
--------------------------------------------------------------------------------------------------
Character SFB %                                6.739         7.270         5.509        10.015         8.684
Character SFS-1 %                              9.687         9.940         8.560        10.700        11.523
Total rolls %                                 33.659        33.530        39.478        36.691        35.331
Clean alternates %                            30.841        29.934        22.738        19.827        21.528
Total alternates %                            41.490        40.328        31.443        27.483        32.387
Strict redirects %                             6.630         7.122        11.058        10.938         9.238
Full scissors %                                1.477         1.741         1.449         6.710         2.355
Max main-finger load %                        18.868        21.164        16.053        22.470        21.650


TRIGRAM FLOW - CHARACTER TARGET KEYS
--------------------------------------------------------------------------------------------------
Metric                                      neo-tron          TRON        NICOLA           JIS      Naginata
Inrolls %                                     16.929        17.414        23.198        18.881        17.668
Outrolls %                                    16.730        16.116        16.279        17.810        17.663
Total rolls %                                 33.659        33.530        39.478        36.691        35.331
Onehands / 3-rolls %                           1.734         1.766         2.507         2.987         2.142
Clean alternates %                            30.841        29.934        22.738        19.827        21.528
Alternate-SFS %                               10.649        10.394         8.705         7.656        10.859
Total alternates %                            41.490        40.328        31.443        27.483        32.387
3-finger redirects %                           3.606         3.889         6.231         5.470         4.444
Redirect-SFS %                                 3.024         3.233         4.826         5.468         4.794
Total strict redirects %                       6.630         7.122        11.058        10.938         9.238

FINGER LOAD - CHARACTER TARGET KEYS
--------------------------------------------------------------------------------------------------
Finger            neo-tron          TRON        NICOLA           JIS      Naginata
LP                   6.859         6.859         8.614         8.252         3.081
LR                  10.913         9.082        16.053         9.600         6.279
LM                  11.068        12.646        11.421        14.425        13.554
LI                  18.353        16.242        13.268        22.470        21.650
RI                  18.868        21.164        15.363        16.142        17.359
RM                  13.401        13.468        11.896         9.476        19.188
RR                   9.908         9.908        12.919         9.296        12.512
RP                  10.630        10.630        10.465        10.339         6.377


WORST SFBs — ALL OUTPUT LAYERS
--------------------------------------------------------------------------------------------------
Layout          #1              #2              #3              #4              #5
Neo-TRON        いき 0.1603%    えい 0.1435%    では 0.1340%    ると 0.1128%    いを 0.1001%
TRON            けい 0.2656%    いの 0.2176%    いき 0.1603%    えい 0.1435%    では 0.1340%
NICOLA          ん、 0.1471%    には 0.1410%    くの 0.1215%    う。 0.1178%    かし 0.1152%
JIS             こう 0.7320%    いし 0.4594%    うか 0.2722%    った 0.2605%    うき 0.2136%
Naginata        た。 0.3990%    いる 0.2537%    いん 0.2151%    さく 0.1501%    し、 0.1439%


WORST BASE-LAYER SFBs 1-5 RANKING — ALL FIVE LAYOUTS COMBINED
--------------------------------------------------------------------------------------------------
Rank    Layout          SFB     Frequency
1       JIS             こう    0.7320%
2       JIS             いし    0.4594%
3       JIS             うか    0.2722%
4       Naginata        いる    0.2537%
5       TRON            いの    0.2176%

NOTES
--------------------------------------------------------------------------------------------------
• Rolls, alternates, redirects and finger load are calculated from character target keys.
• Layer access is treated as neutral for comparison purposes. Metrics describe the resulting character
  target-key geometry and frequency patterns only.
