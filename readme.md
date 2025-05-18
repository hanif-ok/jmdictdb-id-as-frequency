# JmdictDB ID as Frequency for Yomitan

This dictionary was made as a workaround to add [JmdictDB](https://www.edrdg.org/jmdictdb/index.html) IDs for use in [Japanese Kanji Study - 漢字学習](https://play.google.com/store/apps/details?id=com.mindtwisted.kanjistudy&hl=en_SG/) through anki using the {frequency-average-occurrence} handlebar.

(as a caveat, this dictionary will not work with other frequency dictionaries)

This dictionary extracts the {url} tag from the [Jitendex](https://github.com/stephenmk/Jitendex) dictionary as a base. 

## Usage
1. Import the zip through yomitan
2. Disable all other frequency dictionaries 
3. In Anki tab of yomitan settings, configure anki flash card and Change Model toKanji Study Word Model v3
4. change the ID field to {frequency-average-occurrence}

After this, ankidroid cards made with yomitan should be able to open to open the kanji study app by clicking expressions on the back card.
## Download
A.Download the latest release from the release tab

B. To convert from other jitendex versions, pull from the repository, run the python file, then zip up the result and the index.json file.

