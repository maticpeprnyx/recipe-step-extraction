foreach ($fullpath in Get-ChildItem -Path .\tagged\*.txt) {
    $filename = $fullpath.Name
    $outputfilename = "frequencies\$filename"
    Get-Content $fullpath.FullName | ForEach-Object {$_ -replace '^#', ''} | Select-String "VERB" | ForEach-Object {($_.Line -split ' ')[4]} | python .\code\counter.py | Sort-Object {$_[1]} -Descending | Out-File -FilePath $outputfilename
} 
