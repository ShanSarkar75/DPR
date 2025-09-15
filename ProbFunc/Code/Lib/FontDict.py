# %%
"""
## Reusable font dictionaries and Unicode Defination (GREEK_CHAR)

**Author:** S. Sarkar

**Version:** 0.00

**Release:** Aug/2025

---
"""

# %%
"""
This module defines reusable font dictionaries and Unicode representations for Greek characters and integral symbols to standardize styling across plots 
and figures. Font presets are specified for different text elements such as axis labels, subtitles, and titles, using 'Times New Roman' for consistency. 

The Greek character mapping allows easy embedding of mathematical symbols in plots.

"""

# %%
"""
### For Debugging
"""

# %%
DEBUG = False# True#  Default Set it False
if DEBUG: import matplotlib.pyplot as plt


# %%
# Constants - Special Character 

GREEK_CHAR = {
  'Alpha'   :'\u0391',
  'Beta'    :'\u0392' ,
  'Gamma'   : '\u0393',
  'Delta'   : '\u0394',
  'Epsilon' : '\u0395',
  'Zeta'    : '\u0396',
  'Eta'     : '\u0397',
  'Theta'   : '\u0398',
  'Iota'    : '\u0399',
  'Kappa'   : '\u039A',
  'Lamda'   : '\u039B',
  'M: '     : '\u039C',
  'N: '     : '\u039D',
  'Xi'      : '\u039E',
  'Omicron' : '\u039F',
  'Pi'      : '\u03A0',
  'Rho'    : '\u03A1',
  'Sigma'    : '\u03A3' ,
  'Ta: '    : '\u03A4',
  'Upsilon'    : '\u03A5' ,
  'Phi'    : '\u03A6',
  'Chi'    : '\u03A7',
  'Psi'    : '\u03A8',
  'Omega'    : '\u03A9',
  'alpha'    : '\u03B1',
  'beta'    : '\u03B2',
  'gamma'    : '\u03B3',
  'delta'    : '\u03B4',
  'epsilon'    : '\u03B5',
  'zeta'    : '\u03B6',
  'eta'    : '\u03B7',
  'theta'    : '\u03B8',
  'iota'    : '\u03B9' ,
  'kappa'    : '\u03BA',
  'lamda'    : '\u03BB',
  'mu'    : '\u03BC',
  'nu'    : '\u03BD',
  'xi'    : '\u03BE' ,
  'omicron'    : '\u03BF' ,
  'pi'   : '\u03C0',
  'rho'    : '\u03C1' ,
  'sigma'    : '\u03C3',
  'ta: '    : '\u03C4',
  'upsilon'    : '\u03C5',
  'phi'    : '\u03C6',
  'chi'    : '\u03C7',
  'psi'    : '\u03C8',
  'omega' : '\u03C9',
}

# Define the integral symbol and the function
INTEGRAL = "\u222B"


# %%
"""
## Font Dictionary (Definations) 
"""

# %%
FontSmall = {'family': "Times New Roman",
            'color' :  'k',
            'weight': 'normal',
            'size'  : 7.5};
FontNorm9 = {'family': "Times New Roman",
            'color' :  'k',
            'weight': 'normal',
            'size'  : 9};

FontNorm10 = {'family': "Times New Roman",
              'color' :  'k',
              'weight': 'normal',
              'size'  : 10};

FontNorm11 = {'family': "Times New Roman",
              'color' :  'k',
              'weight': 'normal',
              'size'  : 11};

FontNorm12 = {'family': "Times New Roman",
              'color' :  'k',
              'weight': 'normal',
              'size'  : 12};

SubTitleFont = {'family': "Times New Roman",
                'color' :  'k',
                'weight': 'bold',
                'size'  : 12};

MainTitleFont = {'family': "Times New Roman",
                 'color' :  'k',
                 'weight': 'bold',
                 'size'  :  16};



# %%
"""
## Test Code
"""

# %%
if DEBUG:
    fonts = {
        'FontSmall': FontSmall,
        'FontNorm9': FontNorm9,
        'FontNorm10': FontNorm10,
        'FontNorm11': FontNorm11,
        'FontNorm12': FontNorm12,
        'SubTitleFont': SubTitleFont,
        'MainTitleFont': MainTitleFont,
    }    
    fig, ax = plt.subplots(figsize=(8, 6))

    y_pos = 0.9  # Start near top of plot
    y_step = 0.1

    for i, (name, fontdict) in enumerate(fonts.items()):
        ax.text(0.1, y_pos - i * y_step, f"This is {name}", fontdict=fontdict)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    
#---------------------------------------------------------
    print(f'INTEGRAL: {INTEGRAL}')
    for key in GREEK_CHAR:
        print(f"{key}: {GREEK_CHAR[key]}")    

# %%
