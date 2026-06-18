---
slug: "sola"
url: "/mobilnisite/slovnik/sola/"
type: "slovnik"
title: "SOLA – Synchronized Overlap-Add"
date: 2025-01-01
abbr: "SOLA"
fullName: "Synchronized Overlap-Add"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sola/"
summary: "SOLA je algoritmus pro digitální zpracování signálu používaný pro vysoce kvalitní změnu časové stupnice audio signálů, jako je zrychlení nebo zpomalení přehrávání bez změny tónu. V rámci 3GPP je stand"
---

SOLA je v rámci 3GPP standardizovaný algoritmus pro digitální zpracování signálu pro vysoce kvalitní změnu časové stupnice audia, který umožňuje funkce jako nastavitelná rychlost přehrávání hlasových zpráv bez změny tónu.

## Popis

Synchronized Overlap-Add (SOLA) je sofistikovaný časově-doménový algoritmus pro změnu časové stupnice ([TSM](/mobilnisite/slovnik/tsm/)) audio signálů. Jeho primární funkcí je změnit délku (nebo rychlost přehrávání) audio segmentu bez ovlivnění jeho percepční výšky tónu nebo charakteristiky zvuku. To je odlišné od prostého převzorkování, které by změnilo jak rychlost, tak tón. Algoritmus SOLA pracuje tak, že vstupní audio signál rozloží na krátké, překrývající se analytické rámce. Tyto rámce jsou následně přesunuty na časové ose podle požadovaného faktoru změny rychlosti (α). Pokud α > 1, signál je zrychlen (komprimován v čase); pokud α < 1, je zpomalen (roztažen v čase).

Klíčová inovace SOLA spočívá v kroku 'synchronizované' vzájemné korelace provedeném během procesu překrytí a přidání. Když jsou dva po sobě jdoucí výstupní rámce překryty a přidány dohromady, aby vytvořily souvislý výstupní průběh, může přímé překrytí a přidání s pevným rozestupem způsobit fázové nespojitosti vedoucí ke slyšitelnému zkreslení nebo 'klikání'. SOLA tomu zabraňuje výpočtem vzájemné korelace mezi překrývajícími se částmi obou rámců. Následně identifikuje časové zpoždění (nebo posun), které maximalizuje jejich podobnost. Druhý rámec je před operací překrytí a přidání posunut o toto optimální zpoždění, čímž se efektivně synchronizují průběhy v bodě jejich překrytí. Tato synchronizace zachovává periodickou strukturu kvazi-stacionárních signálů, jako je hlasový projev, což vede k hladkému, vysoce kvalitnímu výstupu s minimálními artefakty.

V kontextu 3GPP je SOLA specifikováno v TS 26.448 pro kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Jedná se o klíčovou komponentu pro implementaci řízení rychlosti přehrávání hlasových zpráv nebo nahrané řeči. Algoritmus pracuje na dekódovaném audio signálu a poskytuje flexibilní a efektivní krok zpracování. Jeho parametry, jako je délka analytického rámce a délka překrytí, jsou optimalizovány pro řečové signály, aby byla vyvážena výpočetní složitost s výstupní kvalitou. Standardizací SOLA zajišťuje 3GPP interoperabilní a vysoce kvalitní změnu časové stupnice napříč různými zařízeními a sítěmi, což zlepšuje uživatelský zážitek u hlasových služeb.

## K čemu slouží

SOLA byla vyvinuta pro řešení problému změny rychlosti přehrávání řeči přirozeným a srozumitelným způsobem. Před pokročilými algoritmy [TSM](/mobilnisite/slovnik/tsm/) způsobovaly jednoduché metody, jako opakování nebo mazání vzorků, závažné percepční artefakty, například kmitání, dozvuk nebo robotický zvuk, zvláště u řečových signálů. Potřeba vysoce kvalitní změny časové stupnice vyvstala z praktických uživatelských funkcí, jako je poslech hlasových zpráv zvýšenou rychlostí pro úsporu času nebo zpomalení zprávy pro lepší pochopení, zejména v hlučném prostředí nebo pro studenty jazyků.

Přijetí a standardizace SOLA v rámci 3GPP byla motivována vývojem hlasových služeb od prostého volání k bohaté multimediální komunikaci. Funkce jako hlasové zprávy, přehrávání audio poznámek a podpora přepisu v reálném čase se staly důležitými. SOLA poskytuje výpočetně efektivní a vysoce kvalitní řešení vhodné pro implementaci na mobilních zařízeních. Řeší omezení dřívějších technik překrytí a přidání dynamickou synchronizací segmentů průběhu, což je klíčové pro zachování přirozené prozódie a srozumitelnosti řeči se změněnou časovou stupnicí. Její zařazení do specifikací kodeku [EVS](/mobilnisite/slovnik/evs/) zajišťuje širokou dostupnost a konzistentní implementaci této vylepšené funkce, což přispívá k bohatšímu ekosystému hlasových služeb.

## Klíčové vlastnosti

- Vysoce kvalitní změna časové stupnice bez změny tónu (Time-Scale Modification)
- Používá vzájemnou korelaci pro optimální synchronizaci překrývajících se audio segmentů
- Minimalizuje slyšitelné artefakty, jako jsou klikání a fázové nespojitosti
- Optimalizováno pro zpracování řečových signálů v telekomunikacích
- Standardizováno jako funkce následného zpracování pro kodek 3GPP EVS
- Umožňuje proměnnou rychlost přehrávání pro hlasové zprávy a nahrané audio

## Definující specifikace

- **TS 26.448** (Rel-19) — EVS Jitter Buffer Management Specification

---

📖 **Anglický originál a plná specifikace:** [SOLA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sola/)
