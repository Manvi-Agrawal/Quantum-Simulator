# Sample Usage: .\measure-times.ps1 .\sample_qasm\ 6>>execution_times.txt
# where sample_qasm is folder containg QASM files and result is stored in execution_times.txt

[CmdletBinding()]
Param(
    [Parameter(Position=1)]
    $QasmDir = ""
)

$QasmFiles = Get-ChildItem  $QasmDir


foreach ($QasmFile in $QasmFiles)
{
    $ExecutionTime = Measure-Command { cs238.py $QasmFile } | Select-Object TotalMilliseconds
    Write-Host $QasmFile, $ExecutionTime.TotalMilliseconds
}
