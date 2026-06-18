---
slug: "ot"
url: "/mobilnisite/slovnik/ot/"
type: "slovnik"
title: "OT – Operational Technology"
date: 2025-01-01
abbr: "OT"
fullName: "Operational Technology"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ot/"
summary: "Hardwarové a softwarové systémy, které monitorují a řídí fyzické průmyslové procesy a zařízení. V kontextu 3GPP se tento termín vztahuje k integraci těchto průmyslových systémů se sítěmi 5G za účelem"
---

OT (Operační technologie) je hardwarový a softwarový systém, který monitoruje a řídí fyzické průmyslové procesy a který je integrován s mobilními sítěmi, jako je 5G, aby umožnil automatizaci továren a chytré sítě.

## Popis

V kontextu 3GPP se termín Operační technologie (OT) vztahuje k oblasti hardwaru a softwaru určeného k detekci, monitorování a řízení fyzických zařízení, procesů a událostí v průmyslovém prostředí. Na rozdíl od tradiční informační technologie ([IT](/mobilnisite/slovnik/it/)), která se zabývá výpočty zaměřenými na data, jsou systémy OT přímo propojeny s fyzickým světem prostřednictvím senzorů, aktuátorů, programovatelných logických řídicích systémů ([PLC](/mobilnisite/slovnik/plc/)) a průmyslových řídicích systémů ([ICS](/mobilnisite/slovnik/ics/)). Práce 3GPP v oblasti OT se zaměřuje na to, jak mohou sítě 5G a novější spolehlivě a bezpečně propojovat tyto OT prvky, aby umožnily transformační průmyslové aplikace.

Integrace OT se sítěmi 5G zahrnuje několik architektonických aspektů. Zařízení OT se stávají uživatelskými zařízeními (UE) připojenými k systému 5G. Síť 5G musí poskytovat konektivní služby, které splňují přísné požadavky OT, jako je komunikace s ultra-spolehlivým nízkým zpožděním ([URLLC](/mobilnisite/slovnik/urllc/)), integrace s časově citlivými sítěmi ([TSN](/mobilnisite/slovnik/tsn/)) a přesné určování polohy. Toho je často dosaženo prostřednictvím neveřejných sítí ([NPN](/mobilnisite/slovnik/npn/)) nebo síťového řezání, kdy jsou pro průmyslový areál vytvářeny vyhrazené logické sítě se specifickými vlastnostmi. Mezi klíčová architektonická vylepšení 3GPP patří podpora průmyslových protokolů založených na Ethernetu přes 5G, mechanismy pro synchronizaci hodin (např. prostřednictvím systému 5G jako mostu TSN) a vylepšené rámce QoS pro zaručení deterministického výkonu.

Princip fungování spočívá v tom, že systém 5G slouží jako komunikační páteř pro OT. Data ze senzorů (např. teploty, tlaku, vizuálních systémů) jsou přenášena prostřednictvím 5G do řídicích systémů. Řídicí příkazy jsou následně odesílány zpět přes 5G k aktuátorům (např. robotickým ramenům, ventilům) s minimálním a předvídatelným zpožděním. Jádrová síť 5G, zejména funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), může být nasazena lokálně v továrně (edge computing) za účelem lokalizace provozu a snížení latence. Správa a orchestrace těchto integrací OT-5G jsou zajišťovány vylepšenými funkcemi [OSS](/mobilnisite/slovnik/oss/)/BSS a správy síťových řezů, což zajišťuje bezpečnost, izolaci a správu životního cyklu průmyslových aplikací.

## K čemu slouží

Integrace OT do standardů 3GPP byla motivována revolucí Průmysl 4.0, která vyžaduje bezdrátovou konektivitu pro flexibilní, rekonfigurovatelnou a chytrou výrobu. Tradiční sítě OT spoléhají na drátové sběrnice (např. PROFIBUS, Modbus) nebo průmyslový Ethernet, které jsou spolehlivé, ale neflexibilní, nákladné na rekonfiguraci a omezují mobilitu. Omezení předchozích bezdrátových technologií (Wi-Fi, 4G) z hlediska spolehlivosti, latence, determinismu a bezpečnosti je činila nevhodnými pro OT aplikace s kritickým nasazením.

3GPP, počínaje vydáním 15, začalo explicitně řešit požadavky OT, aby pozici 5G definovalo jako jednotnou konektivní platformu pro všechna průmyslová odvětví. Cílem je vyřešit problém 'náhrady kabelů' bezdrátovým řešením, které nekompromisně splňuje kritické výkonnostní atributy vyžadované systémy OT. To umožňuje nové schopnosti, jako jsou mobilní roboti, rozšířená realita pro údržbu a bezdrátové řídicí smyčky, které byly dříve neproveditelné. Vytváření pracovních položek zaměřených na OT má za cíl překlenout propast mezi telekomunikačním a průmyslovým světem definováním toho, jak může 5G splnit technické a provozní potřeby vertikálních sektorů, jako je výroba, energetika a doprava.

## Klíčové vlastnosti

- Podpora komunikace s ultra-spolehlivým nízkým zpožděním (URLLC) pro řídicí smyčky
- Integrace s časově citlivými sítěmi (TSN) pro deterministický provoz Ethernetu
- Podpora neveřejných sítí (NPN) pro privátní, lokální nasazení
- Vylepšené služby určování polohy pro sledování aktiv a geofencing
- Podpora Ethernetu/průmyslových protokolů přes uživatelskou rovinu 5G
- Síťové řezání pro vyhrazené, izolované logické sítě na OT aplikaci

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [TSN – AF Time Sensitive Networking Application Function](/mobilnisite/slovnik/tsn/)

## Definující specifikace

- **TR 22.804** (Rel-16) — 5G Automation in Vertical Domains Study
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 28.907** (Rel-19) — Enhanced Management of Non-Public Networks

---

📖 **Anglický originál a plná specifikace:** [OT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ot/)
