---
slug: "pim-dm"
url: "/mobilnisite/slovnik/pim-dm/"
type: "slovnik"
title: "PIM-DM – Protocol-Independent Multicast - Dense Mode"
date: 2025-01-01
abbr: "PIM-DM"
fullName: "Protocol-Independent Multicast - Dense Mode"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pim-dm/"
summary: "PIM Dense Mode (PIM-DM) je multicastový směrovací protokol typu 'zaplav a odřízni', kde jsou data zpočátku zaplavena do všech větví sítě a následně odříznuta tam, kde nejsou příjemci. Je efektivní v p"
---

PIM-DM je multicastový směrovací protokol, který zpočátku zaplaví daty všechny větve sítě a následně odřízne větve, na kterých nejsou příjemci, což jej činí efektivním v prostředích s hustě rozloženými členy skupiny.

## Popis

Protocol-Independent Multicast Dense Mode (PIM-DM) je jeden ze dvou hlavních provozních režimů sady protokolů [PIM](/mobilnisite/slovnik/pim/), druhým je PIM Sparse Mode ([PIM-SM](/mobilnisite/slovnik/pim-sm/)). PIM-DM pracuje za předpokladu, že členové multicastových skupin jsou hustě rozloženi po celé síti, což znamená, že většina podsítí bude mít pro jakoukoli danou multicastovou skupinu alespoň jednoho příjemce. Jeho základní fungování sleduje model 'zaplav a odřízni' neboli 'push'. Když multicastový zdroj začne vysílat provoz, PIM-DM tento provoz zpočátku zaplaví všemi rozhraními s podporou PIM (kromě toho, ze kterého dorazil, na základě kontroly RPF). Tím vytvoří strom nejkratších cest se zdrojem v kořeni.

Mechanismus protokolu zahrnuje periodické zaplavování následované explicitním odřezáváním. Když router přijme multicastová data na rozhraní a nemá žádné příjemce po proudu (což se zjistí absencí hlášení o členství [IGMP](/mobilnisite/slovnik/igmp/)/[MLD](/mobilnisite/slovnik/mld/) nebo downstream PIM joinů), pošle směrem ke zdroji (upstream) zprávu PIM Prune. Tím se daná větev odřízne od distribučního stromu. Tyto odříznuté stavy mají omezenou životnost; po jejím vypršení se zaplavování obnoví a proces odřezávání se může opakovat, pokud příjemci stále chybí. PIM-DM také používá mechanismus Graft pro rychlé opětovné připojení k dříve odříznutému stromu, když se objeví nový příjemce, přičemž vyšle zprávu Graft přímo upstream routeru, aby znovu aktivoval větev bez čekání na další cyklus zaplavování.

Mezi klíčové architektonické prvky patří použití podkladové unicastové směrovací tabulky pro kontroly RPF a udržování stavů specifických pro zdroj (S,G) v každém routeru na potenciální cestě. Na rozdíl od PIM-SM PIM-DM nepoužívá Rendezvous Point ([RP](/mobilnisite/slovnik/rp/)). Okamžitě buduje stromy ke zdroji. Stav je obnovován periodickým zaplavováním dat a souvisejících řídicích zpráv.

Ve specifikacích 3GPP je PIM-DM explicitně zmíněn v TS 29.561 (expozice jádra 5G) jako podporovaný multicastový směrovací protokol. Jeho role v mobilních sítích je typicky pro specifické scénáře nasazení v IP transportní síti poskytovatele služeb nebo pro určité typy multicastových služeb, kde platí předpoklad hustého režimu, jako je například doručování společného kanálu všem uzlům v omezeném segmentu sítě. Poskytuje jednoduchou metodu distribuce multicastu s nízkou latencí bez nutnosti předkonfigurace RP.

## K čemu slouží

PIM-DM byl navržen pro síťová prostředí, kde jsou členové multicastových skupin hustě rozmístěni, což znamená, že příjemci jsou přítomni na vysokém procentu podsítí. Jeho účelem je poskytnout jednoduchý, automatický mechanismus pro budování multicastových distribučních stromů založených na zdroji s minimální konfigurací. Řeší potřebu efektivní komunikace typu many-to-many v omezené síti s hustým výskytem příjemců, jako je podniková [LAN](/mobilnisite/slovnik/lan/) nebo konkrétní datacentrická struktura.

Model 'zaplav a odřízni' řeší problém počáteční latence připojení. V [PIM-SM](/mobilnisite/slovnik/pim-sm/) musí příjemce čekat, než se join propaguje k [RP](/mobilnisite/slovnik/rp/), než začne přijímat data. PIM-DM může díky okamžitému zaplavení dat doručit první pakety s minimálním zpožděním, což může být pro některé aplikace výhodné. To však probíhá za cenu počátečního plýtvání šířkou pásma na větvích bez příjemců, které je následně napraveno odřezáváním. PIM-DM je tedy motivován scénáři, kde je šířka pásma hojná v poměru k počtu podsítí a nízká počáteční latence je ceněna výše než optimální efektivita šířky pásma od samého začátku.

V kontextu přijetí 3GPP poskytuje PIM-DM alternativní možnost multicastového směrovacího protokolu pro transportní sítě, které podporují funkce mobilního jádra. Nabízí síťovým operátorům flexibilitu. Například v těsně propojeném datovém centru hostujícím funkce jádra 5G by mohl být PIM-DM použit pro efektivní interní multicastovou distribuci provozních dat. Jeho specifikace v dokumentech 3GPP zajišťuje, že funkce pro vystavení sítě (NEF) a další prvky mohou být navrženy tak, aby spolupracovaly se sítěmi používajícími PIM-DM, a podporují tak širší škálu možností nasazení od operátorů.

## Klíčové vlastnosti

- Pracuje na modelu 'zaplav a odřízni' (push) pro budování stromů.
- Předpokládá husté rozložení příjemců a zpočátku zaplavuje data do všech větví.
- Používá zprávy Prune k odříznutí větví bez aktivních příjemců.
- Využívá zprávy Graft pro rychlé opětovné připojení odříznutých větví při objevení příjemců.
- Buduje stromy nejkratších cest specifické pro zdroj (S,G) bez nutnosti Rendezvous Point (RP).
- Spoléhá na periodické zaplavování pro obnovu stavu a znovuobjevení nových příjemců.

## Související pojmy

- [PIM – Protocol-Independent Multicast](/mobilnisite/slovnik/pim/)
- [PIM-SM – Protocol Independent Multicast – Sparse Mode](/mobilnisite/slovnik/pim-sm/)
- [IGMP – Internet Group Management Protocol](/mobilnisite/slovnik/igmp/)
- [MLD – Multicast Listener Discovery](/mobilnisite/slovnik/mld/)

## Definující specifikace

- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [PIM-DM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pim-dm/)
