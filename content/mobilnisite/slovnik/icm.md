---
slug: "icm"
url: "/mobilnisite/slovnik/icm/"
type: "slovnik"
title: "ICM – In-Call Modification"
date: 2025-01-01
abbr: "ICM"
fullName: "In-Call Modification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/icm/"
summary: "Servisní schopnost, která umožňuje upravovat aktivní komunikační relace (jako jsou hlasové nebo videohovory) bez přerušení hovoru. Umožňuje uživatelům nebo síti změnit parametry relace, například přid"
---

ICM je servisní schopnost, která umožňuje upravovat aktivní komunikační relace, jako jsou hlasové nebo videohovory, bez přerušení hovoru změnou parametrů, například přidáním videa nebo dalšího účastníka.

## Popis

In-Call Modification (ICM) je servisní funkce v doméně IP Multimedia Subsystem (IMS) a přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)), která umožňuje dynamicky měnit parametry již navázaného, aktivního hovoru nebo relace. Toho je dosaženo přejednáním popisu relace, který je přenášen v signalizačních zprávách SIP (pro IMS) nebo v příslušné signalizaci Bearer Independent Call Control (BICC)/[ISUP](/mobilnisite/slovnik/isup/) (pro CS). Proces může iniciovat některý z koncových bodů účastníků (UE) nebo síťová aplikační služba. V IMS odešle UE v rámci existujícího dialogu požadavek SIP re-INVITE nebo UPDATE, který obsahuje novou nabídku Session Description Protocol (SDP) navrhující změněné charakteristiky médií.

Hlavní síťové prvky, především Serving-Call Session Control Function (S-CSCF), tento požadavek zpracují, aplikují příslušnou servisní logiku a přepošlou jej druhé straně. Vzdálená strana odpoví zprávou SIP 200 OK obsahující SDP odpověď, čímž potvrdí přijetí nových parametrů. To spustí odpovídající aktualizaci přenosové roviny; například může být zapojen Packet Data Network Gateway (PGW) a Policy and Charging Rules Function (PCRF) ke změně vyhrazeného přenašeče pro mediální proud s novými parametry QoS. Architektura zajišťuje, že změna proběhne plynule, při zachování hlavní signalizační asociace (dialogu) a pokud možno bez přerušení média.

ICM podporuje širokou škálu úprav. Mezi ně patří přidání nové mediální komponenty (např. upgrade hlasového hovoru na videohovor), odebrání mediální komponenty (např. zastavení videa pro úsporu šířky pásma), změna kodeku (např. z [AMR](/mobilnisite/slovnik/amr/) na [EVS](/mobilnisite/slovnik/evs/) pro lepší kvalitu), úprava šířky pásma nebo změna časovačů relace. Je také základním mechanismem používaným pro přidání třetí strany do bod-bod hovoru, čímž se změní na konferenční hovor s více účastníky, který je často řízen Multimedia Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)). Tato funkce závisí na schopnosti koncových bodů a síťových uzlů podporovat přejednávání modelu nabídka/odpověď SDP a odpovídající procedury správy přenašečů.

## K čemu slouží

ICM byl vyvinut, aby překonal rigidnost tradičních telefonních hovorů, kde byly charakteristiky hovoru pevně stanoveny při jeho navázání. V raných buněčných systémech jakákoliv změna hovoru (jako přidání videoproudu) vyžadovala ukončení stávajícího hovoru a zřízení nového, což bylo rušivé a poskytovalo špatný uživatelský zážitek. Jak se sítě vyvíjely k podpoře bohatých multimediálních služeb, vznikla jasná potřeba, aby relace během své existence mohly být přizpůsobeny měnícím se potřebám uživatelů, možnostem zařízení nebo stavu sítě.

Standardizovaný v 3GPP Release 5 spolu s IMS byl ICM klíčovým prvkem pro naplnění slibu IMS "jakékoliv médium, kdykoliv". Vyřešil problém servisní flexibility a umožnil operátorům nabízet funkce jako "Přidání videa k hlasu" nebo plynulé zřizování konferencí. Z pohledu efektivity sítě také umožňuje dynamickou adaptaci na síťovou zátěž přejednáním kodeku s nižním datovým tokem bez přerušení hovoru. Jeho vznik byl motivován konvergencí telefonie a datových služeb, která vyžadovala signalizační rámec (SIP/SDP) inherentně podporující takové změny v průběhu relace, což byl významný pokrok oproti statické povaze tradiční signalizace přepojování okruhů.

## Klíčové vlastnosti

- Dynamické přejednání parametrů relace pomocí SIP re-INVITE nebo UPDATE
- Úprava mediálních proudů (přidání, odebrání, změna kodeku, změna šířky pásma)
- Podpora upgradu hlasového hovoru na videohovor (a naopak)
- Základní procedura pro přidání účastníků a vytvoření konferenčního hovoru
- Integrace s řízením politik (PCRF) pro aktualizaci QoS přenašeče
- Aplikovatelné jak v IMS, tak v doménách starších sítí s přepojováním okruhů (CS)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 36.750** (Rel-14) — Study on enhancement of VoLTE
- **TS 45.009** (Rel-19) — GSM AMR Link Adaptation & Control

---

📖 **Anglický originál a plná specifikace:** [ICM na 3GPP Explorer](https://3gpp-explorer.com/glossary/icm/)
