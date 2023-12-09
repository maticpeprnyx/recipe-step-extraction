foreach ($fullpath in Get-ChildItem -Path .\recepty\*.txt) {
    $filename = $fullpath.Name
    $outputfilename = "označkované\$filename"
    python kód/tagger.py $fullpath.FullName | Out-File -FilePath $outputfilename
    Start-Sleep -Seconds 1
} 
