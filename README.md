# Quantum Simulator
Quantum Simulator for basic gates in QASM(X, CX, H, T, T.dag() ).

## Run the simulator
```powershell
python simulator.py <path of QASM File>
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
