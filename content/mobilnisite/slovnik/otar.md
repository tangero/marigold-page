---
slug: "otar"
url: "/mobilnisite/slovnik/otar/"
type: "slovnik"
title: "OTAR – Over-The-Air Rekeying (P25)"
date: 2026-01-01
abbr: "OTAR"
fullName: "Over-The-Air Rekeying (P25)"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/otar/"
summary: "Bezpečnostní procedura pro vzdálenou aktualizaci šifrovacích klíčů v digitálních obousměrných radiových systémech Project 25 (P25). Umožňuje správcům systému měnit kryptografické klíče v celém parku r"
---

OTAR je bezpečnostní procedura pro vzdálenou aktualizaci šifrovacích klíčů v digitálních obousměrných radiových systémech Project 25 (P25) bez fyzického kontaktu.

## Popis

Over-The-Air Rekeying (OTAR) je standardizovaný bezpečnostní protokol definovaný ve specifikacích 3GPP pro systémy Project 25 ([P25](/mobilnisite/slovnik/p25/)) Fáze [II](/mobilnisite/slovnik/ii/). P25 je soubor standardů pro digitální rádiovou komunikaci hojně využívaný složkami veřejné bezpečnosti a federálními i státními agenturami v Severní Americe a jinde. OTAR konkrétně řídí proces vzdálené aktualizace šifrovacích klíčů uložených v účastnických jednotkách (radiostanicích) P25. Jeho primární funkcí je nahradit stávající klíče pro šifrování provozu ([TEK](/mobilnisite/slovnik/tek/)) nebo klíče pro šifrování klíčů ([KEK](/mobilnisite/slovnik/kek/)) novými, což je proces klíčový pro pravidelné obměny klíčů a nouzové odvolání klíčů.

Architektura OTAR se soustředí na zařízení pro správu klíčů (KMF) nebo řadič správy klíčů (KMC), což je centrální autorita odpovědná za generování, ukládání a distribuci klíčů. Infrastruktura P25, včetně základnových stanic (RFSS) a jádra sítě, slouží jako přenosové médium. KMF posílá zprávy pro změnu klíčů prostřednictvím řídicího kanálu nebo kanálů pro provoz P25. Tyto zprávy jsou zabezpečeně zabaleny; nový TEK je typicky zašifrován pomocí aktuálního, bezpečně uloženého KEK, který znají jak KMF, tak cílová účastnická jednotka. Protokol zahrnuje mechanismy pro adresování jednotlivých radiostanic (podle jejich jedinečného ID) nebo celých hovorových skupin, což umožňuje operace změny klíčů jak individuální, tak hromadné.

Proces OTAR zahrnuje několik kroků: zahájení KMF, zabezpečený přenos zašifrovaného nového klíče, příjem a dešifrování účastnickou jednotkou, uložení nového klíče do její zabezpečené paměti a konečně odeslání potvrzení zpět KMF. Tato smyčka potvrzení je zásadní pro provozní jistotu, neboť potvrzuje, že cílové zařízení úspěšně aktualizovalo své klíčové materiály. OTAR funguje ve spojení s infrastrukturou pro správu klíčů přes rádio (over-the-air) v P25, která může také zvládat počáteční načtení klíčů. Díky využití stávající radiové sítě OTAR odstraňuje potřebu logistických operací pro fyzické sebrání nebo kontakt s každou radiostanicí, čímž poskytuje škálovatelnou a rychlou reakční schopnost pro správu bezpečnosti v rozsáhlých nasazeních.

## K čemu slouží

OTAR byl vyvinut, aby překonal závažná logistická a bezpečnostní omezení vlastní manuální správě klíčů pro rozsáhlé, geograficky rozptýlené sítě [P25](/mobilnisite/slovnik/p25/). Před zavedením OTAR vyžadovala změna šifrovacích klíčů, aby technici fyzicky připojili k každé radiostanici zařízení pro načtení klíčů – proces, který u velké agentury mohl trvat týdny či měsíce, během nichž byla komunikace zranitelná, pokud byl klíč kompromitován. Tento statický model správy klíčů byl nekompatibilní s dynamickým prostředím hrozeb a provozními potřebami moderních organizací veřejné bezpečnosti.

Vytvoření OTAR bylo motivováno požadavkem na kryptografickou agilitu a provozní bezpečnost v misi kritických systémů pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)). Řeší problém udržení zabezpečené komunikace po dlouhá období tím, že umožňuje pravidelné, politikou řízené změny klíčů bez přerušení služby. OTAR je zásadní pro implementaci osvědčených bezpečnostních postupů, jako je omezení kryptografické životnosti klíče. Dále poskytuje nástroj pro okamžitou reakci při řízení incidentů; pokud je radiostanice ztracena nebo odcizena, její klíče lze vzdáleně vymazat nebo zneplatnit a nové klíče lze okamžitě distribuovat zbytku parku, čímž se zabrání neoprávněnému přístupu ke komunikačnímu systému. Tato schopnost je základním kamenem důvěryhodných, zabezpečených sítí P25 pro záchranáře.

## Klíčové vlastnosti

- Vzdálená aktualizace klíčů pro šifrování provozu (TEK) a klíčů pro šifrování klíčů (KEK) pro radiostanice P25
- Podporuje operace změny klíčů pro jednoho příjemce (individuální radiostanice) i pro skupinu příjemců (hovorová skupina)
- Pro doručení klíčů využívá stávající řídicí nebo provozní kanály P25, nevyžaduje samostatnou datovou síť
- Používá hierarchii klíčů, kde jsou nové klíče šifrovány pomocí dříve navázaných zabezpečených klíčů
- Zahrnuje povinné potvrzení od účastnické jednotky KMF pro potvrzení doručení
- Umožňuje jak plánované pravidelné změny klíčů, tak okamžité nouzové procedury pro odvolání klíčů

## Definující specifikace

- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [OTAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/otar/)
