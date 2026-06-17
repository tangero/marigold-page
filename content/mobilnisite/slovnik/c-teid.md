---
slug: "c-teid"
url: "/mobilnisite/slovnik/c-teid/"
type: "slovnik"
title: "C-TEID – Common Tunnel Endpoint Identifier"
date: 2025-01-01
abbr: "C-TEID"
fullName: "Common Tunnel Endpoint Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/c-teid/"
summary: "Sdílený identifikátor tunelu používaný v sítích 3GPP pro multiplexování více datových toků přes jediný GTP tunel. Umožňuje efektivní využití zdrojů tím, že umožňuje různým přenosovým kanálům (bearerům"
---

C-TEID je sdílený identifikátor tunelu používaný v sítích 3GPP pro multiplexování více datových toků přes jediný GTP tunel, což umožňuje efektivní využití zdrojů a snížení signalizační zátěže.

## Popis

Common Tunnel Endpoint Identifier (C-TEID) je klíčový parametr v architektuře protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), který umožňuje více datovým tokům sdílet jediný GTP tunel mezi síťovými uzly. V tradičních implementacích GTP vyžaduje každý přenosový kanál (bearer) nebo služební tok vlastní vyhrazený tunel s jedinečnými TEID na obou koncových bodech, což vede k významné signalizační zátěži a spotřebě zdrojů. Mechanismus C-TEID zavádí sdílený identifikátor, který umožňuje multiplexovat více přenosových kanálů nebo datových toků služeb přes jediný GTP tunel, přičemž stále zachovává logické oddělení mezi různými toky pomocí dodatečných identifikátorů nebo kontextových informací.

Architektonicky C-TEID funguje ve vrstvě protokolu [GTP-U](/mobilnisite/slovnik/gtp-u/) (User Plane), primárně mezi Serving Gateway (SGW) a Packet Data Network Gateway (PGW) v Evolved Packet Core (EPC) a mezi User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a dalšími funkcemi 5G Core v systémech 5G. Při vytváření GTP tunelu si mohou síťové uzly vyjednat použití C-TEID namísto přidělování individuálních TEID pro každý přenosový kanál. Toto vyjednávání probíhá během procedur zřizování GTP tunelu, kdy iniciující uzel indikuje svou schopnost podporovat C-TEID a navrhuje jeho použití pro konkrétní datové toky.

Technická implementace zahrnuje rozšíření standardní hlavičky GTP o informaci C-TEID společně s tradičními poli TEID nebo místo nich. Při použití C-TEID jsou do paketů GTP zahrnuty dodatečné kontextové identifikátory nebo identifikátory toků, aby bylo možné rozlišit mezi různými multiplexovanými toky. Tyto doplňkové identifikátory spolupracují s C-TEID, aby jednoznačně identifikovaly každý konkrétní přenosový kanál nebo datový tok služby uvnitř sdíleného tunelu. Přijímací uzel používá jak C-TEID, tak dodatečný identifikátor toku, aby správně směroval pakety do příslušného kontextu přenosového kanálu nebo instance služby.

Klíčové součásti mechanismu C-TEID zahrnují samotnou hodnotu C-TEID (typicky 32bitový identifikátor), parametry identifikace toku, které rozlišují multiplexovaný provoz uvnitř tunelu, a přidružené zásady QoS a zpracování provozu platné pro sdílený tunel. Síť udržuje mapovací tabulky, které asociují C-TEID s více kontexty přenosových kanálů nebo služebních toků, včetně jejich příslušných profilů QoS, charakteristik účtování a směrovacích informací. Toto mapování umožňuje efektivní zpracování paketů při zachování potřebného oddělení mezi různými službami a účastníky.

Během provozu, když paket dorazí ke koncovému bodu GTP tunelu používajícímu C-TEID, přijímací uzel nejprve identifikuje tunel pomocí C-TEID a poté prozkoumá dodatečný identifikátor toku, aby určil konkrétní kontext přenosového kanálu nebo služby. Tato dvouúrovňová identifikace umožňuje efektivní zpracování paketů při zachování logického oddělení vyžadovaného pro různé služby. Mechanismus významně snižuje počet GTP tunelů, které je třeba zřizovat a spravovat, zejména ve scénářích s více souběžnými službami na uživatele nebo ve scénářích nasazení s vysokou hustotou.

## K čemu slouží

C-TEID byl zaveden, aby řešil problémy škálovatelnosti tradičních implementací [GTP](/mobilnisite/slovnik/gtp/), kde každý přenosový kanál vyžadoval vyhrazený tunel s jedinečnými TEID na obou koncových bodech. V časných vydáních 3GPP vytvářelo vzájemně jednoznačné mapování mezi přenosovými kanály a GTP tunely významnou signalizační zátěž během procedur zřizování, modifikace a rušení přenosových kanálů. To se stalo obzvláště problematickým s vývojem směrem k trvale připojeným zařízením a rozmnožením souběžných služeb na uživatelském zařízení, kde může jediné UE udržovat více přenosových kanálů pro různé aplikace současně.

Historicky, před zavedením C-TEID, čelili síťoví operátoři výzvám v podobě složitosti správy tunelů a spotřeby zdrojů ve scénářích s vysokým provozem. Každé nové zřízení přenosového kanálu vyžadovalo kompletní procedury nastavení GTP tunelu, včetně alokace TEID, rezervace zdrojů tunelu a správy stavu na obou koncových bodech. Tento přístup se dobře neškáloval s rostoucím počtem připojených zařízení a trendem směrem k virtualizaci síťových funkcí, kde se efektivní využití zdrojů stalo klíčovým pro nákladově efektivní nasazení.

Vytvoření C-TEID bylo motivováno potřebou snížit signalizační zatížení prvků jádra sítě, minimalizovat počet koncových bodů tunelů, které je třeba spravovat, a zlepšit celkovou efektivitu sítě. Tím, že umožňuje více přenosovým kanálům sdílet jediný GTP tunel, C-TEID snižuje režijní náklady na zpracování spojené se správou tunelů a umožňuje efektivnější využití síťových zdrojů. To se stalo obzvláště důležitým se zavedením síťového řezání (network slicing) v 5G, kde více síťových řezů obsluhujících různé případy užití může potřebovat efektivně sdílet přenosové zdroje při zachování izolace mezi řezy.

## Klíčové vlastnosti

- Umožňuje multiplexování více přenosových kanálů přes jediný GTP tunel
- Snižuje signalizační zátěž pro zřizování a modifikaci přenosových kanálů
- Snižuje počet koncových bodů tunelů, které je třeba spravovat
- Zachovává logické oddělení mezi multiplexovanými toky pomocí dodatečných identifikátorů
- Podporuje efektivní využití zdrojů ve virtualizovaných síťových prostředích
- Kompatibilní s existujícími implementacemi GTP prostřednictvím vyjednávání schopností

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description
- **TS 23.285** (Rel-19) — V2X Architecture Enhancements for LTE
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [C-TEID na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-teid/)
