# pyLMC - Simple Little Man Computer interpretor

Usage: See `main.py`

## Load asm file:
```python
lmc = LMC('fib.lmc')
lmc.run()
```

## Load asm file and save mailbox:
```python
lmc = LMC('fib.lmc')
lmc.saveMailbox('fib.mailbox')
lmc.run()
```

## Load mailbox:
```python
lmc = LMC('fib.mailbox', True)
lmc.run()
```

## Run verbosely:
```python
lmc.run(True)
```
