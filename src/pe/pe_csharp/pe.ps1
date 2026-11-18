<#
.SYNOPSIS
    Run Project Euler solutions. Everything except -Watch goes to the runner;
    see `./pe.ps1 --help`.

.EXAMPLE
    ./pe.ps1                  # highest-numbered problem: checks, then solve
.EXAMPLE
    ./pe.ps1 2 -c -Watch      # problem 2's checks, re-run on every save
.EXAMPLE
    ./pe.ps1 all
#>
# No param() block on purpose: a declared parameter would bind the first bare
# number positionally, and unknown flags like -c would error.
$Watch = $false
$rest = [System.Collections.Generic.List[string]]::new()
foreach ($arg in $args) {
    if ("$arg" -match '^-(Watch|w)$') { $Watch = $true } else { $rest.Add("$arg") }
}

$csproj = Join-Path $PSScriptRoot 'PE/PE.csproj'

if ($Watch) {
    # --no-hot-reload: rebuild and restart on each save, so every run starts clean.
    dotnet watch run --no-hot-reload --project $csproj -- @rest
} else {
    dotnet run --project $csproj -c Release -v q -- @rest
}
exit $LASTEXITCODE
