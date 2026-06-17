---
slug: "etns"
url: "/mobilnisite/slovnik/etns/"
type: "slovnik"
title: "ETNS – European Telecommunications Numbering Space"
date: 2026-01-01
abbr: "ETNS"
fullName: "European Telecommunications Numbering Space"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/etns/"
summary: "Harmonizované číslovací pásmo (+388) definované pro panevropské telekomunikační služby. Poskytuje jednotný a rozpoznatelný formát čísla pro služby provozované napříč více evropskými zeměmi, odlišný od"
---

ETNS je harmonizované evropské číslovací pásmo (+388), které poskytuje jednotný a rozpoznatelný formát čísla pro panevropské telekomunikační služby napříč více zeměmi.

## Popis

European Telecommunications Numbering Space (ETNS) je nadnárodní číslovací zdroj definovaný v rámci směrového čísla země +388, které je vyhrazeno výhradně pro služby v celoevropském měřítku. Spravovaný pod dohledem Evropské komise a Evropské konference pošt a telekomunikací ([CEPT](/mobilnisite/slovnik/cept/)) poskytuje ETNS jednotný formát číslování pro služby, které jsou ze své podstaty panevropské. Na rozdíl od národních telefonních čísel, která jsou vázána na číslovací plán konkrétní země (např. +44 pro UK, +33 pro Francii), má číslo ETNS formát +388 3XX X XXX XXX, kde prefix '3XX' identifikuje konkrétní službu nebo poskytovatele služeb ve všech zúčastněných evropských zemích.

Z architektonického hlediska je ETNS integrován do mezinárodní hierarchie telekomunikačního číslování definované standardem [ITU-T](/mobilnisite/slovnik/itu-t/) E.164. Když uživatel vytočí číslo ETNS, je hovor směrován na základě směrového čísla země +388. Národní operátoři a mezinárodní přepravci musí toto číslo rozpoznat a směrovat hovor na příslušnou bránu nebo servisní platformu, na které je služba ETNS hostována. To často zahrnuje mezifiremní dohody a konfiguraci směrovacích tabulek v telefonních ústřednách (jako [MSC](/mobilnisite/slovnik/msc/), [MGW](/mobilnisite/slovnik/mgw/)) a Session Border Controllerech (SBC) pro VoIP sítě, aby byl provoz na +388 směrován na správný síťový uzel.

Jeho úlohou v síti je oddělit identitu služby od geografické polohy. Společnost nabízející celoevropskou zákaznickou linku může například inzerovat jediné číslo ETNS. Volající z jakékoli zúčastněné evropské země vytočí toto stejné číslo a hovor je směrován do servisního centra společnosti, které může být umístěno v jedné zemi nebo distribuováno napříč několika. Tím odpadá potřeba pro společnost získávat a spravovat samostatná národní čísla v každé zemi. Pro síť to vyžaduje podporu v analýze číslování a směrovací logice, aby bylo s +388 zacházeno jako s odlišným cílem, odděleným od národních a jiných mezinárodních hovorů. Servisní logika pro samotné číslo ETNS (např. distribuce hovorů, [IVR](/mobilnisite/slovnik/ivr/)) je implementována na platformě poskytovatele služeb, na kterou je hovor konečně doručen.

## K čemu slouží

ETNS bylo vytvořeno na podporu rozvoje jednotného evropského telekomunikačního trhu. Před jeho zavedením čelili poskytovatelé služeb, kteří chtěli nabízet panevropské služby, výrazné fragmentaci. Museli získat jiné telefonní číslo v každém národním číslovacím plánu, což vedlo k více kontaktním číslům, zvýšeným administrativním nákladům a rozmělnění značky. Pro koncové uživatele to znamenalo pamatovat si nebo hledat různá čísla v závislosti na jejich poloze, což bylo v rozporu s myšlenkou jednotné evropské služby.

Primární problém, který ETNS řeší, je poskytnutí číslovacího zdroje, který je v rámci Evropy geograficky neutrální. Umožňuje poskytovatelům služeb 'nákup na jednom místě' pro získání čísla, které funguje napříč více zeměmi. To je obzvláště cenné pro nadnárodní korporace, instituce EU, mezinárodní linky pomoci a nově vznikající poskytovatele digitálních služeb, jejichž zákaznická základna není omezena na národní hranice. Podporuje konkurenci a inovace ve službách snížením bariér pro nabízení telekomunikačních služeb v celoevropském měřítku.

Motivace vycházela z regulatorních cílů EU harmonizovat telekomunikace a podporovat služby přesahující hranice. ETNS je hmatatelným nástrojem pro dosažení této integrace na úrovni číslování. Řeší omezení národních číslovacích plánů, které jsou ze své podstaty vázány na národní suverenitu a regulaci, vytvořením nadnárodního prostoru spravovaného pro kolektivní prospěch evropského společenství. I když jeho přijetí bylo pomalejší, než se původně předpokládalo, kvůli komerčním a regulatorním složitostem, zůstává klíčovou součástí evropské strategie telekomunikační infrastruktury.

## Klíčové vlastnosti

- Používá vyhrazené směrovací číslo země +388 v rámci mezinárodního číslovacího plánu E.164
- Poskytuje jednotný, panevropský formát čísla pro služby
- Odděluje identitu služby od geografické polohy volajícího nebo servisní platformy
- Vyžaduje mezifiremní směrovací dohody mezi operátory
- Spravováno na evropské úrovni organizacemi CEPT/EC
- Použitelné pro hlasové služby, fax a další služby založené na telefonii

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs

---

📖 **Anglický originál a plná specifikace:** [ETNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/etns/)
