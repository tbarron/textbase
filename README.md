# textbase -- editing, browsing, searching text files

 * $TEXTBASE_ROOT indicates where the text files should be stored.

 * Different collections of text files can be created in different root
   directories and accessed by changing the value of TEXTBASE_ROOT

 * For example,

         alias mydoc="TEXTBASE_ROOT=$HOME/ref/mydoc python textbase"
