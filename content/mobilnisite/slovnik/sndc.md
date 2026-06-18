---
slug: "sndc"
url: "/mobilnisite/slovnik/sndc/"
type: "slovnik"
title: "SNDC – SubNetwork Dependent Convergence"
date: 2025-01-01
abbr: "SNDC"
fullName: "SubNetwork Dependent Convergence"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sndc/"
summary: "Funkční vrstva v protokolovém zásobníku GPRS a UMTS, která adaptuje síťové protokoly vyšších vrstev (např. IP) pro přenos podkladovou mobilní sítí. Zpracovává funkce jako komprese a segmentace pro opt"
---

SNDC je vrstva SubNetwork Dependent Convergence v GPRS a UMTS, která adaptuje protokoly vyšších vrstev (např. IP) pro rádiový přenos prováděním komprese a segmentace za účelem optimalizace přenosu paketových dat.

## Popis

SubNetwork Dependent Convergence (SNDC) je klíčová podvrstva v rámci vrstvy spojení (data link layer) architektury protokolů [GPRS](/mobilnisite/slovnik/gprs/) a UMTS, která se nachází mezi síťovou vrstvou (např. IP) a vrstvou řízení logického spoje (Logical Link Control, [LLC](/mobilnisite/slovnik/llc/)). Jejím hlavním úkolem je přizpůsobit charakteristiky různých protokolů síťové vrstvy specifickým požadavkům a omezením mobilní paketové sítě, zejména rádiového rozhraní. Vrstva SNDC je definována v několika specifikacích, včetně celkového popisu služby (TS 23.060) a detailních aspektů GPRS pro rozhraní rádiové části (TS 43.064).

Architektonicky SNDC funguje jak v mobilní stanici (Mobile Station, [MS](/mobilnisite/slovnik/ms/)), tak v podpůrném uzlu GPRS (Serving GPRS Support Node, [SGSN](/mobilnisite/slovnik/sgsn/)). Je odpovědná za správu jednoho nebo více SNDC kontextů pro každý aktivní kontext paketového datového protokolu (Packet Data Protocol, [PDP](/mobilnisite/slovnik/pdp/)) uživatele. Každý SNDC kontext odpovídá konkrétnímu protokolu síťové vrstvy (např. IPv4, IPv6) a obsahuje stavové informace nezbytné pro adaptační funkce. Mezi klíčové operační funkce SNDC patří rozlišování protokolů, komprese a segmentace. Rozlišování protokolů umožňuje síti identifikovat typ přenášené datové jednotky síťového protokolu ([N-PDU](/mobilnisite/slovnik/n-pdu/)). Komprese, často využívající algoritmy jako V.42bis, zmenšuje velikost hlaviček protokolů a uživatelských dat pro úsporu vzácné rádiové kapacity. Segmentace rozděluje velké N-PDU ze síťové vrstvy na menší SNDC datové jednotky vhodné pro přenos přes vrstvu LLC a nakonec přes strukturu rádiových bloků.

Jak to funguje, zahrnuje úzkou interakci s vrstvou LLC pod ní a síťovou vrstvou nad ní. Když IP paket dorazí ze síťové vrstvy, vrstva SNDC identifikuje přidružený PDP kontext a jeho odpovídající SNDC kontext. Může aplikovat kompresi hlaviček (např. kompresi hlaviček [TCP/IP](/mobilnisite/slovnik/tcp-ip/)) a následně segmentovat výsledný datový blok. Přidá SNDC hlavičku obsahující informace jako identifikátor protokolu síťové vrstvy (Network Layer Protocol Identifier, NLPI) a pořadová čísla pro opětovné složení. Tato SNDC datová jednotka (Protocol Data Unit, [PDU](/mobilnisite/slovnik/pdu/)) je pak předána vrstvě LLC pro další zpracování, které zahrnuje přidání adresování a informací pro kontrolu rámce před přenosem přes rozhraní Um/Gb. Na přijímací straně je proces obrácený: LLC předá data vrstvě SNDC, která složí segmenty, dekomprimuje data a doručí původní N-PDU příslušné entitě protokolu síťové vrstvy. Tato abstrakce umožňuje různorodým síťovým protokolům efektivně fungovat nad paketovým jádrem GPRS/UMTS, aniž by každý protokol potřeboval specifickou znalost charakteristik rádiového spoje.

## K čemu slouží

SNDC byla vyvinuta k řešení základního problému efektivního přenosu obecných protokolů síťové vrstvy přes kapacitně omezené a na chyby náchylné rádiové rozhraní mobilních sítí 2.5G a 3G. Před GPRS přenosy dat v přepojování okruhů zacházely s daty jako s transparentním proudem, což bylo pro prchavý IP provoz neefektivní. Cíl paketově orientovaného GPRS vyžadoval metodu pro adaptaci standardních protokolů, jako je IP, které byly navrženy pro pevné sítě, na mobilní prostředí.

Vytvoření SNDC bylo motivováno potřebou transparentnosti protokolů a efektivity. Poskytuje standardizovanou konvergenční vrstvu, která izoluje protokoly vyšších vrstev od specifik rádiové technologie. To umožňuje podporu více síťových protokolů (IPv4, IPv6, X.25) bez změn protokolů rádiové sítě. Mezi klíčové problémy, které řeší, patří úspora rádiových prostředků prostřednictvím robustních kompresních algoritmů a zvládání nesouladu mezi typickou velikostí IP paketů a pevnou velikostí rádiových bloků pomocí segmentace a opětovného složení. Zpracováním těchto funkcí ve vyhrazené podvrstvě umožnilo SNDC GPRS nabízet efektivní, flexibilní a na protokolu nezávislé služby paketových dat, čímž položilo základy pro mobilní přístup k internetu, jak jej známe. Jeho návrh byl kritickým krokem ve vývoji mobilních sítí ze systémů zaměřených na hlas k systémům schopným přenášet data.

## Klíčové vlastnosti

- Adaptuje protokoly síťové vrstvy (IP, PPP, X.25) pro přenos přes paketovou síť GPRS/UMTS
- Provádí kompresi hlaviček a dat (např. V.42bis) pro optimalizaci využití rádiových prostředků
- Segmentuje velké síťové PDU na menší jednotky vhodné pro rádiové přenosové bloky
- Poskytuje rozlišování protokolů pro identifikaci typu přenášených dat síťové vrstvy
- Spravuje SNDC kontexty přidružené ke každému aktivnímu PDP kontextu
- Funguje jak v mobilní stanici, tak v SGSN jako součást vrstvy spojení (data link layer)

## Související pojmy

- [SNDCP – Sub-Network Dependent Convergence Protocol](/mobilnisite/slovnik/sndcp/)
- [LLC – SM Low Layer Source Specific Multicast (address)](/mobilnisite/slovnik/llc/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [SNDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sndc/)
