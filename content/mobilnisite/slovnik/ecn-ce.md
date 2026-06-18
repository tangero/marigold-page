---
slug: "ecn-ce"
url: "/mobilnisite/slovnik/ecn-ce/"
type: "slovnik"
title: "ECN-CE – ECN Congestion Experienced"
date: 2025-01-01
abbr: "ECN-CE"
fullName: "ECN Congestion Experienced"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ecn-ce/"
summary: "ECN Congestion Experienced (ECN-CE) je specifický kódový bod v rámci mechanismu Explicit Congestion Notification (ECN), který signalizuje, že síťový uzel zaznamenal přetížení a odpovídajícím způsobem"
---

ECN-CE je specifický kódový bod ECN používaný v sítích 3GPP k signalizaci, že paket narazil na přetížení, což spouští adaptaci přenosové rychlosti na koncových bodech pro proaktivní správu přetížení.

## Popis

[ECN](/mobilnisite/slovnik/ecn/) Congestion Experienced (ECN-CE) je definovaný stav v rámci rámce Explicit Congestion Notification (ECN), při kterém je pole ECN v hlavičce IP nastaveno na hodnotu '11' (binárně) pro indikaci, že paket prošel přetíženým síťovým uzlem. V systémech 3GPP je ECN-CE využíván jako součást end-to-end řízení přetížení napříč mobilními páteřními sítěmi, zejména v Evolved Packet Core (EPC) a 5G Core (5GC). Když router, brána nebo jiný síťový prvek detekuje hrozící přetížení – typicky prostřednictvím algoritmů monitorování front jako Random Early Detection (RED) nebo Controlled Delay (CoDel) – označí pakety s podporou ECN kódovým bodem [CE](/mobilnisite/slovnik/ce/) místo jejich zahazování. Toto označení slouží jako explicitní signál pro transportní vrstvu (např. TCP nebo [QUIC](/mobilnisite/slovnik/quic/)), že dochází k přetížení, což vyzve odesílatele ke snížení přenosové rychlosti. Proces zahrnuje interakci označování na IP vrstvě s protokoly vyšších vrstev za účelem dosažení efektivního řízení provozu.

Architektonicky ECN-CE funguje v rámci širšího mechanismu ECN definovaného v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3168 a adaptovaného 3GPP. Klíčové komponenty zahrnují pole ECN v hlavičkách IPv4 nebo IPv6, které se skládá ze dvou bitů: první bit ([ECT](/mobilnisite/slovnik/ect/)) indikuje podporu ECN a druhý bit (CE) je nastaven na 1 při zaznamenání přetížení. V mobilních sítích mohou uzly jako [PGW](/mobilnisite/slovnik/pgw/)/[UPF](/mobilnisite/slovnik/upf/), TDF nebo PCEF aplikovat označení CE na základě metrik přetížení v reálném čase nebo pravidel politiky z PCRF/PCF. Úlohou ECN-CE je poskytnout přesný indikátor přetížení, který mohou koncové body využít k úpravě svého chování bez nutnosti spoléhat se na odvození ze ztrát, což je zvláště cenné v bezdrátovém prostředí, kde ztráty mohou také pramenit z chyb rádiového spoje.

Jak ECN-CE funguje v praxi, zahrnuje několik kroků. Koncové body indikují svou podporu ECN nastavením bitů ECT během navazování relace. Jak pakety proudí sítí, přetížené uzly kontrolují prahové hodnoty front; pokud jsou překročeny, označí pakety kódem CE, za předpokladu, že bity ECT ukazují tuto schopnost. V 3GPP k tomu často dochází na úzkých místech, jako je rozhraní SGi nebo v rámci GTP tunelů mezi páteřními prvky. Po přijetí příjemce detekuje značku CE a sdělí ji zpět odesílateli prostřednictvím potvrzení transportní vrstvy (např. TCP ACK s příznakem ECN-Echo). Odesílatel pak vyvolá algoritmy pro zamezení přetížení, jako je snížení okna přetížení, aby přetížení zmírnil. Specifikace 3GPP, například pro QoS a řízení politik, zajišťují, že je ECN-CE integrováno s funkcemi správy provozu pro podporu různorodých služeb, od hromadných dat po komunikaci v reálném čase.

## K čemu slouží

ECN-CE bylo vytvořeno, aby poskytovalo jasný, explicitní signál síťového přetížení v rámci rámce ECN, a řešilo tak potřebu přesnější zpětné vazby o přetížení než pouhé zahazování paketů. V mobilních sítích, kde může přetížení rychle degradovat uživatelský zážitek kvůli omezené šířce pásma a proměnným podmínkám, umožňuje ECN-CE včasnou adaptaci přenosové rychlosti, čímž snižuje riziko zahlcení bufferů a nadměrného zpoždění. Řeší problém nejednoznačných indikátorů přetížení, protože ztráta paketů v bezdrátových sítích může být důsledkem rádiových chyb spíše než přetížení, což vede k nevhodným reakcím transportní vrstvy.

Historický kontext vychází z vývoje ECN v IETF, přičemž ECN-CE bylo definováno jako specifický kódový bod v RFC 3168. 3GPP začlenilo ECN-CE počínaje Release 9 pro vylepšení správy přetížení v LTE a novějších sítích, navazujíc na dřívější základy ECN. Předchozí přístupy se spoléhaly na implicitní signály, jako je zahazování paketů, což mohlo způsobovat zbytečné retransmise a kolísání propustnosti, což bylo zvláště škodlivé pro služby v reálném čase. ECN-CE nabídlo standardizovaný způsob, jak odlišit přetížení od jiných příčin ztrát, a tím zlepšit efektivitu sítě.

Motivace pro ECN-CE v 3GPP zahrnují podporu aplikací s nízkou latencí, jako je VoIP a streamování videa, prostřednictvím umožnění proaktivního řízení přetížení, což je v souladu s cíli QoS pro 4G a 5G. Řeší omezení předchozích mechanismů pro přetížení, kterým chyběla podrobná signalizace, a usnadňuje tak lepší využití zdrojů a spokojenost uživatelů. ECN-CE také umožňuje soulad s vyvíjejícími se internetovými standardy a podporuje pokročilé funkce, jako je síťové dělení (network slicing), kde je vyžadováno diferencované zacházení s přetížením.

## Klíčové vlastnosti

- Specifický kódový bod v IP hlavičce (binárně '11') indikující označení paketu kvůli síťovému přetížení
- Spouští mechanismy adaptace přenosové rychlosti na koncových bodech v transportních protokolech s podporou ECN, jako je TCP
- Integrace s řízením politik 3GPP pro podmíněné označování na základě politik předplatitele nebo služby
- Použitelnost v páteřních uzlech mobilní sítě (např. UPF, PGW) a na klíčových rozhraních (SGi, N6)
- Snižuje závislost na ztrátě paketů jako signálu přetížení, minimalizuje zbytečné retransmise
- Podporuje diferencovanou správu přetížení pro různé typy provozu a síťové řezy (network slices)

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 36.750** (Rel-14) — Study on enhancement of VoLTE

---

📖 **Anglický originál a plná specifikace:** [ECN-CE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecn-ce/)
