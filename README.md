# Task 1

# Cryptography
`Cryptography` là một kĩ thuật mã hóa thông tin để bảo vệ quyền riêng tư và tính bảo mật của dữ liệu trong quá trình truyền giao dịch hoặc lưu trữ. Nó sử dụng các giải thuật mã hóa và giải mã để chuyển đổi thông tin thông thường thành dữ liệu được mã hóa và ngược lại.

VD: Bạn muốn gửi một email có nội dung bảo mật cho một người bạn. Bạn có thể sử dụng một giải thuật mã hóa để mã hóa nội dung email trước khi gửi. Chỉ người nhận có thể giải mã nội dung email bằng cách sử dụng khóa giải mã tương ứng.

# Cryptanalysis
`Cryptanalysis` là một quá trình tìm kiếm các điểm yếu trong các thuật toán mật mã và sử dụng các điểm yếu này để giải mã bản mã mà không cần biết khóa bí mật.

VD: Một tổ chức tấn công bảo mật muốn truy cập thông tin bảo mật trong một hệ thống. Họ có thể sử dụng kỹ thuật cryptanalysis để phân tích và giải mã giải thuật mã hóa để truy cập thông tin bảo mật.

# Encode/Decode
`Encode` và `Decode` là hai quá trình liên quan đến mã hóa và giải mã dữ liệu.

`Encode` là quá trình chuyển đổi dữ liệu thông thường thành dữ liệu được mã hóa sử dụng một giải thuật mã hóa để bảo vệ quyền riêng tư hoặc tính bảo mật.

`Decode` là quá trình ngược lại của `encode`, nó là quá trình giải mã dữ liệu đã được mã hóa thành dữ liệu gốc hoặc thông thường. Giải mã có thể yêu cầu sử dụng khóa giải mã tương ứng để giải mã thành thông tin gốc.

VD:Bạn muốn gửi một tin nhắn bảo mật cho một người bạn với nội dung là `mai di choi nhe`. Bạn có thể sử dụng giải thuật mã hóa Base64 để encode tin nhắn của mình. Kết quả là tin nhắn được mã hóa thành một chuỗi ký tự đặc biệt `bWFpIGRpIGNob2kgbmhl`.

Khi người nhận nhận được tin nhắn, họ có thể sử dụng giải thuật giải mã Base64 để decode tin nhắn và nhận được tin nhắn gốc của bạn.
Vậy, quá trình encode và decode giúp cho việc gửi và nhận tin nhắn bảo mật trở nên dễ dàng và an toàn hơn.

# Encrypt/Decrypt 

`Encrypt` và `Decrypt` là hai quá trình liên quan đến mã hóa và giải mã dữ liệu.

`Encrypt` là quá trình mã hóa dữ liệu bằng cách sử dụng một khóa mã hóa để chuyển dữ liệu thông thường thành một chuỗi ký tự hoặc số đặc biệt và không thể đọc được bởi người khác nếu chưa có khóa giải mã tương ứng.

`Decrypt` là quá trình giải mã dữ liệu đã được mã hóa bằng cách sử dụng khóa giải mã tương ứng để trả lại dữ liệu gốc hoặc thông thường.

Vậy, quá trình `Encrypt` và `Decrypt` giúp cho việc bảo vệ dữ liệu và giữ cho thông tin riêng tư của người dùng an toàn.

VD:Bạn muốn gửi một tệp tin nhạy cảm cho một người bạn. Bạn có thể sử dụng giải thuật mã hóa AES để encrypt tệp tin của mình với một khóa mã hóa độc đáo. Kết quả là tệp tin được mã hóa thành một dạng mã hoá và không thể đọc được bởi người khác.

Khi người nhận nhận được tệp tin, họ có thể sử dụng khóa giải mã tương ứng để decrypt tệp tin và nhận được tệp tin gốc của bạn.


# Symmetric and Asymmetric Cryptography
Symmetric và Asymmetric Cryptography là hai kiểu mã hóa khác nhau được sử dụng để bảo vệ thông tin.

`Symmetric Cryptography` (Mã hóa đối xứng): Là kiểu mã hóa sử dụng cùng một khóa để mã hóa và giải mã dữ liệu. Vì vậy, cả hai bên phải giữ khóa mã hóa an toàn để tránh việc bị người khác tấn công.

`Asymmetric Cryptography`(Mã hóa bất đối xứng): Là kiểu mã hóa sử dụng hai khóa khác nhau để mã hóa và giải mã dữ liệu. Một khóa được gọi là khóa công khai hoặc khóa mã hóa, còn khóa còn lại là khóa riêng hoặc khóa giải mã. Khi một người gửi thông tin đến người khác, họ sẽ sử dụng khóa công khai của người nhận để mã hóa thông tin. Nếu ai đó trộm được thông tin, họ sẽ không thể giải mã được vì chỉ có khóa riêng mới có thể giải mã thông tin.

Ví dụ về Asymmetric Cryptography:

Trong một trường hợp gửi email, người gửi sẽ sử dụng khóa công khai của người nhận để mã hóa nội dung email. Khi email đến, người nhận sẽ sử dụng khóa riêng của mình để giải mã và đọc nội dung email.

Ví dụ về Symmetric Cryptography:

Trong một trường hợp truyền tải dữ liệu trong một mạng, hai bên sẽ thỏa thuận sử dụng một khóa chung để mã hóa và giải mã dữ liệu. Khi dữ liệu được gửi từ máy A đến máy B, nội dung sẽ được mã hóa bằng khóa chung và chỉ có máy B mới có thể giải mã được dữ liệu.

# Block Cipher and Stream Cipher

`Block Cipher` và `Stream Cipher` là hai kiểu mã hóa khác nhau trong cryptography.

`Block Cipher`: là một kiểu mã hóa từng block dữ liệu một cách độc lập với những block khác. Mỗi block sẽ được mã hóa bằng cùng một khóa và các block sẽ được gửi đi một cách độc lập với nhau. Kích thước block thường là 128 hoặc 256 bits.

`Stream Cipher`: là một kiểu mã hóa dữ liệu từng byte một. Nó sẽ tạo ra một dòng bit để mã hóa từng byte dữ liệu. Stream Cipher thường được sử dụng trong việc truyền tải dữ liệu trong một mạng vì nó có tốc độ mã hóa và giải mã nhanh hơn Block Cipher.

Ví dụ về Block Cipher:

AES (Advanced Encryption Standard) là một ví dụ của Block Cipher. Nó sử dụng một khóa để mã hóa từng block dữ liệu với kích thước block là 128 bits.
Ví dụ về Stream Cipher:

RC4 (Ron's Code 4) là một ví dụ của Stream Cipher. Nó sử dụng một khóa để tạo ra một dòng bit để mã hóa từng byte dữ liệu. RC4 thường được sử dụng trong việc truyền tải dữ liệu trong một mạng vì tốc độ mã hóa và giải mã nhanh.

# Hash Function 

`Hash Function` là một thuật toán mã hóa tính toán một giá trị băm (hash value) từ một đầu vào bất kỳ (thường là một chuỗi hoặc tập tin). Giá trị băm này là duy nhất cho mỗi đầu vào và có thể được sử dụng để xác định độ tin cậy của dữ liệu.

Ví dụ, một Hash Function có thể được sử dụng để tạo ra một giá trị băm cho một password được lưu trữ trong một database. Khi người dùng nhập password để đăng nhập, Hash Function có thể được sử dụng để tạo ra giá trị băm cho password mới và so sánh nó với giá trị băm đã lưu trữ để xác định xem password có đúng hay không.

# basic-mod1 
```
Challenge
We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message here. 
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
```

 Challenge cho dãy số `54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 ` yêu cầu mod cho 37 và ánh xạ vào bảng kí tự gồm chữ cái,số thập phân và dấu gạch dưới
 
 ```
 from string import ascii_uppercase
x = [54, 396, 131, 198, 225, 258, 87, 258, 128, 211, 57,
     235, 114, 258, 144, 220, 39, 175, 330, 338, 297, 288]


a = ascii_uppercase + "0123456789_"

for i in x:
    print(a[i % 37], end="")
```
 
 ![Screenshot_20230208_045015](https://user-images.githubusercontent.com/83689890/217374767-921eb825-2a5e-44a7-a2ec-c82edbe951a7.png)

Flag là `picoCTF{R0UND_N_R0UND_79C18FB3}`


# base-mod2
```
Challenge
A new modular challenge! Download the message here. Take each number mod 41 and find the modular inverse for the result. 
Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore. 
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
```

Challenge cho dãy số `268 413 110 190 426 419 108 229 310 379 323 373 385 236 92 96 169 321 284 185 154 137 186  ` yêu cầu mod cho 41 tìm nghịch đảo và ánh xạ vào bảng kí tự gồm chữ cái,số thập phân và dấu gạch dưới

```
from string import ascii_uppercase
x = [268, 413, 110, 190, 426, 419, 108, 229, 310, 379, 323,
     373, 385, 236, 92, 96, 169, 321, 284, 185, 154, 137, 186]


a = "0"+ascii_uppercase + "0123456789_"

for i in x:
    print(a[pow(i, -1, 41)], end="")

```

 ![Screenshot_20230208_045842](https://user-images.githubusercontent.com/83689890/217376222-93de4064-8285-46e1-8ea0-512e0e71babe.png)
 
 Flag là `picoCTF{1NV3R53LY_H4RD_C680BDC1}`
 
 # credstuff
 ```
 Description
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here.
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.
```
Challenge cũng cấp một file .tar giải nén ra được 2 file `usernames.txt` và `passwords.txt` .Chúng ta phải tìm user `cultiris`



![Screenshot_20230208_053551](https://user-images.githubusercontent.com/83689890/217382414-ebd867d5-40d2-4d96-b34f-812650bf2dd4.png)

Tìm thấy `cultiris` ở dòng 378 suy ra password cũng ở dòng 378 

![image](https://user-images.githubusercontent.com/83689890/217382606-49a428a4-7c98-454f-9a67-ecf27368d7b5.png)

 password : `cvpbPGS{P7e1S_54I35_71Z3}`
 
 Vì chữ `c` cách chữ `p` trong định dạng flag là `picoCTF{` nên e đoán đây là mã ROT13
 Giải bằng CyberChef 
 
 ![image](https://user-images.githubusercontent.com/83689890/217383605-88da654e-1693-4b78-ad4b-1695254449d7.png)

Flag là `picoCTF{C7r1F_54V35_71M3}`
 
 # morse-code 
 Challenge cho một file WAV âm thanh mouse code 
 
  Upload lên trang  `https://morsecode.world/international/decoder/audio-decoder-adaptive.html`
  
 ![Screenshot_20230208_050544](https://user-images.githubusercontent.com/83689890/217377417-4b73acf9-01f5-47dc-9b35-d76e133e80a7.png)
 
 Flag là `picoCTF{WH47_H47H_90D_W20U9H7}`
 
 
 # rail-fence
 
 ```
 Description
A type of transposition cipher is the rail fence cipher, which is described here. Here is one such cipher encrypted using the rail fence with 4 rails. 
Can you decrypt it?
Download the message here.
Put the decoded message in the picoCTF flag format, picoCTF{decoded_message}.
```
Challenge cho đoạn mã `Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA` 

Dán vào trang `https://www.boxentriq.com/code-breaking/rail-fence-cipher`

![image](https://user-images.githubusercontent.com/83689890/217384184-3eae0a5d-7b23-47b3-b89f-dba79a775716.png)

Flag là `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}`


# transposition-trial

```
Description
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! 
The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
Download the corrupted message here.
```
Challenge cho đoạn mã `heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7`

Thay dấu cách thay dấu gạch dưới và để ý một chút ta sẽ thấy quy luật của từng khối 3 kí tự
![image](https://user-images.githubusercontent.com/83689890/217387688-1276d0e9-2085-4a3e-87df-0b634c197a4f.png)

Mã hóa đổi hoán vị từ (1,2,3)->(2,3,1) để giải ta làm ngược lại (3,1,2)

```
f = open("message.txt", "r", encoding="UTF-8")
s = f.read()

n=3
s3 = [s[i:i+n] for i in range(0, len(s), n)]
result = []

for i in range(len(s3)):
    result.append(s3[i][2]+s3[i][0]+s3[i][1])

print(''.join(result))
```

![image](https://user-images.githubusercontent.com/83689890/217388120-24d6931f-3891-4bc1-9c70-2e019aa954c8.png)

Flag là `picoCTF{7R4N5P051N6_15_3XP3N51V3_A9AFB178}`



# Vigenere
```
Description
Can you decrypt this message?
Decrypt this message using this key "CYLAB".
```

Challenge cho đoạn mã `rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}` với key là `CYLAB`

Giải bằng CyberChef

![image](https://user-images.githubusercontent.com/83689890/217384824-4800d741-1a95-4c54-8a8a-e4283d4a5c8a.png)

Flag là `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_2951a89h}`


 
 
 
 
 
