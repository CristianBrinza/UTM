## Task 2.1

```Wolfram
p = RandomPrime[{2^1023, 2^1024 - 1}];
q = RandomPrime[{2^1023, 2^1024 - 1}];

n = p*q;
phi = (p - 1)*(q - 1);

e = RandomPrime[{2^16, phi}];
While[GCD[e, phi] != 1, e = RandomPrime[{2^16, phi}]];

d = PowerMod[e, -1, phi];

message = ToCharacterCode["Cristian Brinza"];
encryptedMessage = PowerMod[message, e, n];

decryptedMessage = PowerMod[encryptedMessage, d, n];
decryptedText = FromCharacterCode[decryptedMessage];

Print["p value: ", p];
Print[];
Print["q value: ", q];
Print[];
Print["n value: ", n];
Print[];
Print["e value (public exponent): ", e];
Print[];
Print["d value (private exponent): ", d];
Print[];
Print["Encrypted Message: ", encryptedMessage];
Print[];
Print["Decrypted Message: ", decryptedText];

```

## Task 2.2

```Wolfram
p = 96724641360065368215752415020704611306277049777191098963308933907818783780719523951675691263277881732956153852156666038637441827651011653195399387464125861463825463768655909223604457286319231989365777218480115732087974801597798153116864051927916942303011557909305572335650508012996308445887706989167788223239;
g = 2;
x = RandomInteger[{1, p - 2}];
y = PowerMod[g, x, p];

hexMessage = "43 72 69 73 74 69 61 6E 20 42 72 69 6E 7A 61";  (* This is the hexadecimal representation of "Cristian Brinza" *)
decimalMessage = ToExpression["16^^" <> #] & /@ StringSplit[hexMessage];

encrypt[message_, p_, g_, y_] := Module[{k, c1, c2},
  k = RandomInteger[{1, p - 2}];
  c1 = PowerMod[g, k, p];
  c2 = Mod[message*PowerMod[y, k, p], p];
  {c1, c2}
];

encryptedMessage = encrypt[#, p, g, y] & /@ decimalMessage;

decrypt[{c1_, c2_}, p_, x_] := Mod[c2*PowerMod[c1, p - 1 - x, p], p];

decryptedMessage = decrypt[#, p, x] & /@ encryptedMessage;

Print["Cristian Brinza in Decimal Form: ", decimalMessage];
Print[];
Print["Decrypted Message in Decimal Form: ", decryptedMessage];
Print[];
Print["Encrypted Message: ", encryptedMessage];

```

## Task 2.3

```Wolfram
p = 96724641360065368215752415020704611306277049777191098963308933907818783780719523951675691263277881732956153852156666038637441827651011653195399387464125861463825463768655909223604457286319231989365777218480115732087974801597798153116864051927916942303011557909305572335650508012996308445887706989167788223239;
g = 2;

a = RandomInteger[{1, p - 1}];
b = RandomInteger[{1, p - 1}];
A = PowerMod[g, a, p];
B = PowerMod[g, b, p];

sharedSecretP1 = PowerMod[B, a, p];
sharedSecretP2 = PowerMod[A, b, p];

Print["P1's secret number: ", a];
Print[];
Print["P2's secret number: ", b];
Print[];
Print["P1's public key: ", A];
Print[];
Print["P2's public key: ", B];
Print[];
Print["Shared secret computed by P1: ", sharedSecretP1];
Print[];
Print["Shared secret computed by P2: ", sharedSecretP2];

```
