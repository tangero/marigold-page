---
slug: "iw-mt-lr"
url: "/mobilnisite/slovnik/iw-mt-lr/"
type: "slovnik"
title: "IW-MT-LR – Interworking Mobile Terminated Location Request"
date: 2025-01-01
abbr: "IW-MT-LR"
fullName: "Interworking Mobile Terminated Location Request"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iw-mt-lr/"
summary: "Postup služby určování polohy pro stanovení pozice mobilního zařízení připojeného přes Interworking Wireless Local Area Network (I-WLAN). Jedná se o síťově iniciovaný požadavek, což znamená, že požada"
---

IW-MT-LR je síťově iniciovaný postup služby určování polohy pro stanovení pozice mobilního zařízení připojeného přes Interworking WLAN, který umožňuje poskytování služeb založených na poloze pro uživatele I-WLAN.

## Popis

IW-MT-LR je standardizovaný postup definovaný v 3GPP TS 23.271 pro provedení Mobile Terminated Location Request pro uživatelské zařízení (UE), které je aktuálně připojeno přes Interworking Wireless Local Area Network ([I-WLAN](/mobilnisite/slovnik/i-wlan/)). Architektura I-WLAN umožňuje UE přístup ke službám paketové sítě 3GPP prostřednictvím důvěryhodné WLAN přístupové sítě a její integraci s jádrem sítě. Proces IW-MT-LR je iniciován externím klientem služby určování polohy ([LCS](/mobilnisite/slovnik/lcs/) Client), který odešle požadavek na polohu do Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)). GMLC pak směruje požadavek přes jádro sítě k příslušné entitě, která obsluhuje UE přes I-WLAN.

Z architektonického hlediska požadavek prochází z GMLC k Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), aby získal informace o obslužném uzlu UE. Pro UE připojené přes I-WLAN je tímto obslužným uzlem Packet Data Gateway (PDG) nebo v pozdějších architekturách evolved Packet Data Gateway (ePDG) či Trusted WLAN Access Gateway (TWAG). Požadavek na polohu je pak předán k obslužnému uzlu UE. Samotný mechanismus určování polohy závisí na schopnostech UE a I-WLAN. Může využívat síťově založené metody (např. pomocí informací z WLAN přístupového bodu), metody založené na UE (kde UE vypočítá svou vlastní polohu např. pomocí [GNSS](/mobilnisite/slovnik/gnss/)) nebo metody s asistencí UE. Výsledný odhad polohy je následně naformátován a odeslán zpět přes řetězec entit k původnímu LCS klientovi.

Tento postup je klíčovou součástí architektury Interworking WLAN Location Services (I-WLAN LCS). Zajišťuje, že regulační, nouzové a komerční lokalizační služby (jako vyhledávač přátel nebo sledování majetku) mohou být poskytovány konzistentně bez ohledu na to, zda je UE připojeno přes 3GPP rádiovou přístupovou síť nebo přes důvěryhodnou WLAN. Proces zahrnuje standardní rozhraní jako rozhraní Le mezi LCS klientem a GMLC a rozhraní Lg mezi GMLC a HSS/[HLR](/mobilnisite/slovnik/hlr/), přičemž jsou definována rozšíření pro uzly specifické pro I-WLAN. Bezpečnost a ochrana soukromí jsou prvořadé a vyžadují autorizaci LCS klienta a dodržování nastavení ochrany soukromí uživatele (autorizace LCS klienta, kontrola profilu ochrany soukromí účastníka) předtím, než jsou jakékoli informace o poloze zveřejněny.

## K čemu slouží

IW-MT-LR byl zaveden za účelem rozšíření zavedeného rámce lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) buněčných sítí na uživatele připojené přes důvěryhodné WLAN sítě. Jak se 3GPP sítě vyvíjely směrem k integraci WLAN jako důvěryhodné přístupové technologie (I-WLAN), vznikla mezera v možnosti poskytovat standardizované, síťově iniciované lokalizační služby pro tyto uživatele. Bez IW-MT-LR nemohly externí aplikace standardizovaným, bezpečným a z hlediska ochrany soukromí vyhovujícím způsobem vyžádat polohu uživatele na WLAN, což omezovalo kontinuitu služeb.

Hlavní motivací byla parita služeb a konvergence. Operátoři chtěli nabízet stejné portfolio přidaných LCS služeb – jako je nouzová lokalizace, zákonný odposlech, správa vozového parku a účtování založené na poloze – účastníkům bez ohledu na jejich přístupovou síť. Před standardizací byla ad-hoc řešení pro určování polohy přes WLAN proprietární a neintegrovaná se systémy správy účastníků a ochrany soukromí v jádru sítě. IW-MT-LR tento problém řeší využitím stávající architektury a rozhraní LCS a jejich aplikací na kontext I-WLAN. Řeší problém, jak směrovat požadavek na polohu k UE, které není připojeno k tradičnímu MSC, SGSN nebo MME, ale k WLAN bráně, a jak provádět určování polohy v prostředí WLAN.

K jeho vytvoření vedly trendy konvergence sítí v odvětví a rostoucí význam odlehčování sítě přes WLAN (offloading). Zajišťovalo, že kritické služby jako E911 (rozšířené nouzové služby) mohly být v zásadě podporovány i přes WLAN, pokud to regulační rámec a síťová implementace umožňovaly, což architekturu připravilo na budoucí vývoj. Také umožnilo nové komerční služby, které jsou závislé na znalosti polohy účastníka i když je připojen přes Wi-Fi, což se často využívá v interiérech, kde může být signál buněčné sítě slabý.

## Klíčové vlastnosti

- Umožňuje síťově iniciované (mobile terminated) požadavky na polohu pro UE připojená přes I-WLAN.
- Integruje se s jádrovou architekturou 3GPP LCS (GMLC, HSS) pro autorizaci a směrování.
- Podporuje více metod určování polohy použitelných pro WLAN (např. založené na WLAN AP, UE-based GNSS).
- Zajišťuje ochranu soukromí účastníka prostřednictvím standardní verifikace profilu ochrany soukromí LCS.
- Využívá standardizovaná rozhraní rozšířená pro uzly I-WLAN (např. směrem k PDG/ePDG).
- Poskytuje konzistentní uživatelský zážitek ze služby určování polohy napříč 3GPP a důvěryhodným přístupem mimo 3GPP.

## Související pojmy

- [I-WLAN – Interworking Wireless Local Area Network](/mobilnisite/slovnik/i-wlan/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [MT-LR – Mobile Terminated Location Request](/mobilnisite/slovnik/mt-lr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [IW-MT-LR na 3GPP Explorer](https://3gpp-explorer.com/glossary/iw-mt-lr/)
