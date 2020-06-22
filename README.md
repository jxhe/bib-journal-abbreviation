# bib-journal-abbreviation
There are some bibtex tools out there to help abbreviate journal names. However, I found that those packages are often over-complicated with many functions and require extra dependencies which sometimes break in my early trial due to lack of maintenance. For the sole purpose of abbreviating journal names, this script provides a lightweight way to transform your latex bib file without extra dependencies. This script abbreviates the journal names according to the built-in data file `journals.json` from [betterbib](https://github.com/nschloe/betterbib). This data file should satisfiy the requirements in most cases but users can customize the abbreviations in their own json file as well. 



### Usage

```bash
cat /path/to/old/bib/file | python journal_abbrev.py > /path/to/new/bib/file
```

Users can specify their own extra abbreviation rules through customized json file with additionl argument to the python script as `--user-json` (refer to `customize_journal.json` for an example). The customized abbreviation rules would override the default one in the case of conflict.

### Acknowledgement
This is motivated by Wanzhen He.
