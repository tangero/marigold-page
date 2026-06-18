---
slug: "upsc"
url: "/mobilnisite/slovnik/upsc/"
type: "slovnik"
title: "UPSC – UE Policy Section Code"
date: 2025-01-01
abbr: "UPSC"
fullName: "UE Policy Section Code"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upsc/"
summary: "Číselný identifikátor používaný v 5G k určení konkrétní sekce informací o politice UE (URSP, ANDSP, V2X) doručovaných PCF k UE. Umožňuje efektivní cílené aktualizace a správu politik směrování UE, pří"
---

UPSC je číselný identifikátor používaný v 5G k určení konkrétní sekce informací o politice UE, který umožňuje efektivní a cílené aktualizace politik od PCF k UE.

## Popis

Kód sekce politiky UE (UE Policy Section Code – UPSC) je koncept zavedený v architektuře 5G systému (5GS), definovaný v technických specifikacích jako 3GPP TS 24.501 (procedury UE) a TS 29.525 (služby [PCF](/mobilnisite/slovnik/pcf/)). Je klíčovým prvkem v rámci řízení politiky UE, které určuje, jak se UE připojuje k sítím a směruje provoz. PCF (Policy Control Function) je zodpovědná za generování a poskytování informací o politice UE. Tato politika není zasílána jako jeden monolitický blok, ale je strukturována do samostatných sekcí, z nichž každá je identifikována jedinečným UPSC. Hlavními sekcemi politiky jsou politika výběru směrování UE ([URSP](/mobilnisite/slovnik/ursp/)), politika vyhledávání a výběru přístupové sítě ([ANDSP](/mobilnisite/slovnik/andsp/)) a politiky související s [V2X](/mobilnisite/slovnik/v2x/).

UPSC funguje jako manipulátor nebo index. Když PCF potřebuje zřídit, upravit nebo odebrat konkrétní část politiky pro UE, odkazuje se na příslušný UPSC ve své komunikaci s [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function) a nakonec s UE. Například PCF může odeslat služební operaci Npcf_UEPolicyControl_UpdateNotify k AMF, která indikuje aktualizaci pro sekci politiky identifikovanou konkrétní hodnotou UPSC. AMF pak tuto indikaci přepošle k UE pomocí zprávy UE Configuration Update nebo [DL](/mobilnisite/slovnik/dl/) [NAS](/mobilnisite/slovnik/nas/) TRANSPORT. UE po přijetí oznámení pro daný UPSC může následně požádat o aktualizovaný obsah politiky pro tuto konkrétní sekci od PCF, typicky prostřednictvím procedury doručení politiky UE.

Tento segmentovaný přístup, umožněný UPSC, je klíčový pro efektivitu. Umožňuje jemně odstupňovanou správu politik, kdy je nutné přenést pouze změněnou sekci politiky, čímž se snižuje signalizační režie a zatížení zpracování v UE. Každý UPSC je asociován s konkrétním typem a formátem politiky. Například pravidla URSP (která určují, jak UE směruje provoz specifických aplikací k různým síťovým řezům nebo [DNN](/mobilnisite/slovnik/dnn/)) jsou spravována pod svým určeným UPSC. Tato modulární struktura podporuje dynamickou a službami řízenou povahu 5G, kde mohou být politiky pro síťové řezy, edge computing nebo V2X komunikace aktualizovány nezávisle, aniž by to ovlivnilo ostatní domény politik.

## K čemu slouží

Kód sekce politiky UE (UPSC) byl vytvořen, aby řešil omezení monolitické správy politik v předchozích generacích a aby podpořil rozšířený, na řezy citlivý rámec politik v 5G. V 4G/EPS byl ANDSP doručován, ale mechanismy pro aktualizaci politik byly méně podrobné. 5G zavedlo komplexní koncept URSP, který je mnohem složitější a pravděpodobně se bude často měnit v závislosti na uživatelském předplatném, potřebách aplikací a dostupnosti síťových řezů. Byl potřeba mechanismus pro efektivní správu těchto různorodých a dynamických politik.

UPSC řeší problém neefektivních aktualizací politik. Bez kódů sekcí by jakákoli změna politiky vyžadovala opětovný přenos celé sady politik k UE, což by spotřebovalo významné rádiové prostředky a životnost baterie UE. Umožněním cílených aktualizací na úrovni sekcí UPSC minimalizuje signalizační režii. Zároveň poskytuje UE jasnou strukturu pro organizaci a ukládání různých typů politik. To bylo motivováno principy návrhu 5G zaměřenými na flexibilitu a efektivitu, které podporují případy užití, kde politiky pro IoT, rozšířené mobilní širokopásmové připojení a komunikace s ultra spolehlivým nízkým zpožděním mohou potřebovat nezávislou a rychlou adaptaci.

## Klíčové vlastnosti

- Jedinečný číselný kód identifikující sekci politiky UE (např. URSP, ANDSP)
- Umožňuje cílené zřizování, úpravy a odebrání konkrétních sekcí politik
- Je odkazován v signalizaci PCF-síť (Npcf) a síť-UE (NAS)
- Snižuje signalizační režii umožněním částečných aktualizací politik
- Podporuje klíčové typy politik 5G: URSP, ANDSP a V2X politiky
- Nedílná součást procedur doručení a aktualizace politiky UE v 5GS

## Související pojmy

- [URSP – UE Route Selection Policy](/mobilnisite/slovnik/ursp/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [ANDSP – Access Network Discovery and Selection Policy](/mobilnisite/slovnik/andsp/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [UPSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/upsc/)
