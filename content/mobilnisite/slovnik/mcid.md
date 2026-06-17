---
slug: "mcid"
url: "/mobilnisite/slovnik/mcid/"
type: "slovnik"
title: "MCID – Malicious Communication Identity"
date: 2026-01-01
abbr: "MCID"
fullName: "Malicious Communication Identity"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mcid/"
summary: "Bezpečnostní služba definovaná 3GPP pro identifikaci a řešení pokusů o škodlivou komunikaci, jako je podvod nebo obtěžování. Umožňuje síťovým operátorům detekovat, hlásit a zmírňovat hrozby ověřením i"
---

MCID je bezpečnostní služba 3GPP, která identifikuje a řeší pokusy o škodlivou komunikaci tím, že umožňuje síťovým operátorům detekovat, hlásit a zmírňovat hrozby prostřednictvím ověření identity.

## Popis

Služba Malicious Communication Identity (MCID) je standardizovaný bezpečnostní mechanismus v sítích 3GPP navržený pro boj se škodlivou komunikací, včetně podvodných hovorů, spamu a obtěžování. Funguje jako doplňková služba, kterou může aktivovat účastník nebo síťový operátor za účelem identifikace původce potenciálně škodlivé komunikace. Služba zahrnuje specifické procedury pro aktivaci, deaktivaci a dotazování, které jsou typicky řízeny funkcí Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v jádru sítě v IMS sítích nebo ekvivalentními entitami v okruhově spínaných doménách. Po aktivaci může síť trasovat a zaznamenávat identifikační informace, jako je identita volající linky, pro další analýzu nebo právní kroky.

Z architektonického hlediska se MCID integruje s různými síťovými funkcemi, včetně Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data účastníků a Policy and Charging Rules Function (PCRF) pro vynucování politik. Služba spoléhá na signalizační protokoly jako SIP (Session Initiation Protocol) v IMS nebo [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) v legacy systémech pro výměnu informací souvisejících s identitou. Mezi klíčové komponenty patří servisní logika v síťových uzlech, mechanismy ověření identity a rozhraní k systémům pro správu podvodů nebo orgánům činným v trestním řízení. Služba MCID zajišťuje zabezpečené nakládání s identifikačními daty v souladu s předpisy na ochranu soukromí a zároveň umožňuje účinné zmírňování hrozeb.

Během provozu může být MCID spuštěna automaticky na základě síťových politik (např. při detekci vzorců škodlivé činnosti) nebo manuálně účastníkem nahlásivším incident. Po vyvolání síť zachytí podrobné identifikační parametry, jako je číslo volající strany, IP adresa nebo [IMSI](/mobilnisite/slovnik/imsi/) (International Mobile Subscriber Identity), a může je uložit do zabezpečené databáze. Služba podporuje jak zásahy v reálném čase (např. blokování hovoru), tak i analýzu po události pro forenzní účely. Její role přesahuje ochranu jednotlivce k širší bezpečnosti sítě, pomáhá operátorům udržovat důvěru a plnit regulatorní požadavky proti trestné činnosti založené na komunikaci.

## K čemu slouží

MCID byla zavedena jako reakce na rostoucí obavy ze škodlivé komunikace v telekomunikačních sítích, včetně podvodů, spamu a obtěžování, které podkopávají důvěru uživatelů a spolehlivost sítě. Před její standardizací operátoři postrádali jednotnou, interoperabilní metodu pro identifikaci a řešení takových hrozeb, což vedlo k roztříštěným řešením, která byla neefektivní a náchylná k obcházení. Služba poskytuje standardizovaný rámec pro ověření identity, což umožňuje konzistentní vynucování napříč různými typy sítí a regiony.

Historicky, jak se mobilní sítě vyvíjely od 2G přes 3G a dále, rostla složitost a objem komunikací, což vedlo k většímu rozšíření a sofistikovanosti škodlivých aktivit. MCID byla motivována potřebou proaktivního bezpečnostního opatření, které by se dokázalo integrovat s vyvíjejícími se síťovými architekturami, jako je IMS (IP Multimedia Subsystem), a zároveň řešilo právní a regulatorní požadavky na ochranu účastníků. Řeší problémy, jako jsou anonymní podvodné hovory, kde pachatelé skrývají svou identitu, tím, že ukládá požadavky na trasovatelnost a možnosti hlášení.

Vznik MCID také odráží zaměření 3GPP na zvyšování bezpečnosti služeb souběžně s funkčními pokroky. Standardizací nakládání s identitou umožňuje operátorům spolupracovat na zpravodajství o hrozbách a snižuje náklady a úsilí spojené s implementací vlastních bezpečnostních řešení. To se stalo stále důležitějším s nástupem VoIP a multimediálních služeb, kde jsou tradiční mechanismy identity méně účinné.

## Klíčové vlastnosti

- Standardizované ověření identity pro škodlivou komunikaci
- Integrace s IMS a legacy síťovými architekturami
- Podpora automatické i manuální aktivace ze strany účastníků nebo operátorů
- Zabezpečené zaznamenávání a hlášení identifikačních dat (např. identity volající linky)
- Rozhraní k systémům pro správu podvodů a orgánům činným v trestním řízení
- Soulad s požadavky na ochranu soukromí a regulacemi v oblasti bezpečnosti komunikace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.408** (Rel-7) — TIP/TIR Services Protocol Specification
- **TS 24.410** (Rel-8) — Protocol Description of HOLD Services
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [MCID na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcid/)
