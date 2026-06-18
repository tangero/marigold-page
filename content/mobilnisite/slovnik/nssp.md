---
slug: "nssp"
url: "/mobilnisite/slovnik/nssp/"
type: "slovnik"
title: "NSSP – Network Slice Selection Policy"
date: 2026-01-01
abbr: "NSSP"
fullName: "Network Slice Selection Policy"
category: "Network Slicing"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nssp/"
summary: "NSSP je soubor pravidel nakonfigurovaný v uživatelském zařízení (UE), který řídí zařízení při výběru a vyžádání odpovídajících síťových řezů pro jeho aplikace. Mapuje identifikátory aplikací nebo desk"
---

NSSP je soubor pravidel v uživatelském zařízení, který mapuje aplikace nebo provoz na konkrétní identifikátory síťových řezů a řídí zařízení při automatickém výběru a vyžádání odpovídajících síťových řezů.

## Popis

Network Slice Selection Policy (NSSP) je lokální konfigurace v UE, která obsahuje pravidla mapující aplikační provoz na konkrétní Network Slice Selection Assistance Information ([S-NSSAI](/mobilnisite/slovnik/s-nssai/)). Je klíčovým prvkem pro výběr řezu řízený zařízením, který umožňuje UE inteligentně vyžádat síťové řezy, které jsou optimální pro její běžící aplikace, aniž by vyžadoval explicitní zásah uživatele pro každou službu. NSSP je poskytováno UE sítí, typicky prostřednictvím Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), a může být operátorem sítě dynamicky aktualizováno.

Pravidlo NSSP se skládá z několika komponent: deskriptoru provozu a odpovídajícího S-NSSAI. Deskriptor provozu může být definován pomocí různých identifikátorů, jako je Application Identifier (např. OSId + OSAppId), Fully Qualified Domain Name ([FQDN](/mobilnisite/slovnik/fqdn/)) nebo IP 3-tice (cílovou IP adresu, protokol, číslo portu). Když aplikace na UE generuje provoz, operační systém nebo modemový software UE vyhodnotí pravidla NSSP. Pokud provoz odpovídá deskriptoru v pravidle NSSP, UE zahrne přidružené S-NSSAI do svého Requested [NSSAI](/mobilnisite/slovnik/nssai/) během procedur registrace nebo vytváření [PDU](/mobilnisite/slovnik/pdu/) sezení. Tím signalizuje síti (konkrétně [NSSF](/mobilnisite/slovnik/nssf/) a [AMF](/mobilnisite/slovnik/amf/)) přání UE použít daný síťový řez pro odpovídající provoz.

NSSP funguje ve spojení s UE Route Selection Policy (URSP), což je širší politika zahrnující pravidla pro směrování provozu ke konkrétním Data Network Names (DNN), SSC režimům a síťovým řezům. NSSP lze považovat za podmnožinu nebo komponentu zaměřenou specificky na výběr řezu. Existence NSSP umožňuje sofistikované případy použití, jako je současné používání výchozího eMBB řezu pro obecné prohlížení internetu na smartphonu, zatímco automaticky vyžádá nízkolatenční řez pro cloudovou herní aplikaci a vysoce spolehlivý řez pro službu mission-critical push-to-talk, vše na základě předkonfigurovaných politik operátora.

## K čemu slouží

NSSP bylo vytvořeno k vyřešení problému, jak může uživatelské zařízení inteligentně a automaticky vybírat z více dostupných síťových řezů bez spoléhání na manuální konfiguraci uživatelem nebo na zjednodušená výchozí nastavení sítě. V raných nasazeních 5G bez NSSP se mohlo UE registrovat s jedním výchozím řezem pro veškerý svůj provoz, což negovalo výhody specializovaných řezů. Alternativně by vyžadování ručního výběru řezu pro každou aplikaci od uživatelů nebo vývojářů aplikací bylo nepraktické a vedlo by ke špatné uživatelské zkušenosti.

NSSP to řeší tím, že umisťuje inteligenci politik přímo do UE pod kontrolou síťového operátora. To umožňuje operátorovi směrovat specifický, identifikovatelný aplikační provoz na řez, který nabízí nejvhodnější výkonnostní charakteristiky (např. nízkou latenci pro hraní her, vysokou šířku pásma pro 4K video). Umožňuje efektivní využití síťových zdrojů tím, že zajišťuje, že prémiové řezy jsou používány pouze v případě potřeby autorizovanými aplikacemi. Dále připravuje zařízení na budoucí služby; operátor může nasadit nový řez pro vznikající aplikaci (jako jsou AR brýle) a jednoduše poslat nové pravidlo NSSP předplaceným UE, aby umožnil automatické použití tohoto řezu, aniž by vyžadoval aktualizaci operačního systému zařízení. NSSP je proto nezbytné pro realizaci uživatelsky viditelných výhod síťového řezání škálovatelným a automatizovaným způsobem.

## Klíčové vlastnosti

- Obsahuje pravidla mapující deskriptory aplikačního provozu na konkrétní S-NSSAI
- Je konfigurováno v UE síťovým operátorem (např. prostřednictvím UDM/PCF)
- Umožňuje automatický výběr síťového řezu řízený UE pro každou aplikaci
- Deskriptory provozu mohou využívat informace App ID, FQDN nebo IP tice
- Funguje ve spojení se širší politikou UE Route Selection Policy (URSP)
- Podporuje dynamické aktualizace ze strany sítě pro přizpůsobení novým službám nebo politikám

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions

---

📖 **Anglický originál a plná specifikace:** [NSSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nssp/)
