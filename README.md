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
## Khái niệm
`Encrypt` và `Decrypt` là hai quá trình liên quan đến mã hóa và giải mã dữ liệu.

`Encrypt` là quá trình mã hóa dữ liệu bằng cách sử dụng một khóa mã hóa để chuyển dữ liệu thông thường thành một chuỗi ký tự hoặc số đặc biệt và không thể đọc được bởi người khác nếu chưa có khóa giải mã tương ứng.

`Decrypt` là quá trình giải mã dữ liệu đã được mã hóa bằng cách sử dụng khóa giải mã tương ứng để trả lại dữ liệu gốc hoặc thông thường.

Vậy, quá trình `Encrypt` và `Decrypt` giúp cho việc bảo vệ dữ liệu và giữ cho thông tin riêng tư của người dùng an toàn.

## Các thuật toán mã hóa phổ biến
- AES
- DES
- TripleDES
- RSA 
- Twofish

## Ví dụ
Bạn muốn gửi một tệp tin nhạy cảm cho một người bạn. Bạn có thể sử dụng giải thuật mã hóa AES để encrypt tệp tin của mình với một khóa mã hóa độc đáo. Kết quả là tệp tin được mã hóa thành một dạng mã hoá và không thể đọc được bởi người khác.

Khi người nhận nhận được tệp tin, họ có thể sử dụng khóa giải mã tương ứng để decrypt tệp tin và nhận được tệp tin gốc của bạn.


# Symmetric and Asymmetric Cryptography
## Khái niệm
Symmetric và Asymmetric Cryptography là hai kiểu mã hóa khác nhau được sử dụng để bảo vệ thông tin.

`Symmetric Cryptography` (Mã hóa đối xứng): Là kiểu mã hóa sử dụng cùng một khóa để mã hóa và giải mã dữ liệu. Vì vậy, cả hai bên phải giữ khóa mã hóa an toàn để tránh việc bị người khác tấn công.Đây được cho là kỹ thuật mã hóa đơn giản và được sử dụng phổ biến nhất, với một số đặc điểm nổi bật như:

- Do thuật toán mã hóa đối xứng ít phức tạp hơn và có thể thực thi nhanh hơn, đây là kỹ thuật được đặc biệt ưa thích trong các hoạt động truyền tải dữ liệu hàng loạt.
- Văn bản gốc được mã hóa bằng một key trước khi gửi đi, và chính key này cũng sẽ được người nhận sử dụng để giải mã dữ liệu.
- Một số thuật toán mã hóa đối xứng được sử dụng phổ biến nhất bao gồm AES-128, AES-192 và AES-256.

`Asymmetric Cryptography`(Mã hóa bất đối xứng): Là kiểu mã hóa sử dụng hai khóa khác nhau để mã hóa và giải mã dữ liệu. Một khóa được gọi là khóa công khai hoặc khóa mã hóa, còn khóa còn lại là khóa riêng hoặc khóa giải mã. Khi một người gửi thông tin đến người khác, họ sẽ sử dụng khóa công khai của người nhận để mã hóa thông tin. Nếu ai đó trộm được thông tin, họ sẽ không thể giải mã được vì chỉ có khóa riêng mới có thể giải mã thông tin.Đây là loại hình mã hóa ra đời sau mã hóa đối xứng và còn được gọi là công nghệ mã hóa public-key:

- Mã hóa bất đối xứng được cho là an toàn hơn mã hóa đối xứng vì nó sử dụng 2 key riêng biệt cho 2 quy trình mã hóa và giải mã.
- Public key được sử dụng để mã hóa sẽ được công khai, nhưng private key để giải mã là hoàn toàn bí mật.
- Phương pháp mã hóa này được sử dụng trong các giao tiếp hàng ngày qua internet.
- Khi một tin nhắn được mã hóa bằng public key, nó chỉ có thể được giải mã bằng private key. Tuy nhiên, khi một tin nhắn được mã hóa bằng private key, nó có thể được    giải mã bằng public key.
- Chứng chỉ kỹ thuật số trong mô hình máy khách-máy chủ có thể được sử dụng để tìm thấy các public key.
- Điểm hạn chế của mã hóa bất đối xứng là mất nhiều thời gian thực hiện hơn so với mã hóa đối xứng.
- Các kỹ thuật mã hóa bất đối xứng phổ biến bao gồm RSA, DSA và PKCS.

Ví dụ về Asymmetric Cryptography:

Trong một trường hợp gửi email, người gửi sẽ sử dụng khóa công khai của người nhận để mã hóa nội dung email. Khi email đến, người nhận sẽ sử dụng khóa riêng của mình để giải mã và đọc nội dung email.

Ví dụ về Symmetric Cryptography:

Trong một trường hợp truyền tải dữ liệu trong một mạng, hai bên sẽ thỏa thuận sử dụng một khóa chung để mã hóa và giải mã dữ liệu. Khi dữ liệu được gửi từ máy A đến máy B, nội dung sẽ được mã hóa bằng khóa chung và chỉ có máy B mới có thể giải mã được dữ liệu.

# Block Cipher and Stream Cipher
## Khái niệm
`Block Cipher` và `Stream Cipher` là hai kiểu mã hóa khác nhau trong cryptography.

`Block Cipher`: Mật mã khối là một mật mã khóa đối xứng khác. Mật mã khối hoạt động trên các khối (nhóm bit) có độ dài cố định. Mật mã khối sử dụng một phép biến đổi cố định (không thay đổi) cho tất cả các chữ số trong khối. Ví dụ: khi một văn bản thuần túy khối x-bit (cùng với khóa bí mật) được cung cấp làm đầu vào cho công cụ mật mã khối, nó sẽ tạo ra khối văn bản mã x-bit tương ứng. Sự biến đổi thực sự phụ thuộc vào khóa bí mật. Tương tự, thuật toán giải mã khôi phục khối x-bit ban đầu của bản rõ bằng cách sử dụng khối x-bit của bản mã và khóa bí mật ở trên làm đầu vào. Trong trường hợp thông điệp đầu vào quá dài so với kích thước của khối, nó sẽ được chia nhỏ thành các khối và các khối này sẽ được mã hóa (riêng lẻ) bằng cùng một khóa. Tuy nhiên, vì cùng một khóa được sử dụng, mỗi chuỗi lặp lại trong văn bản thuần túy sẽ trở thành một chuỗi lặp lại giống nhau trong văn bản mã và điều này có thể gây ra các lo ngại về bảo mật. Các mật mã khối phổ biến là DES (Tiêu chuẩn mã hóa dữ liệu) và AES (Tiêu chuẩn mã hóa nâng cao).

`Stream Cipher`: Mật mã dòng thuộc họ mật mã khóa đối xứng. Mật mã dòng kết hợp các bit văn bản thuần túy với một dòng bit mã hóa giả ngẫu nhiên với việc sử dụng hoạt động XOR (độc quyền hoặc). Mật mã dòng mã hóa từng chữ số văn bản thuần túy với các phép biến đổi khác nhau cho các chữ số liên tiếp. Vì mã hóa của mỗi chữ số phụ thuộc vào trạng thái hiện tại của công cụ mã hóa, mật mã dòng còn được gọi là mật mã trạng thái. Thông thường, các bit / bit đơn được sử dụng dưới dạng các chữ số đơn. Để tránh lo ngại về bảo mật, cần đảm bảo rằng cùng một trạng thái khởi động không được sử dụng nhiều hơn một lần. Mật mã dòng được sử dụng rộng rãi nhất là RC4.

## Sự khác biệt giữa Mật mã dòng và Mật mã khối là gì?

Mặc dù cả mật mã dòng và mật mã khối đều thuộc họ mật mã đối xứng, nhưng có một số điểm khác biệt chính. Mật mã khối mã hóa các khối bit có độ dài cố định, trong khi mật mã dòng kết hợp các bit văn bản thuần túy với một dòng bit mật mã giả ngẫu nhiên sử dụng phép toán XOR. Mặc dù mật mã khối sử dụng cùng một phép biến đổi, nhưng mật mã dòng sử dụng các phép biến đổi khác nhau dựa trên trạng thái của động cơ. Mật mã luồng thường thực thi nhanh hơn mật mã khối. Về độ phức tạp của phần cứng, mật mã dòng tương đối ít phức tạp hơn. Mật mã luồng là ưu tiên điển hình so với mật mã khối khi văn bản thuần túy có sẵn với số lượng khác nhau (ví dụ: kết nối wifi an toàn), bởi vì mật mã khối không thể hoạt động trực tiếp trên các khối ngắn hơn kích thước khối. Nhưng đôi khi, sự khác biệt giữa mật mã dòng và mật mã khối không rõ ràng lắm. Lý do là, khi sử dụng một số chế độ hoạt động, mật mã khối có thể được sử dụng để hoạt động như một mật mã dòng bằng cách cho phép nó mã hóa đơn vị dữ liệu nhỏ nhất hiện có.

## Ví dụ

AES (Advanced Encryption Standard) là một ví dụ của Block Cipher. Nó sử dụng một khóa để mã hóa từng block dữ liệu với kích thước block là 128 bits.

RC4 (Ron's Code 4) là một ví dụ của Stream Cipher. Nó sử dụng một khóa để tạo ra một dòng bit để mã hóa từng byte dữ liệu. RC4 thường được sử dụng trong việc truyền tải dữ liệu trong một mạng vì tốc độ mã hóa và giải mã nhanh.

# Hash Function 
## Khái niệm 
`Hash Function` là một thuật toán mã hóa tính toán một giá trị băm (hash value) từ một đầu vào bất kỳ (thường là một chuỗi hoặc tập tin). Giá trị băm này là duy nhất cho mỗi đầu vào và có thể được sử dụng để xác định độ tin cậy của dữ liệu.

![image](https://user-images.githubusercontent.com/83689890/217718178-2553919a-6733-4695-ba00-33e6e9f2792b.png)

## Tính chất của Hash
Hàm băm mật mã về cơ bản cần đảm bảo các tính chất sau: 

- Tính tất định, nghĩa là cùng một thông điệp đầu vào luôn tạo ra cùng một hàm băm. 

- Tính hiệu quả. Có khả năng tính toán nhanh chóng giá trị băm của bất kỳ thông điệp nào. 

- Tính nhạy cảm. Đảm bảo rằng bất kỳ một thay đổi nào, dù là nhỏ nhất trên dữ liệu đều sẽ gây ra sự thay đổi cực lớn trên giá trị băm và tạo ra giá trị băm hoàn toàn khác, và không hề có liên hệ gì với giá trị băm cũ (hiệu ứng tuyết lở).

Ngoài ra, với mục đích đảm bảo an toàn cho dữ liệu, các hàm băm mật mã phải có khả năng chịu được tất cả các loại tấn công mã hóa đã biết. Trong lý thuyết mật mã, mức độ an toàn của hàm băm mật mã đã được xác định bằng các thuộc tính sau: 

- Tính kháng tiền ảnh thứ nhất. Tính chất yêu cầu rằng với một giá trị băm h bất kỳ, sẽ khó tìm thấy bất kỳ thông điệp m nào sao cho h = hash (m). Khái niệm này có liên quan đến tính chất một chiều của hàm băm. 

- Tính kháng tiền ảnh thứ hai. Với đầu vào m1, sẽ khó tìm được đầu vào m2 khác sao cho hash(m1) = hash (m2). 

- Tính kháng va chạm. Rất khó để tìm thấy hai thông điệp khác nhau m1 và m2 sao cho hash (m1) = hash (m2). Một giá trị như vậy được gọi là va chạm của hàm băm mật mã.

## Các loại Hash
MD5,SHA-1,RIPEMD160,Bcrypt,Whirlpool,SHA-2,SHA-3,BLAKE2,SHA-256,SHA-512

## Ứng dụng của Hash
- Hashing trong định danh tệp hoặc dữ liệu

- Hashing trong xác minh tính toàn vẹn của thông điệp hoặc tập tin

- Hashing trong tạo và xác nhận chữ ký

- Hashing trong xác minh mật khẩu

- Hashing và Bằng chứng công việc (Proof of Work)





## Ví dụ 
Một Hash Function có thể được sử dụng để tạo ra một giá trị băm cho một password được lưu trữ trong một database. Khi người dùng nhập password để đăng nhập, Hash Function có thể được sử dụng để tạo ra giá trị băm cho password mới và so sánh nó với giá trị băm đã lưu trữ để xác định xem password có đúng hay không.

# basic-mod1 
```
Challenge
We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message here. 
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. 
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
```

 Challenge cho dãy số `54 396 131 198 225 258 87 258 128 211 57 235 114 258 144 220 39 175 330 338 297 288 ` yêu cầu mod cho 37 và ánh xạ vào bảng kí tự gồm chữ cái,số thập phân và dấu gạch dưới
 
 ```python
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

```python
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

```python
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


 
 
 
 
 
