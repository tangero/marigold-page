---
slug: "ndc"
url: "/mobilnisite/slovnik/ndc/"
type: "slovnik"
title: "NDC – National Destination Code"
date: 2025-01-01
abbr: "NDC"
fullName: "National Destination Code"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ndc/"
summary: "Číselná předpona používaná v mezinárodních telefonních číslovacích plánech k identifikaci konkrétní země nebo geografické oblasti. Je klíčovou součástí číslovacího plánu E.164, která umožňuje globální"
---

NDC je číselná předpona v mezinárodním telefonním číslovacím plánu E.164, která identifikuje konkrétní zemi nebo geografickou oblast pro globální směrování hovorů.

## Popis

Národní směrovací kód (National Destination Code – NDC) je základním prvkem mezinárodního veřejného telekomunikačního číslovacího plánu [ITU-T](/mobilnisite/slovnik/itu-t/) E.164. Tvoří část úplné struktury mezinárodního telefonního čísla, která typicky zahrnuje kód země (Country Code – [CC](/mobilnisite/slovnik/cc/)), národní směrovací kód (NDC) a číslo účastníka (Subscriber Number – SN). NDC se používá v rámci země nebo integrované číslovací oblasti k identifikaci konkrétní geografické oblasti, sítě nebo typu služby. Jeho délka a struktura jsou definovány národním číslovacím plánem příslušné země nebo regionu. V mobilních sítích může být NDC součástí mezinárodního čísla [ISDN](/mobilnisite/slovnik/isdn/) mobilní stanice ([MSISDN](/mobilnisite/slovnik/msisdn/)) a napomáhá směrování hovorů ke správnému mobilnímu síťovému operátorovi nebo specifické servisní platformě v zemi.

Z pohledu 3GPP je NDC zmíněn v mnoha specifikacích zabývajících se číslováním, adresováním a identifikací. Je nedílnou součástí protokolů a procedur pro zřizování hovorů, doplňkové služby a propojování s jinými sítěmi (jako PSTN/ISDN). NDC umožňuje síťovým prvkům, jako jsou ústředny mobilní komunikace ([MSC](/mobilnisite/slovnik/msc/)) a domácí registrační místa ([HLR](/mobilnisite/slovnik/hlr/)), správně interpretovat volané číslo. Například při sestavování hovoru obslužná síť analyzuje volané číslice, izoluje NDC a použije jej spolu s kódem země k určení informací pro směrování – zda je hovor určen účastníkovi ve stejné národní síti, v jiné národní síti, nebo vyžaduje zpracování přes mezinárodní bránu.

Jeho role přesahuje základní směrování hovorů. NDC se také používá v řešeních přenositelnosti čísel. Když účastník změní poskytovatele služeb, ale ponechá si své číslo, NDC již nemusí přímo indikovat aktuální síť. V takových případech se databáze přenositelnosti čísel (jako Number Portability Databases – [NPDB](/mobilnisite/slovnik/npdb/)) dotazují pomocí NDC a čísla účastníka, aby získaly aktuální směrovací číslo (např. Routing Number nebo Mobile Network Code). Tím je zajištěno správné doručení hovorů navzdory oddělení vazby mezi NDC a skutečnou obslužnou sítí. NDC tedy funguje jako klíč pro databázové dotazy a rozhodování o směrování v celém řetězci zpracování hovoru.

## K čemu slouží

Národní směrovací kód existuje za účelem strukturování a organizace telefonního číslování na národní úrovni, což umožňuje efektivní a jednoznačné směrování telefonních hovorů v rámci hranic země. Před standardizovanými národními číslovacími plány s jasnými směrovacími kódy čelily telefonní sítě významným výzvám ve škálování, správě růstu počtu účastníků a automatizaci přepojování hovorů. NDC poskytuje hierarchické adresovací schéma, které rozděluje národní číselný prostor na spravovatelné bloky přiřazené konkrétním regionům, městům nebo síťovým operátorům.

Tato hierarchická struktura řeší problém, který vyžadoval, aby operátoři ústředen nebo automatizované zařízení znali každé jednotlivé číslo účastníka. Místo toho mohou ústředny směrovat hovory na základě předpony NDC a nasměrovat hovor na příslušnou regionální ústřednu nebo síťovou bránu. To výrazně zjednodušuje směrovací tabulky a zvyšuje rychlost a spolehlivost sestavení hovoru. Zavedení NDC jako součásti standardu E.164 bylo motivováno globalizací telekomunikací a potřebou interoperability mezi různými národními sítěmi a mezi pevnými a mobilními službami.

V kontextu mobilních sítí standardizovaných 3GPP je účel NDC integrován do procedur správy mobility a řízení hovorů. Umožňuje mobilním sítím bezproblémové rozhraní s globální sítí PSTN/[ISDN](/mobilnisite/slovnik/isdn/) a mezi sebou navzájem. NDC pomáhá identifikovat domovskou síť roamujícího účastníka pro účely účtování a je používán v signalizačních zprávách (jako v ISUP nebo MAP) k předání adresovacích informací. Jeho pokračující relevance je zřejmá při přechodu na plně IP sítě (IMS), kde telefonní čísla (často obsahující NDC) zůstávají primárním identifikátorem účastníka pro telefonní služby, což zajišťuje zpětnou kompatibilitu a kontinuitu služeb.

## Klíčové vlastnosti

- Součást mezinárodního číslovacího plánu ITU-T E.164
- Identifikuje geografickou oblast, síť nebo službu v rámci země
- Umožňuje hierarchické směrování hovorů v národních sítích
- Používá se jako klíč pro dotazy do databází přenositelnosti čísel
- Nedílná součást identifikátorů účastníka, jako je MSISDN
- Usnadňuje propojování mezi mobilními sítěmi a PSTN/ISDN

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.796** (Rel-16) — FRMCS Architectural Analysis
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2
- **TS 43.069** (Rel-19) — Voice Broadcast Service (VBS) Stage 2

---

📖 **Anglický originál a plná specifikace:** [NDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ndc/)
