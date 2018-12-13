# prep-LaSSO
Prepare input files for LaSSO - Lariat Sequence Site Origin *software* (https://github.com/dbitton/LaSSO.git)

## Getting Started

Clone this repository into your local machine

```
git clone https://github.com/fernandalpcosta/prep-LaSSO.git
```

LaSSO *software* require two input files to make the database. The first one is a file with all the intron sequences. The second one is a file with some important information about those introns, the header file.

To understand all the fields that the header file needs to have, take a look inside LaSSO.R script at https://github.com/dbitton/LaSSO/blob/master/LaSSO.R
 
Here, I made a simple script to create the input header file for LaSSO, called getHeaderLaSSO.py


### Prerequisites

* Python3 installed in your machine
* Gff3 file with just intron information
* Gff3 file with just exon information

### Installing

No installation is required, the script is ready to use (executable).

```
python3 getHeaderLaSSO.py
```

## Usage

Once you have ran the getHeaderLaSSO.py script, it will prompt for two files, the gff3 of your introns and gff3 of your exons.

Important: both files has to be from the same source, compatible in ids. On other words, from the same genome version.

## Authors

* **Fernanda Luz P Costa** - *Initial work* - [ferandalpcosta](https://github.com/fernandalpcosta)

## License

Open-source

