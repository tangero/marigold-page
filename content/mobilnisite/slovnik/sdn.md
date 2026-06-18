---
slug: "sdn"
url: "/mobilnisite/slovnik/sdn/"
type: "slovnik"
title: "SDN – Software Defined Networking"
date: 2025-01-01
abbr: "SDN"
fullName: "Software Defined Networking"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sdn/"
summary: "Paradigma síťové architektury, které odděluje řídicí rovinu sítě (která rozhoduje o směrování provozu) od přenosové roviny (která provoz přeposílá). Tím se centralizuje inteligence a umožní programova"
---

SDN je síťová architektura, která odděluje řídicí rovinu od přenosové roviny za účelem centralizace inteligence a umožnění programovatelné, automatizované správy sítě, což je klíčové pro řezání sítí (network slicing) v 5G.

## Popis

Software Defined Networking (SDN) je architektonický rámec, který zásadně odděluje řídicí logiku sítě (řídicí rovina) od podkladových směrovačů a přepínačů, které přeposílají provoz (přenosová rovina). V tradiční síti každé zařízení běží na proprietárním softwaru, který integruje jak řídicí, tak přeposílací funkce. SDN extrahuje řídicí rovinu z těchto distribuovaných zařízení a konsoliduje ji do logicky centralizovaného softwarového řadiče. Tento řadič udržuje globální pohled na síť a diktuje chování přenosových zařízení prostřednictvím standardizovaného jižního rozhraní, nejčastěji protokolu OpenFlow.

V ekosystému 3GPP se principy SDN aplikují k vytvoření flexibilnějších, programovatelných a efektivnějších mobilních sítí. Architektura typicky sestává ze tří vrstev: Aplikační vrstva (kde sídlí síťové aplikace pro orchestraci, řezání sítí nebo politiky), Řídicí vrstva (SDN řadič) a Infrastrukturní vrstva (přenosové síťové prvky). SDN řadič komunikuje severním směrem s aplikacemi prostřednictvím RESTful [API](/mobilnisite/slovnik/api/), což umožňuje aplikacím programovat síť na základě vysokorychlostních politik. Jižním směrem komunikuje s přenosovými prvky (např. přepínači, směrovači nebo v mobilním kontextu uzly přenosové sítě a potenciálně funkcemi RAN/Jádra sítě), aby instaloval pravidla pro toky. Tato pravidla specifikují, jak se má nakládat s provozem odpovídajícím určitým kritériím (jako zdrojová IP, cílová IP, protokol) – přeposlat, zahodit nebo upravit.

Pro 5G je SDN klíčovou technologií, která pracuje v tandemu s virtualizací síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)). Zatímco NFV virtualizuje síťové funkce (jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/)), SDN poskytuje programovatelné propojení mezi těmito virtualizovanými funkcemi. Tato kombinace umožňuje klíčové schopnosti 5G, jako je řezání sítí, kde jsou na sdílené fyzické infrastruktuře vytvářeny vícečetné logické, koncové sítě s různými charakteristikami. SDN řadič může dynamicky vytvářet a upravovat virtuální spoje a šířku pásma pro každý řez. Dále SDN umožňuje řetězení služeb – směrování uživatelského provozu přes specifickou sekvenci [VNF](/mobilnisite/slovnik/vnf/) (např. firewall, optimalizátor). Tato programovatelnost umožňuje operátorům automatizovat poskytování síťových služeb, optimalizovat toky provozu v reálném čase a rychle zavádět nové služby.

## K čemu slouží

Účelem zavádění SDN v mobilních sítích je překonání omezení tradičních, hardware-centrických a vertikálně integrovaných síťových architektur. Starší sítě jsou často rigidní, složité na správu a pomalé v přizpůsobování se novým požadavkům služeb kvůli ruční konfiguraci distribuovaných zařízení. SDN řeší tyto problémy zavedením centralizace, abstrakce a programovatelnosti. Řeší problém provozní složitosti a vysokých nákladů spojených s individuální správou tisíců síťových zařízení.

Historicky evoluce mobilních sítí (od 2G po 4G) vedla ke zvýšené složitosti přenosových a jádrových sítí. Nástup 5G s jeho různorodými požadavky na rozšířenou mobilní širokopásmovou komunikaci (eMBB), ultra-spolehlivou nízkolatenční komunikaci ([URLLC](/mobilnisite/slovnik/urllc/)) a masivní IoT (mIoT) vyžadoval nebývalou síťovou agilitu. SDN bylo identifikováno jako klíčový umožňovatel pro splnění těchto požadavků. Umožňuje operátorům dynamicky alokovat zdroje, optimalizovat cesty provozu pro nízkou latenci a vytvářet izolované virtuální sítě (řezy) přizpůsobené konkrétním službám – vše prostřednictvím softwaru, bez zásahu do fyzického hardwaru.

Navíc SDN usnadňuje inovace a snižuje závislost na jediném dodavateli. Standardizací rozhraní mezi řídicí a přenosovou rovinou mohou operátoři kombinovat hardware od různých dodavatelů a psát své vlastní řídicí aplikace. Tato otevřenost, kombinovaná s [NFV](/mobilnisite/slovnik/nfv/), transformuje síť na flexibilní platformu, kde lze nové služby rychle nasazovat a elasticky škálovat nahoru nebo dolů na základě poptávky. Primárním účelem SDN je tedy učinit síť programovatelnou entitou, kterou lze snadno přizpůsobit pro podporu obchodních a technických cílů 5G a dalších generací.

## Klíčové vlastnosti

- Oddělení řídicí roviny (softwarový řadič) od přenosové roviny (přenosové prvky)
- Logicky centralizovaná síťová inteligence a globální pohled na topologii
- Programovatelnost sítě prostřednictvím otevřených API (severní a jižní rozhraní)
- Dynamické řízení a směrování provozu na základě toků
- Základ pro automatizované poskytování síťových služeb a orchestraci
- Klíčový umožňovatel pro koncové řezání sítí (network slicing) a řetězení služeb

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TR 33.848** (Rel-18) — Technical Report on Virtualisation Security

---

📖 **Anglický originál a plná specifikace:** [SDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdn/)
