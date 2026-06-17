---
slug: "g-cdr"
url: "/mobilnisite/slovnik/g-cdr/"
type: "slovnik"
title: "G-CDR – GGSN (PDP context) generated - Charging Data Record"
date: 2025-01-01
abbr: "G-CDR"
fullName: "GGSN (PDP context) generated - Charging Data Record"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/g-cdr/"
summary: "Detailní záznam protokolu generovaný uzlem Gateway GPRS Support Node (GGSN) nebo jeho 5G ekvivalentem (UPF/SMF) pro kontext/relaci Packet Data Protocol (PDP). Obsahuje informace o využití (objem dat,"
---

G-CDR je detailní záznam o účtování (Charging Data Record) generovaný GGSN nebo jeho 5G ekvivalentem pro PDP kontext, obsahující informace o využití, jako je objem dat a doba trvání, pro účely fakturace a analýzy sítě.

## Popis

GGSN-generovaný záznam o účtování (G-CDR) je základní datová struktura v účtovacích systémech 3GPP, konkrétně pro paketově přepínané služby v [GPRS](/mobilnisite/slovnik/gprs/), UMTS a rozvinutém paketovém jádru. Jedná se o formátovaný záznam obsahující komplexní soubor informací týkajících se datové relace uživatele, známé jako kontext Packet Data Protocol (PDP). GGSN (nebo v 5G kombinované účtovací funkce Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/))) funguje jako funkce spouštěče účtování (Charging Trigger Function - [CTF](/mobilnisite/slovnik/ctf/)). Detekuje události relevantní pro účtování, jako je zřízení, změna a ukončení relace, a shromažďuje příslušné informace pro sestavení [CDR](/mobilnisite/slovnik/cdr/).

G-CDR zahrnuje četná pole, která zachycují identitu účastníka (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)), zapojené síťové elementy (IP adresa GGSN, adresa SGSN), podrobnosti relace (identifikátor PDP kontextu, typ PDP jako IPv4), informace o službě (Access Point Name - [APN](/mobilnisite/slovnik/apn/)) a především údaje o využití. Tato data o využití zahrnují celkový objem přenesených dat ve směru uplink a downlink, dobu trvání relace (čas začátku a konce) a případně parametry QoS spojené s relací. Záznam je generován při uzavření účtovacího kontejneru, což může být spuštěno ukončením relace, dosažením limitu objemu, časového limitu nebo jinými administrativními spouštěči.

Po vygenerování je G-CDR přenesen přes rozhraní Ga (pomocí protokolů jako GTP' nebo Diameter) k funkci Charging Data Function (CDF) nebo přímo do fakturačního systému. Role G-CDR je klíčová pro offline účtování (post-paid fakturace). Poskytuje surová, ověřitelná data, na jejichž základě se vypočítává účastnický účet. Kromě fakturace se G-CDR používá také pro účetnictví (vypořádání mezi operátory), business intelligence, analýzu provozu a plánování sítě. Specifikace jeho polí a postupů přenosu je detailně popsána v 3GPP TS 32.298 a souvisejících specifikacích, aby byla zajištěna interoperabilita mezi síťovými zařízeními a fakturačními systémy různých dodavatelů.

## K čemu slouží

G-CDR existuje, aby umožnil přesné, spolehlivé a standardizované účtování paketových datových služeb v mobilních sítích. Před érou GPRS a mobilních dat bylo účtování primárně založeno na době trvání hovoru. Přechod na paketově přepínané služby zavedl nový paradigma, kde se využití měřilo objemem dat (bajty) namísto času, což si vyžádalo nový účtovací model a odpovídající datové záznamy. G-CDR byl vytvořen, aby zachytil toto objemové využití na síťové bráně k internetu (GGSN).

Řeší problém korelace obrovského množství IP datového provozu s jednotlivými účastníky a jejich služebními předplatnými. Bez standardizovaného formátu CDR by GGSN každého dodavatele produkoval proprietární logy, což by znemožnilo interoperabilitu s fakturačními systémy a bránilo nasazení sítí s více dodavateli. G-CDR poskytuje společný „jazyk“ pro hlášení využití. Také řeší potřebu detailních záznamů, které podporují složité tarifní plány, jako jsou vrstvené datové balíčky, časové tarify a služebně diferencované účtování (např. odlišné účtování dat za sociální média a streamování videa).

Historický kontext začíná jeho zavedením v Release 6 spolu s dospělou definicí paketového jádra UMTS. Jeho vývoj v následujících releasech odráží rostoucí složitost služeb (např. IMS, QoS diferenciace) a přechod k novým architekturám jádra sítě (EPC, 5GC). Koncept G-CDR byl přizpůsoben, ale zůstává koncepčně ústřední, což zajišťuje zpětnou kompatibilitu a stabilní základ pro zajištění příjmů s postupem síťových technologií.

## Klíčové vlastnosti

- Zaznamenává využití dat (počty bajtů pro uplink/downlink) na PDP kontext/relaci
- Obsahuje identifikátory účastníka (IMSI, MSISDN) a identifikátory relace
- Zahrnuje informace o službě, jako je Access Point Name (APN)
- Zachycuje časová razítka relace pro účtování založené na době trvání
- Přenášen standardizovanými protokoly rozhraní Ga (GTP', Diameter)
- Slouží jako primární zdroj dat pro offline (post-paid) fakturaci

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [G-CDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/g-cdr/)
