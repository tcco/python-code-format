# python-code-format

## Setup
Make sure the requirements from `requirements.txt` are added 
and installed into your virtualenv, usually `<app-root-direcotry>/.venv`


## pre-commit

### run with every commit

```
cd .git/hooks
ln -s ../../bin/pre-commit .

git add .
git commit -m "Hello World"
```

Add unit test runners & scripts to pre-commit.
Tox is usually a good choice for isolated testing.
sam validate is also commented out here but useful
if sam is used to deploy.

### manual

Code will only be checked after it has been staged

```
git add <some-python-file>

pre-commit run --all-files
```

## Resources

- [pre-commit](https://pre-commit.com/)
- [black](https://black.readthedocs.io/en/stable/)
- [bandit](https://bandit.readthedocs.io/en/latest/)
