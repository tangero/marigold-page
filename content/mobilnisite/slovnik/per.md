---
slug: "per"
url: "/mobilnisite/slovnik/per/"
type: "slovnik"
title: "PER – Printable character Error Rate"
date: 2026-01-01
abbr: "PER"
fullName: "Printable character Error Rate"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/per/"
summary: "Metrika výkonu pro textové telekomunikační služby měřící poměr chybně doručených tisknutelných znaků k celkovému počtu odeslaných. Je klíčová pro hodnocení spolehlivosti služeb jako SMS, USSD a instan"
---

PER je metrika výkonu měřící poměr chybně doručených tisknutelných znaků k celkovému počtu odeslaných znaků. Používá se k hodnocení spolehlivosti textových služeb, jako je SMS.

## Popis

Printable character Error Rate (PER, míra chybovosti tisknutelných znaků) je klíčový ukazatel výkonu ([KPI](/mobilnisite/slovnik/kpi/)) definovaný ve specifikacích 3GPP pro kvantifikaci spolehlivosti znakově orientovaných telekomunikačních služeb. Měří přesnost přenosu informací u služeb, jejichž datová část se skládá z tisknutelných znaků z definovaných abeced (např. výchozí 7bitová GSM abeceda, [UCS2](/mobilnisite/slovnik/ucs2/)). PER je definována jako poměr mezi počtem tisknutelných znaků, které jsou doručeny chybně k cíli, a celkovým počtem tisknutelných znaků odeslaných zdrojem za dané pozorovací období. Chybné doručení zahrnuje znaky, které jsou oproti původní zprávě substituovány, smazány nebo vloženy.

Architektura pro měření PER zahrnuje koncové body na aplikační vrstvě služby. Zdrojová aplikace (např. [SMS](/mobilnisite/slovnik/sms/) centrum) a cílové aplikace (např. přijímající UE) jsou logické body měření. Výpočet zvažuje celou cestu, včetně transportu v jádře sítě, případných mezifunkčních jednotek a rádiového přístupu. Klíčovými komponentami při vyhodnocování jsou definované znakové sady a pravidla pro mapování a počítání znaků. Například u SMS vyžaduje zpráva obsahující tabulky pro národní jazyky nebo znaky pro přepnutí režimu pečlivou interpretaci pro správné spočítání tisknutelných znaků. Měření se typicky provádí v testovacím prostředí nebo prostřednictvím sond v síti, které mohou porovnat odeslanou a přijatou datovou část.

Fungování PER jako metriky je spojeno s testováním služeb a benchmarkingem. Testovací zařízení generuje zprávy se známými sekvencemi tisknutelných znaků a posílá je testovanou sítí. Přijímací zařízení porovná doručené znaky s originálem. Nesrovnalosti jsou zaznamenány a PER je vypočtena. Tento proces testuje odolnost podkladových transportních protokolů (např. [MAP](/mobilnisite/slovnik/map/) pro SMS), kódovacích/dekódovacích algoritmů a případného překódování, které může nastat mezi různými síťovými doménami. Nízká hodnota PER indikuje vysokou věrnost textové služby, což je prvořadé pro služby, u nichž je kritická integrita dat, jako jsou autentizační kódy (např. jednorázová hesla), finanční upozornění nebo nouzová oznámení. PER se často měří za různých síťových podmínek, včetně okrajového rádiového pokrytí, aby se zajistila odolnost služby.

## K čemu slouží

Metrika míry chybovosti tisknutelných znaků (PER) existuje proto, aby poskytla standardizovanou, kvantifikovatelnou míru kvality pro nehlasové, znakové služby. Když se mobilní sítě vyvinuly za hranice hlasových služeb a začaly nabízet služby zasílání zpráv jako [SMS](/mobilnisite/slovnik/sms/), bylo nutné přesáhnout jednoduché metriky úspěchu/neúspěchu (jako jsou doručovací zprávy) a porozumět kvalitě doručovaného obsahu. Zpráva mohla být doručena, ale poškozena, což je pro mnohé aplikace nepřijatelné.

PER řeší problém nedefinované kvality služby pro text. Před její standardizací operátoři a výrobci postrádali společný způsob, jak provádět benchmarking a porovnávat výkonnost platformy pro zasílání zpráv. Byla motivována potřebou zajistit důvěru uživatelů v služby zasílání zpráv, zejména když se tyto služby začaly používat pro kritickou komunikaci. Vysoká hodnota PER by znamenala, že uživatelé dostávají zkomolené zprávy, což vede k záměně, neúspěšným transakcím a nízké spokojenosti zákazníků.

Její zavedení řeší omezení jednodušších metrik, jako je Frame Error Rate ([FER](/mobilnisite/slovnik/fer/)) nebo Bit Error Rate ([BER](/mobilnisite/slovnik/ber/)), které měří výkon na nižších vrstvách, ale přímo nepřekládají kvalitu vnímanou uživatelem na aplikační vrstvě. PER je specifická pro službu a zaměřuje se na informace smysluplné pro koncového uživatele: na znaky. Je obzvláště důležitá pro vývoj zasílání zpráv směrem ke službám rich communication services ([RCS](/mobilnisite/slovnik/rcs/)), komunikaci typu stroj-stroj (M2M), kde příkazy musí být přesné, a pro interoperabilitu mezi různými sítěmi a znakovými sadami. Definováním PER poskytla 3GPP nástroj síťovým inženýrům pro objektivní hodnocení, odstraňování problémů a zlepšování spolehlivosti základní třídy mobilních služeb.

## Klíčové vlastnosti

- Měří přesnost na aplikační/vrstvě služby pro znakové služby
- Definována pro různé znakové sady včetně výchozí 7bitové GSM a UCS2
- Za chyby považuje substituci, smazání a vložení znaku
- Používá se pro end-to-end testování výkonu a benchmarking
- Kritický KPI pro služby SMS, USSD a instant messaging
- Podporuje testování v řízených i reálných síťových podmínkách

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [BER – Basic Encoding Rules](/mobilnisite/slovnik/ber/)
- [FER – Frame Erasure Rate / Frame Error Rate](/mobilnisite/slovnik/fer/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [RCS – Return Channel via Satellite](/mobilnisite/slovnik/rcs/)

## Definující specifikace

- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 25.469** (Rel-19) — HNBAP Specification for HNB to HNB-GW Interface
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.881** (Rel-15) — MBMS FEC for Mission Critical Services Study
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.957** (Rel-19) — Evaluation of MPEG DASH SAND for 3GPP
- **TS 28.403** (Rel-19) — WLAN Performance Measurements
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [PER na 3GPP Explorer](https://3gpp-explorer.com/glossary/per/)
