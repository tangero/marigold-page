---
slug: "5g-vn"
url: "/mobilnisite/slovnik/5g-vn/"
type: "slovnik"
title: "5G-VN – 5G Virtual Network"
date: 2026-01-01
abbr: "5G-VN"
fullName: "5G Virtual Network"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-vn/"
summary: "5G-VN je služba 3GPP umožňující podnikům vytvářet izolované, přizpůsobitelné virtuální sítě na veřejné 5G infrastruktuře. Poskytuje vyhrazené připojení se specifickou kvalitou služeb (QoS), bezpečnost"
---

5G-VN je služba 3GPP umožňující podnikům vytvářet izolované, přizpůsobitelné virtuální sítě na veřejné 5G infrastruktuře s vyhrazeným připojením, kvalitou služeb (QoS), zabezpečením a funkcemi pro privátní případy užití.

## Popis

5G-VN (5G Virtual Network) je komplexní servisní rámec definovaný v 3GPP, který umožňuje poskytovatelům komunikačních služeb ([CSP](/mobilnisite/slovnik/csp/)) nabízet virtualizované, izolované síťové řezy podnikovým zákazníkům na sdílené veřejné 5G infrastruktuře. Architektura staví na schopnostech 5G systému (5GS), konkrétně na síťovém řezání (Network Slicing), ale rozšiřuje je o vyhrazená rozhraní pro správu, vylepšené izolační mechanismy a podnikové síťové funkce. 5G-VN je v podstatě logická instance sítě od konce do konce, která se podniku jeví jako vyhrazená privátní síť, přičemž je hostována na fyzické infrastruktuře CSP.

Technická implementace zahrnuje spolupráci více komponent. Funkce správy 5G-VN (5G-VNMF) slouží jako centrální řídicí entita, která orchestraci životního cyklu virtuální sítě včetně vytvoření, změny, monitorování a ukončení. Rozhraní s funkcí správy síťových řezů ([NSMF](/mobilnisite/slovnik/nsmf/)) a funkcí správy podsítí síťových řezů (NSSMF) slouží k vytvoření a správě podkladových síťových řezů, které tvoří 5G-VN. Brána 5G-VN (5G-VN-GW) zajišťuje připojení mezi 5G-VN a externími datovými sítěmi a často implementuje podnikové politiky, pravidla firewallu a funkce směrování provozu.

Z architektonického pohledu se 5G-VN skládá z několika logických komponent: Oblast 5G-VN (5G-VN Area) definuje geografické pokrytí, kde virtuální síť funguje; Členové 5G-VN (5G-VN Members) jsou autorizovaná uživatelská zařízení (UE), která mají přístup k virtuální síti; Skupiny 5G-VN (5G-VN Groups) umožňují logické seskupení členů pro aplikaci politik; a Služby 5G-VN (5G-VN Services) představují konkrétní aplikace nebo služby připojení nabízené v rámci virtuální sítě. 5G-VN podporuje jak provoz v síti (on-network), kdy veškerý provoz zůstává v síti CSP, tak provoz mimo síť (off-network), kdy může být provoz směrován do podnikových lokalit nebo cloudových prostředí.

Služba funguje prostřednictvím standardizovaných rozhraní: N5g-vn_e (mezi podnikem a CSP pro správu služby), N5g-vn_m (mezi funkcemi správy v síti CSP) a N5g-vn_gw (mezi 5G-VN-GW a dalšími síťovými funkcemi). Tato rozhraní umožňují automatizované zřizování, sledování v reálném čase a dynamické vynucování politik. 5G-VN využívá stávající 5G mechanismy, jako jsou QoS toky (QoS Flows), [PDU](/mobilnisite/slovnik/pdu/) relace (PDU Sessions) a informace pro podporu výběru síťového řezu ([NSSAI](/mobilnisite/slovnik/nssai/)), aby zajistila správné zpracování provozu a izolaci mezi různými virtuálními sítěmi sdílejícími stejnou fyzickou infrastrukturu.

V širším 5G ekosystému představuje 5G-VN klíčový vývoj od základních služeb připojení k nabídkám spravované sítě jako služby (Network-as-a-Service). Umožňuje CSP efektivněji monetizovat své investice do 5G a zároveň poskytuje podnikům výhody 5G (nízká latence, vysoká spolehlivost, masivní připojení) bez kapitálových výdajů a provozní složitosti spojené s budováním a údržbou vlastních privátních sítí. Rámec podporuje různé modely nasazení, od plně cloudových implementací po hybridní architektury kombinující veřejné 5G s podnikovými sítěmi v místě.

## K čemu slouží

5G-VN byl vytvořen, aby uspokojil rostoucí poptávku podniků po vyhrazených vysokovýkonných bezdrátových sítích, které mohou podporovat kritické aplikace, a zároveň využily úspor z rozsahu a pokrytí veřejných 5G sítí. Před 5G-VN měly podniky omezené možnosti: mohly si postavit vlastní privátní sítě (nákladné a složité), používat obecné veřejné mobilní služby (bez izolace a přizpůsobení) nebo implementovat [VPN](/mobilnisite/slovnik/vpn/) nadstavby (zvýšení latence a režie správy). Tyto přístupy buď vyžadovaly významné kapitálové investice, nebo neposkytovaly garantovaný výkon, zabezpečení a možnosti správy potřebné pro průmyslovou automatizaci, chytré továrny a další pokročilé případy užití.

Historický kontext ukazuje, že dřívější generace mobilních sítí (2G, 3G, 4G) se primárně zaměřovaly na spotřebitelské připojení s omezenou podporou specifických podnikových požadavků. Zatímco 4G zavedlo některé základní mechanismy sdílení sítě, postrádaly komplexní izolaci, rozhraní pro správu a přizpůsobení služeb potřebné pro skutečné virtuální privátní sítě. Nástup síťového řezání (Network Slicing) v 5G Release 15 poskytl základní technologii pro vytváření logických sítí, ale šlo primárně o schopnost orientovanou na operátora, bez standardizovaných rozhraní pro podnikovou správu a orchestraci služeb.

5G-VN konkrétně řeší tato omezení tím, že poskytuje kompletní rámec, který překlenuje propast mezi síťovými schopnostmi [CSP](/mobilnisite/slovnik/csp/) a provozními požadavky podniků. Řeší klíčové problémy včetně: jak nabízet izolované síťové instance se zaručenými výkonnostními charakteristikami, jak poskytnout podnikům možnosti samosprávy, jak zajistit bezpečný multi-tenancy na sdílené infrastruktuře a jak podporovat různé podnikové modely připojení (místní breakout, centralizovaný breakout, hybridní modely). Standardizací těchto aspektů v 3GPP umožňuje 5G-VN interoperabilitu mezi zařízeními různých dodavatelů a vytváří konzistentní servisní model, který může být nasazen globálně, čímž urychluje adopci 5G podniky pro iniciativy digitální transformace.

## Klíčové vlastnosti

- Komplexní síťová izolace od konce do konce využívající základ síťového řezání v 5G
- Podniková samospráva prostřednictvím standardizovaného rozhraní N5g-vn_e
- Podpora modelů směrování provozu v síti (on-network) i mimo síť (off-network)
- Flexibilní správa členství s vynucováním politik na základě skupin
- Integrace se stávajícím rámcem QoS v 5G pro zaručení výkonu
- Správa životního cyklu včetně vytvoření, změny, monitorování a ukončení

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [5G-VN na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-vn/)
