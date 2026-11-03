<#
.SYNOPSIS
    Run Advent of Code solutions for a year. Everything after the script's own
    parameters goes to the runner; see `./aoc.ps1 --help`.

.EXAMPLE
    ./aoc.ps1                 # latest day of the latest year: examples, then real input
.EXAMPLE
    ./aoc.ps1 3 -t -Watch     # day 3 examples, re-run on every save
.EXAMPLE
    ./aoc.ps1 all -r -Year 2025
#>
# No param() block on purpose: a declared parameter would bind the first bare
# number (the day) positionally, and unknown flags like -t would error. Pull out
# -Year/-Watch by hand and pass everything else through untouched.
$Year = 0
$Watch = $false
$rest = [System.Collections.Generic.List[string]]::new()
for ($i = 0; $i -lt $args.Count; $i++) {
    switch -Regex ("$($args[$i])") {
        '^-(Year|y)$' { $Year = [int]$args[++$i]; continue }
        '^-(Watch|w)$' { $Watch = $true; continue }
        default { $rest.Add("$($args[$i])") }
    }
}

$root = $PSScriptRoot
if (-not $Year) {
    $Year = Get-ChildItem $root -Directory -Filter 'AoC.Year*' |
        ForEach-Object { [int]($_.Name -replace '^AoC\.Year', '') } |
        Sort-Object | Select-Object -Last 1
}

$csproj = Join-Path $root "AoC.Year$Year/AoC.Year$Year.csproj"
if (-not (Test-Path $csproj)) {
    Write-Error "No project for $Year. Create it with ./new-day.ps1 -Year $Year"
    exit 2
}

if ($Watch) {
    # --no-hot-reload: rebuild and restart on each save, so every run starts clean.
    dotnet watch run --no-hot-reload --project $csproj -- @rest
} else {
    dotnet run --project $csproj -c Release -v q -- @rest
}
exit $LASTEXITCODE
