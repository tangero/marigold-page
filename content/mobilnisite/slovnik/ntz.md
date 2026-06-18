---
slug: "ntz"
url: "/mobilnisite/slovnik/ntz/"
type: "slovnik"
title: "NTZ – No-Transmit Zone"
date: 2026-01-01
abbr: "NTZ"
fullName: "No-Transmit Zone"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ntz/"
summary: "No-Transmit Zone (NTZ, zóna bez vysílání) je geografická oblast nebo množina zdrojů, kde je bezdrátovému zařízení zakázáno vysílat signály. Používá se k zabránění rušení jiných systémů, například půvo"
---

NTZ je geografická oblast nebo množina zdrojů, kde je bezdrátovému zařízení zakázáno vysílat, aby se zabránilo rušení jiných systémů, například původních uživatelů ve sdíleném spektru.

## Popis

No-Transmit Zone (NTZ, zóna bez vysílání) je regulační a technický koncept v 3GPP, zvláště relevantní pro sdílení spektra a správu rádiových zdrojů. Definuje konkrétní geografickou oblast nebo v některých kontextech množinu časově-frekvenčních zdrojů, v rámci kterých nesmí uživatelské zařízení (UE) nebo základnová stanice (gNB/[eNB](/mobilnisite/slovnik/enb/)) vysílat rádiové signály. Primárním mechanismem pro vynucení NTZ jsou síťově řízené politiky doručené UE. Síť, typicky prostřednictvím funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) nebo funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)), může UE poskytnout konfigurační informace o NTZ, které zahrnují geografické souřadnice (např. polygon nebo kruh) a přidružené podmínky.

Z architektonického hlediska se správa NTZ týká několika funkcí jádra sítě. Funkce pro analytiku síťových dat ([NWDAF](/mobilnisite/slovnik/nwdaf/)) nebo jiné funkce pro vystavení sítě mohou potřebu NTZ určit na základě externích vstupů, jako je systém přístupu ke spektru ([SAS](/mobilnisite/slovnik/sas/)) nebo regulační databáze označující chráněné původní uživatele (např. pozemní stanice pevné satelitní služby). Tyto informace jsou předány funkci řízení politik (PCF), která formuluje příslušné politiky. Tyto politiky jsou pak odeslány UE prostřednictvím funkce pro správu přístupu a mobility (AMF) jako součást procedury aktualizace konfigurace UE nebo počáteční registrace. Protokolový zásobník UE, konkrétně vrstva řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)), tyto politiky interpretuje a vynucuje je zákazem vysílání, když se poloha UE (určená pomocí vlastního [GNSS](/mobilnisite/slovnik/gnss/) nebo síťového určování polohy) nachází v definované NTZ.

Role NTZ je klíčová ve scénářích dynamického sdílení spektra, jako je Citizens Broadband Radio Service ([CBRS](/mobilnisite/slovnik/cbrs/)) nebo jiné režimy sdíleného/licencovaného sdíleného přístupu. Chrání uživatele s vyšší prioritou před škodlivým rušením od přenosů mobilní sítě. Když UE vstoupí do NTZ, musí ukončit vysílání na dotčených frekvencích, což může spustit předání spojení na jinou frekvenci nebo buňku mimo zónu. Konfigurace NTZ mohou být dynamické a měnit se v závislosti na denní době nebo aktivitě původního uživatele. To vyžaduje nepřetržité určování polohy UE a vynucování politik. Specifikace podrobně popisují signalizaci (např. v NAS zprávách) a parametry (jako popis geografické oblasti, frekvenční rozsah a časovač platnosti) potřebné k efektivní definici a správě NTZ v celé síti.

## K čemu slouží

Koncept NTZ byl vytvořen, aby umožnil koexistenci mezi mobilními sítěmi a jinými rádiovými systémy sdílejícími stejné frekvenční pásmo, což je problém, který se stal akutním se zavedením dynamického sdílení spektra. Tradiční statické přidělování frekvencí bylo pro flexibilní a efektivní využití spektra nedostatečné. Bez NTZ by mohly mobilní přenosy způsobit škodlivé rušení citlivým původním službám, jako jsou satelitní komunikace nebo radarové systémy, což by vedlo k porušení předpisů a zhoršení kvality těchto služeb.

Historický kontext zahrnuje otevření sdílených frekvenčních pásem, jako je pásmo 3,5 GHz CBRS v USA a podobná pásma po celém světě. Regulátoři vyžadovali mechanismy na ochranu původních uživatelů. 3GPP vyvinulo rámec NTZ, aby poskytlo standardizovanou, síťově řízenou metodu pro geografické vyloučení vysílání. Tím se řeší omezení předchozích, jednodušších přístupů, jako jsou statické vylučovací zóny nebo čistě na detekci založená řešení, kterým chyběla přesnost a kontrola politik nabízená integrovanou správou NTZ. Umožňuje operátorům mobilních sítí dynamicky respektovat ochranné zóny definované centrálním správcem spektra, což umožňuje efektivnější a kompatibilnější využití sdílených spektrálních zdrojů. Vytváření politik NTZ v architektuře jádra 5G sítě umožňuje škálovatelné, automatizované vynucování nezbytné pro rozsáhlá nasazení.

## Klíčové vlastnosti

- Geograficky definovaná oblast, kde je vysílání UE zakázáno
- Řízeno sítí prostřednictvím politik pro UE od PCF/AMF
- Chrání původní uživatele (např. satelitní, radarové) ve sdíleném spektru
- Dynamická konfigurace na základě externích vstupů (např. databází SAS)
- Integrováno s určováním polohy UE pro vynucování
- Podporuje podmínky platnosti (čas, frekvenční rozsah)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)
- **TS 33.759** (Rel-19) — UAS Security Enhancements Phase 3 Study

---

📖 **Anglický originál a plná specifikace:** [NTZ na 3GPP Explorer](https://3gpp-explorer.com/glossary/ntz/)
