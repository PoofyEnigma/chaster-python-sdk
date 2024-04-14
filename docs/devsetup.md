`./.git/hooks/pre-commit`

```#!/bin/sh
#!/bin/sh
autopep8 --in-place --recursive ./src
autopep8 --in-place --recursive ./tests
pylint ./
python3 -m unittest
```

PyCharm is recommended

# References
[pre-commit](https://pre-commit.com/)