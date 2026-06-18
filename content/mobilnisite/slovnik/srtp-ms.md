---
slug: "srtp-ms"
url: "/mobilnisite/slovnik/srtp-ms/"
type: "slovnik"
title: "SRTP-MS – Secure Real-time Transport Protocol Master Salt"
date: 2025-01-01
abbr: "SRTP-MS"
fullName: "Secure Real-time Transport Protocol Master Salt"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srtp-ms/"
summary: "SRTP Master Salt je kryptografická hodnota, která není tajná, a která se používá společně s hlavním klíčem SRTP (SRTP-MK) ve funkci pro odvození klíčů. Zajišťuje, že generované klíče pro šifrování a a"
---

SRTP-MS je Secure Real-time Transport Protocol Master Salt, kryptografická hodnota, která není tajná, a která se používá společně s hlavním klíčem pro odvození jedinečných a nepředvídatelných klíčů pro šifrování a autentizaci relace.

## Popis

SRTP-MS (Secure Real-time Transport Protocol Master Salt) je klíčový parametr v hierarchii odvození klíčů [SRTP](/mobilnisite/slovnik/srtp/). Je to hodnota, která není tajná, náhodná nebo pseudonáhodná, typicky dlouhá 112 bitů pro běžný šifrovací algoritmus AES-CM, která je kombinována s tajným hlavním klíčem SRTP ([SRTP-MK](/mobilnisite/slovnik/srtp-mk/)) pro vytvoření finálních klíčů relace. Primární role hlavního saltu je dodání dodatečné entropie a odlišnosti procesu odvození klíčů. Během nastavení relace je SRTP-MS bezpečně přenesen mezi komunikujícími koncovými body, často v rámci stejného signalizace [SDP](/mobilnisite/slovnik/sdp/), která přenáší materiál klíčů, nebo je odvozena z známého parametru.

Technicky, funkce odvození klíčů ([KDF](/mobilnisite/slovnik/kdf/)) pro SRTP, podle [RFC](/mobilnisite/slovnik/rfc/) 3711, přijímá SRTP-MK, SRTP-MS, index paketu a rychlost odvození klíčů jako vstupní hodnoty. Hlavní salt je použit pro 'osolení' odvození, což znamená, že zajišťuje, že výstupní klíče relace jsou specifické pro tuto konkrétní kombinaci hlavního klíče a saltu. I když by byl stejný SRTP-MK použit pro dvě různé relace (což není doporučeno, ale může nastat v určitých scénářích správy klíčů), použití různého SRTP-MS pro každou relaci by vedlo ke kompletně různým klíčům relace. Tato vlastnost je klíčová pro kryptografickou hygienu a zmírňuje určité typy útoku souvisejících s klíči.

V architektuře systému 3GPP je SRTP-MS generován a distribuován s stejnou mírou bezpečnostních záruk jako SRTP-MK. Často je považován za neoddělitelnou část kontextu klíče. Pro relace využívající bezpečnost přístupu 3GPP může být SRTP-MS odvozen z parametrů síti nebo generován síťovou funkcí zodpovědnou za politiku bezpečnosti médií (např. [P-CSCF](/mobilnisite/slovnik/p-cscf/)). UE a síťový partner (např. Media Resource Function Processor) musí sdílet stejnou hodnotu SRTP-MS pro správné odvození symetrických klíčů relace. Jeho správa je integrální část celkových procedur správy klíčů specifikovaných v 3GPP TS 24.380, 29.380 a 29.582, což zajišťuje, že šifrování médií pro služby jako nouzové volání, VoNR a konverzativní video je robustní a splňuje bezpečnostní standardy.

## K čemu slouží

SRTP-MS existuje pro řešení základního kryptografického požadavku: prevence opakovaného použití výstupu odvození klíčů. Použití pouze hlavního klíče pro odvození může vést ke stejným klíčům relace, pokud je hlavní klíč použit v různých relacích nebo pokud se vstup odvození (např. index paketu) cyklicky opakuje. To by bylo vážnou bezpečnostní slabinou. Hlavní salt poskytuje relaci-unikátní proměnnou, která garantuje odlišnost odvozených klíčů.

Jeho zavedení do bezpečnostního modelu 3GPP bylo motivováno potřebou sladit se s dobře zavedeným standardem [SRTP](/mobilnisite/slovnik/srtp/) [IETF](/mobilnisite/slovnik/ietf/) (RFC 3711), který vyžaduje nebo silně doporučuje použití hlavního saltu. Řeší problém potenciálního opakování klíčového streamu a zesiluje celkový proces odvození klíčů proti kryptoanalytickým útokům. Historicky, v starších nebo jednodušších šifrovacích systémech, vynechání takového saltu mohlo vést ke slabinám, kde by mohly být odhaleny vzory v šifrovaných datách, pokud jsou klíče příbuzné. Zahrnutím SRTP-MS, 3GPP zajišťuje, že jeho implementace bezpečnosti médií získává plnou kryptografickou sílu specifikace SRTP. Poskytuje potřebnou flexibilitu síti pro uplatnění politik oddělení klíčů a podporuje bezpečné mechanismy přechodu klíčů ve spojení s SRTP-MKI.

## Klíčové vlastnosti

- Hodnota, která není tajná, která dodává entropii funkci odvození klíčů SRTP
- Zajišťuje jedinečnost klíčů relace i při opakovaném použití hlavního klíče v různých relacích
- Standardní délka 112 bitů pro použití s AES v Counter Mode
- Distribuována bezpečně společně s hlavním klíčem SRTP během nastavení relace
- Klíčový vstup do procesu odvození klíčů spolu s indexem paketu a rychlostí odvození klíčů
- Zvyšuje kryptografickou robustnost a ochraňuje proti určitým útokům souvisejícím s klíči

## Související pojmy

- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [SRTP-MK – Secure Real-time Transport Protocol Master Key](/mobilnisite/slovnik/srtp-mk/)
- [SRTP-MKI – Secure Real-time Transport Protocol Master Key Identifier](/mobilnisite/slovnik/srtp-mki/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [SRTP-MS na 3GPP Explorer](https://3gpp-explorer.com/glossary/srtp-ms/)
