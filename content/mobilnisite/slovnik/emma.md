---
slug: "emma"
url: "/mobilnisite/slovnik/emma/"
type: "slovnik"
title: "EMMA – Extensible MultiModal Annotation markup language"
date: 2025-01-01
abbr: "EMMA"
fullName: "Extensible MultiModal Annotation markup language"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/emma/"
summary: "EMMA je značkovací jazyk založený na XML, standardizovaný konsorciem W3C a odkazovaný organizací 3GPP, pro reprezentaci interpretací uživatelských vstupů v multimodálních systémech. Umožňuje aplikacím"
---

EMMA je značkovací jazyk založený na XML, standardizovaný konsorciem W3C a odkazovaný organizací 3GPP, určený pro reprezentaci interpretací uživatelských vstupů z různých modalit, jako je hlas nebo klávesnice, v jednotném formátu pro multimodální systémy.

## Popis

Extensible MultiModal Annotation markup language (EMMA) je doporučení konsorcia World Wide Web Consortium (W3C), které poskytuje formát pro výměnu dat pro reprezentaci sémantiky uživatelských vstupů v multimodálních interaktivních systémech. Přestože se nejedná o protokol vynalezený 3GPP, je v rámci specifikací 3GPP (zejména TS 23.333) odkazován jako potenciální komponenta pro standardizaci způsobu, jakým jsou multimodální vstupy anotovány a zpracovávány v architekturách telekomunikačních služeb, zejména pro Multimedia Telephony (MMTel) a další služby založené na IP. Dokumenty EMMA jsou instance XML, které popisují interpretace uživatelských vstupů, jež mohou pocházet z různých modalit, jako je řeč, klávesnice, dotyk nebo gesto.

Dokument EMMA strukturovaně uchovává informace o interpretaci, včetně nezpracovaných vstupních dat, odvozeného významu (jako je rozpoznaný záměr nebo extrahované entity), míry spolehlivosti z procesu rozpoznání, časových informací a zdrojové modality. To umožňuje multimodální aplikaci, potenciálně běžící na síťovém serveru nebo zařízení, slučovat vstupy z různých zdrojů. Například uživatel může říct "ukaž mi tohle" a současně klepnout na mapu; rozpoznávač řeči vygeneruje strukturu EMMA pro výrok a rozpoznávač gest vygeneruje strukturu pro souřadnice klepnutí. Dialogový manažer pak může zpracovat tyto kombinované struktury EMMA k provedení příkazu.

V kontextu 3GPP je úlohou EMMA umožnit interoperabilní pokročilé uživatelské rozhraní pro služby definované v rámci IP Multimedia Subsystem (IMS). Tím, že poskytuje standardizovaný způsob anotace vstupu, umožňuje oddělení servisní logiky od konkrétních rozpoznávacích technologií nebo zařízení. To podporuje vytváření bohatších a přirozenějších rozhraní mezi člověkem a strojem pro služby, jako je interaktivní hlasová odpověď ([IVR](/mobilnisite/slovnik/ivr/)) s vizuálními doplňky, nebo jednotná komunikace, kde vstupem může být řeč nebo text. Specifikace 3GPP odkazují na EMMA jako na součást definice architektury a informačních toků pro multimodální služby, což zajišťuje, že síťové multimodální interakční manažery mohou zpracovávat vstupy ve formátu nezávislém na dodavateli.

## K čemu slouží

EMMA byl vyvinut pracovní skupinou W3C Multimodal Interaction Working Group k řešení problému interoperability v multimodálních systémech, kde aplikace potřebují kombinovat vstupy z různých rozpoznávacích technologií (řeč, ručně psaný text, vizuální vstupy). Před standardizací používal každý rozpoznávač nebo fúzní engine svůj vlastní proprietární datový formát, což ztěžovalo vytváření modulárních a škálovatelných multimodálních aplikací. EMMA poskytl společnou rozšiřitelnou XML slovní zásobu pro reprezentaci interpretací, což umožnilo snadnou integraci různých rozpoznávacích komponent.

Motivace 3GPP pro odkazování na EMMA ve svých specifikacích (počínaje Release 7) byla podpora vývoje telefonních služeb za hranice jednoduchých hlasových hovorů směrem k bohaté, interaktivní službě Multimedia Telephony (MMTel) v rámci IMS. Jak se služby stávaly komplexnějšími a umožňovaly uživatelům interagovat prostřednictvím hlasu, dotyku a klávesnice současně, bylo zapotřebí standardizovaného způsobu zpracování těchto kombinovaných vstupů na úrovni servisní vrstvy. Přijetí existujícího standardu W3C, jako je EMMA, umožnilo 3GPP vyhnout se zbytečnému vynalézání a sladit se s webovými standardy, což usnadnilo konvergenci telekomunikačních a webových služeb. Tím bylo řešeno omezení předchozích architektur telekomunikačních služeb, které byly do značné míry rozděleny podle modalit (např. řízení hlasového hovoru oddělené od textových zpráv), a byl položen základ pro jednotné, kontextově-aware řízení interakce.

## Klíčové vlastnosti

- Formát založený na XML pro reprezentaci sémantických interpretací uživatelského vstupu
- Podpora anotace vstupu z více modalit (řeč, dotyk, klávesnice atd.)
- Zahrnutí metadat, jako jsou míry spolehlivosti, časová razítka a identifikace zdrojové modality
- Umožnění fúze informací poskytnutím společné struktury pro vstupy z různých rozpoznávačů
- Rozšiřitelnost prostřednictvím XML jmenných prostorů pro akomodaci doménově specifické sémantiky
- Umožnění interoperability mezi různými rozpoznávacími enginy a multimodální aplikační logikou

## Související pojmy

- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [EMMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/emma/)
