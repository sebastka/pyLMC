# pyLMC - Simple Little Man Computer interpretor in Python

Usage: See `main.py`

## Load asm file:
```python
lmc = LMC(filename: str)
```

## Load asm file and save mailbox:
```python
lmc = LMC(filename: str)
lmc.saveMailbox()
```

## Load mailbox:
```python
lmc = LMC('code.txt', True)
```

## Run:
```python
lmc.run()
```

## Run verbosely:
```python
lmc.run(True)
```
