# Carbon Name

a python library convert carbon number (organic chemistry) into its English name

## Usage

example

```python
import carbon_number

print(
    "the name of alkane with 11 carbons is",
    carbon_number.carbon_name(11) + carbon_number.suffix("alkane")
)
```

output

```plaintext
the name of alkane with 11 carbons is undecane
```

try to run test.py!

![test.py output](https://s2.loli.net/2023/08/15/tgJEL2TsmaSXWeq.png)

support range: 1~999
