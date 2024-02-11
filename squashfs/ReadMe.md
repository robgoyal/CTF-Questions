1. mkdir output
2. dd if=recovery.bin of=output/note.txt bs=1 count=54
3. dd if=recovery.bin of=output/data.tar.gz bs=1 skip=55 count=38438
4. tar -xzvf output/data.tar.gz
5. dd if=recovery.bin of=output/fakesquashfs.zip bs=1 skip=38493 count=2143  # (add 22 for the footer)
6. dd if=recovery.bin of=output/note2.txt bs=1 skip=40636 count=106
7. dd if=recovery.bin of=output/realzip.zip bs=1 skip=40743a
8. zip2john output/realzip.zip > crackme
9. john --wordlist=password.list crackme
10. unzip realzip.zip  # with the password nirvana1!
11. mkdir mnt
12. sudo mount sample.csv ./mnt -t squashfs -o loop
13. mv mnt/backup .
14. cat backup/sysadmin.flag
