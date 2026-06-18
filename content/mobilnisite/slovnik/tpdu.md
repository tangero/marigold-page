---
slug: "tpdu"
url: "/mobilnisite/slovnik/tpdu/"
type: "slovnik"
title: "TPDU – Transport Protocol Data Unit"
date: 2025-01-01
abbr: "TPDU"
fullName: "Transport Protocol Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tpdu/"
summary: "TPDU je základní datová jednotka v transportních protokolech 3GPP, představující paket uživatelských dat nebo řídicích informací vyměňovaných mezi partnerskými protokolovými entitami. Je klíčová pro s"
---

TPDU je základní datová jednotka v transportních protokolech 3GPP, představující paket uživatelských nebo řídicích informací vyměňovaných mezi partnerskými entitami za účelem strukturované enkapsulace a spolehlivého doručení.

## Popis

Transport Protocol Data Unit (TPDU) je klíčový koncept v protokolové architektuře 3GPP, představující diskrétní jednotku dat, která je vyměňována mezi partnerskými entitami na dané protokolové vrstvě. Skládá se z hlavičky Protocol Control Information ([PCI](/mobilnisite/slovnik/pci/)) a uživatelských dat, která sama mohou být Service Data Unit ([SDU](/mobilnisite/slovnik/sdu/)) z vyšší vrstvy. Struktura a sémantika TPDU jsou definovány konkrétním používaným protokolem, například pro signalizaci nebo transport uživatelské roviny. Při činnosti protokolová entita přijme SDU z vyšší vrstvy, přidá vlastní PCI a vytvoří TPDU, které pak předá dolní vrstvě, kde se stane SDU pro tuto nižší vrstvu. Tento proces enkapsulace pokračuje směrem dolů protokolovým zásobníkem, dokud nejsou data fyzicky přenesena.

Architektonicky jsou TPDU definovány v kontextu konkrétních specifikací protokolů, jako jsou [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), Radio Access Network Application Part ([RANAP](/mobilnisite/slovnik/ranap/)) nebo Short Message Service ([SMS](/mobilnisite/slovnik/sms/)). Formát TPDU zahrnuje pole pro adresování, pořadová čísla, typ přenášených dat a kontrolu chyb, což je nezbytné pro funkce jako segmentace, opětovné složení, řízení toku a obnova po chybě. Například v SMS nese TPDU typu TP-Data vlastní obsah krátké zprávy spolu s adresami odesílatele a příjemce. Konzistentní definice TPDU napříč rozhraními zajišťuje interoperabilitu mezi síťovými prvky od různých výrobců.

Její role v síti je fundamentální; TPDU umožňují vrstvený komunikační model, který je základem všech systémů 3GPP. Poskytují standardizovaný kontejner pro informace, ať už se jedná o hlasové pakety uživatele, IP data nebo signalizační zprávy pro správu mobility. Zpracování TPDU protokolovými zásobníky v síťových uzlech, jako jsou [SGSN](/mobilnisite/slovnik/sgsn/), GGSN, [MME](/mobilnisite/slovnik/mme/) a eNodeB, umožňuje poskytování komplexních služeb. Porozumění TPDU je klíčové pro analýzu protokolových tras, řešení problémů v síti a návrh efektivních síťových funkcí, které tyto datové jednotky zpracovávají vysokou rychlostí.

## K čemu slouží

Koncept TPDU existuje, aby poskytl standardizovanou a strukturovanou metodu pro výměnu dat mezi protokolovými vrstvami a přes síťová rozhraní v telekomunikačních systémech. Řeší základní problém, jak zabalit, adresovat a řídit tok informací v vícevýrobním a vrstveném síťovém prostředí. Před takovou formalizací mohly ad-hoc datové formáty vést k problémům s interoperabilitou a neefektivnímu zpracování.

Motivace pro definování TPDU ve specifikacích 3GPP vychází z potřeby spolehlivé a jednoznačné komunikace. Specifikací přesného formátu a pravidel pro zpracování datových jednotek na každé protokolové vrstvě 3GPP zajišťuje, že síťový prvek vyvinutý jedním výrobcem může správně interpretovat a zpracovat zprávy od jiného. To je klíčové pro globální roaming a interoperabilitu služeb, které definují moderní mobilní sítě. Abstrakce TPDU umožňuje nezávislý vývoj aplikací vyšších vrstev na podkladových transportních mechanismech, což podporuje inovace a škálovatelnost.

## Klíčové vlastnosti

- Standardizovaná enkapsulace řídicích protokolových informací a uživatelských dat
- Definuje základní jednotku výměny pro komunikaci protokolů typu peer-to-peer
- Umožňuje funkce jako segmentace, opětovné složení a číslování sekvencí
- Formáty specifikované podle protokolu (např. GTP-U TPDU, SMS TPDU)
- Nezbytné pro interoperabilitu mezi síťovými prvky od různých výrobců
- Základ pro analýzu protokolů a řešení problémů v síti

## Související pojmy

- [SDU – Signalling Data Unit](/mobilnisite/slovnik/sdu/)
- [PDU – Protocol Data Unit](/mobilnisite/slovnik/pdu/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.040** (Rel-19) — SMS Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification

---

📖 **Anglický originál a plná specifikace:** [TPDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpdu/)
