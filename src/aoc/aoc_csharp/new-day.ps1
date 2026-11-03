<#
.SYNOPSIS
    Scaffold an Advent of Code day (and the year project, if it doesn't exist yet).

.DESCRIPTION
    Creates, only when missing:
      AoC.Year<Year>/              project + Program.cs, added to coding-challenges.sln
      AoC.Year<Year>/Day<DD>.cs    solution stub (both parts throw NotImplementedException)
      <data>/<Year>/aoc<Year>-<DD>-test.txt       empty, paste the example here
      <data>/<Year>/aoc<Year>-<DD>-test.expected  two lines: part 1 and part 2 example answers
    Then downloads the real input (needs AOC_SESSION in the environment or .env).

.EXAMPLE
    ./new-day.ps1                  # in December: today's puzzle; otherwise the next missing day
.EXAMPLE
    ./new-day.ps1 -Year 2026 -Day 4 -NoDownload
.EXAMPLE
    ./new-day.ps1 -Year 2027 -ProjectOnly
#>
param(
    [int]$Year,
    [int]$Day,
    [switch]$NoDownload,
    [switch]$ProjectOnly
)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$repo = (Resolve-Path (Join-Path $root '../../..')).Path
$sln = Join-Path $repo 'coding-challenges.sln'

$eastern = [TimeZoneInfo]::ConvertTimeBySystemTimeZoneId([DateTime]::UtcNow, 'Eastern Standard Time')

if (-not $Year) {
    if ($eastern.Month -eq 12) {
        $Year = $eastern.Year
    } else {
        $Year = Get-ChildItem $root -Directory -Filter 'AoC.Year*' |
            ForEach-Object { [int]($_.Name -replace '^AoC\.Year', '') } |
            Sort-Object | Select-Object -Last 1
    }
}

$project = Join-Path $root "AoC.Year$Year"
$csproj = Join-Path $project "AoC.Year$Year.csproj"

if (-not (Test-Path $csproj)) {
    New-Item -ItemType Directory -Force $project | Out-Null
    Set-Content -Path $csproj -NoNewline -Value @'
<Project Sdk="Microsoft.NET.Sdk">

    <!-- TargetFramework, ImplicitUsings, Nullable come from ../Directory.Build.props -->
    <PropertyGroup>
        <OutputType>Exe</OutputType>
    </PropertyGroup>

    <ItemGroup>
        <ProjectReference Include="..\AoC.Shared\AoC.Shared.csproj" />
    </ItemGroup>

</Project>

'@
    Set-Content -Path (Join-Path $project 'Program.cs') -NoNewline -Value @'
// Days are discovered automatically. Run `dotnet run -- --help` for options.
return AoC.Shared.AocRunner.Run(args);

'@
    dotnet sln $sln add --in-root $csproj | Out-Host
    Write-Host "Created project $project"
}

if ($ProjectOnly) { return }

if (-not $Day) {
    $existing = @(Get-ChildItem $project -Filter 'Day*.cs' |
        ForEach-Object { [int]($_.BaseName -replace '^Day', '') })
    if ($eastern.Year -eq $Year -and $eastern.Month -eq 12 -and $existing -notcontains $eastern.Day) {
        $Day = $eastern.Day
    } else {
        $Day = 1
        while ($existing -contains $Day) { $Day++ }
    }
}

$dd = '{0:D2}' -f $Day
$dayFile = Join-Path $project "Day$dd.cs"
if (Test-Path $dayFile) {
    Write-Host "Exists  $dayFile"
} else {
    $template = @'
using AoC.Shared;

namespace AoC.Year__YEAR__;

public class Day__DD__ : IDay
{
    public int Year => __YEAR__;
    public int Day => __DAY__;

    public string SolvePart1(string[] input)
    {
        throw new NotImplementedException();
    }

    public string SolvePart2(string[] input)
    {
        throw new NotImplementedException();
    }
}

'@
    $code = $template.Replace('__YEAR__', "$Year").Replace('__DD__', $dd).Replace('__DAY__', "$Day")
    Set-Content -Path $dayFile -NoNewline -Value $code
    Write-Host "Created $dayFile"
}

# Data files. Resolve the data root the same way the runner does, by asking it.
$dataRoot = (dotnet run --project $csproj -v q -- --print-data-path) | Select-Object -Last 1
$yearData = Join-Path $dataRoot "$Year"
New-Item -ItemType Directory -Force $yearData | Out-Null

$testFile = Join-Path $yearData "aoc$Year-$dd-test.txt"
$expectedFile = [IO.Path]::ChangeExtension($testFile, '.expected')
if (-not (Test-Path $testFile)) {
    New-Item -ItemType File $testFile | Out-Null
    Write-Host "Created $testFile  (paste the example input here)"
}
if (-not (Test-Path $expectedFile)) {
    Set-Content -Path $expectedFile -Value @('?', '?')
    Write-Host "Created $expectedFile  (replace the ?s with the example answers)"
}

if (-not $NoDownload) {
    dotnet run --project $csproj -v q -- $Day --fetch | Out-Host
}

Write-Host ""
Write-Host "Next:  ./aoc.ps1 $Day -t -Watch   (re-runs the examples on every save)"
