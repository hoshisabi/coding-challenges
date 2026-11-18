<#
.SYNOPSIS
    Scaffold PE/Problems/ProblemNNNN.cs for a Project Euler problem.

.DESCRIPTION
    The stub's Solve throws NotImplementedException (shown as "not implemented")
    and its Checks list is empty: fill it with the small cases the statement gives
    before writing the solve.

.EXAMPLE
    ./new-problem.ps1 31
#>
param(
    [Parameter(Mandatory)][int]$Number
)

$ErrorActionPreference = 'Stop'
$nnnn = '{0:D4}' -f $Number
$file = Join-Path $PSScriptRoot "PE/Problems/Problem$nnnn.cs"

if (Test-Path $file) {
    Write-Host "Exists  $file"
} else {
    $template = @'
using PE.Runner;

namespace PE.Problems;

// https://projecteuler.net/problem=__N__
public class Problem__NNNN__ : IProblem
{
    public int Number => __N__;

    // The statement's small cases, e.g. new("S(10)", () => S(10), "1.1546112276").
    public IEnumerable<Check> Checks => [];

    public object Solve()
    {
        throw new NotImplementedException();
    }
}

'@
    Set-Content -Path $file -NoNewline -Value $template.Replace('__NNNN__', $nnnn).Replace('__N__', "$Number")
    Write-Host "Created $file"
}

Write-Host ""
Write-Host "Next:  ./pe.ps1 $Number -c -Watch   (re-runs the checks on every save)"
