---
slug: "vdi"
url: "/mobilnisite/slovnik/vdi/"
type: "slovnik"
title: "VDI – Video Decoding Interface"
date: 2025-01-01
abbr: "VDI"
fullName: "Video Decoding Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vdi/"
summary: "Standardizované rozhraní v architektuře služby Multimedia Broadcast Multicast Service (MBMS) podle 3GPP, které definuje, jak klientská aplikace nebo uživatelské zařízení vyžádá a přijímá dekódované vi"
---

VDI je standardizované rozhraní v architektuře MBMS podle 3GPP, které definuje, jak klient vyžádá a přijímá dekódované video streamy ze síťového dekodéru, čímž přenáší náročné dekódovací úlohy pro efektivní doručování.

## Popis

Video Decoding Interface (VDI) je funkční rozhraní specifikované v kontextu služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) podle 3GPP a souvisejících rámců pro doručování multimédií. Jeho hlavní úlohou je definovat protokoly a procedury pro interakci klienta, typicky v uživatelském zařízení (UE) nebo terminálu, se síťovou entitou pro dekódování videa. Toto rozhraní umožňuje klientovi vyžádat video obsah doručený v zakódovaném formátu, který je následně dekódován síťovou funkcí před odesláním klientovi ve formátu připraveném k zobrazení. Architektura odděluje výpočetně náročnou úlohu dekódování videa od UE s omezenými zdroji a centralizuje ji v síti.

Provozně VDI funguje tak, že mezi klientem a Video Decoding Function (VDF) v síti naváže relaci. Klient odešle požadavek specifikující požadovaný video obsah a případně požadovaný výstupní formát (např. rozlišení, kodek). Síťová VDF získá zakódovaný video stream, který může být vysílán/multicastován přes MBMS nebo doručen unicastem, provede proces dekódování a následně streamuje dekódované video (např. ve formátu raw YUV nebo lehce zabalené formě) klientovi přes vyhrazený bearer. Tento proces zahrnuje signalizaci pro navázání relace, řídicí příkazy (přehrát, pozastavit, stop) a samotné streamování dekódovaných video dat.

Klíčové komponenty zahrnují VDI klienta v UE, Video Decoding Function v síti (která může být součástí Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) nebo vyhrazeného uzlu pro zpracování médií) a definované aplikační protokoly pro řízení a přenos. Specifikace rozhraní pokrývají aspekty jako vyjednávání schopností, hlášení chyb a synchronizace. Jeho role je klíčová ve scénářích, kdy UE nemá dostatečný výpočetní výkon nebo výdrž baterie pro lokální dekódování vysoce kvalitních video streamů, nebo když síť chce zajistit jednotnou kvalitu videa centrální správou dekódovacího procesu.

## K čemu slouží

Video Decoding Interface bylo vytvořeno, aby řešilo výzvu doručování vysoce kvalitních video služeb širokému spektru mobilních zařízení s různými výpočetními schopnostmi a omezeními baterie. Rané mobilní video služby vyžadovaly, aby UE provádělo plné dekódování videa, což mohlo rychle vybíjet baterie a vyloučit nízkorozpočtová zařízení z přístupu k pokročilému obsahu. VDI to vyřešilo zavedením architektury síťového dekódování, která přenáší tuto složitou úlohu na síťovou infrastrukturu.

Primární problém, který řeší, je umožnění efektivního a spravedlivého multimediálního broadcastu/multicastu. Pro [MBMS](/mobilnisite/slovnik/mbms/), kde je stejný obsah odesílán mnoha uživatelům, může být provedení dekódování jednou v síti a následné streamování dekódovaného videa efektivnější než odesílání zakódovaných streamů, které musí dekódovat každé UE individuálně, zejména pokud lze dekódovaný stream přizpůsobit společnému formátu. To také umožňuje síti provádět centrální transkódování nebo změnu datového toku, aby odpovídaly různým schopnostem zobrazení UE.

Historicky zavedené ve vydání 7 spolu s vylepšeními MBMS bylo VDI součástí snahy o zavedení životaschopných služeb mobilní televize a video broadcastu. Poskytlo standardizovaný způsob implementace architektur videa s tenkým klientem, čímž snížilo náklady a složitost UE. I když není univerzálně nasazeno ve všech sítích, představuje důležitý architektonický koncept v 3GPP pro síťově asistované zpracování médií, jehož princip nachází ozvěny v pozdějších technologiích, jako je mobile edge computing a cloud gaming.

## Klíčové vlastnosti

- Definuje protokoly pro vyžádání síťových relací dekódování videa ze strany UE
- Podporuje doručování dekódovaných video streamů ve formátech připravených k vykreslení
- Umožňuje vyjednávání schopností mezi klientem a síťovou dekódovací funkcí
- Umožňuje odesílání řídicích příkazů (přehrát, pozastavit, stop) přes rozhraní
- Usnadňuje mechanismy hlášení chyb a obnovy pro dekódovací relaci
- Navrženo pro práci s MBMS broadcast/multicast i unicastovými mechanismy doručování

## Definující specifikace

- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [VDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/vdi/)
