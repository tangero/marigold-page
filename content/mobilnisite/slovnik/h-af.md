---
slug: "h-af"
url: "/mobilnisite/slovnik/h-af/"
type: "slovnik"
title: "H-AF – Home Application Function"
date: 2025-01-01
abbr: "H-AF"
fullName: "Home Application Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-af/"
summary: "Aplikační funkce umístěná v domovské síti uživatele. Interaguje s domovským rámcem pro správu politik (PCRF/PCF) za účelem vyžádání řízení politik a účtování pro služby účastníka. Je klíčovým prvkem p"
---

H-AF je aplikační funkce (Application Function) umístěná v domovské síti uživatele, která interaguje s rámcem pro správu politik za účelem vyžádání řízení politik a účtování pro služby účastníka.

## Popis

Domovská aplikační funkce (H-AF) je prvek jádra sítě definovaný v architektuře 3GPP pro řízení politik a účtování (PCC). Nachází se v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) uživatele. Koncepčně je aplikační funkce ([AF](/mobilnisite/slovnik/af/)) prvek sítě, který nabízí aplikace vyžadující dynamické řízení politik a/nebo účtování nad uživatelskou rovinou. Kvalifikátor 'Domovská' (Home) určuje její umístění v domovské síti účastníka, na rozdíl od navštívené AF (V-AF), která může být v navštívené síti při roamingu.

Hlavní úlohou H-AF je vystupovat jako žadatel služby vůči funkci pro pravidla řízení politik a účtování (PCRF v 4G) nebo funkci řízení politik ([PCF](/mobilnisite/slovnik/pcf/) v 5G). To činí prostřednictvím referenčního bodu Rx v 4G (mezi AF a PCRF) nebo referenčního bodu N5 v 5G (mezi AF a PCF). H-AF poskytuje systému PCC informace související se sezením odvozené z aplikační vrstvy. Tyto informace jsou nezbytné pro to, aby PCRF/PCF mohla činit informovaná rozhodnutí o politikách. Například H-AF pro službu IP multimedia subsystému (IMS) by poskytovala podrobnosti o VoIP hovoru, jako je typ média (audio/video), šířka pásma kodeku a paketové filtry popisující zdrojové/cílové IP adresy a porty mediálního toku.

Po přijetí těchto informací o sezení z aplikační vrstvy je PCRF/PCF použije spolu s daty účastníka ze SPR/UDR a stavem sítě k vytvoření dynamických pravidel PCC. Tato pravidla jsou následně zřízena pro funkci vynucení politik a účtování (PCEF) v 4G (typicky PGW) nebo funkci správy sezení ([SMF](/mobilnisite/slovnik/smf/)) v 5G. Pravidla řídí, jak je zacházeno s provozem v uživatelské rovině pro dané aplikační sezení – definují parametry QoS (jako garantovanou přenosovou rychlost), uplatňují gating (blokování/povolení paketů) a spouštějí příslušné účtovací akce. H-AF může také přijímat od PCRF/PCF oznámení o událostech v přenosové síti, jako je ztráta nosných prostředků, což umožňuje aplikaci se přizpůsobit.

Architektonicky je H-AF logická funkce. Její nejběžnější fyzickou realizací je jako součást sítě IMS, například Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)). Může to však být jakýkoli server poskytující službu, která vyžaduje garantovanou QoS od podkladové přenosové sítě, například herní server nebo aplikační brána podniku. Její přítomnost v domovské síti je klíčová pro udržení konzistentního řízení služebních politik a účtování, protože domovský operátor si ponechává pravomoc nad profilem politik účastníka.

## K čemu slouží

H-AF byla vytvořena za účelem překlenutí mezery mezi aplikační vrstvou (servisní vrstvou) a přenosovou/řídicí vrstvou v mobilních sítích. Před architekturou PCC byly síťové prostředky přidělovány staticky nebo na základě jednoduchých konfigurací názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)) bez dynamické interakce z aplikace. To bylo nedostatečné pro nově vznikající služby citlivé na QoS v reálném čase, jako je Voice over IP (VoIP) a streamování videa, které vyžadují specifické garance šířky pásma a nízkou latenci, jež se liší podle sezení.

Rámec PCC, představený ve 3GPP Release 7 a vyvíjený v následujících vydáních, byl navržen tak, aby toto vyřešil umožněním dynamického řízení politik s ohledem na aplikaci. H-AF je základní součástí tohoto řešení. Existuje proto, aby poskytovatelé služeb (jako operátoři IMS) mohli v reálném čase komunikovat své specifické požadavky na prostředky k síťovému mechanismu politik. To umožňuje síti zacházet s aplikačním provozem na základě jednotlivých toků s příslušnou QoS, namísto uplatňování univerzální politiky.

Tím byly řešeny klíčové limity: umožnilo to efektivní využití síťových prostředků přidělováním vysoké QoS pouze v případě potřeby, umožnilo nové výnosové služby se zaručenou kvalitou a poskytlo standardizované rozhraní (Rx/N5) pro integraci poskytovatelů aplikací se sítí. Aspekt 'Domovská' zajišťuje, že domovský operátor účastníka, který vlastní vztah k účastníkovi a profil politik, si udržuje kontrolu nad rozhodnutími o politikách, a to i když je uživatel v roamingu, prostřednictvím interakce mezi domovskou PCRF/[PCF](/mobilnisite/slovnik/pcf/) a politickými entitami navštívené sítě.

## Klíčové vlastnosti

- Nachází se v domovské síti účastníka (HPLMN)
- Poskytuje informace o sezení z aplikační vrstvy PCRF/PCF prostřednictvím rozhraní Rx (4G) nebo N5 (5G)
- Umožňuje dynamické autorizace QoS pro aplikační toky (např. hlas/video IMS)
- Může přijímat oznámení o událostech na úrovni nosiče od rámce pro správu politik
- Logická funkce často umístěná společně s prvky IMS, jako je P-CSCF
- Ústřední prvek architektury 3GPP pro řízení politik a účtování (PCC)

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification

---

📖 **Anglický originál a plná specifikace:** [H-AF na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-af/)
