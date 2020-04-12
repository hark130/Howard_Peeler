# Howard_Peeler
Howard's Peeler is a dedicated web scraper with built in logging and notification.  It was written in Python 3.6.9 and works best in Linux.

## USAGE

`python3 src/HOPE/`

## FEATURES

1. HTML<br>
    1. Connect to URL<br>
    2. Download the HTML page<br>
    3. Parse the HTML<br>
    4. Determine availability<br>
        1. button<br>
        2. time<br>
        3. location chooser<br>
    5. Add something to cart (necessary?)<br>
2. Configuration<br>
    1. Config file or parameters<br>
    2. Poll frequency (every X minutes)<br>
    3. Poll deviation (plus or minus)<br>
    4. Scream frequency (every Y seconds)<br>
    5. Scream duration (number of screams or time duration)<br>
    6. [blink(1)](https://blink1.thingm.com/)<br>
3. Notification<br>
    1. ~~"Scream" on a hit (espeak)~~<br>
    2. Implement repeating "Scream"<br>
    3. Multithread the repeating "Scream"<br>
4. ~~Logging~~<br>
    1. ~~Basic (screen or file)~~<br>
    2. ~~Categories~~<br>
    3. ~~Datetime stamp (`YYYY-MM-DD HH:MM:SS HOPE Log message goes here`)~~<br>
5. Miscellaneous<br>
    1. ~~Obfuscated URL~~<br>
    2. Interrupt key/exit code<br>
6. Mulithreading<br>
    1. Write a module<br>
    2. Implement the "scream" in it's own thread<br>

NOTE: Branch names are based on the feature-task identifiers

## CODE REVIEWS

From the Howard_Peeler directory:

* `pycodestyle --max-line-length=100 .`
* Change `HOPE_Logger.__DEBUG__` to `False` before merging into master
