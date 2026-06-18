---
slug: "ivas"
url: "/mobilnisite/slovnik/ivas/"
type: "slovnik"
title: "IVAS – Immersive Voice and Audio Services"
date: 2025-01-01
abbr: "IVAS"
fullName: "Immersive Voice and Audio Services"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ivas/"
summary: "Standardizovaný mediální kodek a servisní rámec 3GPP pro poskytování imerzivních prostorových zvukových zážitků s více kanály přes mobilní sítě. Umožňuje realistické zvukové scény pro hlasové hovory,"
---

IVAS je standardizovaný mediální kodek a servisní rámec 3GPP pro poskytování imerzivních prostorových zvukových zážitků s více kanály přes mobilní sítě za účelem vytvoření realistických zvukových scén pro hovory, hudbu a aplikace rozšířené reality.

## Popis

Immersive Voice and Audio Services (IVAS) je komplexní standard 3GPP zavedený ve vydání Release 16, který definuje nový mediální kodek a související servisní rámec určený pro poskytování vysoce kvalitních imerzivních zvukových zážitků přes sítě 5G a vyvinuté paketové jádro. Jeho jádrem je kodek IVAS, vysoce efektivní a flexibilní zvukový kodek schopný kódovat nejen tradiční stereo nebo mono signály, ale také komplexní prostorové zvukové scény sestávající z více zvukových kanálů (např. 5.1, 7.1.4) a diskrétních zvukových objektů s přidruženými metadaty (jako pozice, velikost a zesílení). To umožňuje vykreslování zvuku v trojrozměrném prostoru kolem posluchače.

Z architektonického hlediska se IVAS integruje do služby Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) 3GPP a dalších rámců pro streamování médií. Funguje v mediální rovině IP Multimedia Subsystem (IMS). Mezi klíčové komponenty patří kodér IVAS, který komprimuje imerzivní zvukovou scénu; dekodér IVAS, který ji rekonstruuje; a renderer IVAS, který využívá funkce přenosu hlavy ([HRTF](/mobilnisite/slovnik/hrtf/)) a informace o přehrávacím systému ke správné prostorizaci zvuku pro konkrétní nastavení posluchače (sluchátka, reproduktorové pole). Servisní rámec, podrobně popsaný v specifikacích jako 26.114 a 26.119, definuje procedury vyjednávání relace pomocí Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)) k navázání mediálních relací podporujících IVAS, včetně podpory dynamického přepínání mezi režimy kodeku na základě síťových podmínek.

Jak to funguje: Během hovoru nebo streamovací relace si koncové body vyjednají podporu IVAS. Zachytávací zařízení (např. 360stupňové mikrofonní pole nebo [XR](/mobilnisite/slovnik/xr/) headset) zachytí prostorovou zvukovou scénu. Kodér IVAS tuto scénu komprimuje a efektivně reprezentuje ambientní kanály a pohyblivé zvukové objekty. Tento bitový proud je paketizován a přenášen přes síť 5G, využívající výhod ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) pro aplikace v reálném čase. Dekodér IVAS přijímacího zařízení scénu rekonstruuje a renderer ji přizpůsobuje v reálném čase na základě orientace hlavy posluchače (pomocí dat sledování hlavy), aby udržel stabilní zvukové pole a vytvořil přesvědčivý pocit přítomnosti. Jeho úlohou je být umožňující zvukovou technologií pro teleprezenci, sociální XR a imerzivní zábavu.

## K čemu slouží

IVAS byl vytvořen, aby řešil omezení tradičních hlasových a zvukových kodeků (jako [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/)) v nastupující éře rozšířené reality ([XR](/mobilnisite/slovnik/xr/)), teleprezence a imerzivních médií. Starší kodeky byly navrženy pro mono nebo stereo přehrávání a nebyly schopné přenášet prostorové signály nezbytné pro realistická virtuální prostředí nebo skupinovou komunikaci, kde je kritické porozumět tomu, kdo mluví a odkud. Motivací bylo definovat jediný efektivní standard pro všechny případy použití imerzivního zvuku a vyhnout se fragmentaci.

Historický kontext představuje vývoj 5G, který slibuje vylepšené mobilní širokopásmové připojení (eMBB), masivní IoT a URLLC. Zatímco 5G poskytuje přenosovou cestu, IVAS poskytuje zvukový obsah nové generace, který ospravedlňuje potřebu vysoké šířky pásma a nízké latence. Řeší problém doručování kinokvalitního zvuku založeného na objektech přes bezdrátové sítě pro aplikace jako víceuživatelské VR hry, vzdálená spolupráce ve virtuálních prostorech a imerzivní streamování živé hudby. Předchozí přístupy vyžadovaly proprietární kodeky nebo objemný nekomprimovaný vícekanálový zvuk, které byly neefektivní a neinteroperabilní.

IVAS navíc umožňuje nové servisní paradigmy, jako je 'telefonie s rozšířenou realitou', kde mohou být vzdálení účastníci reprezentováni jako prostorové zvukové objekty v uživatelově prostředí. Řeší potřebu kodeku, který je zároveň vysoce kvalitní pro hudbu a nízkobitový pro konverzační řeč, s plynulým přepínáním mezi režimy. Jeho vytvoření bylo motivováno konvergencí průmyslu z telekomunikací, vysílání a spotřební elektroniky za účelem vytvoření univerzálního standardu pro imerzivní zvuk pro 5G.

## Klíčové vlastnosti

- Kódování prostorového zvuku: Podporuje kódování kanálového zvuku (až 22.2), objektového zvuku a smíšených scén s metadaty.
- Vysoká efektivita a škálovatelnost: Poskytuje vysokou zvukovou kvalitu při datových tocích od 32 kbps pro řeč až přes 512 kbps pro bohaté hudební scény, se škálovatelnou složitostí.
- Dynamické přepínání režimů: Umožňuje plynulé přepínání mezi vyhrazeným režimem pro řeč a obecným zvukovým režimem v rámci probíhající relace pro optimální kvalitu.
- Provoz s nízkou latencí: Navržen pro služby konverzace v reálném čase s cílovými hodnotami celkové latence vhodnými pro XR aplikace.
- Rendering se sledováním hlavy: Integruje se s daty sledování hlavy pro vykreslování binauračního zvuku, který se přizpůsobuje pohybu hlavy posluchače a zachovává stabilitu zvukového pole.
- Standardizovaná integrace s IMS: Definován jako mediální kodek v rámci MTSI a streamovacích služeb 3GPP, což zajišťuje interoperabilitu napříč sítěmi a zařízeními.

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.249** (Rel-19) — Immersive Audio Split Rendering (ISAR)
- **TS 26.250** (Rel-19) — IVAS Codec Introduction
- **TS 26.251** (Rel-19) — IVAS Codec Fixed-Point C Code Specification
- **TS 26.252** (Rel-19) — IVAS Codec Test Sequences Specification
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure
- **TS 26.256** (Rel-19) — Jitter Buffer Management for IVAS
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [IVAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ivas/)
