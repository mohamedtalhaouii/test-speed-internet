#SpeedTeste Libary #Mohamed Talhaoui
import speedtest

st = speedtest.Speedtest()

#Download
download_speed = st.download()/1024**2 #en MB
print("Your Download speed is", download_speed, "Mb") 

#Upload
upload_speed = st.upload()/1024**2
print("Your Upload speed is", upload_speed, "Mb") ##en MB