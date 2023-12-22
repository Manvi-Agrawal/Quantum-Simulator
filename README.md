# Quantum Simulator
Quantum Simulator for basic gates in QASM(X, CX, H, T, T.dag() ).

## Run the simulator
```powershell
python simulator.py <path of QASM File>
```
### Sample Output
```powershell
python simulator.py .\test\sample\bell_state.qasm
```
```text
[(0.707+0j), 0j, 0j, (0.707+0j)]
```

## Testing the simulator
Use `compare_simulators.py` script.
```powershell
python compare_simulators.py <path of QASM File>
```

OR

```powershell
python compare_simulators.py <path of folder containing QASM Files>
```

### Sample From Testing script
``` powershell
python compare_simulators.py .\test\sample\
```
```text
==Simulator comparison : test\sample\bell_state.qasm==
True

 ==Simulator comparison : test\sample\hcancel.qasm==
True

==Simulator comparison : test\sample\tgate.qasm==
True

==Simulator comparison : test\sample\xgate.qasm==
True
```
