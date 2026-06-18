---
slug: "rtpcp"
url: "/mobilnisite/slovnik/rtpcp/"
type: "slovnik"
title: "RTCP – RTP Control Protocol"
date: 2015-01-01
abbr: "RTCP"
fullName: "RTP Control Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rtpcp/"
summary: "RTCP je řídicí protokol, který pracuje společně s RTP v multimediálních relacích. Poskytuje statistické údaje, řídicí informace a synchronizační data pro účastníky relace RTP mimo přenosové pásmo. Je"
---

RTCP je řídicí protokol, který pracuje společně s RTP a poskytuje statistické údaje, synchronizaci a informace o účastnících mimo přenosové pásmo, což je nezbytné pro monitorování QoS a synchronizaci médií ve službách 3GPP IMS.

## Popis

Řídicí protokol [RTP](/mobilnisite/slovnik/rtp/) ([RTCP](/mobilnisite/slovnik/rtcp/)) je definován společně s RTP v dokumentu [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3550 a je profilován pro použití v rámci multimediálních služeb 3GPP. Zatímco RTP přenáší vlastní mediální data, RTCP funguje na samostatném portu (obvykle port RTP + 1) a periodicky vysílá řídicí pakety všem účastníkům relace. Jeho hlavními funkcemi jsou monitorování QoS, synchronizace médií a správa účastníků relace. Pakety RTCP nepřenášejí média; místo toho přenášejí hlášení odesílatele ([SR](/mobilnisite/slovnik/sr/)), hlášení příjemce ([RR](/mobilnisite/slovnik/rr/)), položky popisu zdroje (SDES) a pakety definované aplikací.

Hlášení odesílatele (SR) generují aktivní odesílatelé a obsahují klíčové informace: časovou značku [NTP](/mobilnisite/slovnik/ntp/) udávající čas reálných hodin, časovou značku RTP odpovídající stejnému okamžiku a počty paketů a bajtů odesílatele. To umožňuje příjemcům synchronizovat přehrávání různých mediálních proudů (např. audio s videem pro synchronizaci rtů) a vypočítat dobu oběhu zpoždění. Hlášení příjemce (RR) generují účastníci, kteří nic neodesílají, a poskytují odesílatelům zpětnou vazbu o kvalitě příjmu. RR obsahuje údaje jako podíl ztracených paketů, kumulativní počet ztracených paketů, nejvyšší přijaté pořadové číslo a kolísání doby příchodu. Tato zpětná vazba je pro odesílatele nebo mezilehlý prvek zásadní pro případnou adaptaci přenosových rychlostí nebo parametrů kodeku.

Pakety popisu zdroje (SDES) sdělují identifikátory účastníků a další popisné informace. Položka kanonického jména (CNAME) je povinná a poskytuje trvalý, globálně jedinečný identifikátor zdroje napříč více relacemi RTP, což je nezbytné pro synchronizaci souvisejících proudů (jako jsou samostatné audio a video kanály ze stejného zdroje). Mezi další volitelné položky může patřit jméno uživatele, e-mail, telefonní číslo nebo data specifická pro aplikaci. RTCP také definuje pakety BYE pro oznámení, že účastník relaci opouští. Protokol je navržen tak, aby byl škálovatelný, a to řízením rychlosti odesílání paketů RTCP; celkový řídicí provoz je omezen na malé procento (obvykle 5 %) celkové šířky pásma relace.

V ekosystému 3GPP, zejména pro služby založené na IMS jako VoLTE, hraje RTCP klíčovou roli v monitorování kvality služeb a diagnostice. Zpětná vazba v paketech RR o ztrátě paketů a kolísání poskytuje metriky výkonu nosiče LTE nebo 5G a cesty v jádru sítě v reálném čase. Operátoři sítí mohou tato data monitorovat pro řešení problémů a zajištění dodržování QoS. Dále se RTCP používá ve spojení s funkcí IMS Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) pro funkce jako konferenční hovory, kde MRF může míchat hlášení RTCP. Zatímco RTCP poskytuje cennou zpětnou vazbu, 3GPP také definuje další mechanismy pro podrobnější měření QoS a řízení politik, ale RTCP zůstává primárním nástrojem pro monitorování samotné mediální relace na koncích.

## K čemu slouží

RTCP byl vytvořen k řešení problémů spojených se správou multimediální relace v reálném čase, kde účastníci nemají přímý přehled o výkonu sítě nebo stavu ostatních účastníků. Samotné RTP doručuje média, ale nenabízí mechanismus, jak by odesílatelé věděli, zda jsou jejich pakety úspěšně přijímány, nebo jak by příjemci synchronizovali více souvisejících proudů (jako samostatné audio a video z jednoho zdroje). Bez RTCP by byly aplikace "hluché" k podmínkám v síti a zápasily by s problémy se synchronizací.

Jeho účel je trojí: 1) **Monitorování QoS a zpětná vazba**: Poskytnout odesílatelům a příjemcům kvantitativní údaje o ztrátě paketů, kolísání a době oběhu. To umožňuje adaptivní aplikace (např. přepnutí na kodek s nižším datovým tokem při přetížení) a poskytuje operátorům sítí cenné diagnostické informace. 2) **Synchronizace mezi médii**: Poskytnout potřebnou časovou korelaci (pomocí časových značek NTP a RTP v paketech SR) pro synchronizaci přehrávání samostatně kódovaných audio a video proudů, čímž se zajistí přesná synchronizace rtů. 3) **Správa relace**: Sdělit identitu účastníka (pomocí CNAME) a oznámit změny v účasti (připojení/opuštění pomocí paketů BYE), což je nezbytné pro víceúčastnické relace a uživatelská rozhraní.

V kontextu přechodu 3GPP na hlas a video přes IP se RTCP stal klíčovou součástí pro zajištění služeb. Pro VoLTE a ViLTE je udržení vysoké kvality hlasu/videa prvořadé. Zpětná vazba RTCP umožňuje jak uživatelskému zařízení (UE), tak síti monitorovat kvalitu hovoru v reálném čase. Tato data mohou být využita systémy správy sítě pro proaktivní detekci chyb a IMS pro případné nové vyjednání relace. Zatímco 3GPP definuje další nástroje pro měření QoS (jako rozhraní Gx pro řízení politik), RTCP poskytuje standardizovaný pohled na stav mediální cesty na aplikační vrstvě mezi koncovými body, který doplňuje metriky síťové vrstvy.

## Klíčové vlastnosti

- Hlášení odesílatele (SR) pro přenosové statistiky a časovou synchronizaci
- Hlášení příjemce (RR) pro zpětnou vazbu o ztrátě paketů, kolísání a době oběhu zpoždění
- Pakety popisu zdroje (SDES) pro identifikaci účastníka (CNAME)
- Pakety BYE pro řádné oznámení o opuštění relace
- Škálovatelný provoz podle šířky pásma (řídicí provoz omezen na ~5 % šířky pásma relace)
- Poskytuje kanonická jména (CNAME) pro synchronizaci napříč proudy

## Související pojmy

- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)

## Definující specifikace

- **TS 26.236** (Rel-12) — Packet Switched Conversational Multimedia Protocols

---

📖 **Anglický originál a plná specifikace:** [RTCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtpcp/)
