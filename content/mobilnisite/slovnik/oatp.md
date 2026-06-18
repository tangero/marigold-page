---
slug: "oatp"
url: "/mobilnisite/slovnik/oatp/"
type: "slovnik"
title: "OATP – On-board Automatic Train Protection"
date: 2026-01-01
abbr: "OATP"
fullName: "On-board Automatic Train Protection"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oatp/"
summary: "OATP je služba definovaná standardem 3GPP pro železniční komunikace, která poskytuje funkce kritického řízení a ochrany vlaku. Umožňuje bezpečný a efektivní provoz vlaků doručováním zásadních signaliz"
---

OATP je železniční služba definovaná standardem 3GPP, která zajišťuje kritické řízení a ochranu vlaku doručováním zásadních signalizačních dat přes mobilní sítě, čímž umožňuje bezpečný provoz a podporuje řízení vlaku založené na komunikaci (Communication-Based Train Control).

## Popis

On-board Automatic Train Protection (OATP, palubní automatická ochrana vlaku) je služba definovaná v rámci standardizačního rámce 3GPP pro železniční a kritické komunikace, konkrétně jako součást Future Railway Mobile Communication System ([FRMCS](/mobilnisite/slovnik/frmcs/)), který je nástupcem systému [GSM-R](/mobilnisite/slovnik/gsm-r/). OATP označuje palubní subsystém odpovědný za příjem, zpracování a reakci na příkazy automatické ochrany vlaku. Funguje tak, že vytváří spolehlivé komunikační spoje s nízkou latencí mezi vlakem a zabezpečovacími zařízeními podél trati prostřednictvím 3GPP mobilní sítě (např. 4G LTE nebo 5G). Mezi klíčové komponenty patří Palubní jednotka (OBU) s komunikačním modulem, Bezpečnostní počítač (Vital Computer) odpovědný za zpracování kritické z hlediska bezpečnosti a rozhraní k brzdovým a trakčním systémům vlaku. Služba OATP přijímá Povolení k jízdě (Movement Authorities) a další bezpečnostně kritická data z Radiového blokového centra ([RBC](/mobilnisite/slovnik/rbc/)) nebo zabezpečovacího zařízení. Kontinuálně monitoruje rychlost a polohu vlaku a porovnává je s přijatým profilem povolení k jízdě. Pokud hrozí, že vlak překročí své povolení nebo bezpečnou rychlost, systém OATP autonomně zahájí brzdění, aby vynutil bezpečnost. Jeho úlohou je poskytovat kontinuální, poruchově bezpečný nadřazený ochranný systém, který vylepšuje nebo nahrazuje tradiční pevné blokové kolejové obvody a návěstidla podél trati, což umožňuje vyšší kapacitu a flexibilnější provoz.

## K čemu slouží

OATP byla vytvořena za účelem modernizace železniční signalizace a řízení prostřednictvím využití standardizované buněčné technologie, což znamená posun za hranice zastaralého, na hlas zaměřeného systému [GSM-R](/mobilnisite/slovnik/gsm-r/). Řeší omezení tradičních systémů, které jsou často založeny na pevné infrastruktuře s vysokými náklady na instalaci a údržbu a omezenými datovými schopnostmi. Primární problém, který OATP řeší, je potřeba vysoce výkonného, na data orientovaného komunikačního systému pro bezpečnostně kritické řízení vlaku, aby podpořil pokročilé provozní koncepty, jako je signalizace s pohyblivým blokem a vyšší stupně automatizace. Její vznik motivovala potřeba globálního železničního průmyslu zvýšit kapacitu tratí, zlepšit provozní efektivitu a zvýšit bezpečnost, a to vše při přechodu na budoucím vývojům odolný, na IP založený komunikační standard ([FRMCS](/mobilnisite/slovnik/frmcs/)), který může využívat pokroky komerčních mobilních sítí. OATP umožňuje realizaci řízení vlaku založeného na komunikaci (CBTC) a ETCS úrovně 3 přes mobilní sítě.

## Klíčové vlastnosti

- Bezpečnostně kritická datová komunikace pro příkazy řízení vlaku (např. Povolení k jízdě)
- Kontinuální monitorování a vynucování limitů rychlosti a polohy vlaku v reálném čase
- Palubní bezpečnostní zpracování pro autonomní, poruchově bezpečné ochranné zásahy
- Podpora provozu přes 3GPP sítě 4G LTE a 5G NR jako součást FRMCS
- Rozhraní k brzdovým a trakčním systémům vlaku pro vynucování příkazů
- Navrženo pro vysokou dostupnost, integritu a komunikaci s velmi nízkou latencí

## Definující specifikace

- **TR 22.889** (Rel-17) — FRMCS Study; Stage 1
- **TR 22.989** (Rel-20) — FRMCS Analysis and Requirements

---

📖 **Anglický originál a plná specifikace:** [OATP na 3GPP Explorer](https://3gpp-explorer.com/glossary/oatp/)
