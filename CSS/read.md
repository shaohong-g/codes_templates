## Prequisite
1. Live Server extension (VSCode)


## Practice
- Reset styling during initilization
    ```
    <!-- Reset styling -->
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box; # content + padding
    }
    ```
- Difference between % and vw/vh
    ```css
    <!-- vw does not take into account of the additional scrollbars -->
    body {width:100%} # better choice since you do not want horizontal scrollbar to appear
    body {width:100vw}
    ```
- Font family
    - [Google fonts](https://fonts.google.com/)


## Common tags
1. text
    - font-size
    - font-family
        - Set more than one font so that should one fails, the other font will be selected
    - font-style
    - font-weight
    - text-transform
        - uppercase
        - capitalize
    - text-align
        - left
        - justify
        - right
    - text-indent (use em unit)
    - font
        - inherit
    - text-decoration
        - line-through
        - none
        - underline
    - line-height
    - letter-spacing / word-spacing (em unit)
2. Color
    - color
    - background-color
3. Others
    - border
        - 3px solid black
    - min-height
    - margin
    - padding

## Theories
1. Three types of CSS
    - Inline CSS
    ```html
    <p style="color:gray">Inline CSS takes precedent over the other two<p>
    ```
    - Internal or Embedded CSS
    ```html
    <style>
        .p {
            text-align: center;
        }
    </style>
    ```
    - External CSS
    ```html
    <link rel="stylesheet" href="style.css" />
    ```
2. Selectors
    - tags : body, p
    - classes : .firstClass, .secondClass
    - id : #firstId, #SecondId (Must be unique)
3. Rules
    - Group selectors into common style 
    ```css
    h1, h2 {color: blue}
    ```
    - Style nested selectors (in this case, h2 tags that are nested within a h1 tag)
    ```css
    h1 h2 {color: blue}
    ```
    - Precedent over css styles as follows: `ID > class > tags`
    ```css
    <!-- Result is Brown in color as it takes precedent -->
    #test {
    color: brown;
    }
    .test {
        color: black;
    }
    p {
        color:aquamarine;
    }
    ```
    - `!important` overwrite the existing rules (not recommended)
    ```css
    <!-- color will be aquamarine -->
    p !important {color:aquamarine;}
    p {color:black;}
    ```
    - Pseudo class (placement matters)
    ```css
    a:visited {color: purple} # after click/visited
    a:hover {color: purple} # hovering
    a:active {color: purple} # onclick
    a:focus {color: purple} 
    ```
4. Colors - How can you identify colors [Color picker and constrast](https://coolors.co/)
    - color name
    - rbg(0,0,0)
    - rgba(0,0,0,0.5) #Last value is the transpancy value
    - hexadecimal codes (#000000 - black)
        - can use color palette
    - hsl : hue, saturation, lightness (0, 100%, 50%)
5. Length Units (Root is default to 16px if not specified)
    - px : absolute unit
    - % : percentage relative to the parent unit
    - rem : relative to the root element (2rem = 32px)
    - em : relative to the parent unit
        - use more for padding, margin etc
    - ch : limit number of characters in a single line
    - vw : % relative to viewpoint width
    - vh : % relative to viewpoint height
6. CSS Box model
    - Margin > border > padding > content
    - Margin / Padding
        - Either use margin-right, padding-right etcetc
        - shorthand using margin/padding
            - top/bottom, left/right
            - top, right/left, bottom
            - top, right, bottom, left
            - auto -> set it center
7. display
    - inline
        - span view but elements inside does not affect box-size
    - block
        - paragraph for each element
    - inline-block
    - flow-root

## Dive deep
- Hyperlinks
    ```css
    a {
        text-decoration: none; # Default is underline
        cursor: not-allowed; # Default is pointers
        color: blue;
    }
    ```





Sites
https://stackoverflow.com/questions/19206919/how-to-create-checkbox-inside-dropdown

https://www.w3schools.com/cssref/css_selectors.php

https://webdeasy.de/en/top-css-buttons-en/

https://css-tricks.com/snippets/css/a-guide-to-flexbox/