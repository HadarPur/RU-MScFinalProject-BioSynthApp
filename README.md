# Flexible and comprehensive software app for design of synthetic DNA sequences without unwanted patterns

## Pre-Requisite

Please execute the following command within your working environment:

```
pip3 install -r requirements.txt
```

## Pre Processing

To operate the application, the user must provide the following **three input text files**:

1. **Target sequence file** – a plain text file containing a DNA sequence composed exclusively of the characters A, T,
   G, and C. The sequence must be provided on a **single continuous line**. For example:

    ```
    ATAGTACATATC
    ```

2. **Unwanted pattern list** – a plain text file containing DNA patterns (substrings) that should be eliminated from the
   target sequence. Each pattern must appear **on a separate line**, separated by whitespace. For example:

    ```
    TAGTAC
    ATATCA
    ```

3. **Codon usage file** – a plain-text file that defines the relative codon usage frequencies for a specific organism.
   To obtain and prepare this file:

   ### Step 1: Extract Codon Usage Data

    1. Visit the Kazusa Codon Usage Database:  
       https://www.kazusa.or.jp/codon/

    2. Under the **QUERY Box for search with Latin name of organism**, enter the name of the organism. For example:  
       `Marchantia polymorpha`

    3. Click the **Submit** button.

    4. In the search results, locate the desired genome type (e.g., `chloroplast`) and click the corresponding link
       under the `Link` column.

    5. The codon usage table will appear. Ensure to choose a format and then click **submit**. You should see the
       following header:

        ```
        fields: [triplet] [amino acid] [fraction] [frequency: per thousand] ([number])
        ```

    6. Select the entire codon usage table (not including the header), for example:

        ```
        UUU F 0.94 63.5 (  1558)  UCU S 0.40 25.8 (   634)  UAU Y 0.89 33.4 (   820)  UGU C 0.85  8.6 (   212)
        UUC F 0.06  4.4 (   107)  UCC S 0.05  3.0 (    73)  UAC Y 0.11  4.1 (   100)  UGC C 0.15  1.5 (    38)
        ...
        ```

    7. Copy and paste it into a plain text file.

    8. Save the file.

   ### Step 2: Convert to BioSynth Format

    1. Make sure you have the local script named `convert_kazusa_to_biosynth.py`. It should be under the BioSynth
       directory.

    2. This script reads the codon usage file you just created and outputs a two-column text file in the format required
       by the BioSynth app: each line should contain a codon followed by its usage frequency, separated by whitespace.

    3. Run the script from the command line:

        ```bash
        python3 ./convert_kazusa_to_biosynth.py <codon_usage_file_path>
        ```

    4. The output file `biosynth_codon_usage.txt` will contain lines like:

        ```
        TAC 0.56
        GCT 0.89
        ...
        ```

   This transformation ensures that rare codons have higher substitution costs, reflecting biological codon bias.

   **Note:**  
   If you wish to get the table from another resource, please make sure to write your own converter script to ensure
   that you are in the right format.

## Executing the Terminal Program

To execute the elimination tool via the terminal, use the following command:

```
python3 ./BioSynth.py -s <seq_file_path> -p <pattern_file_path> -c <codon_usage_file_path> -a <transition_substitution_cost> -b <transversion_substitution_cost> -w <non_synonymous_substitution_cost>
```

### Examples
For example, you can run the program using short options:

```
python3 ./BioSynth.py -s ./files/no_coding/s_file_no_coding.txt -p ./files/no_coding/p_file_no_coding.txt -c ./files/no_coding/biosynth_codon_usage.txt -a 1.02 -b 1.98 -w 99.96
```

Or, with the full option names:

```
python3 ./BioSynth.py --s_path ./files/no_coding/s_file_no_coding.txt \
--p_path ./files/no_coding/p_file_no_coding.txt \
--c_path ./files/no_coding/biosynth_codon_usage.txt \
--alpha 1.02 --beta 1.98 --w 99.96
```

## Executing the Graphical User Interface (GUI)

To launch the graphical user interface of the elimination tool, run:

```
python3 ./BioSynth.py -g
```

You're all set! 🚀
