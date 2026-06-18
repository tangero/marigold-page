---
slug: "rstp"
url: "/mobilnisite/slovnik/rstp/"
type: "slovnik"
title: "RSTP – Rapid Spanning Tree Protocol"
date: 2026-01-01
abbr: "RSTP"
fullName: "Rapid Spanning Tree Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rstp/"
summary: "RSTP je síťový protokol, který zabraňuje vzniku smyček v ethernetových sítích vytvořením logické topologie bez smyček. Zajišťuje spolehlivost a stabilitu sítě rychlou konvergencí k nové topologii po v"
---

RSTP je síťový protokol, který zajišťuje spolehlivost sítě tím, že zabraňuje vzniku smyček v ethernetových sítích a rychle konverguje k nové topologii po výpadku spoje.

## Popis

Rapid Spanning Tree Protocol (RSTP) je vývojovým nástupcem původního protokolu Spanning Tree Protocol ([STP](/mobilnisite/slovnik/stp/)), standardizovaným jako [IEEE](/mobilnisite/slovnik/ieee/) 802.1w a přijatým ve specifikacích 3GPP pro správu síťových topologií. Funguje na vrstvě datového spoje (vrstva 2) a zabraňuje broadcastovým bouřím a vícenásobnému přenosu rámců způsobeným smyčkami v ethernetových sítích s redundantními cestami. RSTP dynamicky vytváří logickou topologii bez smyček tím, že určí jeden přepínač jako kořenový most a pro všechny ostatní přepínače vypočítá nejkratší cestu k tomuto kořeni, přičemž redundantní porty zablokuje, aby smyčky odstranil.

RSTP přináší oproti STP významná vylepšení v době konvergence. Zatímco STP mohlo rekonfiguraci po změně topologie trvat 30 až 50 sekund, RSTP tuto dobu typicky zkracuje na 1 až 2 sekundy. Toho je dosaženo mechanismy, jako je handshake typu návrh/souhlas pro rychlý přechod portu do stavu přeposílání, a odstraněním stavů naslouchání a učení pro určené porty. RSTP definuje role portů (kořenový, určený, náhradní, záložní a zakázaný) a stavy (zahazování, učení, přeposílání) pro efektivní správu toků provozu.

Mezi klíčové komponenty patří Bridge Protocol Data Units (BPDU), což jsou zprávy vyměňované mezi přepínači za účelem sdílení informací o topologii. RSTP používá BPDU jako keepalive mechanismy; pokud přepínač přestane přijímat BPDU od souseda, může rychle detekovat výpadek spoje. Protokol také podporuje okrajové porty (připojené ke koncovým zařízením), které přecházejí přímo do stavu přeposílání, a definice typu spoje (bod-bod nebo sdílený) pro optimalizaci konvergence. V sítích 3GPP je RSTP odkazováno pro zajištění odolné přenosové sítě backhaul a transportu, zejména ve scénářích zahrnujících konvergenci pevných a mobilních sítí a síťové segmenty, kde je spolehlivá konektivita vrstvy 2 klíčová.

## K čemu slouží

RSTP bylo vytvořeno, aby řešilo omezení původního protokolu Spanning Tree Protocol ([STP](/mobilnisite/slovnik/stp/)), který trpěl pomalou dobou konvergence, což mohlo vést k významným výpadkům sítě během změn topologie. V telekomunikacích je spolehlivost sítě prvořadá a 30-50 sekundová rekonvergence STP byla nedostatečná pro služby v reálném čase, jako je hlas a video. RSTP poskytuje rychlý převzetí služeb při selhání, což zajišťuje minimální narušení provozu v sítích s redundantními spoji.

Motivace pro zahrnutí RSTP do standardů 3GPP, zejména od vydání Release 16, vychází z potřeby robustních transportních sítí pro 5G a další generace. Jak se sítě vyvíjejí, aby podporovaly ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a síťové segmenty, musí být podkladový transport vysoce dostupný a rychle adaptabilní. Rychlá konvergence RSTP odpovídá přísným požadavkům 5G na spolehlivost a kontinuitu služeb.

Historicky bylo STP dostačující pro základní prostředí [LAN](/mobilnisite/slovnik/lan/), ale moderní sítě vyžadují rychlejší obnovu. RSTP tento problém řeší zavedením nových rolí a stavů portů a použitím BPDU jako průběžných kontrol stavu. Tento protokol je nezbytný pro prevenci smyček, které mohou způsobit broadcastové bouře, jež degradují výkon sítě a mohou vést k jejímu úplnému selhání, čímž zajišťuje stabilní provoz ve složitých architekturách 3GPP.

## Klíčové vlastnosti

- Rychlá konvergence během 1-2 sekund po změně topologie
- Definuje role portů: kořenový, určený, náhradní, záložní
- Používá handshake typu návrh/souhlas pro rychlý přechod portu
- Okrajové porty přecházejí přímo do stavu přeposílání
- Využívá BPDU jako keepalive mechanismy pro detekci výpadku spoje
- Podporuje typy spojů bod-bod a sdílené pro optimalizaci

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements

---

📖 **Anglický originál a plná specifikace:** [RSTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rstp/)
