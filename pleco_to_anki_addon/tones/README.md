# pinyin tone converter 🔢
Converts Mandarin pinyin with tone numbers to pinyin with tone marks.

Example:
> numerical:  
> bao1 guo3
>
> tone marks:  
> bāo guǒ

# how to use

To try out the converter,  use the [cli tool](https://github.com/em-shea/tones/blob/master/cli.py). This tool prompts the user to input numerical pinyin and returns pinyin with tone marks.

The main function 'convert_from_numerical_pinyin' is found in [numerical_pinyin_converter.py](https://github.com/em-shea/tones/blob/master/numerical_pinyin_converter.py). This function takes a numerical pinyin string ("bao1 guo3") as input and returns a converted string ("bāo guǒ").

```python 
from numerical_pinyin_converter import convert_from_numerical_pinyin

convert_from_numerical_pinyin("bao1 guo3") # Returns bāo guǒ
```

As an example use case, [csv_example](https://github.com/em-shea/tones/tree/master/csv_example) includes a [wrapper](https://github.com/em-shea/tones/blob/master/csv_example/csv_wrapper.py) for the converter to take a csv file as input and output a new, modified csv file. There are example original and modified csv files included.

# what is pinyin

[Pinyin](https://en.wikipedia.org/wiki/Pinyin) is the most commonly used romanization system for Mandarin. Numerical pinyin is often used to avoid issues with utf8 encoding. Where utf8 encoding is not a concern, pinyin with tone marks is generally preferred.
