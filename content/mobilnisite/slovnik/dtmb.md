---
slug: "dtmb"
url: "/mobilnisite/slovnik/dtmb/"
type: "slovnik"
title: "DTMB – Digital Terrestrial Multimedia Broadcast"
date: 2025-01-01
abbr: "DTMB"
fullName: "Digital Terrestrial Multimedia Broadcast"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dtmb/"
summary: "Vysílací služba ve standardech 3GPP pro distribuci multimediálního obsahu přes pozemní rádiové sítě. Umožňuje efektivní streamování videa a audia vysoké kvality do mobilních i pevných zařízení s využi"
---

DTMB je vysílací služba 3GPP pro distribuci multimediálního obsahu přes pozemní rádiové sítě, která umožňuje efektivní streamování videa a audia do mobilních i pevných zařízení s využitím buněčné infrastruktury.

## Popis

Digital Terrestrial Multimedia Broadcast (DTMB) je vysílací služba standardizovaná v rámci 3GPP, konkrétně navržená pro distribuci multimediálního obsahu, jako je lineární televize, rozhlas a souborová média, přes pozemní rádiové sítě. Funguje jako služba typu point-to-multipoint a využívá infrastrukturu rádiového přístupu a jádra sítě (core network) buněčných sítí k efektivní distribuci obsahu velkému počtu uživatelů současně. Služba je definována tak, aby pracovala spolu s existujícími buněčnými technologiemi, což umožňuje operátorům využívat své spektrum a síťové prostředky jak pro unicastové, tak pro vysílací služby, a tím optimalizovat využití zdrojů.

Z architektonického hlediska se DTMB integruje se sítí Evolved Packet Core (EPC) nebo 5G Core (5GC) a využívá entity jako Broadcast/Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) pro poskytování služeb a distribuci obsahu. Rádiová přístupová síť, typicky LTE nebo 5G NR, je rozšířena o vysílací specifické přenosové režimy, jako je provoz v Single Frequency Network (SFN), aby bylo zajištěno konzistentní pokrytí a kvalita příjmu. Mezi klíčové komponenty patří BM-SC, který spravuje oznámení služeb, zabezpečení a synchronizaci obsahu, a eNodeB/gNB, který vysílá obsah přes vyhrazené vysílací přenosové kanály (broadcast bearers) nebo fyzické kanály.

Technický provoz zahrnuje přijímání multimediálního obsahu BM-SC od poskytovatelů obsahu, jeho zapouzdření do IP paketů a předání do rádiové přístupové sítě přes jádro sítě. RAN následně naplánuje a vysílá obsah pomocí vysílacích specifických technik fyzické vrstvy, jako je Physical Multicast Channel (PMCH) v LTE nebo podobné mechanismy v NR. DTMB podporuje různé kodeky a adaptivní streamování s proměnným datovým tokem, aby vyhovělo různým možnostem zařízení a síťovým podmínkám. Jeho úlohou v síti je poskytovat škálovatelnou a efektivní alternativu k unicastovému streamování pro populární živé události nebo plánované vysílání, což snižuje zahlcení sítě a zlepšuje uživatelský zážitek.

Integrace DTMB do standardů 3GPP zajišťuje interoperabilitu s existujícími buněčnými zařízeními a sítěmi a umožňuje funkce jako objevování služeb, distribuce elektronického průvodce službami ([ESG](/mobilnisite/slovnik/esg/)) a podpora systémů podmíněného přístupu pro prémiový obsah. Služba je navržena jako flexibilní, podporující jak samostatné vysílací sítě, tak konvergované sítě kombinující vysílací a širokopásmové služby. To činí z DTMB klíčový prvek pro služby vysílání nové generace, včetně mobilní televize a systémů veřejného varování, v rámci buněčného ekosystému.

## K čemu slouží

DTMB bylo vytvořeno, aby reagovalo na rostoucí poptávku po efektivních vysílacích službách pro multimédia přes buněčné sítě, zejména pro živé události, televizi a výstražné systémy. Před jeho standardizací se buněčné sítě primárně spoléhaly na unicastové streamování videoobsahu, které se stává neefektivním a způsobuje zahlcení, když mnoho uživatelů současně žádá stejný obsah. Tento přístup spotřebovává značnou šířku pásma a může zhoršovat výkon sítě. DTMB tento problém řeší zavedením vysílacího režimu, který obsah přenáší jednou přes sdílený kanál a obslouží tak všechny zainteresované uživatele v oblasti pokrytí bez duplikace datových proudů.

Historický kontext zahrnuje vývoj mobilních vysílacích technologií, jako je Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) v dřívějších vydáních 3GPP, které položily základy pro efektivní distribuci obsahu. S nástupem videa vysokého rozlišení a potřebou lepší efektivity spektra však bylo DTMB zavedeno ve vydání 18, aby vylepšilo a modernizovalo vysílací schopnosti v rámci 5G. Řeší omezení předchozích vysílacích řešení tím, že se plynuleji integruje s 5G NR, podporuje vyšší datové toky a umožňuje dynamické přidělování zdrojů mezi vysílací a unicastové služby.

Motivace pro DTMB zahrnují také umožnění nových případů užití, jako je mobilní televize, streamování rozsáhlých událostí a spolehlivé systémy veřejného varování, které vyžadují robustní širokoplošné pokrytí. Využitím pozemního vysílání v rámci buněčného spektra poskytuje DTMB operátorům nákladově efektivní řešení pro nabídku vysílacích služeb bez nutnosti samostatné infrastruktury, čímž pohání inovace v distribuci médií a zlepšuje zapojení uživatelů v éře 5G.

## Klíčové vlastnosti

- Efektivní distribuce obsahu typu point-to-multipoint přes pozemní rádiové sítě
- Integrace s rádiovými přístupovými sítěmi 5G NR a LTE
- Podpora provozu v Single Frequency Network (SFN) pro zlepšené pokrytí
- Dynamické sdílení zdrojů mezi vysílacími a unicastovými službami
- Schopnosti oznamování služeb a elektronického průvodce službami (ESG)
- Mechanismy podmíněného přístupu a ochrany obsahu

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TR 36.792** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [DTMB na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtmb/)
