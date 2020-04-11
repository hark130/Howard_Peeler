# Howard_Peeler
Howard's Peeler is a dedicated web scraper with built in logging and notification.  It was written in Python 3.6.9 and works best in Linux.

## FEATURES

1. HTML<br>
  a. Connect to URL<br>
  b. Download the HTML page<br>
  c. Parse the HTML<br>
  d. Determine availability<br>
    i.   button<br>
    ii.  time<br>
    iii. location chooser<br>
  e. Add something to cart (necessary?)<br>
2. Configuration<br>
  a. Config file or parameters<br>
  b. Poll frequency (every X minutes)<br>
  c. Poll deviation (plus or minus)<br>
  d. Scream frequency (every Y seconds)<br>
  e. Scream duration (number of screams or time duration)<br>
  f. [blink(1)](https://blink1.thingm.com/)<br>
3. Notification<br>
  a. "Scream" on a hit (espeak)<br>
4. Logging<br>
  a. Basic (screen or file)<br>
  b. Categories<br>
  c. Format (YYYYMMDD-HH:MM:SS HOPE <msg>)<br>
5. Miscellaneous<br>
  a. Obfuscated URL<br>
  b. Interrupt key/exit code<br>

NOTE: Branch names are based on the feature-task identifiers
