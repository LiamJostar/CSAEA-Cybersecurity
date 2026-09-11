#hashing is one way. same algorithm changes pw, but cant be turned back.
import hashlib

password = "liam123"
data = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()
print(f"password: {password}")
print(f"Hash: {digest}")

passwords = ["green200", "yellow100", "red300", "purple500", "blue400"]
for p in passwords:
    data = p.encode("utf-8") #text to bytes
    digest = hashlib.sha256(data).hexdigest()

    print(f"password: {p}")
    print(f"Hash: {digest}", "\n")