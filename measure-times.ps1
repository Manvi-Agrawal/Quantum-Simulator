
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
