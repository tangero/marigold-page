---
slug: "sef"
url: "/mobilnisite/slovnik/sef/"
type: "slovnik"
title: "SEF – Service Element Function"
date: 2025-01-01
abbr: "SEF"
fullName: "Service Element Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sef/"
summary: "Funkční komponenta v architektuře správy 3GPP, která modeluje a spravuje konkrétní, znovupoužitelný servisní prvek. Poskytuje standardizovaný způsob pro definování, vytváření instancí a správu samosta"
---

SEF je funkční komponenta v architektuře správy 3GPP, která modeluje a spravuje konkrétní, znovupoužitelný servisní prvek jako standardizovaný stavební blok pro telekomunikační služby.

## Popis

Service Element Function (SEF, funkce servisního prvku) je konceptuální entita v rámci Telekomunikační manažerské sítě ([TMN](/mobilnisite/slovnik/tmn/)) 3GPP a pozdějších rámců pro správu, konkrétně definovaná v kontextu Sdíleného datového prostředí (SDE) a správy služeb. Představuje spravovaný objekt, který modeluje samostatný, znovupoužitelný prvek telekomunikační služby. SEF není fyzický síťový uzel, ale logický konstrukt správy, který zapouzdřuje atributy, chování a životní cyklus konkrétní servisní schopnosti. Příklady toho, co může SEF modelovat, zahrnují schránku hlasové pošty, pravidlo přesměrování hovoru, profil QoS nebo komponentu tarifního plánu. Jeho hlavní úlohou je poskytnout standardizované, abstrahované rozhraní pro systém správy, aby mohl konfigurovat, monitorovat a řídit tyto jemně odstupňované servisní prvky.

Architektonicky se SEF nacházejí ve vrstvě správy služeb ([SML](/mobilnisite/slovnik/sml/)) hierarchie TMN. Jsou spravovány nadřazenými funkcemi správy služeb ([SMF](/mobilnisite/slovnik/smf/)), které skládají více SEF dohromady, aby vytvořily kompletní služby pro zákazníky. Každý SEF je definován bází informací pro správu ([MIB](/mobilnisite/slovnik/mib/)), která specifikuje jeho spravovatelné atributy, operace, které na něm lze provádět (např. vytvořit, upravit, smazat, pozastavit), a oznámení, která může vysílat. SEF komunikuje s funkcemi správy zdrojů ([RMF](/mobilnisite/slovnik/rmf/)), aby namapoval svou logickou konfiguraci na skutečné síťové zdroje (jako síťové elementy a funkce síťových elementů), které implementují funkcionalitu servisního prvku. Tato abstrakce odděluje servisní logiku od implementace zdrojů.

Fungování SEF zahrnuje správu jeho životního cyklu prostřednictvím standardizovaných rozhraní, typicky založených na protokolech jako Common Management Information Protocol ([CMIP](/mobilnisite/slovnik/cmip/)) nebo později [SNMP](/mobilnisite/slovnik/snmp/) a webové služby. Když je pro zákazníka zřizována nová služba, systém správy služeb vytvoří instance potřebných objektů SEF (např. jeden pro čekání hovoru, jeden pro konkrétní datový tok) a nakonfiguruje jejich atributy podle zákaznického předplatného. SEF pak zajišťují konzistentní aplikaci a udržování těchto konfigurací. Poskytují bod pro správu poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS) na úrovni servisního prvku. Rozkládáním složitých služeb na spravovatelné SEF získávají operátoři flexibilitu při návrhu nových balíčků služeb a zlepšují efektivitu procesů aktivace, zajištění a účtování služeb.

## K čemu slouží

Koncept SEF byl vytvořen, aby řešil složitost a rigiditu správy monolitických telekomunikačních služeb. V raných systémech správy byly služby často spravovány jako nedělitelné celky, což ztěžovalo opětovné použití společných komponent, přizpůsobení nabídek nebo rychlé nasazení nových služeb. SEF zavedl modulární, objektově orientovaný přístup ke správě služeb, inspirovaný principy softwarového inženýrství. Jeho účelem je umožnit dekompozici služeb, což operátorům dovoluje definovat služby jako kompozice standardizovaných, spravovatelných stavebních bloků.

To řeší několik klíčových problémů: snižuje dobu vývoje nových služeb podporou opětovného použití předdefinovaných a otestovaných servisních prvků; zjednodušuje zřizování a modifikaci služeb, protože změny lze provádět na úrovni prvku namísto celé služby; a zvyšuje provozní efektivitu poskytnutím jasnější izolace poruch a podrobnějšího monitorování výkonu. SEF je základním konceptem pro dosažení flexibilního vytváření a správy služeb v prostředí s více dodavateli, protože poskytuje společný model pro reprezentaci a řízení samostatných servisních schopností v rámci systémů správy, nezávisle na podkladové síťové technologii.

## Klíčové vlastnosti

- Modeluje samostatný, znovupoužitelný stavební blok telekomunikační služby
- Definuje standardizovaný spravovaný objekt s atributy, operacemi a oznámeními
- Umožňuje modulární návrh a skládání služeb
- Poskytuje vrstvu abstrakce mezi servisní logikou a fyzickými/virtuálními zdroji
- Podporuje plnou správu FCAPS na úrovni granularity servisního prvku
- Usnadňuje rychlé zřizování a přizpůsobení služeb prostřednictvím manipulace s prvky

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [SEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sef/)
