#pip install speedtest-cli
import speedtest 

s = speedtest.Speedtest()

print("Ölçülüyor...\n")

downloadSpeed = s.download() / 1048576
uploadSpeed = s.upload() / 1048576

pingResult = round(s.results.ping)

print(f"İndirme hızı: {downloadSpeed: .2f} Mbps")
print(f"Yükleme hızı: {uploadSpeed: .2f} Mbps")
print(f"Ping: {pingResult} ms")