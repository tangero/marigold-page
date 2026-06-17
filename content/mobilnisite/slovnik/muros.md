---
slug: "muros"
url: "/mobilnisite/slovnik/muros/"
type: "slovnik"
title: "MUROS – Multi-User Reusing One Slot"
date: 2025-01-01
abbr: "MUROS"
fullName: "Multi-User Reusing One Slot"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/muros/"
summary: "Technika pro zvýšení kapacity sítí GSM/EDGE, při které více uživatelů sdílí stejný fyzický časový slot pomocí pokročilého zpracování signálu, jako je adaptivní víceuživatelská konstelace nebo potlačen"
---

MUROS je technika pro zvýšení kapacity sítí GSM/EDGE, při které více uživatelů sdílí stejný fyzický časový slot za použití pokročilého zpracování signálu za účelem zvýšení spektrální účinnosti.

## Popis

Multi-User Reusing One Slot (MUROS) je funkce vyvinutá pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) za účelem zvýšení kapacity. V tradičním GSM je jeden časový slot na kmitočtovém nosiči vyhrazen jednomu uživateli po dobu hovoru nebo datové relace. MUROS tento princip porušuje tím, že umožňuje multiplexovat dva (nebo potenciálně více) uživatelů na stejný fyzický zdroj časového slotu. Toho je dosaženo nikoli prostým časovým dělením, ale sofistikovaným zpracováním signálu jak na základnové stanici ([BTS](/mobilnisite/slovnik/bts/)), tak v mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Mezi klíčové techniky patří použití adaptivních neortogonálních modulačních konstelací (jako jsou varianty Gaussian Minimum Shift Keying), které kódují data pro více uživatelů současně, a nasazení pokročilých přijímačů s možností potlačení interference pro oddělení signálů na sdíleném kanálu. Síťový scheduler páruje uživatele na základě jejich podmínek na rádiovém kanálu a úrovní výkonu, aby optimalizoval zisk z multiplexování. MUROS funguje transparentně vůči protokolům vyšších vrstev a znovu využívá stávající strukturu fyzické vrstvy GSM. Efektivně zdvojnásobuje kapacitu hlasových kanálů na dané sadě nosičů, čímž zmírňuje přetížení v hustě obydlených městských oblastech nebo během špičky provozu, a představuje významný vývoj v prodloužení životnosti technologie 2G.

## K čemu slouží

MUROS byl vytvořen, aby řešil kritická omezení kapacity, kterým čelí operátoři GSM, zejména když rozšíření chytrých telefonů zvýšilo datový provoz a hlasový provoz zůstal významný. Získání nového spektra je drahé a často nemožné a zhušťování sítě přidáváním dalších stanovišť má také vysoké náklady a logistické výzvy. MUROS poskytl řešení, které lze nasadit softwarovou aktualizací, pro získání větší kapacity z existujících spektrálních zdrojů GSM. Řešil problém přetížených oblastí a umožnil operátorům odložit kapitálové výdaje na nové nosiče nebo stanoviště. Technika byla motivována potřebou podporovat pokračující růst zařízení Machine-to-Machine (M2M) a IoT v sítích 2G, které jsou často nasazovány pro své výhody v pokrytí a životnosti baterie. Opětovným využitím slotu MUROS efektivně umožňuje formu neortogonálního mnohonásobného přístupu (NOMA) pro GSM, což je koncept, který později ovlivnil vývoj v technologiích 4G a 5G, a činí z něj průkopnickou technologii pro zvýšení kapacity.

## Klíčové vlastnosti

- Umožňuje dvěma uživatelům sdílet jeden časový slot GSM
- Používá adaptivní víceuživatelské modulační schémata (např. AQPSK, 8PSK-MUROS)
- Vyžaduje pokročilé přijímače s podporou potlačení interference
- Transparentní vůči core network a uživatelským aplikacím
- Dynamicky páruje uživatele na základě podmínek na kanálu pro optimální výkon
- Významně zvyšuje hlasovou a datovou kapacitu na jeden transceiver

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 43.801** (Rel-12) — VAMOS Enhancements Study for GERAN
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MUROS na 3GPP Explorer](https://3gpp-explorer.com/glossary/muros/)
