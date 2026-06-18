---
slug: "str"
url: "/mobilnisite/slovnik/str/"
type: "slovnik"
title: "STR – Session-Termination-Request"
date: 2025-01-01
abbr: "STR"
fullName: "Session-Termination-Request"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/str/"
summary: "Session-Termination-Request (STR) je příkaz Diameter používaný v sítích 3GPP k explicitnímu požadavku na ukončení zavedené relace Diameter, například relace IP-CAN nebo relace řízení kreditu. Je to kr"
---

STR je příkaz Diameter v sítích 3GPP, který explicitně žádá o ukončení zavedené relace Diameter, například relace IP-CAN nebo relace řízení kreditu, za účelem řádného vyčištění relace a uvolnění prostředků.

## Popis

Session-Termination-Request (STR) je specifický příkaz Diameter s kódem (275) definovaný v základním protokolu Diameter ([RFC](/mobilnisite/slovnik/rfc/) 6733) a podrobně profilovaný ve specifikacích 3GPP pro různá rozhraní. Je součástí stavového automatu relace Diameter a používá se klientem nebo serverem Diameter k signalizaci úmyslného ukončení aplikační relace Diameter. V kontextech 3GPP tyto relace často odpovídají relacím služeb vyšší úrovně, jako je relace IP Connectivity Access Network ([IP-CAN](/mobilnisite/slovnik/ip-can/)) v Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) nebo relace Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) ve funkci Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)).

Příkaz STR je typicky iniciován uzlem, který službu ukončuje (např. PGW při odpojení uživatele), a je odeslán jeho partnerskému uzlu Diameter (např. PCRF nebo Online Charging System). Příkaz nese atribut Session-Id Attribute-Value Pair ([AVP](/mobilnisite/slovnik/avp/)) pro jednoznačnou identifikaci relace, která má být ukončena. Zahrnuje také další relevantní AVP, jako je Termination-Cause AVP, který udává důvod ukončení (např. "DIAMETER_LOGOUT", "DIAMETER_SERVICE_NOT_PROVIDED", "DIAMETER_BAD_ANSWER"). Po přijetí STR musí příjemce provést všechny nezbytné procedury vyčištění spojené s danou relací. To zahrnuje uvolnění všech interně držených prostředků, aktualizaci záznamů o účtování a odvolání všech aktivních pravidel politiky, která byla pro relaci zřízena.

Příjemce STR musí odpovědět příkazem Session-Termination-Answer ([STA](/mobilnisite/slovnik/sta/)). Příkaz STA potvrzuje ukončení relace a může obsahovat konečná účtovací data nebo jiné výsledkové informace. Tato výměna žádost-odpověď zajišťuje, že obě strany dialogu Diamater mají synchronizovaný pohled na stav relace, což zabraňuje únikům prostředků, chybám v účtování nebo zastaralému vynucování politik. Mechanismus STR/STA je zásadní pro spolehlivý provoz online účtování, řízení politik a správu mobility v jádrových sítích 4G (EPC) a 5G.

## K čemu slouží

Příkaz STR existuje, aby poskytoval spolehlivý, explicitní a standardizovaný mechanismus pro ukončení relace v rámci protokolového rámce Diameter. Před protokolem Diameter protokoly jako [RADIUS](/mobilnisite/slovnik/radius/) postrádaly robustní správu stavu relace a explicitní signalizaci ukončení, což mohlo vést k problémům, jako je "zastarání relace", kdy síťové prostředky zůstaly přiděleny po odpojení uživatele, nebo k nepřesnému účtování, kdy relace nebyly řádně uzavřeny. Protokol Diameter a z něj vyplývající příkaz STR byly navrženy tak, aby tyto nedostatky řešily pro komplexní, stavové síťové služby.

V architekturách 3GPP, zejména se zavedením rámce Policy and Charging Control (PCC), se relace staly složitějšími a zahrnovaly více síťových funkcí (PCRF, PCEF, OCS), které potřebovaly koordinovat stav. Implicitní časový limit relace byl nedostatečný pro přesné účtování v reálném čase a dynamické vynucování politik. STR poskytuje deterministický signál, který umožňuje všem zúčastněným uzlům synchronně provést konečné výpočty účtování, uplatnit jakékoli politiky spouštěné ukončením a zaznamenat přesný důvod konce relace. To je klíčové pro služby s předplacením, kde musí být konečný odpočet přesný, a pro služby s platbou po použití, kde jsou podrobné záznamy o relacích potřebné pro účtování.

Jeho zavedení a profilování v 3GPP (zejména od vydání 11 pro rozhraní jako Gx, Gy a S9) bylo hnací silou potřeby větší spolehlivosti v sítích LTE/EPC zpracovávajících datové služby s vysokou hodnotou. Řešil problém nejednoznačného konce relací, zajišťoval včasné uvolnění síťových prostředků a správné vyrovnání finančních transakcí, což je základní pro komerční provoz mobilního širokopásmového připojení.

## Klíčové vlastnosti

- Příkaz Diameter s kódem 275 používaný pro explicitní signalizaci ukončení relace
- Nese AVP Session-Id pro jednoznačnou identifikaci relace, která má být ukončena
- Obsahuje AVP Termination-Cause pro specifikaci důvodu ukončení relace (např. odhlášení uživatele, administrativní akce)
- Spouští procedury vyčištění včetně uvolnění prostředků a odvolání politik v přijímacím uzlu
- Vyžaduje povinnou odpověď Session-Termination-Answer (STA) pro potvrzení
- Zásadní pro přesné konečné účtování a účtování v interakcích s Online Charging System (OCS)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.219** (Rel-19) — Sy Reference Point Stage 3 Specification

---

📖 **Anglický originál a plná specifikace:** [STR na 3GPP Explorer](https://3gpp-explorer.com/glossary/str/)
