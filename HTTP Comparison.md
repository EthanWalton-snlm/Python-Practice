#### Ethan Walton

# HTTP 2 vs HTTP 3

## HTTP 3's Increased Performance 🚀

HTTP 3 has improved performance as it is **UDP-based**.

- Unlike HTTP 2, HTTP 3 does not use a TCP connection. This aids HTTP 3 because if there is packet loss, the connection is not abandoned. If a packet is lost in a UDP connection, it only interupts one stream.
- Since HTTP 3 uses UDP, there is no 3-way handshake, as a result there is a reduced wait for acknowledgements that HTTP 2 endures in it's TCP connection.

## HTTP 2's Head of Line (HOL) Blocking 🚧

As mentioned previously, if a packet is dropped over HTTP 2 the entire connection is interupted. This is called HOL blocking.

## HTTP 3's Enforced Encryption 🔐

In HTTP 2, Transport Layer Security (TLS) encryption is optional. HTTP 3 enforces this, resulting in a more secure data transfer.

- <font color="red">**However,**</font> TLS encryption makes it harder for firewalls to access packets, potentially leaving users prone to cyber attacks.

## Implementing HTTP 3 🤔

Implementing HTTP 3 can require existing infrastructure to be modified.

- Therefore, a higher set of skills is also required.

## A Visual Comparison 👀

### HTTP 2

![HTTP 2 Visually](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5MQCKq4WKwM4fCqDGYJ8Ui/1f9306b608618fe78e3e57a1392a9b11/image1-1.gif)

### HTTP 3

![HTTP 3 Visually](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/6DSF88gTgVSsmiVExIa3Ry/5e26b2b32f6bd00dda851caa4c9c46e6/image4-1.gif)

## Summary 📝

- HTTP 3 has better performance.
- HTTP 3 uses UDP and HTTP 2 uses TCP.
- HTTP 2 suffers from HOL blocking.
- HTTP 3 enforces TLS encryption.
  - This can increase the risk of cyber attacks.
- HTTP 3 can be difficult to implement.

## Sources 🔍

- [Cloudflare](https://blog.cloudflare.com/http-3-vs-http-2/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/what-is-http-3-how-it-is-different-from-http-2/)
